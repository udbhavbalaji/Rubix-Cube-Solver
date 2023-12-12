"""
This file holds the code to initiailize a random cube, as well as ensure that the cube can be recreated in real life.
POSSIBLE ADDITIONS: Ability for user to enter a cube configuration to test out the program
"""

import numpy as np
from Constraints import Colours, Axes, PieceType, PossibleCornerPieces, FacePositions, Orientation, PossibleOperations
from Transformations import GridTransformations, FaceTransformations
import Predicates
from Operations import OPERATIONS

class Cube():
    
    NUM_FACES = 6
    # $ Face Order: Front, Right, Back, Left, Top, Bottom
    # $ Colour Order: Blue, Orange, Green, Red, White, Yellow
    COLOURS = [Colours.BLUE, Colours.ORANGE, Colours.GREEN, Colours.RED, Colours.WHITE, Colours.YELLOW]
    
    def __init__(self, current=None, initial=None, blue=None, white=None, yellow=None, red=None, orange=None, green=None, is_copy=False, shift=None):
        self.current_perspective = current
        self.initial_perspective = initial
        
        self.blue_face = blue
        self.white_face = white
        self.yellow_face = yellow
        self.red_face = red
        self.orange_face = orange
        self.green_face = green
        
        self._kwargs_dict = self.init_kwargs()
                
        if not is_copy:
            self.initialize_random_cube()
            
        self.kwargs_dict = self.init_kwargs()
                        
    def __str__(self):
        front = self.current_perspective.copy()
        
        left_grid = self.get_2D_cube_grid(front.left, Orientation.LEFT)
        right_grid = self.get_2D_cube_grid(front.right, Orientation.RIGHT)
        top_grid = self.get_2D_cube_grid(front.top, Orientation.TOP)
        bottom_grid = self.get_2D_cube_grid(front.bottom, Orientation.BOTTOM)
        back_grid = self.get_2D_cube_grid(front.opposite, Orientation.BACK)
        front_grid = self.get_2D_cube_grid(front, Orientation.FRONT)
        
        output = f'      ______\n'
        output += f'     !{left_grid[0]}|\n     !{left_grid[1]}|\n     !{left_grid[2]}|\n'
        output += '________________________\n'
        output += f'{front_grid[0]}|{bottom_grid[0]}|{back_grid[0]}|{top_grid[0]}|\n'
        output += f'{front_grid[1]}|{bottom_grid[1]}|{back_grid[1]}|{top_grid[1]}|\n'
        output += f'{front_grid[2]}|{bottom_grid[2]}|{back_grid[2]}|{top_grid[2]}|\n'
        output += '________________________\n'
        output += f'     !{right_grid[0]}|\n     !{right_grid[1]}|\n     !{right_grid[2]}|\n'
        output += f'      ______'
        
        return output
            
    def init_kwargs(self):
        kwargs_template = {
            'cube': None,
            'axis': None,
            'current_front': None
        }
        kwargs_dict = {}
        
        for i in range(len(PossibleOperations.MOVES)):
            kwargs = kwargs_template.copy()
            if i < 8 or i == (len(PossibleOperations.MOVES)-1):
                kwargs['cube'] = self
                if i in [0, 1, 6]:
                    kwargs['axis'] = Axes.VERTICAL
                elif i in [4, 5, 7]:
                    kwargs['axis'] = Axes.HORIZONTAL
            else:
                kwargs['current_front'] = self.current_perspective
                
            operation = OPERATIONS[i]
            kwargs_dict[PossibleOperations.MOVES[i]] = (operation, kwargs)
        
        return kwargs_dict
            
    @property
    def kwargs_dict(self):
        return self._kwargs_dict
    
    @kwargs_dict.setter
    def kwargs_dict(self, new_dict):
        self._kwargs_dict = new_dict
    
    def copy(self):
        """
        This method creates and returns a copy of the current object (Cube) with all attribute values duplicated.

        Returns:
            Cube: A copy of the current instance is created and returned.
        """
        return Cube(self.current_perspective, self.initial_perspective, self.blue_face, self.white_face, self.yellow_face, \
                    self.red_face, self.orange_face, self.green_face, is_copy=True)
    
    def initialize_random_cube(self):
        """
        * This method initializes the Rubix Cube. The faces are created, edges are joined, and positional attributes assigned.
        ! So far, I've done initializing the cube.
        TODO: Complete all possible operations (rotations and movements)
        TODO: Finish reset perspective
        TODO: Shuffle the cube (multiple operations)
        * More documentation will follow
        
        @params: None
        @modifies: Cube().__getattrs__.* - All attributes in Cube()
        @returns: None
        """
        
        #* Creating the faces
        
        self.blue_face = Face(self.COLOURS[0])
        self.orange_face = Face(self.COLOURS[1])
        self.green_face = Face(self.COLOURS[2])
        self.red_face = Face(self.COLOURS[3])
        self.white_face = Face(self.COLOURS[4], is_side_face=False)
        self.yellow_face = Face(self.COLOURS[5], is_side_face=False)
        
        ## Joining the faces to make a cube
        self.current_perspective = self.blue_face
        
        ## Joining the side faces
        self.blue_face.left = self.red_face
        self.blue_face.right = self.orange_face
        
        self.orange_face.left = self.blue_face
        self.orange_face.right = self.green_face
        
        self.green_face.left = self.orange_face
        self.green_face.right = self.red_face
        
        self.red_face.left = self.green_face
        self.red_face.right = self.blue_face
        
        ## Joining the top face
        self.white_face.front = self.blue_face
        self.blue_face.top = self.white_face
        
        self.white_face.right = self.orange_face
        self.orange_face.top = self.white_face
        
        self.white_face.back = self.green_face
        self.green_face.top = self.white_face
        
        self.white_face.left = self.red_face
        self.red_face.top = self.white_face
        
        ## Joining the bottom face
        self.yellow_face.front = self.blue_face
        self.blue_face.bottom = self.yellow_face
        
        self.yellow_face.right = self.orange_face
        self.orange_face.bottom = self.yellow_face
        
        self.yellow_face.back = self.green_face
        self.green_face.bottom = self.yellow_face
        
        self.yellow_face.left = self.red_face
        self.red_face.bottom = self.yellow_face
        
        ## Connecting opposite faces
        self.white_face.opposite = self.yellow_face
        self.yellow_face.opposite = self.white_face
        
        self.blue_face.opposite = self.green_face
        self.green_face.opposite = self.blue_face
        
        self.red_face.opposite = self.orange_face
        self.orange_face.opposite = self.red_face
        
        ## Initializing complements
        # Blue Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY, verbose=False)
        # self.rotate_left(Axes.VERTICAL)
        # Orange Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY, verbose=False)
        # self.rotate_left(Axes.VERTICAL)
        # Green Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY, verbose=False)
        # self.rotate_left(Axes.VERTICAL)
        # Red Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY, verbose=False)
        # self.rotate_left(Axes.VERTICAL)
        # Back to Blue Face
        self.move(PossibleOperations.ROTATE_DOWN, verbose=False)
        # self.rotate_down()
        # White Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_DOWN, verbose=False)
        self.move(PossibleOperations.ROTATE_DOWN, verbose=False)
        # self.rotate_up()
        # self.rotate_up()
        # Yellow Face
        self.assign_complements(self.current_perspective)
        
        # Back to Blue Face
        self.move(PossibleOperations.RESET_PERSPECTIVE, verbose=False)
        # self.reset_perspective()
        
    def assign_complements(self, face):        
        ## Assigning complements of edge pieces
        face.grid[FacePositions.TOP_CENTER].complement = face.top.grid[FacePositions.BOTTOM_CENTER]
        face.grid[FacePositions.MID_LEFT].complement = face.left.grid[FacePositions.MID_RIGHT]
        face.grid[FacePositions.MID_RIGHT].complement = face.right.grid[FacePositions.MID_LEFT]
        face.grid[FacePositions.BOTTOM_CENTER].complement = face.bottom.grid[FacePositions.TOP_CENTER]
        
        ## Assigning complements for corner pieces
        face.grid[FacePositions.TOP_LEFT].complements = (face.top.grid[FacePositions.BOTTOM_LEFT], face.left.grid[FacePositions.TOP_RIGHT])
        face.grid[FacePositions.TOP_RIGHT].complements = (face.top.grid[FacePositions.BOTTOM_RIGHT], face.right.grid[FacePositions.TOP_LEFT])
        face.grid[FacePositions.BOTTOM_LEFT].complements = (face.bottom.grid[FacePositions.TOP_LEFT], face.left.grid[FacePositions.BOTTOM_RIGHT])
        face.grid[FacePositions.BOTTOM_RIGHT].complements = (face.bottom.grid[FacePositions.TOP_RIGHT], face.right.grid[FacePositions.BOTTOM_LEFT])
        
    def get_kwargs(original_func):
        
        def perform_operation(self, operation, verbose=True):
            shift, kwargs = self.kwargs_dict[operation]
            shift(**kwargs)
            original_func(self, operation, verbose)
        
        return perform_operation
        
    @get_kwargs
    def move(self, operation, verbose=True):
        if verbose:
            print(operation)
    
    # def rotate_left(self, axis):
    #     """
    #     * This method performs the operation of rotating the cube leftwards. It makes calls to get the 
    #     * transformed faces of the cube. These values are then transferred into the existing Face object.
        
    #     @params: axis (ENUM) - The enum is defined in Constraints.Axes . Tells the program along which axis to rotate.
    #     @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
    #     @returns: None
    #     """
    #     current = self.current_perspective
        
    #     if axis == Axes.VERTICAL:
    #         print('ROTATING LEFT VERTICALLY')
    #         ## Getting transformed Top & Bottom Faces
    #         new_top_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=True, is_left=True)
    #         new_bottom_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=False, is_left=True)
            
    #         ## Getting transformed Top & Bottom Grids
    #         new_top_grid = GridTransformations.LeftAndRight.transform_top_face(current, axis, is_left=True)
    #         new_bottom_grid = GridTransformations.LeftAndRight.transform_bottom_face(current, axis, is_left=True)
            
    #         ## Updating grid for each transformed face
    #         new_top_face.grid = new_top_grid
    #         new_bottom_face.grid = new_bottom_grid
            
    #         ## Changing perspective to right face
    #         self.current_perspective = self.current_perspective.right
            
    #         ## Transferring transformed attribute values to original object
    #         self.transfer_faces(self.current_perspective.top, new_top_face)
    #         self.transfer_faces(self.current_perspective.bottom, new_bottom_face)
    #     else:
    #         print('ROTATING LEFT HORIZONTALLY')
    #         ## Getting transformed Left & Right Faces
    #         new_right_face = FaceTransformations.LeftAndRight.transform_right_face(current, is_left=True)
    #         new_left_face = FaceTransformations.LeftAndRight.transform_left_face(current, is_left=True)
            
    #         ## Getting transformed Left & Right Grids
    #         new_right_grid = GridTransformations.LeftAndRight.transform_right_face(current, axis, is_left=True)
    #         new_left_grid = GridTransformations.LeftAndRight.transform_left_face(current, axis, is_left=True)
            
    #         ## Getting transformed Front & Back Faces
    #         new_front_face = FaceTransformations.LeftAndRight.transform_front_back_faces(current, is_front=True, is_left=True)
    #         new_back_face = FaceTransformations.LeftAndRight.transform_front_back_faces(current, is_front=False, is_left=True)
            
    #         ## Getting transformed Front & Back Grids
    #         new_front_grid = GridTransformations.LeftAndRight.transform_front_face(current, axis, is_left=True)
    #         new_back_grid = GridTransformations.LeftAndRight.transform_back_face(current, axis, is_left=True)
            
    #         ## Getting transformed Top & Bottom Faces
    #         new_top_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=True, is_left=True)
    #         new_bottom_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=False, is_left=True)
            
    #         ## Getting transformed Top & Bottom Faces
    #         new_top_grid = GridTransformations.LeftAndRight.transform_top_face(current, axis, is_left=True)
    #         new_bottom_grid = GridTransformations.LeftAndRight.transform_bottom_face(current, axis, is_left=True)
            
    #         ## Updating grid for each transformed face
    #         new_left_face.grid = new_left_grid
    #         new_right_face.grid = new_right_grid
    #         new_front_face.grid = new_front_grid
    #         new_back_face.grid = new_back_grid
    #         new_top_face.grid = new_top_grid
    #         new_bottom_face.grid = new_bottom_grid
            
    #         ## Transferring transformed attribute values to original object
    #         self.transfer_faces(self.current_perspective, new_front_face)
    #         self.transfer_faces(self.current_perspective.left, new_top_face)
    #         self.transfer_faces(self.current_perspective.right, new_bottom_face)
    #         self.transfer_faces(self.current_perspective.top, new_right_face)
    #         self.transfer_faces(self.current_perspective.bottom, new_left_face)
    #         self.transfer_faces(self.current_perspective.opposite, new_back_face)
                
    # def rotate_right(self, axis):
    #     """
    #     * This method performs the operation of rotating the cube rightwards. It makes calls to get the 
    #     * transformed faces of the cube. These values are then transferred into the existing Face object.
        
    #     @params: axis (ENUM) - The enum is defined in Constraints.Axes . Tells the program along which axis to rotate.
    #     @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
    #     @returns: None
    #     """
    #     current = self.current_perspective
        
    #     if axis == Axes.VERTICAL:
    #         print('ROTATING RIGHT VERTICALLY')
    #         ## Getting transformed Top & Bottom Faces
    #         new_top_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=True, is_left=False)
    #         new_bottom_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=False, is_left=False)
            
    #         ## Getting transformed Top & Bottom Grids
    #         new_top_grid = GridTransformations.LeftAndRight.transform_top_face(current, axis, is_left=False)
    #         new_bottom_grid = GridTransformations.LeftAndRight.transform_bottom_face(current, axis, is_left=False)
            
    #         ## Updating grid for each transformed face
    #         new_top_face.grid = new_top_grid
    #         new_bottom_face.grid = new_bottom_grid
            
    #         ## Changing perspective to left face
    #         self.current_perspective = self.current_perspective.left
            
    #         ## Transferring transformed attribute values to original object
    #         self.transfer_faces(self.current_perspective.top, new_top_face)
    #         self.transfer_faces(self.current_perspective.bottom, new_bottom_face)
    #     else:
    #         print('ROTATING RIGHT HORIZONTALLY')
    #         ## Getting transformed Left & Right Faces
    #         new_right_face = FaceTransformations.LeftAndRight.transform_right_face(current, is_left=False)
    #         new_left_face = FaceTransformations.LeftAndRight.transform_left_face(current, is_left=False)
            
    #         ## Getting transformed Left & Right Grids
    #         new_right_grid = GridTransformations.LeftAndRight.transform_right_face(current, axis, is_left=False)
    #         new_left_grid = GridTransformations.LeftAndRight.transform_left_face(current, axis, is_left=False)
            
    #         ## Getting transformed Front & Back Faces
    #         new_front_face = FaceTransformations.LeftAndRight.transform_front_back_faces(current, is_front=True, is_left=False)
    #         new_back_face = FaceTransformations.LeftAndRight.transform_front_back_faces(current, is_front=False, is_left=False)
            
    #         ## Getting transformed Front & Back Grids
    #         new_front_grid = GridTransformations.LeftAndRight.transform_front_face(current, axis, is_left=False)
    #         new_back_grid = GridTransformations.LeftAndRight.transform_back_face(current, axis, is_left=False)
            
    #         ## Getting transformed Top & Bottom Faces
    #         new_top_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=True, is_left=False)
    #         new_bottom_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=False, is_left=False)
            
    #         ## Getting transformed Top & Bottom Grids
    #         new_top_grid = GridTransformations.LeftAndRight.transform_top_face(current, axis, is_left=False)
    #         new_bottom_grid = GridTransformations.LeftAndRight.transform_bottom_face(current, axis, is_left=False)
            
    #         ## Updating grid for each transformed face
    #         new_left_face.grid = new_left_grid
    #         new_right_face.grid = new_right_grid
    #         new_front_face.grid = new_front_grid
    #         new_back_face.grid = new_back_grid
    #         new_top_face.grid = new_top_grid
    #         new_bottom_face.grid = new_bottom_grid
            
    #         ## Transferring transformed attribute values to original object
    #         self.transfer_faces(self.current_perspective, new_front_face)
    #         self.transfer_faces(self.current_perspective.left, new_bottom_face)
    #         self.transfer_faces(self.current_perspective.right, new_top_face)
    #         self.transfer_faces(self.current_perspective.top, new_left_face)
    #         self.transfer_faces(self.current_perspective.bottom, new_right_face)
    #         self.transfer_faces(self.current_perspective.opposite, new_back_face)
        
    # def rotate_up(self):
    #     """
    #     * This method performs the operation of rotating the cube upwards. It makes calls to get the 
    #     * transformed faces of the cube. These values are then transferred into the existing Face object.
        
    #     @params: None
    #     @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
    #     @returns: None
    #     """
    #     print('ROTATING UP')
    #     current = self.current_perspective
        
    #     ## Getting transformed Left & Right Faces
    #     new_left_face = FaceTransformations.UpAndDown.transform_left_face(current, is_rotate_down=False)
    #     new_right_face = FaceTransformations.UpAndDown.transform_right_face(current, is_rotate_down=False)
        
    #     ## Getting transformed Left & Right Grids
    #     new_left_grid = GridTransformations.UpAndDown.transform_left_face(current, is_rotate_down=False)
    #     new_right_grid = GridTransformations.UpAndDown.transform_right_face(current, is_rotate_down=False)
        
    #     ## Getting transformed Front & Back Faces
    #     new_front_face = FaceTransformations.UpAndDown.transform_front_back_faces(current, is_rotate_down=False)
    #     new_back_face = FaceTransformations.UpAndDown.transform_front_back_faces(current, is_front=False, is_rotate_down=False)
        
    #     ## Getting transformed Back Grid
    #     new_back_grid = GridTransformations.UpAndDown.transform_back_face(current, is_rotate_down=False)
        
    #     ## Getting transformed Top & Bottom Faces
    #     new_top_face = FaceTransformations.UpAndDown.transform_top_bottom_faces(current, is_rotate_down=False)
    #     new_bottom_face = FaceTransformations.UpAndDown.transform_top_bottom_faces(current, is_top=False, is_rotate_down=False)
        
    #     ## Getting transformed Top Grid
    #     new_bottom_grid = GridTransformations.UpAndDown.transform_bottom_face(current, is_rotate_down=False)
    #     new_top_grid = GridTransformations.UpAndDown.transform_top_face(current, is_rotate_down=False)
        
    #     ## Updating grid for each transformed face
    #     new_left_face.grid = new_left_grid
    #     new_right_face.grid = new_right_grid
    #     new_top_face.grid = new_top_grid
    #     new_bottom_face.grid = new_bottom_grid
    #     new_back_face.grid = new_back_grid
        
    #     ## Changing perspective to top face
    #     self.current_perspective = self.current_perspective.bottom
        
    #     ## Transferring transformed attribute values to original object
    #     self.transfer_faces(self.current_perspective, new_bottom_face)
    #     self.transfer_faces(self.current_perspective.right, new_right_face)
    #     self.transfer_faces(self.current_perspective.left, new_left_face)
    #     self.transfer_faces(self.current_perspective.top, new_front_face)
    #     self.transfer_faces(self.current_perspective.bottom, new_back_face)
    #     self.transfer_faces(self.current_perspective.opposite, new_top_face)
        
    # def rotate_down(self):
    #     """
    #     * This method performs the operation of rotating the cube downwards. It makes calls to get the 
    #     * transformed faces of the cube. These values are then transferred into the existing Face object.
        
    #     @params: None
    #     @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
    #     @returns: None
    #     """
    #     print('ROTATING DOWN')
    #     current = self.current_perspective
        
    #     ## Getting transformed Left & Right Faces
    #     new_left_face = FaceTransformations.UpAndDown.transform_left_face(current, is_rotate_down=True)
    #     new_right_face = FaceTransformations.UpAndDown.transform_right_face(current, is_rotate_down=True)
        
    #     ## Getting transformed Left & Right Grids
    #     new_left_grid = GridTransformations.UpAndDown.transform_left_face(current, is_rotate_down=True)
    #     new_right_grid = GridTransformations.UpAndDown.transform_right_face(current, is_rotate_down=True)
        
    #     ## Getting transformed Front & Back Faces
    #     new_front_face = FaceTransformations.UpAndDown.transform_front_back_faces(current, is_rotate_down=True)
    #     new_back_face = FaceTransformations.UpAndDown.transform_front_back_faces(current, is_front=False, is_rotate_down=True)
        
    #     ## Getting transformed Back Grid
    #     new_back_grid = GridTransformations.UpAndDown.transform_back_face(current, is_rotate_down=True)
        
    #     ## Getting transformed Top & Bottom Faces
    #     new_top_face = FaceTransformations.UpAndDown.transform_top_bottom_faces(current, is_rotate_down=True)
    #     new_bottom_face = FaceTransformations.UpAndDown.transform_top_bottom_faces(current, is_top=False, is_rotate_down=True)
        
    #     ## Getting transformed Top Grid
    #     new_top_grid = GridTransformations.UpAndDown.transform_top_face(current, is_rotate_down=True)
    #     new_bottom_grid = GridTransformations.UpAndDown.transform_bottom_face(current, is_rotate_down=True)
        
    #     ## Updating grid for each transformed face
    #     new_left_face.grid = new_left_grid
    #     new_right_face.grid = new_right_grid
    #     new_top_face.grid = new_top_grid
    #     new_bottom_face.grid = new_bottom_grid
    #     new_back_face.grid = new_back_grid
        
    #     ## Changing perspective to top face
    #     self.current_perspective = self.current_perspective.top
        
    #     ## Transferring transformed attribute values to original object
    #     self.transfer_faces(self.current_perspective, new_top_face)
    #     self.transfer_faces(self.current_perspective.right, new_right_face)
    #     self.transfer_faces(self.current_perspective.left, new_left_face)
    #     self.transfer_faces(self.current_perspective.top, new_back_face)
    #     self.transfer_faces(self.current_perspective.bottom, new_front_face)
    #     self.transfer_faces(self.current_perspective.opposite, new_bottom_face)
          
    # def invert_cube(self, axis=Axes.VERTICAL):
    #     """
    #     * This method performs the operation of inverting the cube. It makes calls to get the 
    #     * transformed faces of the cube. These values are then transferred into the existing Face object.
        
    #     @params: axis (ENUM) - The enum is defined in Constraints.Axes . Tells the program along which axis to invert.
    #     @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
    #     @returns: None
    #     """
    #     current = self.current_perspective
        
    #     if axis == Axes.VERTICAL:
    #         print('INVERTING CUBE VERTICALLY')
            
    #         ## Getting transformed Top & Bottom Faces
    #         new_top_face = FaceTransformations.Inversion.transform_top_bottom_faces(current, axis, is_top=True)
    #         new_bottom_face = FaceTransformations.Inversion.transform_top_bottom_faces(current, axis, is_top=False)
            
    #         ## Getting transformed Top & Bottom Grids
    #         new_top_grid = GridTransformations.Inversion.transform_top_face(current, axis)
    #         new_bottom_grid = GridTransformations.Inversion.transform_bottom_face(current, axis)
            
    #         ## Updating grid for each transformed face
    #         new_top_face.grid = new_top_grid
    #         new_bottom_face.grid = new_bottom_grid
            
    #         ## Changing perspective to opposite face
    #         self.current_perspective = self.current_perspective.opposite
            
    #         ## Transferring transformed attribute values to original object
    #         self.transfer_faces(self.current_perspective.top, new_top_face)
    #         self.transfer_faces(self.current_perspective.bottom, new_bottom_face)
            
    #     else:
    #         print('INVERTING CUBE HORIZONTALLY')
            
    #         ## Getting transformed Top & Bottom Faces
    #         new_top_face = FaceTransformations.Inversion.transform_top_bottom_faces(current, axis, is_top=True)
    #         new_bottom_face = FaceTransformations.Inversion.transform_top_bottom_faces(current, axis, is_top=False)
            
    #         ## Getting transformed Top & Bottom Grids
    #         new_top_grid = GridTransformations.Inversion.transform_top_face(current, axis)
    #         new_bottom_grid = GridTransformations.Inversion.transform_bottom_face(current, axis)
            
    #         ## Getting transformed Front & Back Faces
    #         new_front_face = FaceTransformations.Inversion.transform_front_back_faces(current, is_front=True)
    #         new_back_face = FaceTransformations.Inversion.transform_front_back_faces(current, is_front=False)
            
    #         ## Getting transformed Front & Back Grids
    #         new_front_grid = GridTransformations.Inversion.transform_front_face(current, axis)
    #         new_back_grid = GridTransformations.Inversion.transform_back_face(current, axis)
            
    #         ## Getting transformed Left & Right Faces
    #         new_left_face = FaceTransformations.Inversion.transform_right_left_faces(current, is_left_face=True)
    #         new_right_face = FaceTransformations.Inversion.transform_right_left_faces(current, is_left_face=False)
            
    #         ## Getting transformed Left & Right Grids
    #         new_left_grid = GridTransformations.Inversion.transform_left_face(current, axis)
    #         new_right_grid = GridTransformations.Inversion.transform_right_face(current, axis)
            
    #         ## Updating grid for each transformed face
    #         new_left_face.grid = new_left_grid
    #         new_right_face.grid = new_right_grid
    #         new_top_face.grid = new_top_grid
    #         new_bottom_face.grid = new_bottom_grid
    #         new_back_face.grid = new_back_grid
    #         new_front_face.grid = new_front_grid
            
    #         ## Changing perspective to opposite face
    #         self.current_perspective = self.current_perspective.opposite
            
    #         ## Transferring transformed attribute values to original object
    #         self.transfer_faces(self.current_perspective, new_back_face)
    #         self.transfer_faces(self.current_perspective.right, new_right_face)
    #         self.transfer_faces(self.current_perspective.left, new_left_face)
    #         self.transfer_faces(self.current_perspective.top, new_bottom_face)
    #         self.transfer_faces(self.current_perspective.bottom, new_top_face)
    #         self.transfer_faces(self.current_perspective.opposite, new_front_face)
        
    # def transfer_faces(self, old, new):
    #     """
    #     *This method transplants values from the copied face object to the original face object of the cube.
        
    #     @params: old (Face): Original face object from the Cube class
    #     @      : new (Face): Copied face object with updated attributes (after transformation)
        
    #     @modified: Face.*: All attributes from the Face class
    #     @returns: None
    #     """
    #     old.left = new.left
    #     old.right = new.right
    #     old.top = new.top
    #     old.bottom = new.bottom
    #     old.front = new.front
    #     old.back = new.back
    #     old.is_side_face = new.is_side_face
    #     old.grid = new.grid
    
    def print_cube_grid(self):
        front = self.current_perspective.copy()
        
        left_grid = self.get_2D_cube_grid(front.left, Orientation.LEFT)
        right_grid = self.get_2D_cube_grid(front.right, Orientation.RIGHT)
        top_grid = self.get_2D_cube_grid(front.top, Orientation.TOP)
        bottom_grid = self.get_2D_cube_grid(front.bottom, Orientation.BOTTOM)
        back_grid = self.get_2D_cube_grid(front.opposite, Orientation.BACK)
        front_grid = self.get_2D_cube_grid(front, Orientation.FRONT)
        
        print(f'      ______')
        print(f'     !{left_grid[0]}|\n     !{left_grid[1]}|\n     !{left_grid[2]}|')
        print('________________________')
        print(f'{front_grid[0]}|{bottom_grid[0]}|{back_grid[0]}|{top_grid[0]}|')
        print(f'{front_grid[1]}|{bottom_grid[1]}|{back_grid[1]}|{top_grid[1]}|')
        print(f'{front_grid[2]}|{bottom_grid[2]}|{back_grid[2]}|{top_grid[2]}|')
        print('________________________')
        print(f'     !{right_grid[0]}|\n     !{right_grid[1]}|\n     !{right_grid[2]}|')
        print(f'      ______')
        
    def get_2D_cube_grid(self, face, orientation):
        if orientation == Orientation.LEFT:
            first_row = f'{face.grid[FacePositions.TOP_RIGHT].colour[0]} {face.grid[FacePositions.TOP_CENTER].colour[0]} {face.grid[FacePositions.TOP_LEFT].colour[0]}'
            second_row = f'{face.grid[FacePositions.MID_RIGHT].colour[0]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.MID_LEFT].colour[0]}'
            third_row = f'{face.grid[FacePositions.BOTTOM_RIGHT].colour[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour[0]} {face.grid[FacePositions.BOTTOM_LEFT].colour[0]}'
            
        elif orientation in [Orientation.FRONT, Orientation.BOTTOM, Orientation.TOP]:
            first_row = f'{face.grid[FacePositions.TOP_LEFT].colour[0]} {face.grid[FacePositions.MID_LEFT].colour[0]} {face.grid[FacePositions.BOTTOM_LEFT].colour[0]}'
            second_row = f'{face.grid[FacePositions.TOP_CENTER].colour[0]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour[0]}'
            third_row = f'{face.grid[FacePositions.TOP_RIGHT].colour[0]} {face.grid[FacePositions.MID_RIGHT].colour[0]} {face.grid[FacePositions.BOTTOM_RIGHT].colour[0]}'
            
        elif orientation == Orientation.BACK:
            first_row = f'{face.grid[FacePositions.BOTTOM_RIGHT].colour[0]} {face.grid[FacePositions.MID_RIGHT].colour[0]} {face.grid[FacePositions.TOP_RIGHT].colour[0]}'
            second_row = f'{face.grid[FacePositions.BOTTOM_CENTER].colour[0]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.TOP_CENTER].colour[0]}'
            third_row = f'{face.grid[FacePositions.BOTTOM_LEFT].colour[0]} {face.grid[FacePositions.MID_LEFT].colour[0]} {face.grid[FacePositions.TOP_LEFT].colour[0]}'
            
        elif orientation == Orientation.RIGHT:
            first_row = f'{face.grid[FacePositions.BOTTOM_LEFT].colour[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour[0]} {face.grid[FacePositions.BOTTOM_RIGHT].colour[0]}'
            second_row = f'{face.grid[FacePositions.MID_LEFT].colour[0]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.MID_RIGHT].colour[0]}'
            third_row = f'{face.grid[FacePositions.TOP_LEFT].colour[0]} {face.grid[FacePositions.TOP_CENTER].colour[0]} {face.grid[FacePositions.TOP_RIGHT].colour[0]}'
        
        return (first_row, second_row, third_row)
    
    def print_cube_structure_2D(self):
        front = self.current_perspective.copy()
        # Printing Format
        #       Left
        # Front Bottom Back Top
        #       Right
        print('\n            Left')
        print('Front    Bottom     Back    Top')
        print('            Right\n')
        print(f'\n          {front.left.center_colour}')
        print(f'{front.center_colour}    {front.bottom.center_colour}    {front.opposite.center_colour}    {front.top.center_colour}')
        print(f'          {front.right.center_colour}\n')
        
    def get_attributes(self):
        front = self.current_perspective
        right_face = front.right
        left_face = front.left
        top_face = front.top
        bottom_face = front.bottom
        opposite_face = front.opposite
        
        print('\nFront Attributes')
        print(f'Front: {front}, Left: {left_face}, Right: {right_face}, Top: {top_face}, Bottom: {bottom_face}, \
                Back: {opposite_face}')
        print('Front Colours')
        print(f'Front: {front.center_colour}, Left: {front.left.center_colour}, Right: {front.right.center_colour}, \
                Top: {front.top.center_colour}, Bottom: {front.bottom.center_colour}, Back: {front.opposite.center_colour}\n')
    
    def reset_perspective(self):
        print('RESETTING PERSPECTIVE')
        iters = 0
        while True:
            blue_face_orientation = self.get_orientation()
            if Predicates.FacePredicates.is_correct_perspective(self):
                break
            else:
                orientation = self.get_orientation()
                print(orientation)
                if orientation == Orientation.TOP:
                    self.move(PossibleOperations.ROTATE_DOWN)
                    # self.rotate_down()
                elif orientation == Orientation.BOTTOM:
                    self.move(PossibleOperations.ROTATE_UP)
                    # self.rotate_up()
                elif orientation == Orientation.BACK:
                    if Predicates.FacePredicates.is_white_face_top(self.current_perspective, self.white_face):
                        self.move(PossibleOperations.INVERT_CUBE_VERTICALLY)
                        # self.invert_cube(Axes.VERTICAL)
                    else:
                        self.move(PossibleOperations.INVERT_CUBE_HORIZONTALLY)
                        # self.invert_cube(Axes.HORIZONTAL)
                elif orientation == Orientation.LEFT:
                    self.move(PossibleOperations.ROTATE_RIGHT_VERTICALLY)
                    # self.rotate_right(Axes.VERTICAL)
                elif orientation == Orientation.RIGHT:
                    self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY)
                    # self.rotate_left(Axes.VERTICAL)
                else:
                    if iters > 5:
                        raise Exception('Invalid Cube! Exiting Infinite Loop')
                    else:
                        self.move(PossibleOperations.ROTATE_LEFT_HORIZONTALLY)
                        # self.rotate_left(Axes.HORIZONTAL)
                iters += 1
    
    def get_orientation(self):
        if Predicates.FacePredicates.are_faces_equal(self.current_perspective.top, self.blue_face):
            return Orientation.TOP
        elif Predicates.FacePredicates.are_faces_equal(self.current_perspective.right, self.blue_face):
            return Orientation.RIGHT
        elif Predicates.FacePredicates.are_faces_equal(self.current_perspective.left, self.blue_face):
            return Orientation.LEFT
        elif Predicates.FacePredicates.are_faces_equal(self.current_perspective.bottom, self.blue_face):
            return Orientation.BOTTOM
        elif Predicates.FacePredicates.are_faces_equal(self.current_perspective.opposite, self.blue_face):
            return Orientation.BACK
        

