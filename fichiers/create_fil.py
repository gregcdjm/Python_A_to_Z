import os
import shutil

source = "fichiers./lock.png"
target = "TKINTER_interface./lock.png"

shutil.copy(source, target)
os.remove(source)