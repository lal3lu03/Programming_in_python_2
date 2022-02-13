"""
Author: Maximilian Hageneder
Exercise: 04
Matr.Nr.: k11942708
"""

import numpy as np


def ex4(image_array: np.ndarray, border_x: tuple, border_y: tuple):
    if not isinstance(image_array, np.ndarray) or image_array.ndim != 2:
        raise NotImplementedError(f"image_data must be numpy array of shape (H, W)")

    x1, x2 = border_x
    y1, y2 = border_y
    try:
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
    except:
        raise ValueError(f"borders are not int")

    if x1 < 1 or x2 < 1 or y1 < 1 or y2 < 1:
        raise ValueError("The borders are smaller than 1")

    border_x_start = x1
    border_x_end = image_array.shape[0] - x2

    border_pixels_x = border_x_end - border_x_start

    border_y_start = y1
    border_y_end = image_array.shape[1] - y2

    border_pixels_y = border_y_end - border_y_start

    if border_pixels_x < 16 or border_pixels_y < 16:
        raise ValueError(f"border for cropped out rectangle should be >= 16 but is {border_pixels_x} "
                         f"and {border_pixels_y}")

    known_array = np.zeros_like(image_array)
    known_array[border_x_start:border_x_end, border_y_start:border_y_end] = 1

    target_array = np.copy(image_array[border_x_start:border_x_end, border_y_start:border_y_end])

    image_array[:border_x_start] = 0
    image_array[border_x_end:] = 0
    image_array[:, :border_y_start] = 0
    image_array[:, border_y_end:] = 0
    input_array = image_array

    return input_array, known_array, target_array