class Face:
    
    def __init__(self, colour=None, right=None, left=None, top=None, bottom=None, front=None, back=None, opposite=None, is_side_face=True, is_copy=False, grid=None):
        self.center_colour = colour
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom
        self.front = front
        self.back = back
        self.opposite = opposite
        self.is_side_face = is_side_face
        
        if is_copy:
            self.grid = grid
        else:
            self.grid = self.initialize_center_pieces()
        
    def copy(self):
        return Face(self.center_colour, self.right, self.left, self.top, self.bottom, self.front, self.back, self.opposite, self.is_side_face, is_copy=True, grid=self.grid.copy())
        
    def initialize_center_pieces(self):
        ## Creating center piece
        center_piece = Piece(FacePositions.MID_CENTER, self, PieceType.CENTER)
        colour = center_piece.colour[0]
        
        ## Creating edge pieces
        top_center_piece = EdgePiece(FacePositions.TOP_CENTER, self, PieceType.EDGE)
        mid_left_piece = EdgePiece(FacePositions.MID_LEFT, self, PieceType.EDGE)
        bottom_center_piece = EdgePiece(FacePositions.BOTTOM_CENTER, self, PieceType.EDGE)
        mid_right_piece = EdgePiece(FacePositions.MID_RIGHT, self, PieceType.EDGE)
        
        ## Creating corner pieces
        top_left_piece = CornerPiece(FacePositions.TOP_LEFT, self, PieceType.CORNER)
        top_right_piece = CornerPiece(FacePositions.TOP_RIGHT, self, PieceType.CORNER)
        bottom_left_piece = CornerPiece(FacePositions.BOTTOM_LEFT, self, PieceType.CORNER)
        bottom_right_piece = CornerPiece(FacePositions.BOTTOM_RIGHT, self, PieceType.CORNER)
        
        # if self.is_test:
            
        #     grid = [
        #         [1, 2, 3],
        #         [4, 5, 6],
        #         [7, 8, 9]
        #     ]
        
        # else:
        
        grid = [
            [top_left_piece, top_center_piece, top_right_piece],
            [mid_left_piece, center_piece, mid_right_piece],
            [bottom_left_piece, bottom_center_piece, bottom_right_piece]
        ]
        
        return np.array(grid)


