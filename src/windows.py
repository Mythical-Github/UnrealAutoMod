import pygetwindow
from os import system
from screeninfo import get_monitors
from utilities import get_game_process_name
from enums import WindowAction, ScriptStateType, get_enum_member_from_value


def does_window_exist(window_title: str, use_substring_check: bool = False) -> bool:
    try:
        if use_substring_check:
            all_window_titles = pygetwindow.getAllTitles()
            matched_windows = [window for window in all_window_titles if window_title in window]
            return len(matched_windows) > 0
        else:
            all_window_titles = pygetwindow.getWindowsWithTitle(window_title)
            return len(all_window_titles) > 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def get_windows_by_title(window_title: str, use_substring_check: bool = False) -> list:
    if use_substring_check:
        all_windows = pygetwindow.getAllWindows()
        matched_windows = [window for window in all_windows if window_title in window.title]
        return matched_windows
    else:
        matched_windows = pygetwindow.getWindowsWithTitle(window_title)
        return matched_windows


def get_window_by_title(window_title: str, use_substring_check: bool = False) -> pygetwindow.Win32Window:
    windows = get_windows_by_title(window_title, use_substring_check)
    if not windows:
        raise ValueError(f'No windows found with title "{window_title}"')
    return windows[0]


def minimize_window(window: pygetwindow.Win32Window):
    pygetwindow.Window.minimize(window)


def maximize_window(window: pygetwindow.Win32Window):
    pygetwindow.Window.maximize(window)


def close_window(window: pygetwindow.Win32Window):
    pygetwindow.Window.close(window)


def move_window_to_moniter(window: pygetwindow.Win32Window, monitor_index: int = 0):
    screen_info = get_monitors()
    if monitor_index < len(screen_info):
        monitor = screen_info[monitor_index]
        window.moveTo(monitor.x, monitor.y)
    else:
        print('Invalid monitor index.')


def set_window_size(window: pygetwindow.Win32Window, width: int, height: int):
    window.size = (width, height)


def change_window_name(window_name: str):
    system(f'title {window_name}')


def get_game_window() -> pygetwindow.Win32Window:
    return get_window_by_title(get_game_process_name())


def move_window(window: pygetwindow.Win32Window):
    pass


def window_checks(current_state: WindowAction):
    from settings import settings
    window_settings = settings['auto_move_windows']
    for window in window_settings:
        settings_state = get_enum_member_from_value(ScriptStateType, window['script_state'])
        if settings_state == current_state:
            title = window['window_name']
            windows_to_change = get_windows_by_title(title)
            for window_to_change in windows_to_change:
                way_to_change_window = get_enum_member_from_value(WindowAction, window['window_behaviour'])
                if way_to_change_window == WindowAction.MAX:
                    maximize_window(window_to_change)
                elif way_to_change_window == WindowAction.MIN:
                    minimize_window(window_to_change)
                elif way_to_change_window == WindowAction.CLOSE:
                    close_window(window_to_change)
                elif way_to_change_window == WindowAction.MOVE:
                    move_window(window_to_change)
                elif way_to_change_window == WindowAction.NONE:
                    pass
                else:
                    print('invalid window behaviour specified in settings')