

def generate_mods():
    from unreal_auto_mod import engine, game_runner, packing, thread_game_monitor
    engine.toggle_engine_off()
    packing.cooking()
    packing.generate_mods()
    game_runner.run_game()
    thread_game_monitor.game_monitor_thread()
    engine.toggle_engine_on()
