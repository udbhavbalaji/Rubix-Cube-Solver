import unittest
from cube_init import RubixCube, Face, Piece
from Constraints import FacePositions, Axes, PossibleOperations
from Transformations import FaceTransformations, GridTransformations
import Predicates

class TestRubixCube(unittest.TestCase):
    
    def setUp(self):
        self.cube = RubixCube()
        pass
    
    def tearDown(self):
        pass
    
    # @unittest.skip(reason='Unable to debug. Will try again later!')
    def test_cube_init(self):
        left_face = self.cube.current_perspective.left
        top_face = self.cube.current_perspective.top
        bottom_face = self.cube.current_perspective.bottom
        
        self.assertEqual(left_face.right, self.cube.current_perspective)
        self.assertEqual(top_face.back, self.cube.current_perspective.opposite)
        self.assertEqual(bottom_face.front, self.cube.current_perspective)
        
    def test_predicate_correct_perspective_init(self):
        self.assertTrue(Predicates.FacePredicates.is_correct_perspective(self.cube))
        
    def test_predicate_correct_perspective_after_rotation(self):
        self.cube.move(PossibleOperations.ROTATE_DOWN)
        self.cube.move(PossibleOperations.ROTATE_UP)
        self.assertTrue(Predicates.FacePredicates.is_correct_perspective(self.cube))
            
    def test_opposite_faces(self):
        self.assertEqual(self.cube.current_perspective.opposite, self.cube.green_face)
        self.assertEqual(self.cube.current_perspective.left, self.cube.red_face)
        self.assertEqual(self.cube.current_perspective.right, self.cube.orange_face)
        self.assertEqual(self.cube.current_perspective.top, self.cube.white_face)
        self.assertEqual(self.cube.current_perspective.bottom, self.cube.yellow_face)
        self.assertEqual(self.cube.current_perspective, self.cube.blue_face)

    def test_left_face_transformation_rotate_down(self):
        #$ Testing transformation when rotating down
        new_left_face = FaceTransformations.UpAndDown.transform_left_face(self.cube.current_perspective, is_rotate_down=True)
        self.assertEqual(new_left_face.top, self.cube.current_perspective.opposite)
        self.assertEqual(new_left_face.right, self.cube.current_perspective.top)
        self.assertEqual(new_left_face.opposite, self.cube.current_perspective.right)
    
    def test_left_face_transformation_rotate_up(self):
        #$ Testing transformation when rotating up
        new_left_face = FaceTransformations.UpAndDown.transform_left_face(self.cube.current_perspective, is_rotate_down=False)
        self.assertEqual(new_left_face.top, self.cube.current_perspective)
        self.assertEqual(new_left_face.right, self.cube.current_perspective.bottom)
        self.assertEqual(new_left_face.opposite, self.cube.current_perspective.right)
        
    def test_left_face_transformation_rotate_left_horizontal(self):
        #$ Testing transformation when rotating left horizontally
        new_left_face = FaceTransformations.LeftAndRight.transform_left_face(self.cube.current_perspective, is_left=True)
        self.assertEqual(new_left_face.left, self.cube.current_perspective.top)
        self.assertEqual(new_left_face.front, self.cube.current_perspective)
        self.assertEqual(new_left_face.opposite, self.cube.current_perspective.right)
        
    def test_left_face_transformation_rotate_right_horizontal(self):
        #$ Testing transformation when rotating right horizontally
        new_left_face = FaceTransformations.LeftAndRight.transform_left_face(self.cube.current_perspective, is_left=False)
        self.assertEqual(new_left_face.left, self.cube.current_perspective.bottom)
        self.assertEqual(new_left_face.front, self.cube.current_perspective)
        self.assertEqual(new_left_face.opposite, self.cube.current_perspective.right)
        
    def test_left_face_transformation_invert_cube_horizontal(self):
        #$ Testing transformation when inverting cube horizontally
        new_left_face = FaceTransformations.Inversion.transform_right_left_faces(self.cube.current_perspective, is_left_face=True)
        self.assertEqual(new_left_face.top, self.cube.current_perspective.bottom)
        self.assertEqual(new_left_face.opposite, self.cube.current_perspective.right)
        self.assertEqual(new_left_face.right, self.cube.current_perspective.opposite)
        
    def test_right_face_transformation_rotate_down(self):
        #$ Testing transformation when rotating down
        new_right_face = FaceTransformations.UpAndDown.transform_right_face(self.cube.current_perspective, is_rotate_down=True)
        self.assertEqual(new_right_face.top, self.cube.current_perspective.opposite)
        self.assertEqual(new_right_face.right, self.cube.current_perspective.bottom)
        self.assertEqual(new_right_face.opposite, self.cube.current_perspective.left)
    
    def test_right_face_transformation_rotate_up(self):
        #$ Testing transformation when rotating up
        new_right_face = FaceTransformations.UpAndDown.transform_right_face(self.cube.current_perspective, is_rotate_down=False)
        self.assertEqual(new_right_face.top, self.cube.current_perspective)
        self.assertEqual(new_right_face.right, self.cube.current_perspective.top)
        self.assertEqual(new_right_face.opposite, self.cube.current_perspective.left)
        
    def test_right_face_transformation_rotate_left_horizontal(self):
        #$ Testing transformation when rotating right horizontally
        new_right_face = FaceTransformations.LeftAndRight.transform_right_face(self.cube.current_perspective, is_left=True)
        self.assertEqual(new_right_face.right, self.cube.current_perspective.bottom)
        self.assertEqual(new_right_face.front, self.cube.current_perspective)
        self.assertEqual(new_right_face.opposite, self.cube.current_perspective.left)
        
    # def test_right_face_transformation_rotate_right_horizontal(self):
    #     cube = Cube()
        
    #     #$ Testing transformation when rotating right horizontally
    #     new_right_face = FaceTransformations.rightAndRight.transform_right_face(cube.current_perspective, is_left=False)
    #     self.assertEqual(new_right_face.right, cube.current_perspective.bottom)
    #     self.assertEqual(new_right_face.front, cube.current_perspective)
    #     self.assertEqual(new_right_face.opposite, cube.current_perspective.right)
        
    # def test_right_face_transformation_invert_cube_horizontal(self):
    #     cube = Cube()
    #     #$ Testing transformation when inverting cube horizontally
    #     new_right_face = FaceTransformations.Inversion.transform_right_right_faces(cube.current_perspective, is_left_face=True)
    #     self.assertEqual(new_right_face.top, cube.current_perspective.right)
    #     self.assertEqual(new_right_face.front, cube.current_perspective)
    #     self.assertEqual(new_right_face.opposite, cube.current_perspective.right)
        


if __name__ == '__main__':
    unittest.main()