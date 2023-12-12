import unittest
from CubeInit import Cube, Face, Piece
from Constraints import FacePositions, Axes
from Transformations import FaceTransformations, GridTransformations
import Predicates

class TestRubixCube(unittest.TestCase):
    
    def test_cube_init(self):
        cube = Cube()
        self.assertEqual(cube.current_perspective.left.right, cube.current_perspective)
        self.assertEqual(cube.current_perspective.top.back, cube.current_perspective.opposite)
        self.assertEqual(cube.current_perspective.bottom.front, cube.current_perspective)
        
    def test_predicate_correct_perspective_init(self):
        cube = Cube()
        self.assertTrue(Predicates.FacePredicates.is_correct_perspective(cube))
        
    def test_predicate_correct_perspective_after_rotation(self):
        cube = Cube()
        cube.rotate_down()
        cube.rotate_up()
        self.assertTrue(Predicates.FacePredicates.is_correct_perspective(cube))
            
    def test_opposite_faces(self):
        cube = Cube()
        self.assertEqual(cube.current_perspective.opposite, cube.green_face)
        self.assertEqual(cube.current_perspective.left, cube.red_face)
        self.assertEqual(cube.current_perspective.right, cube.orange_face)
        self.assertEqual(cube.current_perspective.top, cube.white_face)
        self.assertEqual(cube.current_perspective.bottom, cube.yellow_face)
        self.assertEqual(cube.current_perspective, cube.blue_face)

    def test_left_face_transformation_rotate_down(self):
        cube = Cube()
        
        #$ Testing transformation when rotating down
        new_left_face = FaceTransformations.UpAndDown.transform_left_face(cube.current_perspective, is_rotate_down=True)
        self.assertEqual(new_left_face.top, cube.current_perspective.opposite)
        self.assertEqual(new_left_face.right, cube.current_perspective.top)
        self.assertEqual(new_left_face.opposite, cube.current_perspective.right)
    
    def test_left_face_transformation_rotate_up(self):
        cube = Cube()
        
        #$ Testing transformation when rotating up
        new_left_face = FaceTransformations.UpAndDown.transform_left_face(cube.current_perspective, is_rotate_down=False)
        self.assertEqual(new_left_face.top, cube.current_perspective)
        self.assertEqual(new_left_face.right, cube.current_perspective.bottom)
        self.assertEqual(new_left_face.opposite, cube.current_perspective.right)
        
    def test_left_face_transformation_rotate_left_horizontal(self):
        cube = Cube()
        
        #$ Testing transformation when rotating left horizontally
        new_left_face = FaceTransformations.LeftAndRight.transform_left_face(cube.current_perspective, is_left=True)
        self.assertEqual(new_left_face.left, cube.current_perspective.top)
        self.assertEqual(new_left_face.front, cube.current_perspective)
        self.assertEqual(new_left_face.opposite, cube.current_perspective.right)
        
    def test_left_face_transformation_rotate_right_horizontal(self):
        cube = Cube()
        
        #$ Testing transformation when rotating right horizontally
        new_left_face = FaceTransformations.LeftAndRight.transform_left_face(cube.current_perspective, is_left=False)
        self.assertEqual(new_left_face.left, cube.current_perspective.bottom)
        self.assertEqual(new_left_face.front, cube.current_perspective)
        self.assertEqual(new_left_face.opposite, cube.current_perspective.right)
        
    def test_left_face_transformation_invert_cube_horizontal(self):
        cube = Cube()
        #$ Testing transformation when inverting cube horizontally
        new_left_face = FaceTransformations.Inversion.transform_right_left_faces(cube.current_perspective, is_left_face=True)
        self.assertEqual(new_left_face.top, cube.current_perspective.bottom)
        self.assertEqual(new_left_face.opposite, cube.current_perspective.right)
        self.assertEqual(new_left_face.right, cube.current_perspective.opposite)
        
    def test_right_face_transformation_rotate_down(self):
        cube = Cube()
        
        #$ Testing transformation when rotating down
        new_right_face = FaceTransformations.UpAndDown.transform_right_face(cube.current_perspective, is_rotate_down=True)
        self.assertEqual(new_right_face.top, cube.current_perspective.opposite)
        self.assertEqual(new_right_face.right, cube.current_perspective.bottom)
        self.assertEqual(new_right_face.opposite, cube.current_perspective.left)
    
    def test_right_face_transformation_rotate_up(self):
        cube = Cube()
        
        #$ Testing transformation when rotating up
        new_right_face = FaceTransformations.UpAndDown.transform_right_face(cube.current_perspective, is_rotate_down=False)
        self.assertEqual(new_right_face.top, cube.current_perspective)
        self.assertEqual(new_right_face.right, cube.current_perspective.top)
        self.assertEqual(new_right_face.opposite, cube.current_perspective.left)
        
    def test_right_face_transformation_rotate_left_horizontal(self):
        cube = Cube()
        
        #$ Testing transformation when rotating right horizontally
        new_right_face = FaceTransformations.LeftAndRight.transform_right_face(cube.current_perspective, is_left=True)
        self.assertEqual(new_right_face.right, cube.current_perspective.bottom)
        self.assertEqual(new_right_face.front, cube.current_perspective)
        self.assertEqual(new_right_face.opposite, cube.current_perspective.left)
        
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