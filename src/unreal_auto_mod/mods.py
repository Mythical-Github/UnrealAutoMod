

def create_mods():
    from unreal_auto_mod import (
        engine,
        game_runner,
        packing,
        thread_game_monitor,
        utilities,
    )
    utilities.clean_working_dir()
    engine.toggle_engine_off()
    packing.make_mods()
    if not utilities.get_skip_launching_game():
        game_runner.run_game()
        thread_game_monitor.game_monitor_thread()
        engine.toggle_engine_on()
    utilities.clean_working_dir()
