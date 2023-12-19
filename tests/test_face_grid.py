import numpy as np
import unittest
from cube_init import Face
from Constraints import Axes, Colours, FacePositions
from Transformations import GridTransformations
from Predicates import GridPredicates

class TestFaceGridRotateOnceUpDown(unittest.TestCase):
    
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
        
    def test_transform_back_face_rotate_up_down(self):
        self.front.opposite = self.face
        self.face.opposite = self.front
        expected_down_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        expected_up_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        result_down_grid = GridTransformations.UpAndDown.transform_back_face(self.front, is_rotate_down=True, is_test=True)
        result_up_grid = GridTransformations.UpAndDown.transform_back_face(self.front, is_rotate_down=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_down_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_up_grid)))
    
    def test_transform_top_face_rotate_up_down(self):
        self.front.top = self.face
        self.face.front = self.front
        
        expected_down_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_up_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        
        result_down_grid = GridTransformations.UpAndDown.transform_top_face(self.front, is_rotate_down=True, is_test=True)
        result_up_grid = GridTransformations.UpAndDown.transform_top_face(self.front, is_rotate_down=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_down_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_up_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_up_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_down_grid)))
        
    def test_transform_bottom_face_rotate_up_down(self):
        self.front.bottom = self.face
        self.face.front = self.face
        
        expected_down_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        expected_up_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
        result_down_grid = GridTransformations.UpAndDown.transform_bottom_face(self.front, is_rotate_down=True, is_test=True)
        result_up_grid = GridTransformations.UpAndDown.transform_bottom_face(self.front, is_rotate_down=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_down_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_up_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_down_grid, np.array(expected_up_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_up_grid, np.array(expected_down_grid)))
    
