import os

def iterator(directory):
    directory = directory


    archives = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            archives.append(os.path.join(root, file))

    return archives