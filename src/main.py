import os
import os
import sys
import json
import glob
import psutil
import shutil
import msvcrt
import subprocess
import time
import pygetwindow as gw
import pyautogui
from screeninfo import get_monitors


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)


game_name = sys.argv[1]
preset_name = sys.argv[2]


SETTINGS_JSON = f"{SCRIPT_DIR}/../data/{game_name}/{preset_name}/settings.json"


with open(SETTINGS_JSON) as file:
    json_data = json.load(file)


WINDOW_TITLE = json_data["window_title"]
os.system(f"title {WINDOW_TITLE}")


def find_and_move_window(window_name, target_monitor, resolution):
    windows = gw.getWindowsWithTitle(window_name)

    if not windows:
        print(f"Window with name '{window_name}' not found.")
        return

    monitors = get_monitors()

    if target_monitor < 0 or target_monitor >= len(monitors):
        print(f"Invalid monitor index: {target_monitor}")
        return
        
    target_monitor_info = monitors[target_monitor]
    target_x, target_y = target_monitor_info.x, target_monitor_info.y
    
    window = windows[0]
    window.moveTo(target_x, target_y)
    window.resizeTo(resolution[0], resolution[1])


def find_and_move_all_windows():
    windows_data = json_data["auto_move_windows"]
    time.sleep(windows_data["wait_to_move_delay"])
    windows = windows_data["windows"]
    for window in windows:
        arg_1 = window["window_name"]
        arg_2 = window["monitor"]
        arg_3 = window["resolution"]["x"]
        arg_4 = window["resolution"]["y"]
        arg_5 = (arg_3, arg_4)
        find_and_move_window(arg_1, arg_2, arg_5)
        


use_alt_pak_creation_method = json_data["alt_pak_creation_method"]["use_alt_method"]
output_dir = json_data["paths"]["output_dir"]
uproject = json_data["paths"]["unreal_project_file"]
engine_dir = json_data["paths"]["unreal_engine_dir"]
game_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(json_data["paths"]["game_exe"])))))
uproject_dir = os.path.dirname(os.path.abspath(json_data["paths"]["unreal_project_file"]))
repak_pak_ver = json_data["repak_pak_ver"]
repak_exe = json_data["paths"]["repak_exe"]
packing_dir = f"{SCRIPT_DIR}/../data/{game_name}/{preset_name}/mod_packaging/temp"
uproject_name = os.path.basename(uproject)[:-9]

alt_uproject_name_in_game_dir = json_data["alt_uproject_name_in_game_dir"]["use_alt_method"]

if alt_uproject_name_in_game_dir == "True":

    alt_dir_name = json_data["alt_uproject_name_in_game_dir"]["name"]

    game_paks_dir = f"{game_dir}/{alt_dir_name}/Content/Paks"
else:
    game_paks_dir = f"{game_dir}/{uproject_name}/Content/Paks"

game_win64_exe = json_data["paths"]["game_exe"]
persistent_file_dir = f"{SCRIPT_DIR}/../data/{game_name}/{preset_name}/mod_packaging/persistent_files"
launch_method = json_data["launch_method"]
process_list = json_data["process_kill_list"]
mod_list_max = (len(json_data["mod_pak_list"]))
ue_version = json_data["unreal_engine_version"]
iostore = json_data["iostore"]


if ue_version.startswith("5"):
    win_dir_type = "Windows"
else:
    win_dir_type = "WindowsNoEditor"


output_content_dir = f"{output_dir}/{win_dir_type}/{uproject_name}/Content"


def print_possible_commands():
    print("""
Usage: python main.py <game_name> <preset_name> <script_arg>

Available script_args:
- 0 or run_ide
- 1 or run_fmodel
- 2 or run_blender
- 3 or open_game_dir
- 4 or open_uproject_dir
- 5 or open_downloads_dir
- 6 or test_mods_cooked
- 7 or test_mods_paks
- 8 or test_mods_both
- 9 or run_game
""")


if len(sys.argv) != 4:
    print_possible_commands()
    
    msvcrt.getch()
    
    sys.exit(1)

script_arg = sys.argv[3]

def run_app(application_path):
    try:
        subprocess.Popen(application_path)
    except Exception as e:
        print("An error occurred:", e)
        

def is_process_running(process_name):
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False





def open_dir_in_file_browser(path):
    try:
        if path != "":
            subprocess.Popen(['explorer', path])
        else:
            raise ValueError("Path variable is empty.")
    except Exception as e:
        print("An error occurred:", e)


def run_blender():
    run_app(json_data["paths"]["blender_exe"])


def run_ide():
    run_app(json_data["paths"]["ide_exe"])


def run_fmodel():
    run_app(json_data["paths"]["fmodel_exe"])


def open_game_dir():
    open_dir_in_file_browser(game_dir)
    

def open_uproject_dir():
    open_dir_in_file_browser(uproject_dir)


def open_downloads_dir():
    home_dir = os.path.expanduser("~")
    downloads_dir = f"{home_dir}\\Downloads"
    open_dir_in_file_browser(downloads_dir)
    
    
