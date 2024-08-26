

def create_mods():
    import enums
    import engine
    import packing
    import utilities
    import game_runner
    import script_states
    import thread_constant
    import thread_game_monitor
    
    script_states.ScriptState.set_script_state(enums.ScriptStateType.INIT)
    thread_constant.constant_thread()
    script_states.ScriptState.set_script_state(enums.ScriptStateType.POST_INIT)
    utilities.clean_working_dir()
    packing.make_mods()
    engine.toggle_engine_off()
    if not utilities.get_skip_launching_game():
        game_runner.run_game()
        thread_game_monitor.game_monitor_thread()
        engine.toggle_engine_on()
    thread_constant.stop_constant_thread()
    utilities.clean_working_dir()
