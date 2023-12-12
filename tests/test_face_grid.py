import numpy as np
import unittest
from CubeInit import Face
from Constraints import Axes, Colours, FacePositions
from Transformations import GridTransformations
from Predicates import GridPredicates

class TestFaceGrid(unittest.TestCase):
    
    def setUp(self):
        self.face = Face(Colours.BLUE)
        self.front = Face(Colours.WHITE)
        test_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.face.grid = np.array(test_grid)
    
    def tearDown(self):
        pass
    
    def test_transform_right_face_rotate_up_down(self):
        self.front.right = self.face
        self.face.left = self.front
        expected_up_grid = [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ]
        expected_down_grid = [
            [3,6,9],
            [2,5,8],
            [1,4,7]
        ]
        result_up_grid = GridTransformations.UpAndDown.transform_right_face(self.front, is_rotate_down=False, is_test=True)
        result_down_grid = GridTransformations.UpAndDown.transform_right_face(self.front, is_rotate_down=True, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_up_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_down_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_down_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_up_grid)))
        
    def test_transform_left_face_rotate_up_down(self):
        self.front.left = self.face
        self.face.right = self.front
        expected_down_grid = [
            [7,4,1],
            [8,5,2],
            [9,6,3]
        ]
        expected_up_grid = [
            [3,6,9],
            [2,5,8],
            [1,4,7]
        ]
        result_up_grid = GridTransformations.UpAndDown.transform_left_face(self.front, is_rotate_down=False, is_test=True)
        result_down_grid = GridTransformations.UpAndDown.transform_left_face(self.front, is_rotate_down=True, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_up_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_down_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_up_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_down_grid)))
    
    pass


if __name__ == "__main__":
    unittest.main()