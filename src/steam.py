import winreg


def get_steam_exe_location():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Valve\Steam", 0, winreg.KEY_READ)
        install_path, _ = winreg.QueryValueEx(reg_key, "InstallPath")
        winreg.CloseKey(reg_key)
        steam_exe_path = f"{install_path}\\steam.exe"
        return steam_exe_path
    except FileNotFoundError:
        return "Steam: installation not found in the registry."
    except Exception as e:
        return f"Error: An error occurred: {e}"
