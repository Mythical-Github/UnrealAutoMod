import time
import threading
import tempo_windows as windows
import tempo_utilities as utilities
from tempo_enums import ScriptStateType
from tempo_script_states import ScriptState


def engine_moniter_thread():
    start_engine_monitor_thread()
    print('Engine monitering thread started')
    engine_monitor_thread.join()
    print('Engine monitering thread ended')  


def engine_monitor_thread_runner(tick_rate=0.1):
    while run_monitoring_thread:
        time.sleep(tick_rate)
        engine_monitor_thread_logic()


def engine_monitor_thread_logic():
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


    engine_window_name = utilities.get_engine_window_title()
    if not found_process:
        engine_process_name = utilities.get_engine_process_name()
        if utilities.is_process_running(engine_process_name):
            print('Found engine process running')
            found_process = True
    elif not found_window:
        if windows.does_window_exist(engine_window_name):
            print('Found engine window running')
            found_window = True
            ScriptState.set_script_state(ScriptStateType.POST_ENGINE_OPEN)
    elif not window_closed:
        if not windows.does_window_exist(engine_window_name):
            print('Engine window closed')
            window_closed = True
            ScriptState.set_script_state(ScriptStateType.POST_ENGINE_CLOSE)
            stop_engine_monitor_thread()


def start_engine_monitor_thread():
    global engine_monitor_thread
    global run_monitoring_thread
    run_monitoring_thread = True
    engine_monitor_thread = threading.Thread(target=engine_monitor_thread_runner, daemon=True)
    engine_monitor_thread.start()


def stop_engine_monitor_thread():
    global run_monitoring_thread
    run_monitoring_thread = False
