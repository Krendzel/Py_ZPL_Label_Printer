import os
from os.path import isfile, join
import glob

def list_files(path):
    for file in glob.glob(path):
        if isfile(file):
            filename = os.path.basename(file)
            full_path = file




list_files('templates/*.txt')