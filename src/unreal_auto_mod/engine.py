from unreal_auto_mod import gen_py_utils as general_utils
from unreal_auto_mod import hook_states, thread_engine_monitor, ue_dev_py_utils, utilities
from unreal_auto_mod.enums import ExecutionMode, HookStateType, PackagingDirType


def open_game_engine():
    hook_states.set_hook_state(HookStateType.PRE_ENGINE_OPEN)
    command = ue_dev_py_utils.get_unreal_editor_exe_path(utilities.get_unreal_engine_dir())
    utilities.run_app(command, ExecutionMode.ASYNC, utilities.get_engine_launch_args())
    hook_states.set_hook_state(HookStateType.POST_ENGINE_OPEN)
    thread_engine_monitor.engine_monitor_thread()


def close_game_engine():
    hook_states.set_hook_state(HookStateType.PRE_ENGINE_CLOSE)
    if ue_dev_py_utils.get_win_dir_type(utilities.get_unreal_engine_dir()) == PackagingDirType.WINDOWS_NO_EDITOR:
        game_engine_processes = general_utils.get_processes_by_substring('UE4Editor')
    else:
        game_engine_processes = general_utils.get_processes_by_substring('UnrealEditor')
    for process_info in game_engine_processes:
        general_utils.kill_process(process_info['name'])
    hook_states.set_hook_state(HookStateType.POST_ENGINE_CLOSE)


def toggle_engine_off():
    if utilities.is_toggle_engine_during_cooking_in_use():
        close_game_engine()


def toggle_engine_on():
    if utilities.is_toggle_engine_during_cooking_in_use():
        open_game_engine()
