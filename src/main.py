import sys
import tempo_threads as threads
import tempo_packing as packing
from tempo_game_runner import run_game
from tempo_script_states import ScriptState
from tempo_enums import ScriptState as script_state


def main():
    threads.start_constant_thread()
    ScriptState.set_script_state(script_state.POST_INIT)
    packing.pre_packaging()
    packing.post_packaging()
    packing.pre_pak_creation()
    packing.post_pack_creation()
    ScriptState.set_script_state(script_state.PRE_GAME_LAUNCH)
    run_game()
    ScriptState.set_script_state(script_state.POST_GAME_LAUNCH)
    if threads.is_post_game_closed_enum_used_in_config:
        threads.start_game_monitor_thread()
        threads.game_monitor_thread.join()


if __name__ == '__main__':
    main()
    sys.exit()
