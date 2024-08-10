import os
import platform

def iterator(directory):
    directory = directory
    archives = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            archives.append(os.path.join(root, file))
    return archives

def get_operational_system():
    """
    operating system the script is running on.

   Returns:
  - 'Windows' for Windows systems
  - 'Linux' for Linux systems
  - 'macOS' for macOS systems
  - 'Unknown' for other operating systems
    """
    system = platform.system().lower()

    if system == 'windows':
        return 'Windows'
    elif system == 'linux':
        return 'Linux'
    elif system == 'darwin':
        return 'macOS'
    else:
        return 'Unknown'

def get_home_directory():
    return os.path.expanduser('-')