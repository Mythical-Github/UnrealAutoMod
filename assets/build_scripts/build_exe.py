import os
import sys
import shutil
import subprocess


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)


src_dir = os.path.dirname(os.path.dirname(SCRIPT_DIR))

json_path = f"{SCRIPT_DIR}/UnrealAutoModCLI.json"
dist_dir = f"{SCRIPT_DIR}/dist"
build_dir = f"{SCRIPT_DIR}/build"
spec_file = f"{SCRIPT_DIR}/UnrealAutoModCLI.spec"
built_exe = f"{dist_dir}/UnrealAutoModCLI.exe"
placed_exe = f"{src_dir}/UnrealAutoModCLI.exe"

def run_pyinstaller():
    subprocess.run(["pyinstaller", "--onefile", json_path, "--distpath", dist_dir, "--noconfirm"], check=True)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def delete_directory(directory_path):
    if os.path.exists(directory_path):
        shutil.rmtree(directory_path)

def copy_file(src, dst):
    if os.path.exists(src):
        shutil.copy(src, dst)

def main():
    print(f"json_path: {json_path}")
    print(f"dist_dir: {dist_dir}")
    print(f"build_dir: {build_dir}")
    print(f"spec_file: {spec_file}")
    print(f"built_exe: {built_exe}")
    print(f"placed_exe: {placed_exe}")

    run_pyinstaller()

    delete_file(placed_exe)

    copy_file(built_exe, placed_exe)
    # delete_directory(dist_dir)
    # delete_directory(build_dir)
    delete_file(spec_file)


if __name__ == "__main__":
    main()
