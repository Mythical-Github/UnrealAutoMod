import settings
import utilities
import windows
from enums import ExecutionMode, ScriptStateType, get_enum_from_val


def alt_exe_checks(script_state_type: ScriptStateType):
    alt_exe_methods = utilities.get_alt_exe_methods()
    for alt_exe_method in alt_exe_methods:
        value = alt_exe_method['script_state']
        exe_state = get_enum_from_val(ScriptStateType, value)
        if exe_state == script_state_type:
            exe_path = alt_exe_method['alt_exe_path']
            exe_args = alt_exe_method['variable_args']
            exe_exec_mode = get_enum_from_val(ExecutionMode, alt_exe_method['execution_mode'])
            utilities.run_app(exe_path, exe_exec_mode, exe_args)


def is_script_state_used(state: ScriptStateType) -> bool:
    if isinstance(settings.settings, dict):
        if "process_kill_info" in settings.settings:
            process_kill_info = settings.settings.get("process_kill_info", {})
            if "processes" in process_kill_info:
                for process in process_kill_info["processes"]:
                    if isinstance(state, ScriptStateType):
                        state = state.value
                    if process.get("script_state") == state:
                        return True

        if "auto_move_windows" in settings.settings:
            for window in utilities.get_auto_move_windows():
                if isinstance(state, ScriptStateType):
                    state = state.value
                if window.get("script_state") == state:
                    return True

        if "alt_exe_methods" in settings.settings:
            for method in utilities.get_alt_exe_methods():
                if isinstance(state, ScriptStateType):
                    state = state.value
                if method.get("script_state") == state:
                    return True

    return False


def routine_checks(state: ScriptStateType):
    if not state == ScriptStateType.CONSTANT:
        print(f'routine checks for the {state} are running')
    if is_script_state_used(state):
        utilities.kill_processes(state)
        windows.window_checks(state)
        alt_exe_checks(state)
    if not state == ScriptStateType.CONSTANT:
        print(f'routine checks for the {state} finished')


class ScriptState():
    global script_state

    def set_script_state(new_state: ScriptStateType):
        global script_state
        script_state = new_state
        print(f'Script State changed to {new_state}')
        # calling this on preinit causes problems so will avoid for now
        if not new_state == ScriptStateType.PRE_INIT:
            routine_checks(new_state)
            routine_checks(ScriptStateType.PRE_ALL)
            routine_checks(ScriptStateType.POST_ALL)

    # set_script_state(ScriptStateType.PRE_INIT)
