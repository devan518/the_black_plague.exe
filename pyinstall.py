import PyInstaller.__main__

PyInstaller.__main__.run([
    'DO_NOT_RUN.py',
    '--windowed',
    '--noconsole',
    '--onefile',
])