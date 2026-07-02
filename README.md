# spatialepi.org

Public marketing / download site for **MESA** — an offline address geocoder and
spatial-analysis desktop application for public-health GIS.

- **Live site:** https://www.spatialepi.org (served by GitHub Pages from this repo's `main` branch).
- **App source:** the MESA application itself lives in a **private** repository; this repo
  intentionally contains only the public website, so nothing sensitive is exposed by Pages.

## Structure

| File | Purpose |
|------|---------|
| `index.html` | Single-page landing + downloads site (self-contained, no build step). |
| `manifest.json` | *(added by CI later)* per-platform download URLs + SHA-256 checksums. |
| `404.html` | Custom not-found page. |
| `favicon.svg` | Site icon. |
| `CNAME` | Custom domain (`www.spatialepi.org`) — do not remove. |
| `.nojekyll` | Disables Jekyll processing (this is plain HTML). |

## Wiring up downloads

The download buttons are stubbed as "coming soon". When the release pipeline
(`release.yml` in the app repo) publishes per-OS binaries, drop a `manifest.json`
in this repo's root:

```json
{
  "version": "1.0.0",
  "date": "2026-07-02",
  "builds": {
    "windows": { "url": "https://.../MESA-1.0.0-win-x64.exe",     "sha256": "..." },
    "macos":   { "url": "https://.../MESA-1.0.0-macos-arm64.dmg", "sha256": "..." },
    "linux":   { "url": "https://.../MESA-1.0.0-linux-x64.AppImage", "sha256": "..." }
  }
}
```

`index.html` fetches it on load and lights up the buttons automatically — the
site never needs a per-release edit.

## Local preview

```sh
python3 -m http.server 8000   # then open http://localhost:8000
```
