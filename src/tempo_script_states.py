from tempo_settings import settings
import tempo_utilities as utilities
from tempo_enums import ScriptStateType


def is_script_state_used_in_config(state):
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
    if is_script_state_used_in_config(state):
        utilities.kill_processes(state)


class ScriptState():
    global script_state

    def set_script_state(new_state):
        global script_state
        script_state = new_state
        print(f'Script State changed to {new_state}')
        routine_checks(new_state)
    
    set_script_state(ScriptStateType.INIT)
