# Amito Releases

Official downloads for apps by **Amito**. This repository holds installers only; the source code is kept private.

Every installer is built automatically by GitHub Actions and published here as a GitHub Release.

| App | Latest version | Platforms |
|---|---|---|
| [ADM, Amito Download Manager](#adm-amito-download-manager) | 1.0.0 | macOS, Windows, Linux |

---

## ADM, Amito Download Manager

A fast, multi-threaded download manager. ADM splits every file across up to 32 threads, shows exactly what each thread is doing, and tells you to the second when a download will finish. It also has a built-in internet speed test. Free.

**Highlights**

- Multi-threaded downloads, up to 32 threads per file
- Pause, resume across restarts, and automatic retries
- Live thread lanes and speed chart
- Category folders, batch adding, and clipboard link detection
- Global speed limit and checksum verification
- Internet speed test with server choice
- Six themes plus custom colours

### Download ADM 1.0.0

**macOS** (macOS 12 Monterey or later)

| Mac | Installer | Archive |
|---|---|---|
| Apple Silicon (M1 and later) | [ADM-1.0.0-mac-arm64.dmg](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-mac-arm64.dmg) | [.zip](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-mac-arm64.zip) |
| Intel | [ADM-1.0.0-mac-x64.dmg](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-mac-x64.dmg) | [.zip](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-mac-x64.zip) |

**Windows** (Windows 10 or 11)

| PC | Installer | Portable |
|---|---|---|
| x64 (most PCs) | [ADM-1.0.0-win-x64.exe](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-win-x64.exe) | [.zip](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-win-x64.zip) |
| ARM64 (Snapdragon) | [ADM-1.0.0-win-arm64.exe](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-win-arm64.exe) | [.zip](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-win-arm64.zip) |
| Not sure | [ADM-1.0.0-win.exe](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-win.exe) (both, larger) | |

**Linux** (Ubuntu 20.04, Debian 11, Fedora 36 or newer)

| CPU | AppImage (any distro) | .deb (Debian, Ubuntu) | .tar.gz |
|---|---|---|---|
| x64 | [ADM-1.0.0-linux-x86_64.AppImage](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-linux-x86_64.AppImage) | [ADM-1.0.0-linux-amd64.deb](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-linux-amd64.deb) | [.tar.gz](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-linux-x64.tar.gz) |
| ARM64 | [ADM-1.0.0-linux-arm64.AppImage](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-linux-arm64.AppImage) | [ADM-1.0.0-linux-arm64.deb](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-linux-arm64.deb) | [.tar.gz](https://github.com/amiamitswe/amito-releases/releases/download/adm-v1.0.0/ADM-1.0.0-linux-arm64.tar.gz) |

Older versions: [all ADM releases](https://github.com/amiamitswe/amito-releases/releases?q=adm-v)

### Installing

The current builds are not code-signed yet, so your system may warn you the first time you open ADM.

- **macOS:** open the `.dmg` and drag ADM into Applications. The first time, right-click ADM and choose **Open**, then **Open** again.
- **Windows:** run the `.exe`. If SmartScreen appears, click **More info**, then **Run anyway**.
- **Linux AppImage:** make it executable, then run it:
  ```bash
  chmod +x ADM-1.0.0-linux-x86_64.AppImage
  ./ADM-1.0.0-linux-x86_64.AppImage
  ```
- **Linux .deb:**
  ```bash
  sudo apt install ./ADM-1.0.0-linux-amd64.deb
  ```

### Verify your download

Each file's SHA-256 checksum is listed next to it on the release page. To check a file:

- **macOS / Linux:** `shasum -a 256 <file>`
- **Windows (PowerShell):** `Get-FileHash <file>`

### Report a problem

Found a bug or have an idea? [Open an issue](https://github.com/amiamitswe/amito-releases/issues/new) and start the title with **[ADM]**. Please include your operating system, the ADM version and the steps to reproduce it.

---

© 2026 Amit Samadder. All rights reserved.
