import unittest
from CubeInit import Cube, Face, Piece

class TestValidity(unittest.TestCase):
    
    def test_cube_init(self):
        self.assertEqual(Cube().current_perspective.opposite.center_colour, Cube().green_face.center_colour)
        pass
    
    
    pass


if __name__ == '__main__':
    unittest.main()