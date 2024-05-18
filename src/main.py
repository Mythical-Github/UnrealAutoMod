import os
import sys
import tempo_enums as enum
import tempo_windows as windows
import tempo_packing as packing
import tempo_utilities as utilities
from tempo_settings import settings


class ScriptState():
    global SCRIPT_STATE_TYPE
    global script_state
    SCRIPT_STATE_TYPE = enum.ScriptState
    script_state = SCRIPT_STATE_TYPE.INIT
    
    
    def set_script_state(new_state):
        script_state = new_state 


def routine_checks():
    pass


def run_game():
    game_launch_type = enum.GameLaunchType
    launch_type = game_launch_type(settings['game_info']['launch_type'])
    if launch_type ==   game_launch_type.EXE:
        run_game_command = settings['game_info']['game_exe_path']
        launch_params = settings['game_info']['launch_params']
        for launch_param in launch_params:
            run_game_command = f'{run_game_command} {launch_param}'
        utilities.run_app(run_game_command, enum.ExecutionMode.ASYNC)
    elif launch_type == game_launch_type.STEAM: 
        steam_app_id = settings['game_info']['game_id']
        os.system(f'start steam://rungameid/{steam_app_id}')
    # elif launch_type == game_launch_type.EPIC:
    #     pass
    # elif launch_type == game_launch_type.ITCH_IO:
    #     pass
    # elif launch_type == game_launch_type.BATTLE_NET:
    #     pass
    # elif launch_type == game_launch_type.ORIGIN:
    #     pass
    # elif launch_type == game_launch_type.UBISOFT:
    #     pass
    else:
        raise ValueError('Unsupported launch_type specified in the settings.json under game_info[launch_type]')
        

def main():
    run_game()
    # kill_processes()
    # if windows.does_window_exist('Tempo', True):
    #     windows_to_manage = windows.get_windows_by_title('Tempo', True)
    #     for window in windows_to_manage:
    #         print("window")
    #         windows.move_window_to_moniter(window, 1)
    #         windows.set_window_size(window, 1550, 900)


if __name__ == '__main__':
    main()
    sys.exit()
