import sys
import tempo_threads as threads
import tempo_packing as packing
from tempo_game_runner import run_game
from tempo_enums import ScriptStateType
from tempo_script_states import ScriptState


def main():
    threads.start_constant_thread()
    ScriptState.set_script_state(ScriptStateType.POST_INIT)
    packing.pre_packaging()
    packing.post_packaging()
    packing.pre_pak_creation()
    packing.post_pack_creation()
    run_game()
    ScriptState.set_script_state(ScriptStateType.POST_GAME_LAUNCH)
    if threads.is_post_game_closed_enum_used_in_config:
        threads.start_game_monitor_thread()
        threads.game_monitor_thread.join()


if __name__ == '__main__':
    main()
    sys.exit()
