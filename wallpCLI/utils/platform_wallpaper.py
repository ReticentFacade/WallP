import subprocess
from wallpCLI.utils.helper import get_random_wallp

def set_wallpaper_macOS(new_wallp_path):
    try:
        script = f'Tell application "Finder" to set desktop picture to POSIX file "{new_wallp_path}"'
        subprocess.run(["osascript", "-e", script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting wallpaper: \n{e}")
