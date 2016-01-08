# -*- coding: utf-8 -*-
"""
This class represents the algorithm Guo Hall
"""
__authors__ = {"Andreas Firczynski": "andreasfir91@googlemail.com"}

import cv2
from nefi2.model.algorithms._alg import *
from thinning import guo_hall_thinning


class AlgBody(Algorithm):
    """Guo Hall algorithm implementation"""

    def __init__(self):
        """
        Guo Hall object constructor
        Instance vars:
            self.name -- name of the algorithm
            self.parent -- name of the appropriated category
        """
        self.name = "Guo Hall graph detector"
        self.parent = "Graph detection"


    def process(self, image):
        """
        Use the Guo Hall thining algorithm from the thinning package to the current image
        Args:
            image: image instance

        """
        skeleton = guo_hall_thinning(image)
        #TODO nodes and edges detection