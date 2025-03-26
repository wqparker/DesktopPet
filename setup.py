"""
setup.py for py2app - builds a macOS .app bundle from DesktopPet.py
"""
from setuptools import setup
import glob
import os

APP = ['DesktopPet.py']

# Option A: List each GIF explicitly
DATA_FILES = [
    ('Gifs', [
        'Gifs/Johnny_Idle_4x.gif',
        'Gifs/Johnny_walk_left_4x.gif',
        'Gifs/Johnny_walk_right_4x.gif',
        'Gifs/Nelly_Idle_4x.gif',
    ])
]

# Option B (automated): If you have many GIFs, you can auto-collect them:
# DATA_FILES = []
# all_gifs = glob.glob('Gifs/*.gif')
# if all_gifs:
#     DATA_FILES.append(('Gifs', all_gifs))

OPTIONS = {
    'argv_emulation': True,
    # Include any packages needed by your app:
    'includes': ['PyQt5'],
    # If you have a custom icon (.icns) file for your app, set it here:
    # 'iconfile': 'myicon.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
