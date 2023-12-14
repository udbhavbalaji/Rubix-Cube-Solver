import numpy as np
import unittest
from cube_init import Face
from Constraints import Axes, Colours, FacePositions
from Transformations import GridTransformations
from Predicates import GridPredicates

class TestGridPredicates(unittest.TestCase):
    
    def setUp(self):
        self.face = Face('Blue')
        self.test_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.face.grid = np.array(self.test_grid)
        pass
    
    def tearDown(self):
        pass
    
    
    def test_are_grids_equal(self):
        self.assertTrue(GridPredicates.are_grids_equal(self.face.grid, self.face.grid))
        self.assertFalse(GridPredicates.are_grids_equal(self.face.grid, np.flip(self.face.grid)))
        self.assertFalse(GridPredicates.are_grids_equal(self.face, self.face))
    
        
        
    pass
