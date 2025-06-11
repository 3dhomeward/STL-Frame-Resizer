
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
![2025-06-10 (2)](https://github.com/user-attachments/assets/3e947eb5-ef46-429b-bb37-9741780226ff)

## 📄 License

Apache 2.0

## 💬 Feedback & Issues

Open a GitHub issue or contact me via email sjames@csandra3d.com.
