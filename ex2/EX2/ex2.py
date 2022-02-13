"""
Author: Maximilian Hageneder
Exercise: 02
Matr.Nr.: k11942708
"""

import os
import shutil
import glob
from PIL import Image
import numpy as np
import hashlib


def ex2(inp_dir: str, out_dir: str, logfile: str):
    inp_dir = os.path.abspath(inp_dir)
    files = glob.glob(os.path.join(inp_dir, '**', '*'), recursive=True)
    files.sort()
    os.makedirs(out_dir, exist_ok=True)

    valid_files = 0
    hash_list = []
    with open(logfile, 'w') as _:
        pass
    for file in files:
        if not (file.endswith('.jpg') or file.endswith('.JPG') or file.endswith(
                '.JPEG') or file.endswith('.jpeg')):
            with open(logfile, 'a') as logf:
                print(f'{file[len(inp_dir) + 1:]};1', file=logf)
            continue
        if not os.path.getsize(file) > 10000:
            with open(logfile, 'a') as logf:
                print(f'{file[len(inp_dir) + 1:]};2', file=logf)
            continue
        try:
            image = Image.open(file)
        except:
            with open(logfile, 'a') as logf:
                print(f'{file[len(inp_dir) + 1:]};3', file=logf)
            continue
        np_image = np.array(image)
        image_shape = np_image.shape
        if not (len(image_shape) == 2 and min(image_shape) >= 100):
            with open(logfile, 'a') as logf:
                print(f'{file[len(inp_dir) + 1:]};4', file=logf)
            continue
        if np.std(np_image) <= 0:
            with open(logfile, 'a') as logf:
                print(f'{file[len(inp_dir) + 1:]};5', file=logf)
            continue
        np_image_bytes = np_image.tostring()
        hashing_f = hashlib.sha256()
        hashing_f.update(np_image_bytes)
        np_image_hash = hashing_f.digest()

        if np_image_hash in hash_list:
            with open(logfile, 'a') as logf:
                print(f'{file[len(inp_dir) + 1:]};6', file=logf)
            continue

        hash_list.append(np_image_hash)

        shutil.copy(file, os.path.join(out_dir, f'{valid_files:07d}.jpg'))
        valid_files += 1

    return valid_files
