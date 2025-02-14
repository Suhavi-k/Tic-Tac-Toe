import json
import os

SETTINGS_FILE = "settings.json"

DEFAULT_SETTINGS = {
    "Sound_effect": {
        "X": ".Sounds& Effects/xTone.mp3",
        "O": ".Sounds& Effects/OTone.mp3",
        "Victory": ".Sounds& Effects/win.mp3",
        "volume": 1.0
    },
    "music": {
        "enabled": True,
        "track": ".Sounds& Effects/music.mp3",
        "volume": 0.5
    }
}

def load_settings():
    """Load game settings from the JSON file, with default values if missing."""
    if not os.path.exists(SETTINGS_FILE):
        print("WARNING: settings.json not found, creating default settings.")
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

    try:
        with open(SETTINGS_FILE, "r") as file:
            settings = json.load(file)

            # Ensure all required keys exist
            for key, default_value in DEFAULT_SETTINGS.items():
                if key not in settings:
                    settings[key] = default_value

            return settings
    except (json.JSONDecodeError, FileNotFoundError):
        print("ERROR: settings.json is corrupt. Resetting to default.")
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

def save_settings(settings):
    """Save game settings to the JSON file."""
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)

if __name__ == "__main__":
    settings = load_settings()
    print("Current Settings:", json.dumps(settings, indent=4))
