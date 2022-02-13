"""
Author: Maximilian Hageneder
Exercise: 03
Matr.Nr.: k11942708
"""

import os
import glob
from PIL import Image
import numpy as np


class ImageNormalizer(object):
    def __init__(self, input_dir: str):
        # ex 2,3,5
        # scan remove input, sort list to ABC, store in self.file_paths
        a = sorted(glob.glob(os.path.join(input_dir, '**', '*.jpg'),
                             recursive=True))
        self.absolute_file_names = a
        self.file_paths = []
        for file in a:
            self.file_paths.append(file.replace(input_dir + os.sep, ''))
        self.n_file_paths = len(a)
        self.file_names = [os.path.basename(x) for x in self.file_paths]
        # nwe empty numpy array of mean
        self.mean = np.empty(shape=(len(self.file_names)), dtype=np.float64)
        # new empty numpy array of standard divisor
        self.std = np.empty(shape=(len(self.file_names),), dtype=np.float64)
        self.input_dir = input_dir

    def analyze_images(self):
        # compute and store the mean and std in numpy array
        for i, filename in enumerate(self.absolute_file_names):
            with Image.open(os.path.join(self.input_dir, filename)) as image:
                np_image = np.array(image)
            self.mean[i] = np.mean(np_image,dtype=np.float64)
            self.std[i] = np.std(np_image,dtype=np.float64)
        # sort mean and std in np.flot64 array
        mean = sorted(self.mean)
        std = sorted(self.std)
        return mean, std

    def get_images_data(self):
        if self.mean is None:
            raise ValueError
        elif self.std is None:
            raise ValueError
        # loob over filenames in input dir
        for filename in self.file_names:
            with Image.open(os.path.join(self.input_dir, filename)) as image:
                # read image as numpy array float32
                np_image = np.array(image, dtype=np.float32)
            np_image_normalized = (np_image - np_image.mean()) / np_image.std()
            yield np_image_normalized
