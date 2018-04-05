import os

for folderName, subfolders, filenames in os.walk('.'):
    print('The current folder is ' + folderName)

    for filename in filenames:
        print('FILE INSIDE ' + os.path.abspath(folderName) + '\\' + filename)

    print('')