def test_mods_paks():
    print("This is not currently implemented")


def package_uproject_cooked():    
    os.chdir(engine_dir)
    command = f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun -project="{uproject}" -noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -cook -allmaps -stage -archive -archivedirectory="{output_dir}"'
    print(command)
    os.system(command)
 
def package_uproject_paks():    
    os.chdir(engine_dir)
    os.system(f'Engine\\Build\\BatchFiles\\RunUAT.bat BuildCookRun -project="{uproject}" -noP4 -platform=Win64 -clientconfig=Development -serverconfig=Development -cook -allmaps -stage -archive -archivedirectory={output_dir} -pak')
  

def copy_main_files_cooked():
    global pak_type
    pak_type = ""
    if not os.path.isdir(packing_dir):
        os.mkdir(packing_dir)       
    for i in range (mod_list_max):
        mod_entry = json_data["mod_pak_list"][i]
        status_entry = mod_entry["status"]
        entry = mod_entry["name"]
        self_made_pak = mod_entry["self_made_pak"]
        if self_made_pak == "True":
            if status_entry == "on":
                pak_type = mod_entry["pak_type"] 
                mod_files_to_copy = f"{output_content_dir}/Mods/{entry}"
                place_to_copy_to = f"{packing_dir}/{entry}/{uproject_name}/Content/Mods/{entry}"
                shutil.copytree(mod_files_to_copy, place_to_copy_to)
            else:
                mod_pak_type = mod_entry["pak_type"] 
                pak_type = mod_entry["pak_type"] 
                inactive_pak_file = f"{game_paks_dir}/{mod_pak_type}/{entry}.pak"
                print(inactive_pak_file)
                if os.path.isfile(inactive_pak_file):
                    os.remove(inactive_pak_file)
    

def copy_persistent_files():
    copy_tree((persistent_file_dir), packing_dir)


def get_file_extensions(file_path):
    # Extract the directory and file name without extension
    directory, file_name = os.path.split(file_path)
    
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return set()  # Return an empty set to indicate no valid extensions found

    file_name_no_ext, _ = os.path.splitext(file_name)

    try:
        # Get all files in the same directory that start with the same name
        matching_files = [f for f in os.listdir(directory) if f.startswith(file_name_no_ext)]
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return set()  # Return an empty set to indicate no valid extensions found

    # Extract unique extensions from matching files
    extensions = set(os.path.splitext(f)[1].lower() for f in matching_files)

    return extensions


def copy_manually_specified_files():
    if not os.path.isdir(packing_dir):
        os.mkdir(packing_dir)       
    for i in range (mod_list_max):
        mod_entry = json_data["mod_pak_list"][i]
        status_entry = mod_entry["status"]
        entry = mod_entry["name"]
        self_made_pak = mod_entry["self_made_pak"]
        manually_specified_files = mod_entry["manually_specified_files"]
        if status_entry == "on":
            if self_made_pak == "True":
                if len(manually_specified_files) > 0:
                    for manually_specified_file in manually_specified_files:
                        test = f"{output_dir}/{win_dir_type}/{uproject_name}/{manually_specified_file}"
                        file_extensions = get_file_extensions(test)
                        for file_extension in file_extensions:
                            mod_file_to_copy = f"{output_dir}/{win_dir_type}/{uproject_name}/{manually_specified_file}{file_extension}"
                            place_to_copy_to = f"{packing_dir}/{entry}/{uproject_name}/{manually_specified_file}{file_extension}"
                            os.makedirs(os.path.dirname(place_to_copy_to), exist_ok=True)
                            shutil.copy(mod_file_to_copy, place_to_copy_to)
                    

def copy_tree(src, dst, merge=True):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copy_tree(s, d, merge)
        else:
            if merge and os.path.exists(d):
                base, ext = os.path.splitext(d)
                counter = 1
                while os.path.exists(d):
                    d = f"{base}_{counter}{ext}"
                    counter += 1
            shutil.copy2(s, d)


def cleanup_files():
    if os.path.isdir(packing_dir):
        shutil.rmtree(packing_dir)


