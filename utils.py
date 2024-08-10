import os
import platform

def get_script_directory():
    """Returns the directory where the script is located."""
    return os.path.dirname(os.path.abspath(__file__))
def iterator(directory, exclude_dirs=None, exclude_files=None, allowed_extensions=None):

    """
    :param directory:
    :param exclude_dirs:
    :param exclude_files:
    :return List of file extensions allowed for
    """
    if exclude_dirs is None:
        exclude_dirs = []
    if exclude_files is None:
        exclude_files = []
    if allowed_extensions is None:
        allowed_extensions = ['.txt', '.doc', '.pdf', '.jpg']

    # Add current directory to exclude list
    script_dir = get_script_directory()
    exclude_dirs.append(script_dir)

    directory = directory
    archives = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]

        for file in files:
            file_path = os.path.join(root, file)

            if file in exclude_files:
                continue

            if allowed_extensions and not any(file.endswith(ext) for ext in allowed_extensions):
                continue

            archives.append(file_path)

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