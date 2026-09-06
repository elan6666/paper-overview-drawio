# 环境安装与首次检查

[English](setup.en.md)

先检查已有环境，只补缺失项，不重复安装或升级已经可用的软件。以下命令在本技能仓库根目录执行；路径不同请替换为实际位置。安装指引与当前辅助脚本对应，不代表所有平台都已完成实机验证。

## 需要哪些软件

| 组件 | 何时需要 | 安装与检查 |
| --- | --- | --- |
| 支持本地 skill 的代理宿主 | 使用技能工作流 | 让当前会话识别 `SKILL.md`，并确认文件读写、检索、图片查看工具可调用 |
| draw.io Desktop | App 精修和本仓库的批量导出 | 安装官方桌面版，打开测试文件；网页版可人工编辑，但不能代替本地导出程序 |
| Python | 运行本仓库辅助脚本 | 新环境建议 Python 3.11 或更新的受支持版本；先检查 `python3 --version`，Windows 用 `py --version` |
| PyMuPDF | 辅助导出、PDF 审核、PDF 对比预览 | 在虚拟环境内安装 `requirements.txt`；仅编译简单场景和语义检查不需要它 |
| Git | 通过 clone 安装或更新技能 | `git --version`；也可从仓库下载 ZIP，无须为 ZIP 安装方式额外装 Git |
| 电脑操作工具 | 自动在 App 内修改 | 必须由宿主提供并支持当前系统；安装 draw.io 本身不会给代理增加操作工具 |
| 生图、subagent | 生成插图、独立审图 | 确认当前会话实际提供相关工具；本仓库不附模型、凭据或独立代理运行时 |

不需要为了使用本技能安装 Node.js、构建 Electron、部署 draw.io 服务、GPU 或下载模型权重。若已有合适的 Python 运行时可复用；不要默认使用系统全局 pip。

## 1. 安装 draw.io Desktop

从 [draw.io 官方发布页](https://github.com/jgraph/drawio-desktop/releases)选择匹配操作系统与处理器架构的稳定安装包，无须克隆或编译 draw.io 源码。

- **macOS**：打开下载的 DMG，把 draw.io 拖入 Applications。已安装 Homebrew 时也可运行 `brew install --cask drawio`（[Homebrew 软件页](https://formulae.brew.sh/cask/drawio)）；不必只为它先安装 Homebrew。
- **Windows**：选择官方 Windows 安装包或便携版。记住实际的 `draw.io.exe` 路径，便携版路径尤其需要自己指定。
- **Linux**：选择适合发行版的 DEB、RPM 或 AppImage，按发行版方式安装；AppImage 需要执行权限。App 精修需要可交互的桌面会话。纯无头服务器不能因此获得 App 操作能力；CLI 导出也可能需要额外的显示环境，须单独验证。

辅助脚本会检查 macOS 默认位置，或 PATH 中的 `drawio` / `draw.io`。找不到时设置 **可执行文件** 路径（不是 `.app` 文件夹或安装包）：

```bash
# macOS / bash / zsh；仅非默认路径才必须设置
export DRAWIO_PATH="/Applications/draw.io.app/Contents/MacOS/draw.io"
# Linux 自定义位置示例：替换为实际文件
# export DRAWIO_PATH="/absolute/path/to/drawio.AppImage"
```

```powershell
# Windows PowerShell：先确认实际安装位置，再修改此示例
$env:DRAWIO_PATH = 'C:\Program Files\draw.io\draw.io.exe'
Test-Path $env:DRAWIO_PATH
```

## 2. 安装 Python 依赖

缺少 Python 时，macOS / Windows 可使用 [Python 官方安装包](https://www.python.org/downloads/)；Linux 使用发行版包管理器安装 Python 3、pip 与 venv（Debian / Ubuntu 常见包名为 `python3 python3-pip python3-venv`）。安装后重开终端，确认解释器能运行。

在技能仓库根目录建立独立环境。这里显式调用虚拟环境解释器，不需要激活脚本或更改 PowerShell 执行策略：

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

依赖来自 [PyMuPDF 官方安装说明](https://pymupdf.readthedocs.io/en/latest/installation.html)。不要安装名字叫 `fitz` 的独立包来修复导入：本仓库部分脚本用的是 PyMuPDF 的兼容导入名 `fitz`。若安装失败，先核对 Python 版本、平台 wheel 和报错，再决定是否需要额外构建工具。

## 3. 跑一次最小导出

用随仓库提供的小场景检查编译和 PNG / SVG / PDF 导出，不需要论文数据。它只是环境测试，不是设计模板。以下使用 `outputs/setup-check-1`；再次运行时换一个新目录，脚本不会覆盖已有结果。

```bash
# macOS / Linux
.venv/bin/python scripts/overview.py build assets/examples/paper-contract.json assets/examples/version-1.scene.json --out outputs/setup-check-1/demo.drawio
.venv/bin/python scripts/overview.py export outputs/setup-check-1/demo.drawio --out-dir outputs/setup-check-1/export --contract assets/examples/paper-contract.json
```

Windows 在 PowerShell 中执行相同参数，将开头的 `.venv/bin/python` 换成 `.\.venv\Scripts\python.exe`。

确认三个导出文件实际存在且能打开，查看文字、箭头与字体。报告中 `visual_review: not-reviewed` 表示仍需查看图片，不是导出失败。这里只检查环境，不宣称论文图质量通过。

## 4. 验证 App 操作与其他能力

通过宿主提供的电脑操作工具，读取 draw.io 窗口，在测试副本上选择一个元素、轻微移动并保存；核对实际文件中的变化。能读截图或无障碍树，不等于能点击和保存。若工具提示权限缺失，按其说明让用户在系统设置中授权实际的宿主或辅助进程；不要猜进程名或绕过系统权限。

缺少电脑操作工具时，说明当前只能生成/修改文件，由用户在 App 中精修，或指导其配置宿主支持的电脑操作集成。不要声称 `pip install` 能安装这项能力。遇到 `noWindowsAvailable`，参见[已验证的窗口恢复办法](drawio-authoring.md#recover-a-non-interactive-window)。

需要生图时再检查宿主的 imagegen 工具和技能，缺少时说明配置入口或当前限制，不把 API 密钥写进仓库。独立 subagent 不可用时进行自查并披露。检索不可用时可使用用户提供的可核实论文，但不能声称已经联网查新。

## 常见问题

| 现象 | 处理 |
| --- | --- |
| `python3` / `py` 不存在 | 安装 Python，重开终端；使用实际可用的解释器路径 |
| `No module named venv` / `ensurepip` | 安装发行版匹配的 venv / pip 包，或换用完整 Python 安装 |
| `externally-managed-environment` | 使用上述 `.venv`，不加 `--break-system-packages` |
| `No module named fitz/pymupdf` | 对运行脚本的同一个解释器执行 `-m pip install -r requirements.txt` |
| `Draw.io Desktop unavailable` | 检查安装，设置指向真实可执行文件的 `DRAWIO_PATH` |
| 导出失败或超时 | 检查 draw.io 是否能启动、桌面会话及错误输出，保留失败信息；更换输出目录再试 |
| `Refusing overwrite` | 使用新的版本目录，保留原文件及用户修改 |
| App 可见但点不动 | 区分宿主工具、权限和窗口连接问题，按恢复指引验证后再继续 |

首次设置完成后，简短记录实际解释器、draw.io 路径、依赖检查、导出结果以及 App / 生图 / subagent 的可用状态。后续复用已有环境；只有路径、版本或错误发生变化时才重新排查。
