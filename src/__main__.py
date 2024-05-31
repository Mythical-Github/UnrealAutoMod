from sys import exit
import threads as threads
from packing import make_mods
from game_runner import run_game
from enums import ScriptStateType
from script_states import ScriptState, is_script_state_used


def main():
    ScriptState.set_script_state(ScriptStateType.INIT)
    threads.constant_thread()
    ScriptState.set_script_state(ScriptStateType.POST_INIT)
    make_mods()
    import utilities
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
    exit()
    