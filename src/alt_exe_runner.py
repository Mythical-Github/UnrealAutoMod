from utilities import run_app
from settings import settings
from enums import ExecutionMode, ScriptStateType, get_enum_from_val


def alt_exe_checks(script_state_type: ScriptStateType):
    alt_exe_methods = settings['alt_exe_methods']
    for alt_exe_method in alt_exe_methods:
        value = alt_exe_method['script_state']
        exe_state = get_enum_from_val(ScriptStateType, value)
        if exe_state == script_state_type:
            exe_path = alt_exe_method['alt_exe_path']
            exe_args = alt_exe_method['variable_args']
            exe_exec_mode = alt_exe_method['execution_mode']
            exe_exec_mode = get_enum_from_val(ExecutionMode, exe_exec_mode)
            run_app(exe_path, exe_exec_mode, exe_args)
