from os.path import dirname, join, expanduser, exists
from os import makedirs


def get_game_data_folder() -> str:
    # Possible paths
    local_games_folder = join(expanduser("~"), "Documents", "My Games")
    one_drive_folder = join(expanduser("~"), "OneDrive")
    es_onedrive_folder = join(expanduser("~"), "OneDrive", "Documentos")
    en_onedrive_folder = join(expanduser("~"), "OneDrive", "Documents")
    # Determine if OneDrive sync is active and the language of it
    onedrive_active = False
    onedrive_language = None
    if exists(one_drive_folder):
        onedrive_active = True
        onedrive_language = "spanish" if exists(es_onedrive_folder) else "english"
    # Set the default save folder and the game name
    save_folder = local_games_folder
    game_name = "Prototype"
    # Set the save folder in case OneDrive sync is active
    if onedrive_active:
        if onedrive_language == "spanish":
            save_folder = join(es_onedrive_folder, "My Games", game_name)
        elif onedrive_language == "english":
            save_folder = join(en_onedrive_folder, "My Games", game_name)
    else:
        save_folder = join(save_folder, game_name)
    # If the directory doesn't exist, create it
    if not exists(save_folder):
        makedirs(save_folder)
    return save_folder


# Data paths
ROOT = dirname(dirname(__file__))
DATA_FOLDER = get_game_data_folder()
PREFERENCES_FILE = join(DATA_FOLDER, "preferences.json")
SAVES_FOLDER = join(DATA_FOLDER, "Saves")
SAVES_FILES = [join(SAVES_FOLDER, f"save{i}") for i in range(1, 4)]
# Assets paths
