import unittest
from cube_init_m import RubixCube
from constants import Colours, Orientation
import face_transformation as ft

class TestFaceTransformation(unittest.TestCase):
    
    def setUp(self) -> None:
        self.cube = RubixCube()
        
    def tearDown(self) -> None:
        pass
    
    def test_transform_front_face_rotate_up(self) -> None:
        # YOUR CODE HERE
        result_front_face = ft.RotateUp.transform_front_face(self.current_perspective, is_test=True)
        self.assertEqual(result_front_face.orientation_to_cube, Orientation.TOP)
        self.assertEqual(result_front_face.front, self.cube.current_perspective.bottom)
        self.assertEqual(result_front_face.back, self.cube.current_perspective.top)
        self.assertIsNone(result_front_face.top)
        self.assertIsNone(result_front_face.bottom)
        
    def test_transform_back_face_rotate_up(self) -> None:
        # YOUR CODE HERE
        result_back_face = ft.RotateUp.transform_back_face(self.current_perspective, is_test=True)
        self.assertEqual(result_back_face.orientation_to_cube, Orientation.BOTTOM)
        self.assertEqual(result_back_face.front, self.cube.current_perspective.bottom)
        self.assertEqual(result_back_face.back, self.cube.current_perspective.top)
        self.assertIsNone(result_back_face.top)
        self.assertIsNone(result_back_face.bottom)
        
    def test_transform_left_face_rotate_up(self):
        # YOUR CODE HERE
        result_left_face = ft.RotateUp.transform_left_face(self.current_perspective, is_test=True)
        self.assertEqual(result_left_face.orientation_to_cube, Orientation.LEFT)
        self.assertEqual(result_left_face.left, self.cube.current_perspective.top)
        self.assertEqual(result_left_face.top, self.cube.current_perspective)
        self.assertIsNone(result_left_face.front)
        self.assertIsNone(result_left_face.back)
        
    def test_transform_right_face_rotate_up(self):
        # YOUR CODE HERE
        result_right_face = ft.RotateUp.transform_right_face(self.cube.current_perspective, is_test=True)
        self.assertEqual(result_right_face.orientation_to_cube, Orientation.RIGHT)
        self.assertEqual(result_right_face.right, self.cube.current_perspective.top)
        self.assertEqual(result_right_face.top, self.cube.current_perspective)
        self.assertIsNone(result_right_face.front)
        self.assertIsNone(result_right_face.back)