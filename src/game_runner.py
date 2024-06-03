import steam
import settings
import utilities
import script_states
from enums import ScriptStateType, GameLaunchType, ExecutionMode


def get_override_automatic_launcher_exe_finding() -> bool:
    return settings.settings['game_info']['override_automatic_launcher_exe_finding']


def run_game_exe():
    run_game_command = settings.settings['game_info']['game_exe_path']
    launch_params = settings.settings['game_info']['launch_params']
    for launch_param in launch_params:
        run_game_command = f'{run_game_command} {launch_param}'
    utilities.run_app(run_game_command, ExecutionMode.ASYNC)


def run_game_steam():
    if get_override_automatic_launcher_exe_finding():
        steam_exe = settings.settings['game_info']['game_launcher_exe']
    else:
        steam_exe = steam.get_steam_exe_location()
    steam_app_id = settings.settings['game_info']['game_id']
    launch_params = settings.settings['game_info']['launch_params']
    run_game_command = f'{steam_exe} -applaunch {steam_app_id}'
    for launch_param in launch_params:
        run_game_command = f'{run_game_command} {launch_param}'
    utilities.run_app(run_game_command, ExecutionMode.ASYNC)


def run_game():
    script_states.ScriptState.set_script_state(ScriptStateType.PRE_GAME_LAUNCH)
    launch_type = GameLaunchType(settings.settings['game_info']['launch_type'])
    if launch_type == GameLaunchType.EXE:
        run_game_exe()
    elif launch_type == GameLaunchType.STEAM:
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
        raise ValueError('Unsupported launch_type specified in the settings.json')
