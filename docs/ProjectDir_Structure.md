# Project Directory Structure: 
```
➜  WallP ✗ tree 
.
├── README.md
├── docs
│   └── ProjectDir_Structure.md
├── requirements.txt
├── setup.py
├── tests
├── wallpCLI
│   ├── __init__.py
│   ├── cli.py
│   └── core.py
└── wallpapers
    ├── wallpaper1.png
    ├── wallpaper2.png
    ├── wallpaper3.png
    ├── wallpaper4.png
    └── wallpaper5.png

5 directories, 12 files
```

1.  `wallp/__init__.py`:
 This file can be left empty. It signifies that the wallp directory should be treated as a Python package.

2. `wallp/core.py`:
This file will contain the core functionality for changing and setting wallpapers.

3. `wallp/cli.py`:
This file will handle the command-line interface (CLI).

4. `wallpapers/`:
This directory contains sample wallpaper images.

5. `tests/`:
Unit tests for the application are in this directory.

6. `requirements.txt`:
List the dependencies for your project. For now, it might be empty.

7. `setup.py`:
Configuration for packaging your application.
