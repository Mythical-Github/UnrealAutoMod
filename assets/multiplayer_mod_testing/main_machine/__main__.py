import os
import sys
import time
import socket
import pyjson5 as json


if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(sys.executable)
else:
    SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))

SETTINGS_JSON = f'{SCRIPT_DIR}/settings.json'


def load_settings(settings_file):
    with open(settings_file, 'r') as file:
        settings = json.load(file)
    return settings


SETTINGS = load_settings(SETTINGS_JSON)


def get_server_entries():
    return SETTINGS['servers']


def get_server_title(entry):
    return entry['title'] 


def get_server_ip(entry):
    return entry['ip'] 


def get_server_port(entry):
    return entry['port'] 


def send_file(file_path, host, port):
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        client_socket.send(len(file_name).to_bytes(4, 'big'))
        client_socket.send(file_name.encode())

        client_socket.send(file_size.to_bytes(8, 'big'))

        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                client_socket.sendall(chunk)
        print(f"Sent file: {file_name}")


def send_files():
    for entry in get_server_entries():
        for file_path in sys.argv[1:]:
            if os.path.isfile(file_path):
                send_file(file_path, get_server_ip(entry), get_server_port(entry))
            elif os.path.isdir(file_path):
                for root, dirs, files in os.walk(file_path):
                    for file in files:
                        send_file(os.path.join(root, file), get_server_ip(entry), get_server_port(entry))
            print('delay of one second happening to prevent disconnection')
            time.sleep(1)


def cli_logic():
    if len(sys.argv) < 2:
        print("Usage: client.py <file1> <file2> ...")
        sys.exit(1)
    else:
        send_files()


def main():
    cli_logic()


if __name__ == "__main__":
    main()
