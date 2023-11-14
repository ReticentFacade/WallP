import argparse;
# from .core import change_wallpaper, set_wallpaper;
import sys
sys.path.append("/Users/Reticent/Desktop/Work/ProjectWorkspace/github/WallP") 
from wallpCLI.core import change_wallpaper, set_wallpaper

def main(): 
    parser = argparse.ArgumentParser(description='WallP - Dynamic Wallpaper Scheduler'); 

    parser.add_argument('command', choices=['change', 'set'], help = 'Command to execute');
    parser.add_argument('path', help = 'Path to the wallpaper file [for `set` command]');

    args = parser.parse_args();

    if args.command == 'change': 
        change_wallpaper();

    elif args.command == 'set' and args.path:
        set_wallpaper(args.path);

    else: 
        parser.print_help();

if __name__ == '__main__': 
    main();