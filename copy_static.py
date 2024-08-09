import os
import shutil
import sys

base_dir = "./"
docs_static_dir = os.path.join(base_dir, "crmlxrms_administration_concession_general/_docs/source/_static")

def print_progress_bar(iteration, total, length=40):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '=' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent}% Complete')
    sys.stdout.flush()

def copy_png_files(src, dst):

    if os.path.abspath(dst) == os.path.abspath(src):
        print("Error: The destination directory cannot be the same as the source directory.")
        return

    total_files = sum(len(files) for _, _, files in os.walk(src) if any(f.endswith(".png") for f in files))
    copied_files = 0

    for root, _, files in os.walk(src):
        for file in files:
            if file.endswith(".png"):
                src_file = os.path.join(root, file)
                if os.path.abspath(dst) in os.path.abspath(root):
                    continue
                relative_path = os.path.relpath(root, base_dir)
                dst_dir = os.path.join(dst, relative_path)
                os.makedirs(dst_dir, exist_ok=True)
                shutil.copy(src_file, os.path.join(dst_dir, file))
                copied_files += 1
                print_progress_bar(copied_files, total_files)
    
    print_progress_bar(total_files, total_files)
    print()  

copy_png_files(base_dir, docs_static_dir)
