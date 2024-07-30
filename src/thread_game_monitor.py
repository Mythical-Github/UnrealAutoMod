import threading
import time

import script_states
import utilities
import windows
from enums import ScriptStateType
import log

found_process = False
found_window = False
window_closed = False
run_monitoring_thread = False
game_monitor_thread = ''


def game_monitor_thread_runner(tick_rate: float = 0.01):
    while run_monitoring_thread:
        time.sleep(tick_rate)
        game_monitor_thread_logic()


def game_monitor_thread_logic():
    global found_process
    global found_window
    global window_closed

    if not found_process:
        if utilities.is_process_running(utilities.get_game_process_name()):
            log.log_message('Process: Found Game Process')
            found_process = True
    elif not found_window:
        if windows.get_game_window():
            log.log_message('Window: Game Window Found')
            found_window = True
            script_states.ScriptState.set_script_state(ScriptStateType.POST_GAME_LAUNCH)
    elif not window_closed:
        if not windows.get_game_window():
            log.log_message('Window: Game Window Closed')
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


def game_monitor_thread():
    start_game_monitor_thread()
    log.log_message('Thread: Game Monitoring Thread Started')
    game_monitor_thread.join()
    log.log_message('Thread: Game Monitoring Thread Ended')
