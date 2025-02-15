import json
import os

CONFIG_PATH = os.path.expanduser("~/.mystical-project_config.json")

def save_config(data):
    """Save the configuration to the file."""
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f)

def load_config():
    """Load the configuration from the file."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {}

def set_token(token):
    """Save the token to the configuration."""
    config = load_config()
    config["token"] = token
    save_config(config)

def get_token():
    """Get the token from the configuration."""
    return load_config().get("token")

def remove_token():
    """Remove the token from the configuration."""
    config = load_config()
    config["token"] = None
    save_config(config)