import time
import windows
import threading
import utilities
import script_states
from enums import ScriptStateType


found_process = False
found_window = False
window_closed = False
run_monitoring_thread = False
game_monitor_thread = ''


def game_monitor_thread_runner(tick_rate: float = 0.1):
    while run_monitoring_thread:
        time.sleep(tick_rate)
        game_monitor_thread_logic()


def game_monitor_thread_logic():
    global found_process
    global found_window
    global window_closed

    if not found_process:
        if utilities.is_process_running(utilities.get_game_process_name()):
            print('Found game process running')
            found_process = True
    elif not found_window:
        if windows.get_game_window():
            print('Found game window running')
            found_window = True
            script_states.ScriptState.set_script_state(ScriptStateType.POST_GAME_LAUNCH)
    elif not window_closed:
        if not windows.get_game_window():
            print('Game window closed')
            script_states.ScriptState.set_script_state(ScriptStateType.POST_GAME_CLOSE)
            stop_game_monitor_thread()
            window_closed = True


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
    start_game_monitor_thread()
    print('game monitering thread started')
    game_monitor_thread.join()
    print('game monitering thread ended')  
