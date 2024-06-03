import time
import threading
import windows as windows
import utilities as utilities
from enums import ScriptStateType
from script_states import ScriptState


init_done = False


def game_monitor_thread_runner(tick_rate: float = 0.1):
    while run_monitoring_thread:
        time.sleep(tick_rate)
        game_monitor_thread_logic()


def game_monitor_thread_logic():
    global found_process
    global found_window
    global window_closed
    global init_done

    
    try:
        if not init_done:
            found_process = False
            found_window = False
            window_closed = False
            init_done = True
    except NameError:
            found_process = False
            found_window = False
            window_closed = False
            init_done = True

    game_window_name = utilities.get_game_window_title()
    if not found_process:
        game_process_name = utilities.get_game_process_name()
        if utilities.is_process_running(game_process_name):
            print('Found game process running')
            found_process = True
    elif not found_window:
        if windows.does_window_exist(game_window_name):
            print('Found game window running')
            found_window = True
            ScriptState.set_script_state(ScriptStateType.POST_GAME_LAUNCH)
    elif not window_closed:
        if not windows.does_window_exist(game_window_name):
            print('Game window closed')
            window_closed = True
            ScriptState.set_script_state(ScriptStateType.POST_GAME_CLOSE)
            stop_game_monitor_thread()


def start_game_monitor_thread():
    global game_monitor_thread
    global run_monitoring_thread
    run_monitoring_thread = True
    game_monitor_thread = threading.Thread(target=game_monitor_thread_runner, daemon=True)
    game_monitor_thread.start()


def stop_game_monitor_thread():
    global run_monitoring_thread
    run_monitoring_thread = False


def game_moniter_thread():
    # later on have this only activate when
    start_game_monitor_thread()
    print('game monitering thread started')
    game_monitor_thread.join()
    print('game monitering thread ended')  