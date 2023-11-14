from setuptools import setup, find_packages

setup(
    name='wallpCLI',
    version='0.1.0',
    packages=find_packages(),
    description='WallP - Dynamic Wallpaper Scheduler',
    author='ReticentFacade',
    install_requires=[
        'setuptools',
        'wheel'
    ],
    entry_points={
    'console_scripts': [
        'wallp = wallpCLI.cli:main',
        ],
    },
)