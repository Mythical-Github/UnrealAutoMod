import thread_constant
import thread_game_monitor
from packing import make_mods
from game_runner import run_game
from enums import ScriptStateType
from script_states import ScriptState
from utilities import toggle_engine_off, toggle_engine_on, clean_working_dir, get_skip_launching_game


def main():
    ScriptState.set_script_state(ScriptStateType.INIT)
    thread_constant.constant_thread()
    ScriptState.set_script_state(ScriptStateType.POST_INIT)
    clean_working_dir()
    make_mods()    
    toggle_engine_off()
    if not get_skip_launching_game():   
        run_game()
        thread_game_monitor.game_moniter_thread()
        toggle_engine_on()
    thread_constant.stop_constant_thread()
    clean_working_dir()


if __name__ == '__main__':
    main()
