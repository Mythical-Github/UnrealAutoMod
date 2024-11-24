from unreal_auto_mod import log_py as log
from unreal_auto_mod import main_logic, utilities, win_man_enums, win_man_py
from unreal_auto_mod import win_man_py as windows
from unreal_auto_mod.enums import ExecutionMode, HookStateType, get_enum_from_val

hook_state = None


def exec_events_checks(hook_state_type: HookStateType):
    exec_events = utilities.get_exec_events()
    for exec_event in exec_events:
        value = exec_event['hook_state']
        exe_state = get_enum_from_val(HookStateType, value)
        if exe_state == hook_state_type:
            exe_path = exec_event['alt_exe_path']
            exe_args = exec_event['variable_args']
            exe_exec_mode = get_enum_from_val(ExecutionMode, exec_event['execution_mode'])
            utilities.run_app(exe_path, exe_exec_mode, exe_args)


def is_hook_state_used(state: HookStateType) -> bool:
    if isinstance(main_logic.settings, dict):
        if "process_kill_events" in main_logic.settings:
            process_kill_events = main_logic.settings.get("process_kill_events", {})
            if "processes" in process_kill_events:
                for process in process_kill_events["processes"]:
                    if isinstance(state, HookStateType):
                        state = state.value
                    if process.get('hook_state') == state:
                        return True

        if "window_management_events" in main_logic.settings:
            for window in utilities.get_window_management_events():
                if isinstance(state, HookStateType):
                    state = state.value
                if window.get("hook_state") == state:
                    return True

        if "exec_events" in main_logic.settings:
            for method in utilities.get_exec_events():
                if isinstance(state, HookStateType):
                    state = state.value
                if method.get("hook_state") == state:
                    return True

    return False


def window_checks(current_state: win_man_enums.WindowAction):
    window_settings_list = utilities.get_window_management_events()
    for window_settings in window_settings_list:
        settings_state = get_enum_from_val(HookStateType, window_settings['hook_state'])
        if settings_state == current_state:
            title = window_settings['window_name']
            windows_to_change = win_man_py.get_windows_by_title(title)
            for window_to_change in windows_to_change:
                way_to_change_window = get_enum_from_val(win_man_enums.WindowAction, window_settings['window_behaviour'])
                if way_to_change_window == win_man_enums.WindowAction.MAX:
                    windows.maximize_window(window_to_change)
                elif way_to_change_window == win_man_enums.WindowAction.MIN:
                    windows.minimize_window(window_to_change)
                elif way_to_change_window == win_man_enums.WindowAction.CLOSE:
                    windows.close_window(window_to_change)
                elif way_to_change_window == win_man_enums.WindowAction.MOVE:
                    windows.move_window(window_to_change, window_settings)
                else:
                    log.log_message('Monitor: invalid window behavior specified in settings')


def routine_checks(state: HookStateType):
    if state != HookStateType.CONSTANT:
        log.log_message(f'Routine Check: {state} is running')
    if is_hook_state_used(state):
        utilities.kill_processes(state)
        window_checks(state)
        exec_events_checks(state)
    if state != HookStateType.CONSTANT:
        log.log_message(f'Routine Check: {state} finished')


def set_hook_state(new_state: HookStateType):
    global hook_state
    hook_state = new_state
    log.log_message(f'Hook State: changed to {new_state}')
    # calling this on preinit causes problems so will avoid for now
    if new_state != HookStateType.PRE_INIT:
        routine_checks(new_state)
        routine_checks(HookStateType.PRE_ALL)
        routine_checks(HookStateType.POST_ALL)
        log.log_message(f'Timer: Time since script execution: {utilities.get_running_time()}')