class TestFaceGridRotateOnceLeftRight(unittest.TestCase):
    
    def setUp(self):
        self.face = Face(Colours.BLUE)
        self.front = Face(Colours.WHITE)
        test_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.face.grid = np.array(test_grid)
        self.front.grid = np.array(test_grid)
    
    def tearDown(self):
        pass
    
    def test_transform_left_face_rotate_left_right(self):
        self.front.left = self.face
        self.face.right = self.front
        
        expected_left_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_left_horizontal_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        expected_right_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_right_horizontal_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        
        result_left_vertical_grid = GridTransformations.LeftAndRight.transform_left_face(self.front, Axes.VERTICAL, is_left=True, is_test=True)
        result_left_horizontal_grid = GridTransformations.LeftAndRight.transform_left_face(self.front, Axes.HORIZONTAL, is_left=True, is_test=True)
        
        result_right_vertical_grid = GridTransformations.LeftAndRight.transform_left_face(self.front, Axes.VERTICAL, is_left=False, is_test=True)
        result_right_horizontal_grid = GridTransformations.LeftAndRight.transform_left_face(self.front, Axes.HORIZONTAL, is_left=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_horizontal_grid)))
        
        self.assertTrue(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_vertical_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_vertical_grid)))
        
    def test_transform_right_face_rotate_left_right(self):
        self.front.right = self.face
        self.face.left = self.front
        
        expected_left_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_left_horizontal_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        expected_right_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_right_horizontal_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        
        result_left_vertical_grid = GridTransformations.LeftAndRight.transform_right_face(self.front, Axes.VERTICAL, is_left=True, is_test=True)
        result_left_horizontal_grid = GridTransformations.LeftAndRight.transform_right_face(self.front, Axes.HORIZONTAL, is_left=True, is_test=True)
        
        result_right_vertical_grid = GridTransformations.LeftAndRight.transform_right_face(self.front, Axes.VERTICAL, is_left=False, is_test=True)
        result_right_horizontal_grid = GridTransformations.LeftAndRight.transform_right_face(self.front, Axes.HORIZONTAL, is_left=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_horizontal_grid)))
        
        self.assertTrue(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_vertical_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_vertical_grid)))
        
    def test_transform_top_face_rotate_left_right(self):
        self.front.top = self.face
        self.face.bottom = self.front
        
        expected_left_vertical_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        expected_left_horizontal_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        expected_right_vertical_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        expected_right_horizontal_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        
        result_left_vertical_grid = GridTransformations.LeftAndRight.transform_top_face(self.front, Axes.VERTICAL, is_left=True, is_test=True)
        result_left_horizontal_grid = GridTransformations.LeftAndRight.transform_top_face(self.front, Axes.HORIZONTAL, is_left=True, is_test=True)
        
        result_right_vertical_grid = GridTransformations.LeftAndRight.transform_top_face(self.front, Axes.VERTICAL, is_left=False, is_test=True)
        result_right_horizontal_grid = GridTransformations.LeftAndRight.transform_top_face(self.front, Axes.HORIZONTAL, is_left=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_horizontal_grid)))
        
        self.assertTrue(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_vertical_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_vertical_grid)))
        
    def test_transform_bottom_face_rotate_left_right(self):
        self.front.bottom = self.face
        self.face.front = self.front
        
        expected_left_vertical_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        expected_left_horizontal_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        expected_right_vertical_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        expected_right_horizontal_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        
        result_left_vertical_grid = GridTransformations.LeftAndRight.transform_bottom_face(self.front, Axes.VERTICAL, is_left=True, is_test=True)
        result_left_horizontal_grid = GridTransformations.LeftAndRight.transform_bottom_face(self.front, Axes.HORIZONTAL, is_left=True, is_test=True)
        
        result_right_vertical_grid = GridTransformations.LeftAndRight.transform_bottom_face(self.front, Axes.VERTICAL, is_left=False, is_test=True)
        result_right_horizontal_grid = GridTransformations.LeftAndRight.transform_bottom_face(self.front, Axes.HORIZONTAL, is_left=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_horizontal_grid)))
        
        self.assertTrue(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_right_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_right_vertical_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_left_vertical_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_left_vertical_grid)))
        
    def test_transform_back_face_rotate_left_right(self):
        self.front.opposite = self.face
        self.face.opposite = self.front
        
        expected_left_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_left_horizontal_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        expected_right_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_right_horizontal_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        
        result_left_vertical_grid = GridTransformations.LeftAndRight.transform_back_face(self.front, Axes.VERTICAL, is_left=True, is_test=True)
        result_left_horizontal_grid = GridTransformations.LeftAndRight.transform_back_face(self.front, Axes.HORIZONTAL, is_left=True, is_test=True)
        
        result_right_vertical_grid = GridTransformations.LeftAndRight.transform_back_face(self.front, Axes.VERTICAL, is_left=False, is_test=True)
        result_right_horizontal_grid = GridTransformations.LeftAndRight.transform_back_face(self.front, Axes.HORIZONTAL, is_left=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_horizontal_grid)))
        
        self.assertTrue(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_vertical_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_vertical_grid)))
        
    def test_transform_front_face_rotate_left_right(self):
        expected_left_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_left_horizontal_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        expected_right_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_right_horizontal_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        
        result_left_vertical_grid = GridTransformations.LeftAndRight.transform_front_face(self.front, Axes.VERTICAL, is_left=True, is_test=True)
        result_left_horizontal_grid = GridTransformations.LeftAndRight.transform_front_face(self.front, Axes.HORIZONTAL, is_left=True, is_test=True)
        
        result_right_vertical_grid = GridTransformations.LeftAndRight.transform_front_face(self.front, Axes.VERTICAL, is_left=False, is_test=True)
        result_right_horizontal_grid = GridTransformations.LeftAndRight.transform_front_face(self.front, Axes.HORIZONTAL, is_left=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_horizontal_grid)))
        
        self.assertTrue(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_left_vertical_grid, np.array(expected_left_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_left_horizontal_grid, np.array(expected_left_vertical_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_right_vertical_grid, np.array(expected_right_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_right_horizontal_grid, np.array(expected_right_vertical_grid)))
    

class TestFaceGridInversionOnce(unittest.TestCase):
    
    def setUp(self):
        self.face = Face(Colours.BLUE)
        self.front = Face(Colours.WHITE)
        self.test_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.face.grid = np.array(self.test_grid)
        self.front.grid = np.array(self.test_grid)
    
    def tearDown(self):
        pass
    
    def test_transform_left_face_inversion(self):
        self.front.left = self.face
        self.face.right = self.front
        
        expected_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_horizontal_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        
        result_vertical_grid = GridTransformations.Inversion.transform_left_face(self.front, Axes.VERTICAL, is_test=True)
        result_horizontal_grid = GridTransformations.Inversion.transform_left_face(self.front, Axes.HORIZONTAL, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_vertical_grid)))
        
    def test_transform_right_face_inversion(self):
        self.front.right = self.face
        self.face.left = self.front
        
        expected_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_horizontal_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        
        result_vertical_grid = GridTransformations.Inversion.transform_right_face(self.front, Axes.VERTICAL, is_test=True)
        result_horizontal_grid = GridTransformations.Inversion.transform_right_face(self.front, Axes.HORIZONTAL, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_vertical_grid)))
        
    def test_transform_top_face_inversion(self):
        self.front.top = self.face
        self.face.front = self.front
        
        expected_vertical_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        expected_horizontal_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        
        result_vertical_grid = GridTransformations.Inversion.transform_top_face(self.front, Axes.VERTICAL, is_test=True)
        result_horizontal_grid = GridTransformations.Inversion.transform_top_face(self.front, Axes.HORIZONTAL, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_vertical_grid, np.array(self.test_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(self.test_grid)))
        
    def test_transform_bottom_face_inversion(self):
        self.front.bottom = self.face
        self.face.front = self.front
        
        expected_vertical_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        expected_horizontal_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        
        result_vertical_grid = GridTransformations.Inversion.transform_bottom_face(self.front, Axes.VERTICAL, is_test=True)
        result_horizontal_grid = GridTransformations.Inversion.transform_bottom_face(self.front, Axes.HORIZONTAL, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_vertical_grid, np.array(self.test_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(self.test_grid)))
        
    def test_transform_front_face_inversion(self):
        expected_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_horizontal_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        
        result_vertical_grid = GridTransformations.Inversion.transform_front_face(self.front, Axes.VERTICAL, is_test=True)
        result_horizontal_grid = GridTransformations.Inversion.transform_front_face(self.front, Axes.HORIZONTAL, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_vertical_grid)))
        
    def test_transform_back_face_inversion(self):
        self.front.opposite = self.face
        self.face.opposite = self.front
        
        expected_vertical_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_horizontal_grid = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        
        result_vertical_grid = GridTransformations.Inversion.transform_back_face(self.front, Axes.VERTICAL, is_test=True)
        result_horizontal_grid = GridTransformations.Inversion.transform_back_face(self.front, Axes.HORIZONTAL, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_vertical_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_horizontal_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_vertical_grid, np.array(expected_horizontal_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_horizontal_grid, np.array(expected_vertical_grid)))


