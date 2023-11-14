# WallP - Dynamic Wallpaper Scheduler
WallP is a simple command-line tool that allows you to dynamically change your desktop wallpaper. 

## Features

- Change your desktop wallpaper with a single command.
- Schedule wallpaper changes based on your preferences.
- Upcoming: Cross-platform support (macOS, Linux, and Windows).

## Installation

Make sure you have Python installed on your system. Then, follow these steps:

1. Clone the repository:
```
git clone git@github.com:ReticentFacade/WallP.git
cd WallP
```

2. Create a virtual environment (optional but recommended):
 ```
 python3 -m venv venv
 source venv/bin/activate
 ```

3. Install dependencies:
 ```
 pip install -r requirements.txt
 ```

4. Install the WallP CLI:
 ```
 pip install .
 ```

## Usage

### Changing Wallpaper

To change your wallpaper, use the following command:
```
wallp change
```
This will select a random wallpaper from your specified directory.

## TODO:
- [ ] Scheduling wallpaper changes
- [ ] Setting up configuration for Linux and Windows

## Configuration
WallP automatically detects your wallpaper directory based on your OS. If you want to customize the directory, modify the get_wallpaper_dir() function in cli.py.

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Follow the guidelines in CONTRIBUTING.md.


