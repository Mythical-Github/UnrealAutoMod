import tempo_enums as enum


class ScriptState():
    global script_state
    script_state = enum.ScriptStateType.INIT
    
    def set_script_state(new_state):
        global script_state
        script_state = new_state
        print(f'Script State changed to {new_state}')


def routine_checks(script_state):
    # print('ran routine checks')
    pass
