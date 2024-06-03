import utilities
import thread_constant
import thread_game_monitor
from packing import make_mods
from game_runner import run_game
from enums import ScriptStateType
from script_states import ScriptState


def main():
    ScriptState.set_script_state(ScriptStateType.INIT)
    thread_constant.constant_thread()
    ScriptState.set_script_state(ScriptStateType.POST_INIT)
    utilities.clean_working_dir()
    make_mods()
    utilities.toggle_engine_off()
    if not utilities.get_skip_launching_game():
        run_game()
        thread_game_monitor.game_moniter_thread()
        utilities.toggle_engine_on()
    thread_constant.stop_constant_thread()
    utilities.clean_working_dir()


if __name__ == '__main__':
    main()
