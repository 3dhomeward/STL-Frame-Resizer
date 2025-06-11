
# STL Frame Resizer

**Resize 3D frame parts by stretching only the center region — preserve connectors and precision features.**  
No Blender or CAD experience required.

## ✨ Features
- Drag-and-drop or browse to select `.stl` files
- Stretch along **X, Y, or Z axis**
- Keeps **14.5 mm fixed zones** at both ends
- Exports a resized STL instantly
- Clean, simple GUI — no command line needed

## 🧠 How It Works
This app segments your STL into three parts:
1. **Fixed Start** (14.5 mm)
2. **Middle Stretchable Region** (user-defined)
3. **Fixed End** (14.5 mm)

Only the middle is resized — ideal for modular frames, rails, and panel-based designs.

## 📂 Files Included

| File                    | Purpose                                |
|-------------------------|----------------------------------------|
| `stl_frame_resizer.pyw` | Python GUI script                      |
| `stl_frame_resizer.spec`| PyInstaller build config               |
| `README.md`             | This file                              |
| `LICENSE`               | Project license                        |

## ▶️ Running the App

**If you have Python installed:**

```bash
pip install trimesh numpy
```

Then double-click `stl_frame_resizer.pyw`

**To build the standalone .exe:**

```bash
pip install pyinstaller
pyinstaller stl_frame_resizer.spec
```

The `.exe` will be in `dist/stl_frame_resizer/`.

## 📷 Screenshot
*Include a screenshot of the app window here once ready*

## 📄 License

MIT License recommended — but feel free to use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) if preferred.

## 💬 Feedback & Issues

Open a GitHub issue or contact me via [your website or contact link].