#! DeprecationWarning: Class Row will not be used for this project and will be subsequently removed in future versions.
class Row:
    def __init__(self, left, center, right):
        self.left = left
        self.center = center
        self.right = right
        pass
    pass


#! DeprecationWarning: Class Column will not be used for this project and will be subsequently removed in future versions.
class Column:
    def __init__(self, top, center, bottom):
        self.top = top
        self.center = center
        self.bottom = bottom
        pass
    pass


class Piece:
    
    def __init__(self, face_position, face, piece_type):
        self.face_position = face_position
        self.face = face
        self._colour = self.face.center_colour
        self._piece_type = piece_type
        
    @property
    def colour(self):
        return self._colour
    
    @property
    def piece_type(self):
        return self._piece_type
        

class EdgePiece(Piece):
    
    def __init__(self, face_position, face, piece_type, complement=()):
        super().__init__(face_position, face, piece_type)
        self._complement = complement
        
    @property
    def complement(self):
        return self._complement
    
    @complement.setter
    def complement(self, new_complement):
        self._complement = new_complement
        
        
class CornerPiece(Piece):
    
    def __init__(self, face_position, face, piece_type, complements=()):
        super().__init__(face_position, face, piece_type)
        self._complements = complements
        
    @property
    def complements(self):
        return self._complements
    
    @complements.setter
    def complements(self, new_complements):
        self._complements = new_complements
    
    
