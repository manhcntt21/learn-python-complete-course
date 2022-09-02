# copyfile(): copies contents of a file
# copy(): copyfile() + permission mode + destination can be a directory
# copy2(): copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copy('./data/copy-1.txt', './data/copy-2.txt') # src, dst
