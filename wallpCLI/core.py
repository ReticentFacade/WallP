import os
from pathlib import Path
from wallpCLI.utils.helper import get_wallpaper_dir, get_random_wallp
from wallpCLI.utils.platform_wallpaper import set_wallpaper_macOS

def change_wallpaper():
    # new_wallp_path = path or get_random_wallp()
    new_wallp_path = get_random_wallp()

    if new_wallp_path:
        # Currently just for mac:
        set_wallpaper_macOS(new_wallp_path)
        print(f"Changed wallpaper to {new_wallp_path}!")

    else:
        print("Could not change wallpaper! >.<")


def set_wallpaper(image_file):
    wallp_directory = get_wallpaper_dir()
    image_path = os.path.join(wallp_directory, image_file)

    if os.path.exists(image_path):
        # Add logic here to set the wallpaper based on the platform
        set_wallpaper_macOS(image_path)
        print(f'Successfully set wallpaper to: {image_path}!')
    else:
        print(f'Error: Image file not found: {image_path}')