if __name__ == "__main__":
    cube1 = Cube()
    # print(Predicates.FacePredicates.is_correct_perspective(cube))
    # cube.print_cube_grid()
    # cube.get_attributes()
    # cube.rotate_down()
    # cube.rotate_left(Axes.HORIZONTAL)
    # Shifts.top_row_left(cube.current_perspective)
    
    # Shifts.top_row_left(cube.current_perspective)
    # Shifts.bottom_row_left(cube.current_perspective)
    # Shifts.bottom_row_left(cube.current_perspective)
    # print(cube.current_perspective.grid[FacePositions.TOP_LEFT])
    # print(cube.current_perspective.grid[FacePositions.TOP_LEFT].complements)
    
    # print(cube.current_perspective.left.grid[FacePositions.TOP_RIGHT])
    # print(cube.current_perspective.left.grid[FacePositions.TOP_RIGHT].complements)
    # # cube.rotate_left(Axes.HORIZONTAL)
    
    # cube.move(Shifts.RIGHT_COL_UP)
    # cube1.move(PossibleOperations.ROTATE_LEFT_VERTICALLY)
    # cube1.print_cube_grid()
    # cube1.move(PossibleOperations.ROTATE_RIGHT_VERTICALLY)
    # decorated_move = cube1.get_kwargs(cube1.move)
    # decorated_move(cube1, PossibleOperations.ROTATE_LEFT_VERTICALLY)
    
    # print(cube.current_perspective.top.grid[FacePositions.BOTTOM_LEFT])
    # print(cube.current_perspective.top.grid[FacePositions.BOTTOM_LEFT].complements)
    # Shifts.top_row_left(cube.current_perspective)
    # Shifts.top_row_left(cube.current_perspective)
    # Shifts.bottom_row_left(cube.current_perspective)
    # Shifts.bottom_row_left(cube.current_perspective)
    # cube2 = Cube()
    # cube2.rotate_left(Axes.VERTICAL)
    
    # cube.rotate_down()
    
    # Shifts.top_row_left(cube.current_perspective)
    # Shifts.top_row_left(cube.current_perspective)
    # Shifts.bottom_row_left(cube.current_perspective)
    # Shifts.bottom_row_left(cube.current_perspective)
    
    # Shifts.right_column_up(cube.current_perspective)
    # Shifts.left_column_up(cube.current_perspective)
    # cube1.move(PossibleOperations.RIGHT_COL_UP)
    cube1.move(PossibleOperations.ROTATE_DOWN)
    cube1.move(PossibleOperations.ROTATE_LEFT_HORIZONTALLY)
    
    print(cube1)
    cube1.move(PossibleOperations.RESET_PERSPECTIVE)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_left(Axes.VERTICAL)
    # cube.rotate_right(Axes.VERTICAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # Shifts.right_column_up(cube.current_perspective)
    # cube1.print_cube_grid()
    print(cube1)
    # cube2.print_cube_grid()
    # Shifts.right_column_down(cube.current_perspective)
    # print('Blue')
    # print(cube.current_perspective.grid)
    # print('Red')
    # print(cube.current_perspective.left.grid)
    # print('Orange')
    # print(cube.current_perspective.right.grid)
    # print('Green')
    # print(cube.current_perspective.opposite.grid)
    # print('White')
    # print(cube.current_perspective.top.grid)
    # print('Yellow')
    # print(cube.current_perspective.bottom.grid)
    # cube.rotate_up()
    # cube.rotate_up()
    # cube.rotate_up()
    # cube.rotate_up()
    # cube.rotate_up()
    # cube.rotate_up()
    # cube.rotate_up()
    # cube.rotate_up()
    # print(Predicates.FacePredicates.is_correct_perspective(cube))
    # print(Predicates.FacePredicates.is_blue_face_front(cube.current_perspective, cube.blue_face))
    # print(Predicates.FacePredicates.is_white_face_top(cube.current_perspective, cube.white_face))
    # print(Predicates.FacePredicates.is_orange_face_right(cube.current_perspective, cube.orange_face))
    # print(Predicates.FacePredicates.is_red_face_left(cube.current_perspective, cube.red_face))
    # print(Predicates.FacePredicates.is_green_face_back(cube.current_perspective, cube.green_face))
    # print(Predicates.FacePredicates.is_yellow_face_bottom(cube.current_perspective, cube.yellow_face))
    # cube.print_cube_grid()
    # cube.get_attributes()
    # cube.reset_perspective()
    # cube.print_cube_grid()
    
