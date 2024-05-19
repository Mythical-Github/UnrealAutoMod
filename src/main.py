import os
import sys
import tempo_enums as enum
import tempo_windows as windows
import tempo_packing as packing
import tempo_utilities as utilities
from tempo_settings import settings
import tempo_game_runner as game_runner


class ScriptState():
    global SCRIPT_STATE_TYPE
    global script_state
    SCRIPT_STATE_TYPE = enum.ScriptState
    script_state = SCRIPT_STATE_TYPE.INIT
    
    
    def set_script_state(new_state):
        script_state = new_state 


def routine_checks():
    pass


def main():
    game_runner.run_game()


if __name__ == '__main__':
    main()
    sys.exit()
