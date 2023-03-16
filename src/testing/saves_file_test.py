from os.path import exists, join, expanduser, dirname
from os import makedirs
import json





# Constants
DATA_FOLDER = get_game_data_folder()
PREFERENCES_FILE = join(DATA_FOLDER, "preferences.json")
SAVES_FOLDER = join(DATA_FOLDER, "Saves")
SAVE_FILES = [join(SAVES_FOLDER, f"save{i}") for i in range(1, 4)]
# Preferences
if not exists(PREFERENCES_FILE):
    with open(PREFERENCES_FILE, "w") as preferences_file:
        json.dump({"width": 1280, "height": 720}, preferences_file)
# Saves
if not exists(SAVES_FOLDER):
    makedirs(SAVES_FOLDER)

for index, save_path in enumerate(SAVE_FILES):
    if not exists(save_path):
        with open(save_path, "w") as save_file:
            json.dump({"data": "empty"}, save_file)
