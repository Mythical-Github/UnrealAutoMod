import settings
import routine_checks
from enums import ScriptStateType


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
            for window in settings.settings["auto_move_windows"]:
                if isinstance(state, ScriptStateType):
                    state = state.value
                if window.get("script_state") == state:
                    return True

        if "alt_exe_methods" in settings.settings:
            for method in settings.settings["alt_exe_methods"]:
                if isinstance(state, ScriptStateType):
                    state = state.value
                if method.get("script_state") == state:
                    return True

    return False


class ScriptState():
    global script_state

    def set_script_state(new_state: ScriptStateType):
        global script_state
        script_state = new_state
        print(f'Script State changed to {new_state}')
        routine_checks.routine_checks(new_state)
        # calling this on preinit causes problems so will avoid for now
        if not new_state == ScriptStateType.PRE_INIT:
            routine_checks.routine_checks(ScriptStateType.PRE_ALL)
            routine_checks.routine_checks(ScriptStateType.POST_ALL)

    set_script_state(ScriptStateType.PRE_INIT)