import tempo_enums as enum


class ScriptState():
    global script_state
    script_state = enum.ScriptState.INIT
    
    def set_script_state(new_state):
        global script_state
        script_state = new_state


def routine_checks():
    print('ran routine checks')
    pass
