import windows
import utilities
import script_states
import alt_exe_runner
from enums import ScriptStateType


def routine_checks(state: ScriptStateType):
    if not state == ScriptStateType.CONSTANT:
        print(f'routine checks for the {state} are running')
    if script_states.is_script_state_used(state):
        utilities.kill_processes(state)
        windows.window_checks(state)
        alt_exe_runner.alt_exe_checks(state)
    if not state == ScriptStateType.CONSTANT:
        print(f'routine checks for the {state} finished')