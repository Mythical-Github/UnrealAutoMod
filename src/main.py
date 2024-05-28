import sys
import tempo_threads as threads
import tempo_packing as packing
from tempo_game_runner import run_game
from tempo_enums import ScriptStateType
from tempo_script_states import ScriptState, is_script_state_used


def main():
    ScriptState.set_script_state(ScriptStateType.INIT)
    threads.constant_thread()
    ScriptState.set_script_state(ScriptStateType.POST_INIT)
    packing.pre_packaging()
    packing.post_packaging()
    packing.pre_pak_creation()
    packing.post_pak_creation()
    import tempo_utilities as utilities
    if utilities.is_toggle_engine_during_testing_in_use():
        utilities.close_game_engine()
    run_game()
    threads.game_moniter_thread()
    if utilities.is_toggle_engine_during_testing_in_use():
        utilities.open_game_engine()
        from engine_moniter import engine_moniter_thread
        engine_moniter_thread()
    if is_script_state_used(ScriptStateType.CONSTANT):
        threads.stop_constant_thread()


if __name__ == '__main__':
    main()
    sys.exit()
    