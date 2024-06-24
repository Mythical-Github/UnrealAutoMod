import script_states
import steam
import utilities
from enums import ScriptStateType, GameLaunchType, ExecutionMode


def run_game_exe():
    run_game_command = utilities.get_game_exe_path()
    for launch_param in utilities.get_game_launch_params():
        run_game_command = f'{run_game_command} {launch_param}'
    utilities.run_app(run_game_command, ExecutionMode.ASYNC)


def run_game_steam():
    if utilities.get_override_automatic_launcher_exe_finding():
        steam_exe = utilities.get_game_launcher_exe_path()
    else:
        steam_exe = steam.get_steam_exe_location()
    launch_params = utilities.get_game_launch_params()
    run_game_command = f'{steam_exe} -applaunch {utilities.get_game_id()}'
    for launch_param in launch_params:
        run_game_command = f'{run_game_command} {launch_param}'
    utilities.run_app(run_game_command, ExecutionMode.ASYNC)


def run_game():
    script_states.ScriptState.set_script_state(ScriptStateType.PRE_GAME_LAUNCH)
    launch_type = GameLaunchType(utilities.get_game_info_launch_type_enum_str_value())
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
