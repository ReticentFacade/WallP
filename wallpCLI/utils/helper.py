import os
import random
import platform
from pathlib import Path

def get_wallpaper_dir():
    system_platform = platform.system()

    if system_platform == 'Darwin':  # mac
        possible_directories = [
            # Path.home() / 'Pictures',
            # Path.home() / 'Library' / 'Desktop Pictures',
            Path.home() / 'Desktop' / 'Rest' / 'wallpapers',
        ]

    # elif system_platform == 'Linux':
    #     possible_directories = [
    #         Path.home(),
    #         Path.home() / 'Pictures',
    #     ]
    # elif system_platform == 'Windows':
    #     possible_directories = [
    #         Path.home() / 'Pictures',
    #         Path.home() / 'Documents' / 'Wallpapers',
    #     ]
    else:
        # Add conditions for other platforms if needed
        possible_directories = [
            Path.home(),
        ]

    for directory in possible_directories:
        if directory.is_dir():
            print(f"Using wallpaper directory: {directory}")
            return str(directory)

    # Default: return a generic path
    default_directory = Path.home()
    print(f"Using default wallpaper directory: {default_directory}")
    return str(default_directory)


def get_random_wallp():
    wallp_dir = get_wallpaper_dir()
    # image_files = [f for f in os.listdir(wallp_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    image_files = [f for f in os.listdir(wallp_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print("No files found in the wallpaper directory!")
        return None

    return os.path.join(wallp_dir, random.choice(image_files))