class TestFaceGridColShiftsUpDown(unittest.TestCase):
    
    def setUp(self):
        self.face = Face(Colours.BLUE)
        self.front = Face(Colours.WHITE)
        self.from_col_face = Face(Colours.RED)
        self.test_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.face.grid = np.array(self.test_grid)
        self.front.grid = np.array(self.test_grid)
        self.from_col_face.grid = np.array(self.test_grid)
    
    def tearDown(self):
        pass
    
    def test_transform_left_face_col_shift(self):
        self.front.left = self.face
        self.face.right = self.front
        
        expected_left_col_up_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        expected_left_col_down_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        
        result_left_col_up_grid = GridTransformations.ColumnUpAndDown.transform_left_face(self.front, is_rotate_down=False, is_test=True)
        result_left_col_down_grid = GridTransformations.ColumnUpAndDown.transform_left_face(self.front, is_rotate_down=True, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_left_col_down_grid, np.array(expected_left_col_down_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_left_col_up_grid, np.array(expected_left_col_up_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_left_col_down_grid, np.array(expected_left_col_up_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_left_col_up_grid, np.array(expected_left_col_down_grid)))
        
    def test_transform_right_face_col_shift(self):
        self.front.right = self.face
        self.face.left = self.front
        
        expected_left_col_up_grid = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        expected_left_col_down_grid = [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
        
        result_right_col_up_grid = GridTransformations.ColumnUpAndDown.transform_right_face(self.front, is_rotate_down=False, is_test=True)
        result_right_col_down_grid = GridTransformations.ColumnUpAndDown.transform_right_face(self.front, is_rotate_down=True, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_right_col_down_grid, np.array(expected_left_col_down_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_right_col_up_grid, np.array(expected_left_col_up_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_right_col_down_grid, np.array(expected_left_col_up_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_right_col_up_grid, np.array(expected_left_col_down_grid)))
        
    def test_transform_front_face_col_shift_down(self):
        self.front.top = self.face
        self.face.front = self.front
        
        result_front_face_left_col_down_grid = GridTransformations.ColumnUpAndDown.transform_front_face(self.front, is_rotate_down=True, is_right_col=False, is_test=True)
        result_front_face_right_col_down_grid = GridTransformations.ColumnUpAndDown.transform_front_face(self.front, is_rotate_down=True, is_right_col=True, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_front_face_left_col_down_grid, np.array(self.test_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_front_face_right_col_down_grid, np.array(self.test_grid)))
        
    def test_transform_front_face_col_shift_up(self):
        self.front.bottom = self.face
        self.face.front = self.front
        
        result_front_face_left_col_up_grid = GridTransformations.ColumnUpAndDown.transform_front_face(self.front, is_rotate_down=False, is_right_col=False, is_test=True)
        result_front_face_right_col_up_grid = GridTransformations.ColumnUpAndDown.transform_front_face(self.front, is_rotate_down=False, is_right_col=True, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_front_face_left_col_up_grid, np.array(self.test_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_front_face_right_col_up_grid, np.array(self.test_grid)))
        
    def test_transform_back_face_col_shift_up(self):
        # YOUR CODE HERE
        self.front.opposite = self.face
        self.face.opposite = self.front
        self.face.top = self.from_col_face
        self.front.top = self.from_col_face
        self.from_col_face.front = self.front
        self.from_col_face.back = self.face
        
        expected_back_face_right_col_up_grid = [
            [9, 2, 3],
            [6, 5, 6],
            [3, 8, 9]
        ]
        expected_back_face_left_col_up_grid = [
            [1, 2, 7],
            [4, 5, 4],
            [7, 8, 1]
        ]
        
        result_back_face_right_col_up_grid = GridTransformations.ColumnUpAndDown.transform_back_face(self.front, is_rotate_down=False, is_right_col=True, is_test=True)
        result_back_face_left_col_up_grid = GridTransformations.ColumnUpAndDown.transform_back_face(self.front, is_rotate_down=False, is_right_col=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_back_face_right_col_up_grid, np.array(expected_back_face_right_col_up_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_back_face_left_col_up_grid, np.array(expected_back_face_left_col_up_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_back_face_right_col_up_grid, np.array(expected_back_face_left_col_up_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_back_face_left_col_up_grid, np.array(expected_back_face_right_col_up_grid)))

    def test_transform_back_face_col_shift_down(self):
        # YOUR CODE HERE
        self.front.opposite = self.face
        self.face.opposite = self.front
        self.front.bottom = self.from_col_face
        self.face.bottom = self.from_col_face
        self.from_col_face.front = self.front
        self.from_col_face.back = self.face
        
        expected_back_face_right_col_down_grid = [
            [9, 2, 3],
            [6, 5, 6],
            [3, 8, 9]
        ]
        expected_back_face_left_col_down_grid = [
            [1, 2, 7],
            [4, 5, 4],
            [7, 8, 1]
        ]
        
        result_back_face_right_col_down_grid = GridTransformations.ColumnUpAndDown.transform_back_face(self.front, is_rotate_down=True, is_right_col=True, is_test=True)
        result_back_face_left_col_down_grid = GridTransformations.ColumnUpAndDown.transform_back_face(self.front, is_rotate_down=True, is_right_col=False, is_test=True)
        
        self.assertTrue(GridPredicates.are_grids_equal(result_back_face_left_col_down_grid, np.array(expected_back_face_left_col_down_grid)))
        self.assertTrue(GridPredicates.are_grids_equal(result_back_face_right_col_down_grid, np.array(expected_back_face_right_col_down_grid)))
        
        self.assertFalse(GridPredicates.are_grids_equal(result_back_face_left_col_down_grid, np.array(expected_back_face_right_col_down_grid)))
        self.assertFalse(GridPredicates.are_grids_equal(result_back_face_right_col_down_grid, np.array(expected_back_face_left_col_down_grid)))
        
        pass

    
    pass




if __name__ == "__main__":
    unittest.main()