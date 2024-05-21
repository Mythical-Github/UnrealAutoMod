import tempo_enums as enum
from tempo_settings import settings
import tempo_utilities as utilities
from tempo_script_states import ScriptState


def run_game_exe():
    run_game_command = settings['game_info']['game_exe_path']
    launch_params = settings['game_info']['launch_params']
    for launch_param in launch_params:
        run_game_command = f'{run_game_command} {launch_param}'
    utilities.run_app(run_game_command, enum.ExecutionMode.ASYNC)
    ScriptState.set_script_state(enum.ScriptState.POST_GAME_LAUNCH)

def run_game_steam():
    steam_exe = settings['game_info']['game_launcher_exe']
    steam_app_id = settings['game_info']['game_id']
    launch_params = settings['game_info']['launch_params']
    run_game_command = f'{steam_exe} -applaunch {steam_app_id}'
    for launch_param in launch_params:
        run_game_command = f'{run_game_command} {launch_param}'
    utilities.run_app(run_game_command, enum.ExecutionMode.ASYNC)
    ScriptState.set_script_state(enum.ScriptState.POST_GAME_LAUNCH)


def run_game():
    game_launch_type = enum.GameLaunchType
    launch_type = game_launch_type(settings['game_info']['launch_type'])
    if launch_type ==   game_launch_type.EXE:
        run_game_exe()
    elif launch_type == game_launch_type.STEAM:
        run_game_steam()
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
