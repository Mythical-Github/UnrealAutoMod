import os
import sys
import subprocess
import json
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
os.chdir(SCRIPT_DIR)

TITLE = "Tempo"
ICON = "path/to/icon.png"
BACKGROUND_COLOR = "background-color: #111111;"
BUTTON_STYLE = "background: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #330000, stop: 1 #660000); color: white; border: 1px solid teal;"

class ScriptRunner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(TITLE)
        self.setStyleSheet(BACKGROUND_COLOR)

        # Create a scrollable area for the buttons
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget(scroll_area)
        scroll_layout = QVBoxLayout(scroll_widget)

        # Load script arguments from JSON
        script_args_data = self.load_script_args_from_json("settings.json")

        # Add buttons for each script argument
        for arg_data in script_args_data:
            button = self.create_button(arg_data["button_text"], arg_data["script_arg"])
            scroll_layout.addWidget(button)

        scroll_widget.setLayout(scroll_layout)
        scroll_area.setWidget(scroll_widget)

        # Set the horizontal scroll policy to off
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Set the main layout to a QHBoxLayout for side-by-side arrangement
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def load_script_args_from_json(self, json_file):
        try:
            with open(json_file, "r") as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def create_button(self, button_text, script_arg):
        button = QPushButton(button_text)
        button.setMinimumHeight(int(20 * 1.25))  # Adjusted height
        button.setMinimumWidth(int(150 * 1.5))   # Adjusted width
        button.setStyleSheet(BUTTON_STYLE)
        button.clicked.connect(lambda checked, arg=script_arg: self.run_script(arg))
        return button

    def run_script(self, script_arg):
        game_name = "the_baby_in_yellow_steam"
        preset_name = "biy_mythical"
        command = ["TempoCLI.exe", game_name, preset_name, script_arg]
        subprocess.Popen(command)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ICON))
    win = ScriptRunner()
    win.show()
    sys.exit(app.exec_())
