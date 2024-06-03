import windows
import utilities
import alt_exe_runner
from settings import settings
from enums import ScriptStateType


def is_script_state_used(state: ScriptStateType) -> bool:
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

def routine_checks(state: ScriptStateType):
    if not state == ScriptStateType.CONSTANT:
        print(f'routine checks for the {state} are running')
    if is_script_state_used(state):
        utilities.kill_processes(state)
        windows.window_checks(state)
        alt_exe_runner.alt_exe_checks(state)
    if not state == ScriptStateType.CONSTANT:
        print(f'routine checks for the {state} finished')


class ScriptState():
    global script_state

    def set_script_state(new_state: ScriptStateType):
        global script_state
        script_state = new_state
        print(f'Script State changed to {new_state}')
        routine_checks(new_state)
        # calling this on preinit causes problems so will avoid for now
        if not new_state == ScriptStateType.PRE_INIT:
            routine_checks(ScriptStateType.PRE_ALL)
            routine_checks(ScriptStateType.POST_ALL)

    set_script_state(ScriptStateType.PRE_INIT)