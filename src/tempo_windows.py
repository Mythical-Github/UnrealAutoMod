import os
import screeninfo
import pygetwindow


def does_window_exist(window_title, use_substring_check=False):
    if use_substring_check:
        all_windows_titles = pygetwindow.getAllTitles()
        matched_windows = []
        for window in all_windows_titles:
            if window_title in window:
                matched_windows.append(window_title)
        if len(matched_windows) <= 0:
            return False
        else:
            return True
    else:
        all_windows_titles = pygetwindow.getWindowsWithTitle(window_title)
        if len(all_windows_titles) <= 0:
            return False
        else:
            return True


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
        raise ValueError(f"No windows found with title '{window_title}'")
    return windows[0]


def minimize_window(window):
    pygetwindow.Window.minimize(window)


def maximize_window(window):
    pygetwindow.Window.maximize(window)


def close_window(window):
    pygetwindow.Window.close(window)


def move_window_to_moniter(window, monitor_index=0):
    screen_info = screeninfo.get_monitors()
    if monitor_index < len(screen_info):
        monitor = screen_info[monitor_index]
        window.moveTo(monitor.x, monitor.y)
    else:
        print("Invalid monitor index.")


def set_window_size(window, width, height):
    window.size = (width, height)


def change_window_name(window_name):
    os.system(f'title {window_name}')


def get_game_window():
    pass