def make_and_move_paks():
    subfolders = [ f.path for f in os.scandir(packing_dir) if f.is_dir() ]
    for dir_to_pack in subfolders:
        pak_name = os.path.basename(dir_to_pack)
        pak_file = f"{pak_name}.pak"
        command = ""
        
        if use_alt_pak_creation_method == "True":
            for i in range (mod_list_max):
                mod_entry = json_data["mod_pak_list"][i]
                mod_name = mod_entry["name"]
                mod_status = mod_entry["status"]
                if mod_status == "on":
                    alt_exe = json_data["alt_pak_creation_method"]["alt_exe_path"]
                    args = json_data["alt_pak_creation_method"]["variable_args"]
                    
                    command = f'"{alt_exe}" '
                    
                    for arg in args:
                        if arg == "/" or arg == " ":
                            command = f"{command}{arg}"
                        else:
                            if arg == '""':
                                command = f'{command}"'
                            else:                    
                                variable_value = locals().get(arg)
                                if variable_value is not None:
                                    command = f"{command}{variable_value}"
                                else:
                                    variable_value = globals().get(arg)
                                    if variable_value is not None:
                                        command = f"{command}{variable_value}"
                                    else:
                                        print(f"Error: Variable '{arg}' not found")
                                        
            if not command == "":
                subprocess.run(command, check=True)
        else:
            command = [repak_exe, "pack", "--version", repak_pak_ver, dir_to_pack]
            subprocess.run(command, check=True)
        try:
            for i in range (mod_list_max):
                mod_entry = json_data["mod_pak_list"][i]
                mod_name = mod_entry["name"]
                mod_status = mod_entry["status"]
                if mod_status == "on":
                    if mod_name == pak_name:
                        mod_pak_type = mod_entry["pak_type"]
                        mod_pak_type_dir = f"{game_paks_dir}/{mod_pak_type}"
                        if not os.path.isdir(mod_pak_type_dir):
                            os.mkdir(mod_pak_type_dir)
                        output_pak = f"{game_paks_dir}/{mod_pak_type}/{pak_name}.pak"
                        if not use_alt_pak_creation_method == "True":
                            new_pak = f"{packing_dir}/{pak_file}"
                            if os.path.isfile(output_pak):
                                os.remove(output_pak)
                            shutil.copy(new_pak, output_pak)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")     


def kill_processes():
    for process in process_list:
        if is_process_running(process):
            os.system(f'taskkill /f /im "{process}"')
            

def run_game():
    if launch_method == "win64_exe":
        run_game_command = game_win64_exe
        launch_params = json_data["extra_launch_params"]
        for launch_param in launch_params:
            run_game_command = f"{run_game_command} {launch_param}"
        subprocess.Popen(run_game_command)
    if launch_method == "steam":
        steam_app_id = json_data["steam_game_app_id"]
        os.system(f"start steam://rungameid/{steam_app_id}")
    find_and_move_all_windows()


def copy_pak_files_paks():
    if not os.path.isdir(packing_dir):
        os.mkdir(packing_dir)       
    for i in range (mod_list_max):
        mod_entry = json_data["mod_pak_list"][i]
        status_entry = mod_entry["status"]
        entry = mod_entry["name"]
        self_made_pak = mod_entry["self_made_pak"]
        mod_pak_type = mod_entry["pak_type"]
        pak_chunk_num = mod_entry["pak_chunk_num"]
        
        if iostore == "True":
             file_extensions = [
            ".pak",
            ".utoc",
            ".ucas"        
            ]           
        else:
            file_extensions = [
            ".pak"     
            ]
        
        for file_extension in file_extensions:
            pak_name = entry
            pak_file = f"{pak_name}{file_extension}"
            old_file = f"{game_paks_dir}/{mod_pak_type}/{pak_name}{file_extension}"
            new_file = f"{output_dir}/{win_dir_type}/{uproject_name}/Content/Paks/pakchunk{pak_chunk_num}-{win_dir_type}{file_extension}"

            
            directory_path = f"{game_paks_dir}/{mod_pak_type}"
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            
            
            if status_entry == "on":
                if self_made_pak != "True":
                    shutil.copy(new_file, old_file)
            if status_entry == "off":
                if self_made_pak != "True":
                    if os.path.isfile(old_file):
                        os.remove(old_file)


def test_mods_cooked():
    kill_processes()
    cleanup_files()
    package_uproject_cooked()
    copy_main_files_cooked()
    copy_persistent_files()
    copy_manually_specified_files()
    make_and_move_paks()
    cleanup_files()
    run_game()
    
    
def test_mods_paks():
    kill_processes()
    cleanup_files()
    package_uproject_paks()
    copy_pak_files_paks()
    cleanup_files()
    run_game()
    

def test_mods_both():
    kill_processes()
    cleanup_files()
    package_uproject_cooked()
    package_uproject_paks()
    copy_main_files_cooked()
    copy_persistent_files()
    copy_manually_specified_files()
    make_and_move_paks()
    copy_pak_files_paks()
    cleanup_files()
    run_game()


def main():
    script_args = {
        'run_ide': run_ide,
        'run_fmodel': run_fmodel,
        'run_blender': run_blender,
        'open_game_dir': open_game_dir,
        'open_uproject_dir': open_uproject_dir,
        'open_downloads_dir': open_downloads_dir,
        'test_mods_cooked': test_mods_cooked,
        'test_mods_paks': test_mods_paks,
        'test_mods_both': test_mods_both,
        'run_game': run_game
    }

    if script_arg in script_args:
        script_args[script_arg]()
    elif script_arg.isdigit():
        index = int(script_arg)
        if 0 <= index < len(script_args):
            script_arg_names = list(script_args.keys())
            selected_script_arg = script_arg_names[index]
            script_args[selected_script_arg]()
        else:
            print_possible_commands()
    else:
        print_possible_commands()


if __name__ == "__main__":
    main()
    sys.exit()
