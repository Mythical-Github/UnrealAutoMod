import time
import threading
import tempo_windows as windows
import tempo_settings as settings
import tempo_utilities as utilities
from tempo_enums import ScriptStateType
from tempo_script_states import routine_checks



def is_constant_enum_used_in_config():
    auto_move_windows = settings.get("auto_move_windows", [])
    for window in auto_move_windows:
        if window.get("script_state") == "constant":
            return True
    return False


def is_post_game_closed_enum_used_in_config():
    auto_move_windows = settings.get("auto_move_windows", [])
    for window in auto_move_windows:
        if window.get("script_state") == "post_game_closed":
            return True
    return False


def constant_thread_runner(tick_rate=0.1):
    while True:
        time.sleep(tick_rate)
        constant_thread_logic()
        

def constant_thread_logic():
    routine_checks(ScriptStateType.CONSTANT)


def start_constant_thread():
    if is_constant_enum_used_in_config:
        global constant_thread
        constant_thread = threading.Thread(target=constant_thread_runner, daemon=True)
        constant_thread.start()
    else:
        print('The constant thread was not used in the config, so it was never started')


def game_monitor_thread_runner(tick_rate=0.1):
    while run_monitoring_thread:
        time.sleep(tick_rate)
        game_monitor_thread_logic()


def game_monitor_thread_logic():
    game_window_name = utilities.get_game_process_name()
    
    print(f"Monitoring game window: {game_window_name}")
    
    while True:
        try:
            game_window = windows.get_game_window()
            print(f"Game window '{game_window_name}' is still open.")

        except ValueError:

            print(f"Game window '{game_window_name}' has closed.")
            break

        time.sleep(1)


def start_game_monitor_thread():
    global game_monitor_thread
    global run_monitoring_thread
    run_monitoring_thread = True
    game_monitor_thread = threading.Thread(target=game_monitor_thread_runner, daemon=True)
    game_monitor_thread.start()


def stop_game_monitor_thread():
    global run_monitoring_thread
    run_monitoring_thread = False
    if game_monitor_thread.is_alive():
        game_monitor_thread.join()
