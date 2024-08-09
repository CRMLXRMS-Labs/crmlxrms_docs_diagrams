import os
import shutil


base_dir = "./"
docs_static_dir = os.path.join(base_dir, "crmlxrms_administration_concession_general/_docs/source/_static")

def copy_png_files(src, dst):
    for root, _, files in os.walk(src):
        for file in files:
            if file.endswith(".png"):
                src_file = os.path.join(root, file)
                
                relative_path = os.path.relpath(root, base_dir)
                dst_dir = os.path.join(dst, relative_path)
                os.makedirs(dst_dir, exist_ok=True)
                shutil.copy(src_file, os.path.join(dst_dir, file))
                print(f"Copied {src_file} to {os.path.join(dst_dir, file)}")

copy_png_files(base_dir, docs_static_dir)
