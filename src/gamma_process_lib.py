# -*- coding: utf-8 -*-
"""
Created on Tue 06 Feb 2024

Author: YIJU WU (gn02129251)

File: gamma_process_lib.py

Topic: This module includes functions for image gamma processing (or histogram processing).

"""
import numpy as np
from numpy.typing import ArrayLike


def gamma_correction(img: ArrayLike, gamma: float) -> ArrayLike:
    """Apply gamma correction to an image.

    Args:
        img (ArrayLike): The input image.
        gamma (float): The gamma value for correction.

    Raises:
        ValueError: If the gamma value is less than zero.

    Returns:
        ArrayLike: The gamma-corrected image.
    """
    if not gamma >= 0:
        raise ValueError("The gamma value should be equal to or greater than zero.")

    corrected_img = img.copy().astype(np.float64)
    corrected_img /= 255
    corrected_img = (corrected_img**gamma * 255).astype(np.uint8)

    return corrected_img


def main(*args):
    return 0


if __name__ == "__main__":
    main()
