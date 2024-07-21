import os
import sys
import json
import socket
import subprocess


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(sys.executable)
else:
    SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))

SETTINGS_JSON = f'{SCRIPT_DIR}/other_machine_settings.json'


def load_settings(settings_file):
    with open(settings_file, 'r') as file:
        settings = json.load(file)
    return settings


SETTINGS = load_settings(SETTINGS_JSON)


def get_paks_dir():
    return SETTINGS['mods_dir']


def get_server_ip():
    return SETTINGS['server_ip']


def get_server_port():
    return SETTINGS['server_port']


def get_process_kill_strings():
    return SETTINGS['process_kill_strings']


def get_exec_path():
    return SETTINGS['exec_path']


def start_game():
    desktop_file = get_exec_path()
    if os.path.exists(desktop_file):
        subprocess.call(['xdg-open', desktop_file])
    else:
        print(f"Desktop file not found: {desktop_file}")


def close_game():
    for process_kill_str in get_process_kill_strings():
        os.system(f'killall {process_kill_str}')


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started at {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        file_name_size = int.from_bytes(client_socket.recv(4), 'big')
        file_name = client_socket.recv(file_name_size).decode()
        file_name = f'{get_paks_dir()}/{file_name}'

        file_size = int.from_bytes(client_socket.recv(8), 'big')
        
        with open(file_name, 'wb') as file:
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = client_socket.recv(chunk_size)
                if not chunk:
                    break
                file.write(chunk)
                remaining -= len(chunk)

        print(f"Received file: {file_name}")
        client_socket.close()
        close_game()
        start_game()


if __name__ == "__main__":
    start_server(get_server_ip(), get_server_port())
