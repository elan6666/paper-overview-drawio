# Environment setup and first-run checks

[中文](setup.md)

Check existing tools first. Install only missing components; do not reinstall or upgrade working software by default. Run the commands below from this skill's repository root, adjusting paths for your installation. These instructions match the current helpers; they do not claim live testing on every platform.

## Components

| Component | Needed for | Setup / check |
| --- | --- | --- |
| Agent host supporting local skills | Skill workflow | Ensure the session recognizes `SKILL.md` and exposes file access, retrieval and image inspection |
| draw.io Desktop | App refinement and bundled batch export | Install the official desktop app and open a test file; the web editor does not replace the local executable |
| Python | Bundled helper scripts | For a new environment, use Python 3.11 or a newer supported release; check `python3 --version`, or `py --version` on Windows |
| PyMuPDF | Export helper, PDF audit and comparison previews | Install `requirements.txt` in a virtual environment; simple scene compilation and semantic checks only use the standard library |
| Git | Clone-based installation / updates | Check `git --version`; downloading the repository ZIP is an alternative that does not require Git |
| Computer-use tools | Automated App editing | Must be supplied by the host and support the current OS; installing draw.io does not add these tools to the agent |
| Image generation and subagents | Generated artwork and independent review | Verify actual session tools; this repository includes no models, credentials or separate agent runtime |

Using this skill does not require Node.js, building Electron, running a draw.io server, a GPU or model weights. Reuse a suitable existing Python runtime when available; do not default to global system pip.

## 1. Install draw.io Desktop

Choose a stable installer matching your OS and architecture from the [official releases](https://github.com/jgraph/drawio-desktop/releases). Building draw.io from source is unnecessary.

- **macOS:** open the DMG and drag draw.io to Applications. If Homebrew is already installed, `brew install --cask drawio` is another option ([Homebrew package](https://formulae.brew.sh/cask/drawio)). Homebrew itself is not required.
- **Windows:** use an official installer or portable build. Note the actual `draw.io.exe` location, especially for a portable installation.
- **Linux:** use a DEB, RPM or AppImage appropriate for the distribution. AppImages need executable permission. App refinement requires an interactive desktop session. A headless server does not gain UI control from installation alone; CLI export may also require additional display setup and must be verified separately.

The helper checks the default macOS location and `drawio` / `draw.io` on PATH. If necessary, set the path to the **executable**, not an `.app` directory or installer:

```bash
# macOS / bash / zsh; only necessary for a non-discoverable location
export DRAWIO_PATH="/Applications/draw.io.app/Contents/MacOS/draw.io"
# Custom Linux location: replace with the actual file
# export DRAWIO_PATH="/absolute/path/to/drawio.AppImage"
```

```powershell
# Windows PowerShell: check the installation location and adapt this example
$env:DRAWIO_PATH = 'C:\Program Files\draw.io\draw.io.exe'
Test-Path $env:DRAWIO_PATH
```

## 2. Install Python dependencies

If Python is missing, use the [official installers](https://www.python.org/downloads/) on macOS / Windows, or the distribution's Python 3, pip and venv packages on Linux (commonly `python3 python3-pip python3-venv` on Debian / Ubuntu). Reopen the terminal and verify the interpreter runs.

Create an isolated environment in the skill repository root. Calling its interpreter directly avoids activation scripts and PowerShell execution-policy changes:

```bash
# macOS / Linux
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -c "import sys, pymupdf; print(sys.executable); print(pymupdf.__doc__)"
```

```powershell
# Windows PowerShell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -c "import sys, pymupdf; print(sys.executable); print(pymupdf.__doc__)"
```

See the [official PyMuPDF installation guide](https://pymupdf.readthedocs.io/en/latest/installation.html). Do not install the unrelated package named `fitz`: some helpers use PyMuPDF's compatibility import name `fitz`. On installation failure, check the Python version, platform wheel availability and actual error before adding build tools.

## 3. Run a minimal export

The bundled small scene checks compilation and PNG / SVG / PDF export without paper data. It is an environment fixture, not a design template. These commands use `outputs/setup-check-1`; choose a new directory for subsequent runs because the helpers refuse to overwrite existing output.

```bash
# macOS / Linux
.venv/bin/python scripts/overview.py build assets/examples/paper-contract.json assets/examples/version-1.scene.json --out outputs/setup-check-1/demo.drawio
.venv/bin/python scripts/overview.py export outputs/setup-check-1/demo.drawio --out-dir outputs/setup-check-1/export --contract assets/examples/paper-contract.json
```

In Windows PowerShell, use the same arguments but replace `.venv/bin/python` with `.\.venv\Scripts\python.exe`.

Confirm that all three exported files exist and open correctly. Inspect text, arrows and fonts. `visual_review: not-reviewed` means visual inspection remains outstanding; it is not an export failure. This checks the environment, not publication quality.

## 4. Verify App control and other capabilities

Using the host's computer-use tools, inspect draw.io, select and slightly move an object in a test copy, then save. Independently verify the file change. Reading a screenshot or accessibility tree does not prove that clicking and saving work. If a tool reports missing permissions, guide the user through granting the relevant host/helper access in system settings using the tool's actual instructions; do not guess process names or bypass system permissions.

When computer-use tools are missing, explain that the agent can generate/edit files and the user can refine them in the App, or guide setup of a computer-use integration supported by the host. Do not claim pip installs this capability. For `noWindowsAvailable`, see the [observed window recovery procedure](drawio-authoring.md#recover-a-non-interactive-window).

Check the host's imagegen skill and tool only when generated assets are useful; explain missing configuration or limitations, and never write API keys into the repository. If independent subagents are unavailable, self-review and disclose that limitation. If retrieval is unavailable, use verifiable supplied papers without claiming a fresh online search.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| `python3` / `py` missing | Install Python, reopen the terminal and use the available interpreter path |
| Missing `venv` / `ensurepip` | Install the distribution's matching venv / pip packages or use a complete Python installation |
| `externally-managed-environment` | Use `.venv` as above, without `--break-system-packages` |
| Missing `fitz/pymupdf` | Run `-m pip install -r requirements.txt` using the same interpreter that runs the helper |
| `Draw.io Desktop unavailable` | Check installation and set `DRAWIO_PATH` to the actual executable |
| Export failure / timeout | Check app startup, desktop session and error output; preserve failure information and retry in a new output directory |
| `Refusing overwrite` | Choose a revisioned output directory; preserve source files and user edits |
| App readable but not clickable | Distinguish host tooling, permissions and window connection issues; verify recovery before continuing |

After setup, briefly record the actual interpreter, draw.io path, dependency check, export result and availability of App control, image generation and subagents. Reuse the environment on later runs; troubleshoot again when paths, versions or errors change.
