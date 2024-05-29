
make sure packaging steps aren't ran unless they're used in the config
use the queue for the above thing
logic for PackingType enums
logic for pak making, moving, and cleanup functions

loose file
unreal pak
engine pak
repak




def stuff():
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
    persistent_file_dir = f"{SCRIPT_DIR}/../data/{game_name}/{preset_name}/mod_packaging/persistent_files"
    mod_list_max = (len(json_data["mod_pak_list"]))
    output_content_dir = f"{output_dir}/{win_dir_type}/{uproject_name}/Content"


def copy_main_files_cooked():
    global pak_type
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


def test_mods_both():
    copy_main_files_cooked()
    copy_persistent_files()
    copy_manually_specified_files()
    make_and_move_paks()
    copy_pak_files_paks()   


LATER:
settings configurator
log file creation
in editor gui editor utility widget
C++ editor widget
logic for settings['engine_info']['fix_up_redirectors_on_proj_open']
engine close enums fire even when engine waszn't actually closed
timeouts to various functions that use them in the settings json
