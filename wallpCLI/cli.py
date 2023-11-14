import os
import argparse;
from wallpCLI.core import change_wallpaper, set_wallpaper
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
# Path to the parent/project directory (previous directory)
project_path = os.path.dirname(current_directory)

# print(f"Project path is: {project_path}")

def main(): 
    parser = argparse.ArgumentParser(description='WallP - Dynamic Wallpaper Scheduler'); 

    parser.add_argument('command', choices=['change', 'set'], help = 'Command to execute');
    # parser.add_argument('path', help = 'Path to the wallpaper file [for `set` command]');

    args = parser.parse_args();

    if args.command == 'change': 
        print("Executing `change` command");
        change_wallpaper();

    # elif args.command == 'set' and args.path:
    #     print("Executing set command");
    #     set_wallpaper(args.path);

    else: 
        parser.print_help();

if __name__ == '__main__': 
    main();