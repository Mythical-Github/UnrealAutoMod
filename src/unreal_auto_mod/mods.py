

def create_mods():
    from unreal_auto_mod import enums
    from unreal_auto_mod import engine
    from unreal_auto_mod import packing
    from unreal_auto_mod import utilities
    from unreal_auto_mod import game_runner
    from unreal_auto_mod import script_states
    from unreal_auto_mod import thread_constant
    from unreal_auto_mod import thread_game_monitor
    
    script_states.ScriptState.set_script_state(enums.ScriptStateType.INIT)
    thread_constant.constant_thread()
    script_states.ScriptState.set_script_state(enums.ScriptStateType.POST_INIT)
    utilities.clean_working_dir()
    engine.toggle_engine_off()
    packing.make_mods()
    if not utilities.get_skip_launching_game():
        game_runner.run_game()
        thread_game_monitor.game_monitor_thread()
        engine.toggle_engine_on()
    thread_constant.stop_constant_thread()
    utilities.clean_working_dir()
