from settings import settings
from enums import ScriptStateType


def is_script_state_used(state):
    if isinstance(settings, dict):
        if "process_kill_info" in settings:
            process_kill_info = settings.get("process_kill_info", {})
            if "processes" in process_kill_info:
                for process in process_kill_info["processes"]:
                    if isinstance(state, ScriptStateType):
                        state = state.value
                    if process.get("script_state") == state:
                        return True

        if "auto_move_windows" in settings:
            for window in settings["auto_move_windows"]:
                if isinstance(state, ScriptStateType):
                    state = state.value
                if window.get("script_state") == state:
                    return True

        if "alt_exe_methods" in settings:
            for method in settings["alt_exe_methods"]:
                if isinstance(state, ScriptStateType):
                    state = state.value
                if method.get("script_state") == state:
                    return True

    return False


def routine_checks(state):
    f'routine checks for the {state} are running'
    if is_script_state_used(state):
        from utilities import kill_processes
        kill_processes(state)
        from windows import window_checks
        window_checks(state)


class ScriptState():
    global script_state

    def set_script_state(new_state):
        global script_state
        script_state = new_state
        print(f'Script State changed to {new_state}')
        routine_checks(new_state)
        routine_checks(ScriptStateType.All)

    
    set_script_state(ScriptStateType.PRE_INIT)
