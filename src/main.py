import sys
import tempo_threads as threads
import tempo_packing as packing
from tempo_game_runner import run_game
from tempo_enums import ScriptStateType
from tempo_script_states import ScriptState


def main():
    threads.constant_thread()
    ScriptState.set_script_state(ScriptStateType.POST_INIT)
    packing.pre_packaging()
    packing.post_packaging()
    packing.pre_pak_creation()
    packing.post_pak_creation()
    run_game()
    threads.game_moniter_thread()


if __name__ == '__main__':
    main()
    sys.exit()
