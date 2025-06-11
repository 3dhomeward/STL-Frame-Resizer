
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import trimesh
import numpy as np
import os

FIXED_START = 14.5
FIXED_END = 14.5

def stretch_stl(file_path, axis, stretch_value, output_path):
    mesh = trimesh.load_mesh(file_path)
    axis_idx = {'x': 0, 'y': 1, 'z': 2}[axis.lower()]
    min_bound = mesh.bounds[0][axis_idx]
    max_bound = mesh.bounds[1][axis_idx]

    start_limit = min_bound + FIXED_START
    end_limit = max_bound - FIXED_END

    vertices = mesh.vertices.copy()
    start_mask = vertices[:, axis_idx] <= start_limit
    end_mask = vertices[:, axis_idx] >= end_limit
    middle_mask = ~start_mask & ~end_mask

    scale_ratio = (end_limit - start_limit + stretch_value) / (end_limit - start_limit)
    vertices[middle_mask, axis_idx] = (
        (vertices[middle_mask, axis_idx] - start_limit) * scale_ratio + start_limit
    )
    vertices[end_mask, axis_idx] += stretch_value

    new_mesh = trimesh.Trimesh(vertices=vertices, faces=mesh.faces)
    new_mesh.export(output_path)

def select_file(entry_widget):
    path = filedialog.askopenfilename(filetypes=[("STL files", "*.stl")])
    if path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, path)

def export_file(input_path, axis, stretch_mm):
    if not input_path or not os.path.isfile(input_path):
        messagebox.showerror("Error", "Please select a valid STL file.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".stl", filetypes=[("STL files", "*.stl")])
    if save_path:
        try:
            stretch_value = float(stretch_mm)
            stretch_stl(input_path, axis, stretch_value, save_path)
            messagebox.showinfo("Success", f"File saved as:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to resize STL:\n{e}")

def create_app():
    root = tk.Tk()
    root.title("Selective STL Frame Resizer")
    root.geometry("400x250")
    root.resizable(False, False)

    tk.Label(root, text="STL File:").pack(pady=(10, 0))
    entry_path = tk.Entry(root, width=40)
    entry_path.pack(padx=10)
    tk.Button(root, text="Browse", command=lambda: select_file(entry_path)).pack(pady=(5, 10))

    tk.Label(root, text="Stretch Axis:").pack()
    axis_var = tk.StringVar(value='y')
    axis_menu = ttk.Combobox(root, textvariable=axis_var, values=['x', 'y', 'z'], state='readonly')
    axis_menu.pack()

    tk.Label(root, text="Stretch Amount (mm):").pack(pady=(10, 0))
    stretch_entry = tk.Entry(root)
    stretch_entry.pack()

    tk.Button(root, text="Resize and Export", command=lambda: export_file(entry_path.get(), axis_var.get(), stretch_entry.get())).pack(pady=15)

    root.mainloop()

if __name__ == "__main__":
    create_app()
