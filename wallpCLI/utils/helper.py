import os
import random
import platform
from pathlib import Path

def get_wallpaper_dir():
    wallp_dir = "/Users/Reticent/Desktop/Work/ProjectWorkspace/github/WallP/wallpapers"
    return str(wallp_dir)
    # system_platform = platform.system();

    # if system_platform == 'Darwin': # mac
    #     return str(Path.home() / 'Library/Application Support/Dock/desktoppicture.db');

    # elif system_platform == 'Linux':
    #     return str(Path.home());

    # elif system_platform == 'Windows':
    #     return str(Path.home() / '');


def get_random_wallp():
    wallp_dir = get_wallpaper_dir()
    image_files = [f for f in os.listdir(
        wallp_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print("No files found in the wallpaper directory!")
        return None

    return os.path.join(wallp_dir, random.choice(image_files))

