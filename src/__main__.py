import engine
import packing
import utilities
import game_runner
import script_states
import thread_constant
import thread_game_monitor
from enums import ScriptStateType


def main():
    script_states.ScriptState.set_script_state(ScriptStateType.INIT)
    thread_constant.constant_thread()
    script_states.ScriptState.set_script_state(ScriptStateType.POST_INIT)
    utilities.clean_working_dir()
    packing.make_mods()
    engine.toggle_engine_off()
    if not utilities.get_skip_launching_game():
        game_runner.run_game()
        thread_game_monitor.game_moniter_thread()
        engine.toggle_engine_on()
    thread_constant.stop_constant_thread()
    utilities.clean_working_dir()


if __name__ == '__main__':
    main()
