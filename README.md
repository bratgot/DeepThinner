# DeepThinner v2.0

**Deep Sample Optimisation for Nuke 16**

Created by Marten Blumen

---

## Overview

DeepThinner reduces deep sample counts per pixel through seven independent, artist-controllable passes. It dramatically improves downstream compositing speed, memory usage, and deep EXR write times with minimal to zero visual impact.

---

## Installation

### Pre-built Plugin (Recommended)

1. Download the correct plugin for your platform:
   - **Windows:** `DeepThinner.dll`
   - **Linux:** `DeepThinner.so`
   - **macOS:** `DeepThinner.dylib`

2. Copy the plugin file to one of the following locations:
   - Your personal Nuke directory: `~/.nuke/` (Linux/macOS) or `%USERPROFILE%\.nuke\` (Windows)
   - A shared plugin directory on your `NUKE_PATH`
   - Your studio's custom plugin directory

3. Copy `menu.py` to the same location as the plugin (or merge its contents into your existing `menu.py`).

4. Restart Nuke. DeepThinner will appear under **Deep > DeepThinner** in the node toolbar.

### Building from Source

#### Requirements

- **Nuke 16** with NDK headers installed
- **CMake 3.15** or later
- **C++17 compiler:**
  - Windows: Visual Studio 2022 (MSVC 19.x)
  - Linux: GCC 9+ or Clang 10+
  - macOS: Xcode 12+ / Apple Clang 12+

#### Windows

```bat
cd C:\path\to\DeepThinner
mkdir build && cd build
cmake -DNUKE_INSTALL_PATH="C:\Program Files\Nuke16.0v8" ..
cmake --build . --config Release
copy Release\DeepThinner.dll %USERPROFILE%\.nuke\
```

#### Linux

```bash
cd /path/to/DeepThinner
mkdir build && cd build
cmake -DNUKE_INSTALL_PATH="/usr/local/Nuke16.0v8" ..
make -j$(nproc)
cp DeepThinner.so ~/.nuke/
```

#### macOS

```bash
cd /path/to/DeepThinner
mkdir build && cd build
cmake -DNUKE_INSTALL_PATH="/Applications/Nuke16.0v8/Nuke16.0v8.app/Contents/MacOS" ..
make -j$(sysctl -n hw.ncpu)
cp DeepThinner.dylib ~/.nuke/
```

---

## File Structure

```
DeepThinner/
├── DeepThinner.cpp    — Plugin source code
├── CMakeLists.txt     — CMake build configuration
├── menu.py            — Nuke menu registration
└── README.md          — This file
```

---

## Quick Start

1. Create a DeepThinner node from **Deep > DeepThinner** (or press Tab and type "DeepThinner").
2. Connect it to your deep stream.
3. The default settings (Occlusion Cutoff + Contribution Cull + Smart Merge) are a good starting point.
4. Render, then open the **Statistics** group in the properties to see your reduction results.
5. Click **Update Statistics** to refresh the numbers at any time.

---

## Passes

| # | Pass                  | Default | What It Does                                                      |
|---|-----------------------|---------|-------------------------------------------------------------------|
| 1 | Depth Range           | Off     | Clips samples outside a near/far Z range                          |
| 2 | Alpha Cull            | On      | Removes samples with alpha at or below a threshold                |
| 3 | Occlusion Cutoff      | On      | Drops everything behind the point where coverage reaches a cutoff |
| 4 | Contribution Cull     | On      | Removes samples whose visible contribution is negligible          |
| 5 | Volumetric Collapse   | Off     | Collapses runs of low-alpha volume samples into fewer samples     |
| 6 | Smart Merge           | On      | Merges Z-close and colour-similar consecutive samples             |
| 7 | Max Samples           | Off     | Hard per-pixel sample cap; drops deepest first                    |

---

## Suggested Settings

### Light Touch (safe for final comp)
- Occlusion Cutoff: **0.9999**
- Contribution Cull: **0.0005**
- Smart Merge Z tolerance: **0.005**, color tolerance: **0.005**

### Moderate (good balance)
- Occlusion Cutoff: **0.999**
- Contribution Cull: **0.001**
- Smart Merge Z tolerance: **0.01**, color tolerance: **0.01**

### Aggressive (previews, layout, WIP)
- Occlusion Cutoff: **0.99**
- Contribution Cull: **0.01**
- Volumetric Collapse: **On**, group size **8**
- Smart Merge Z tolerance: **0.05**, color tolerance: **0.05**
- Max Samples: **64**

---

## Troubleshooting

| Problem                          | Solution                                                                 |
|----------------------------------|--------------------------------------------------------------------------|
| No reduction showing             | Ensure at least one pass is enabled. Check that input has deep data.     |
| Banding in volumes               | Reduce Volumetric Collapse group size or raise volume alpha max.         |
| Edge fringing on transparent obj | Lower Smart Merge color tolerance or disable merge for that section.     |
| Statistics say "No samples"      | Make sure you've rendered (not just validated). Click Update Statistics.  |
| Build error: NOMINMAX            | Ensure you're using the provided CMakeLists.txt with Windows defines.    |
| Build error: DeepOnlyOp.h        | Use DeepThinner v2.0 source — v1 targeted an older Nuke API.            |
| Plugin doesn't appear in menu    | Check that menu.py is in your ~/.nuke/ or NUKE_PATH directory.           |

---

## Compatibility

- **Nuke 16.0v1+** (built against the Nuke 16 NDK)
- Tested on Windows 10/11, CentOS/Rocky 8/9, macOS 13+
- Passes through all channels unchanged — safe for any deep pipeline

---

## Version History

### v2.0
- Seven independent thinning passes (added Depth Range, Occlusion Cutoff, Contribution Cull, Volumetric Collapse)
- Colour-aware smart merge
- In-panel statistics with Update button
- Artist Guide and Technical Notes in the UI
- Thread-local scratch buffers for zero-allocation processing
- Nuke 16 API (DeepFilterOp)

### v1.0
- Initial release with Z-tolerance merge, alpha cull, and max samples

---

## License

This plugin is provided as-is for use in production and personal projects. Created by Marten Blumen.
