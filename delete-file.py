import os
import shutil

path1 = './data/delete-file1.txt'
path2 = './data/delete-folder'

try:
    # os.remove(path2)
    # os.rmdir(path2)  # delete empty folder, dont delete folder contains two or more file
    shutil.rmtree(path2) # delete folder contains files, DANGEROUS
except FileNotFoundError as e:
    print("That file was not found!")
except PermissionError as e:
    print("you do not have permission to delete that")
except OSError as e:
    print("You cannot delete that using {} function".format('rmdir'))
else:
    print("{} was deleted".format(path2))