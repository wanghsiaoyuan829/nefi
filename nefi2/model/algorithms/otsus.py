#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(from opencv docs)
Otsu's binarization automatically calculates a threshold value from image
histogram for a bimodal image. (For images which are not bimodal, binarization
won’t be accurate.)
For this, cv2.threshold() function is used with an extra flag, cv2.THRESH_OTSU.
For threshold value, simply pass zero. Then the algorithm finds the optimal
threshold value and returns you as the second output. If Otsu thresholding is
not used, the optimal threshold is same as the threshold value you used.
"""
from nefi2.model.algorithms._alg import Algorithm
import cv2
import numpy as np


__author__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


class AlgBody(Algorithm):
    """
    Otsu's threshold implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Otsus"
        self.parent = "Segmentation"

    def process(self, args):
        """
        Otsu's thresholding as described in opencv docs.

        Args:
            | *args* : a list of arguments, e.g. image ndarray

        """
        """
        (len(args[0].shape) == 3) => checking if it's grey or RGB image
        """
        if (len(args[0].shape) == 3):
            gray_img = cv2.cvtColor(args[0], cv2.COLOR_RGB2GRAY)
            """
            cvtColor(src[input image],
                     dst[output image of the same size and depth as src,
                     code[color space conversion code])
            cv2.COLOR_RGBGRAY convert a RGB image to gray
            
            """
        else:
            gray_img = args[0]
        self.result['img'] = cv2.threshold(gray_img, 0, 255,
                                           cv2.THRESH_BINARY_INV +
                                           cv2.THRESH_OTSU)[1]
        """
            cv2.threshold[1] will produce two output. First one is
            retval. Second output is our thresholded image.
            [1] will produce second output which is threshold image
            
            *cv2.threshold: if pixel value is greater than a threshold value,
                           it is assigned one value (may be white), else it
                           is assigned another value (may be black). 
            *cv2.threshold(src,threshold value ,maxVal)
            -src:spurce image
            -threshold value: which is used to classify the pixel values.
            -maxVal: which represents the value to be given if pixel value
                     is more than (sometimes less than) the threshold value
            (Black pixel:0 white pixel:255)
            *cv2.THRESH_BINARY_INV: if pixel is higher than threhold value, the
            new pixel is set to 0. Otherwise, it set to MaxVal
        """

if __name__ == '__main__':
    pass
