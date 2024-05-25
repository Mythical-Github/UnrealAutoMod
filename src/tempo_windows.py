import pygetwindow
from os import system
from screeninfo import get_monitors
from tempo_enums import WindowAction
from tempo_utilities import get_game_process_name


def does_window_exist(window_title, use_substring_check=False):
    if use_substring_check:
        all_window_titles = pygetwindow.getAllTitles()
        matched_windows = [window for window in all_window_titles if window_title in window]
        return len(matched_windows) > 0
    else:
        all_window_titles = pygetwindow.getWindowsWithTitle(window_title)
        return len(all_window_titles) > 0


def get_windows_by_title(window_title, use_substring_check=False):
    if use_substring_check:
        all_windows = pygetwindow.getAllWindows()
        matched_windows = [window for window in all_windows if window_title in window.title]
        return matched_windows
    else:
        matched_windows = pygetwindow.getWindowsWithTitle(window_title)
        return matched_windows


def get_window_by_title(window_title, use_substring_check=False):
    windows = get_windows_by_title(window_title, use_substring_check)
    if not windows:
        raise ValueError(f'No windows found with title "{window_title}"')
    return windows[0]


def minimize_window(window):
    pygetwindow.Window.minimize(window)


def maximize_window(window):
    pygetwindow.Window.maximize(window)


def close_window(window):
    pygetwindow.Window.close(window)


def move_window_to_moniter(window, monitor_index=0):
    screen_info = get_monitors()
    if monitor_index < len(screen_info):
        monitor = screen_info[monitor_index]
        window.moveTo(monitor.x, monitor.y)
    else:
        print('Invalid monitor index.')


def set_window_size(window, width, height):
    window.size = (width, height)


def change_window_name(window_name):
    system(f'title {window_name}')


def get_game_window():
    return get_window_by_title(get_game_process_name())


def window_checks(state):
    pass


def get_is_window_enum_used_in_config(window_action):
    pass
