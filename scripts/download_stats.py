"""Collect ADM download counts from this repo's GitHub releases.

Writes stats/adm.json (read by the per-file badges in README.md) and rewrites the
download table between the adm-stats markers in README.md. Run by
.github/workflows/download-stats.yml; uses only the Python standard library.
"""

import datetime
import json
import os
import re
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "amiamitswe/amito-releases")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
PREFIX = "adm-v"  # ADM's release tags in this shared repo: adm-v1.0.0
README = "README.md"
STATS = "stats/adm.json"
# Downloads to leave out (e.g. testing before launch), per release tag and file name.
# GitHub's counts can't be reset, so the stats show each count minus its baseline.
BASELINE = "stats/adm-baseline.json"
START, END = "<!-- adm-stats:start -->", "<!-- adm-stats:end -->"
OSES = ("macOS", "Windows", "Linux")


def load_baseline():
    try:
        with open(BASELINE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def counted(baseline, tag, asset):
    """The asset's download count, minus any baseline recorded for it."""
    ignore = baseline.get(tag, {}).get(asset["name"], 0)
    return max(0, asset["download_count"] - ignore)


def api(path):
    req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/{path}")
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req) as res:
        return json.load(res)


def all_releases():
    releases, page = [], 1
    while True:
        batch = api(f"releases?per_page=100&page={page}")
        releases += batch
        if len(batch) < 100:
            return releases
        page += 1


def os_of(name):
    if "-mac-" in name:
        return "macOS"
    if "-win" in name:
        return "Windows"
    if "-linux-" in name:
        return "Linux"
    return None


def version_key(version):
    return tuple(int(p) if p.isdigit() else 0 for p in re.split(r"[.-]", version))


def main():
    adm = [r for r in all_releases() if r["tag_name"].startswith(PREFIX) and not r["draft"]]
    if not adm:
        print("No ADM releases found")
        return

    baseline = load_baseline()
    latest = max(adm, key=lambda r: version_key(r["tag_name"][len(PREFIX):]))
    version = latest["tag_name"][len(PREFIX):]

    # Per-file counts for the latest release, keyed without the version
    # ("mac-arm64.dmg"), so the README badges keep working across releases.
    files = {}
    by_os = dict.fromkeys(OSES, 0)
    for asset in latest["assets"]:
        name, count = asset["name"], counted(baseline, latest["tag_name"], asset)
        key = re.sub(rf"^ADM-{re.escape(version)}-", "", name)
        files[key] = count
        if os_of(name):
            by_os[os_of(name)] += count

    # All ADM releases together.
    all_time = dict.fromkeys(OSES, 0)
    for release in adm:
        for asset in release["assets"]:
            if os_of(asset["name"]):
                all_time[os_of(asset["name"])] += counted(baseline, release["tag_name"], asset)

    now = datetime.datetime.now(datetime.timezone.utc)
    stats = {
        "version": version,
        "updated": now.strftime("%Y-%m-%d %H:%M UTC"),
        "files": files,
        "os": by_os,
        "total": sum(by_os.values()),
        "allTime": {**all_time, "total": sum(all_time.values())},
        "releases": len(adm),
    }
    os.makedirs(os.path.dirname(STATS), exist_ok=True)
    with open(STATS, "w") as f:
        json.dump(stats, f, indent=2)
        f.write("\n")

    rows = [
        f"| ADM {version} | Downloads |" + (" All versions |" if len(adm) > 1 else ""),
        "|---|---:|" + ("---:|" if len(adm) > 1 else ""),
    ]
    icons = {"macOS": "🍎", "Windows": "🪟", "Linux": "🐧"}
    for name in OSES:
        row = f"| {icons[name]} {name} | {by_os[name]:,} |"
        rows.append(row + (f" {all_time[name]:,} |" if len(adm) > 1 else ""))
    total = f"| **Total** | **{stats['total']:,}** |"
    rows.append(total + (f" **{stats['allTime']['total']:,}** |" if len(adm) > 1 else ""))
    table = "\n".join(rows)
    since = " · counting since 2026-11-11" if baseline else ""
    block = f"{START}\n{table}\n\n<sub>Updated daily from GitHub's download counts{since} · last update {stats['updated']}</sub>\n{END}"

    with open(README) as f:
        readme = f.read()
    if START in readme and END in readme:
        readme = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, readme, flags=re.S)
        with open(README, "w") as f:
            f.write(readme)
    else:
        print("README markers not found; only stats/adm.json was updated")

    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
