"""
This file holds the code to initiailize a random cube, as well as ensure that the cube can be recreated in real life.
POSSIBLE ADDITIONS: Ability for user to enter a cube configuration to test out the program
"""

import numpy as np
from Constraints import Perspectives, Colours, Axes, PieceType, PossibleCornerPieces, FacePositions, Orientation
from Transformations import GridTransformations, FaceTransformations
import Predicates

class Cube(Perspectives):
    
    NUM_FACES = 6
    # $ Face Order: Front, Right, Back, Left, Top, Bottom
    # $ Colour Order: Blue, Orange, Green, Red, White, Yellow
    COLOURS = [Colours.BLUE, Colours.ORANGE, Colours.GREEN, Colours.RED, Colours.WHITE, Colours.YELLOW]
    #//COLOURS = dir(Colours)
    
    def __init__(self, current=None, initial=None, blue=None, white=None, yellow=None, red=None, orange=None, green=None, is_copy=False):
        self.current_perspective = current
        self.initial_perspective = initial
        
        self.blue_face = blue
        self.white_face = white
        self.yellow_face = yellow
        self.red_face = red
        self.orange_face = orange
        self.green_face = green
        
        if not is_copy:
            self.initialize_random_cube()
            
    
    def copy(self):
        return Cube(self.current_perspective, self.initial_perspective, self.blue_face, self.white_face, self.yellow_face, \
                    self.red_face, self.orange_face, self.green_face, is_copy=True)
    
    
    def initialize_random_cube(self):
        
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
        
        ##Joining the bottom face
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
        
        print('\n')
        print(self.blue_face)
        print(self.white_face)
        print(self.green_face)
        print(self.orange_face)
        print(self.yellow_face)
        print(self.red_face)
        print('\n')
        
        self.assign_piece_colours()
        
        
    def assign_piece_colours(self):
        # Assigning edge pieces for Blue face
        #// current = self.current_perspective
        
        #// current.grid[FacePositions.TOP_CENTER] = EdgePiece(FacePositions.TOP_CENTER, self)
        #// current.grid[FacePositions.MID_LEFT] = EdgePiece(FacePositions.MID_LEFT, self)
        #// current.grid[FacePositions.BOTTOM_CENTER] = EdgePiece(FacePositions.BOTTOM_CENTER, self)
        #// current.grid[FacePositions.MID_RIGHT] = EdgePiece(FacePositions.MID_RIGHT, self)
        
        pass
    
    def assign_side_face_edges(self):
        pass
        
        
    def rotate_left(self, axis):
        current = self.current_perspective
        
        if axis == Axes.VERTICAL:
            print('ROTATING LEFT VERTICALLY')
            ## Getting transformed Top & Bottom Faces
            new_top_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=True, is_left=True)
            new_bottom_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=False, is_left=True)
            
            ## Getting transformed Top & Bottom Grids
            new_top_grid = GridTransformations.LeftAndRight.transform_top_face(current, axis, is_left=True)
            new_bottom_grid = GridTransformations.LeftAndRight.transform_bottom_face(current, axis, is_left=True)
            
            ## Updating grid for each transformed face
            new_top_face.grid = new_top_grid
            new_bottom_face.grid = new_bottom_grid
            
            ## Changing perspective to right face
            self.current_perspective = self.current_perspective.right
            
            ## Transferring transformed attribute values to original object
            self.transfer_faces(self.current_perspective.top, new_top_face)
            self.transfer_faces(self.current_perspective.bottom, new_bottom_face)
        else:
            print('ROTATING LEFT HORIZONTALLY')
            ## Getting transformed Left & Right Faces
            new_right_face = FaceTransformations.LeftAndRight.transform_right_face(current, is_left=True)
            new_left_face = FaceTransformations.LeftAndRight.transform_left_face(current, is_left=True)
            
            ## Getting transformed Left & Right Grids
            new_right_grid = GridTransformations.LeftAndRight.transform_right_face(current, axis, is_left=True)
            new_left_grid = GridTransformations.LeftAndRight.transform_left_face(current, axis, is_left=True)
            
            ## Getting transformed Front & Back Faces
            new_front_face = FaceTransformations.LeftAndRight.transform_front_back_faces(current, is_front=True, is_left=True)
            new_back_face = FaceTransformations.LeftAndRight.transform_front_back_faces(current, is_front=False, is_left=True)
            
            ## Getting transformed Front & Back Grids
            new_front_grid = GridTransformations.LeftAndRight.transform_front_face(current, axis, is_left=True)
            new_back_grid = GridTransformations.LeftAndRight.transform_back_face(current, axis, is_left=True)
            
            ## Getting transformed Top & Bottom Faces
            new_top_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=True, is_left=True)
            new_bottom_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=False, is_left=True)
            
            ## Getting transformed Top & Bottom Faces
            new_top_grid = GridTransformations.LeftAndRight.transform_top_face(current, axis, is_left=True)
            new_bottom_grid = GridTransformations.LeftAndRight.transform_bottom_face(current, axis, is_left=True)
            
            ## Updating grid for each transformed face
            new_left_face.grid = new_left_grid
            new_right_face.grid = new_right_grid
            new_front_face.grid = new_front_grid
            new_back_face.grid = new_back_grid
            new_top_face.grid = new_top_grid
            new_bottom_face.grid = new_bottom_grid
            
            ## Transferring transformed attribute values to original object
            self.transfer_faces(self.current_perspective, new_front_face)
            self.transfer_faces(self.current_perspective.left, new_top_face)
            self.transfer_faces(self.current_perspective.right, new_bottom_face)
            self.transfer_faces(self.current_perspective.top, new_right_face)
            self.transfer_faces(self.current_perspective.bottom, new_left_face)
            self.transfer_faces(self.current_perspective.opposite, new_back_face)
            
    def rotate_right(self, axis):
        current = self.current_perspective
        
        if axis == Axes.VERTICAL:
            print('ROTATING RIGHT VERTICALLY')
            ## Getting transformed Top & Bottom Faces
            new_top_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=True, is_left=False)
            new_bottom_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=False, is_left=False)
            
            ## Getting transformed Top & Bottom Grids
            new_top_grid = GridTransformations.LeftAndRight.transform_top_face(current, axis, is_left=False)
            new_bottom_grid = GridTransformations.LeftAndRight.transform_bottom_face(current, axis, is_left=False)
            
            ## Updating grid for each transformed face
            new_top_face.grid = new_top_grid
            new_bottom_face.grid = new_bottom_grid
            
            ## Changing perspective to left face
            self.current_perspective = self.current_perspective.left
            
            ## Transferring transformed attribute values to original object
            self.transfer_faces(self.current_perspective.top, new_top_face)
            self.transfer_faces(self.current_perspective.bottom, new_bottom_face)
        else:
            print('ROTATING RIGHT HORIZONTALLY')
            ## Getting transformed Left & Right Faces
            new_right_face = FaceTransformations.LeftAndRight.transform_right_face(current, is_left=False)
            new_left_face = FaceTransformations.LeftAndRight.transform_left_face(current, is_left=False)
            
            ## Getting transformed Left & Right Grids
            new_right_grid = GridTransformations.LeftAndRight.transform_right_face(current, axis, is_left=False)
            new_left_grid = GridTransformations.LeftAndRight.transform_left_face(current, axis, is_left=False)
            
            ## Getting transformed Front & Back Faces
            new_front_face = FaceTransformations.LeftAndRight.transform_front_back_faces(current, is_front=True, is_left=False)
            new_back_face = FaceTransformations.LeftAndRight.transform_front_back_faces(current, is_front=False, is_left=False)
            
            ## Getting transformed Front & Back Grids
            new_front_grid = GridTransformations.LeftAndRight.transform_front_face(current, axis, is_left=False)
            new_back_grid = GridTransformations.LeftAndRight.transform_back_face(current, axis, is_left=False)
            
            ## Getting transformed Top & Bottom Faces
            new_top_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=True, is_left=False)
            new_bottom_face = FaceTransformations.LeftAndRight.transform_top_bottom_faces(current, axis, is_top=False, is_left=False)
            
            ## Getting transformed Top & Bottom Grids
            new_top_grid = GridTransformations.LeftAndRight.transform_top_face(current, axis, is_left=False)
            new_bottom_grid = GridTransformations.LeftAndRight.transform_bottom_face(current, axis, is_left=False)
            
            ## Updating grid for each transformed face
            new_left_face.grid = new_left_grid
            new_right_face.grid = new_right_grid
            new_front_face.grid = new_front_grid
            new_back_face.grid = new_back_grid
            new_top_face.grid = new_top_grid
            new_bottom_face.grid = new_bottom_grid
            
            ## Transferring transformed attribute values to original object
            self.transfer_faces(self.current_perspective, new_front_face)
            self.transfer_faces(self.current_perspective.left, new_bottom_face)
            self.transfer_faces(self.current_perspective.right, new_top_face)
            self.transfer_faces(self.current_perspective.top, new_left_face)
            self.transfer_faces(self.current_perspective.bottom, new_right_face)
            self.transfer_faces(self.current_perspective.opposite, new_back_face)
        
    def rotate_up(self):
        print('ROTATING UP')
        current = self.current_perspective
        
        ## Getting transformed Left & Right Faces
        new_left_face = FaceTransformations.UpAndDown.transform_left_face(current, is_rotate_down=False)
        new_right_face = FaceTransformations.UpAndDown.transform_right_face(current, is_rotate_down=False)
        
        ## Getting transformed Left & Right Grids
        new_left_grid = GridTransformations.UpAndDown.transform_left_face(current, is_rotate_down=False)
        new_right_grid = GridTransformations.UpAndDown.transform_right_face(current, is_rotate_down=False)
        
        ## Getting transformed Front & Back Faces
        new_front_face = FaceTransformations.UpAndDown.transform_front_back_faces(current, is_rotate_down=False)
        new_back_face = FaceTransformations.UpAndDown.transform_front_back_faces(current, is_front=False, is_rotate_down=False)
        
        ## Getting transformed Back Grid
        new_back_grid = GridTransformations.UpAndDown.transform_back_face(current, is_rotate_down=False)
        
        ## Getting transformed Top & Bottom Faces
        new_top_face = FaceTransformations.UpAndDown.transform_top_bottom_faces(current, is_rotate_down=False)
        new_bottom_face = FaceTransformations.UpAndDown.transform_top_bottom_faces(current, is_top=False, is_rotate_down=False)
        
        ## Getting transformed Top Grid
        new_bottom_grid = GridTransformations.UpAndDown.transform_bottom_face(current, is_rotate_down=False)
        new_top_grid = GridTransformations.UpAndDown.transform_top_face(current, is_rotate_down=False)
        
        ## Updating grid for each transformed face
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid
        new_back_face.grid = new_back_grid
        
        ## Changing perspective to top face
        self.current_perspective = self.current_perspective.bottom
        
        ## Transferring transformed attribute values to original object
        self.transfer_faces(self.current_perspective, new_bottom_face)
        self.transfer_faces(self.current_perspective.right, new_right_face)
        self.transfer_faces(self.current_perspective.left, new_left_face)
        self.transfer_faces(self.current_perspective.top, new_front_face)
        self.transfer_faces(self.current_perspective.bottom, new_back_face)
        self.transfer_faces(self.current_perspective.opposite, new_top_face)
        
    def rotate_down(self):
        
        print('ROTATING DOWN')
        current = self.current_perspective
        
        ## Getting transformed Left & Right Faces
        new_left_face = FaceTransformations.UpAndDown.transform_left_face(current, is_rotate_down=True)
        new_right_face = FaceTransformations.UpAndDown.transform_right_face(current, is_rotate_down=True)
        
        ## Getting transformed Left & Right Grids
        new_left_grid = GridTransformations.UpAndDown.transform_left_face(current, is_rotate_down=True)
        new_right_grid = GridTransformations.UpAndDown.transform_right_face(current, is_rotate_down=True)
        
        ## Getting transformed Front & Back Faces
        new_front_face = FaceTransformations.UpAndDown.transform_front_back_faces(current, is_rotate_down=True)
        new_back_face = FaceTransformations.UpAndDown.transform_front_back_faces(current, is_front=False, is_rotate_down=True)
        
        ## Getting transformed Back Grid
        new_back_grid = GridTransformations.UpAndDown.transform_back_face(current, is_rotate_down=False)
        
        ## Getting transformed Top & Bottom Faces
        new_top_face = FaceTransformations.UpAndDown.transform_top_bottom_faces(current, is_rotate_down=True)
        new_bottom_face = FaceTransformations.UpAndDown.transform_top_bottom_faces(current, is_top=False, is_rotate_down=True)
        
        ## Getting transformed Top Grid
        new_top_grid = GridTransformations.UpAndDown.transform_top_face(current, is_rotate_down=True)
        new_bottom_grid = GridTransformations.UpAndDown.transform_bottom_face(current, is_rotate_down=True)
        
        ## Updating grid for each transformed face
        new_left_face.grid = new_left_grid
        new_right_face.grid = new_right_grid
        new_top_face.grid = new_top_grid
        new_bottom_face.grid = new_bottom_grid
        new_back_face.grid = new_back_grid
        
        ## Changing perspective to top face
        self.current_perspective = self.current_perspective.top
        
        ## Transferring transformed attribute values to original object
        self.transfer_faces(self.current_perspective, new_top_face)
        self.transfer_faces(self.current_perspective.right, new_right_face)
        self.transfer_faces(self.current_perspective.left, new_left_face)
        self.transfer_faces(self.current_perspective.top, new_back_face)
        self.transfer_faces(self.current_perspective.bottom, new_front_face)
        self.transfer_faces(self.current_perspective.opposite, new_bottom_face)
        
    def invert_cube(self, axis=Axes.VERTICAL):
        current = self.current_perspective
        
        if axis == Axes.VERTICAL:
            print('INVERTING CUBE VERTICALLY')
            
            ## Getting transformed Top & Bottom Faces
            new_top_face = FaceTransformations.Inversion.transform_top_bottom_faces(current, axis, is_top=True)
            new_bottom_face = FaceTransformations.Inversion.transform_top_bottom_faces(current, axis, is_top=False)
            
            ## Getting transformed Top & Bottom Grids
            new_top_grid = GridTransformations.Inversion.transform_top_face(current, axis)
            new_bottom_grid = GridTransformations.Inversion.transform_bottom_face(current, axis)
            
            ## Updating grid for each transformed face
            new_top_face.grid = new_top_grid
            new_bottom_face.grid = new_bottom_grid
            
            ## Changing perspective to opposite face
            self.current_perspective = self.current_perspective.opposite
            
            ## Transferring transformed attribute values to original object
            self.transfer_faces(self.current_perspective.top, new_top_face)
            self.transfer_faces(self.current_perspective.bottom, new_bottom_face)
            
        else:
            print('INVERTING CUBE HORIZONTALLY')
            
            ## Getting transformed Top & Bottom Faces
            new_top_face = FaceTransformations.Inversion.transform_top_bottom_faces(current, axis, is_top=True)
            new_bottom_face = FaceTransformations.Inversion.transform_top_bottom_faces(current, axis, is_top=False)
            
            ## Getting transformed Top & Bottom Grids
            new_top_grid = GridTransformations.Inversion.transform_top_face(current, axis)
            new_bottom_grid = GridTransformations.Inversion.transform_bottom_face(current, axis)
            
            ## Getting transformed Front & Back Faces
            new_front_face = FaceTransformations.Inversion.transform_front_back_faces(current, is_front=True)
            new_back_face = FaceTransformations.Inversion.transform_front_back_faces(current, is_front=False)
            
            ## Getting transformed Front & Back Grids
            new_front_grid = GridTransformations.Inversion.transform_front_face(current, axis)
            new_back_grid = GridTransformations.Inversion.transform_back_face(current, axis)
            
            ## Getting transformed Left & Right Faces
            new_left_face = FaceTransformations.Inversion.transform_right_left_faces(current, is_left_face=True)
            new_right_face = FaceTransformations.Inversion.transform_right_left_faces(current, is_left_face=False)
            
            ## Getting transformed Left & Right Grids
            new_left_grid = GridTransformations.Inversion.transform_left_face(current, axis)
            new_right_grid = GridTransformations.Inversion.transform_right_face(current, axis)
            
            ## Updating grid for each transformed face
            new_left_face.grid = new_left_grid
            new_right_face.grid = new_right_grid
            new_top_face.grid = new_top_grid
            new_bottom_face.grid = new_bottom_grid
            new_back_face.grid = new_back_grid
            new_front_face.grid = new_front_grid
            
            ## Changing perspective to opposite face
            self.current_perspective = self.current_perspective.opposite
            
            ## Transferring transformed attribute values to original object
            self.transfer_faces(self.current_perspective, new_back_face)
            self.transfer_faces(self.current_perspective.right, new_right_face)
            self.transfer_faces(self.current_perspective.left, new_left_face)
            self.transfer_faces(self.current_perspective.top, new_bottom_face)
            self.transfer_faces(self.current_perspective.bottom, new_top_face)
            self.transfer_faces(self.current_perspective.opposite, new_front_face)
        
    def transfer_faces(self, old, new):
        """
        *This method transplants values from the copied face object to the original face object of the cube.
        
        @params: old (Face): Original face object from the Cube class
        @      : new (Face): Copied face object with updated attributes (after transformation)
        
        @modified: Face.*: All attributes from the Face class
        @returns: None
        """
        old.left = new.left
        old.right = new.right
        old.top = new.top
        old.bottom = new.bottom
        old.front = new.front
        old.back = new.back
        old.is_side_face = new.is_side_face
        old.grid = new.grid
    
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
        print(face.center_colour)
        if orientation == Orientation.LEFT:
            first_row = f'{face.grid[FacePositions.TOP_RIGHT]} {face.grid[FacePositions.TOP_CENTER]} {face.grid[FacePositions.TOP_LEFT]}'
            second_row = f'{face.grid[FacePositions.MID_RIGHT]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.MID_LEFT]}'
            third_row = f'{face.grid[FacePositions.BOTTOM_RIGHT]} {face.grid[FacePositions.BOTTOM_CENTER]} {face.grid[FacePositions.BOTTOM_LEFT]}'
            
        elif orientation in [Orientation.FRONT, Orientation.BOTTOM, Orientation.TOP]:
            first_row = f'{face.grid[FacePositions.TOP_LEFT]} {face.grid[FacePositions.MID_LEFT]} {face.grid[FacePositions.BOTTOM_LEFT]}'
            second_row = f'{face.grid[FacePositions.TOP_CENTER]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.BOTTOM_CENTER]}'
            third_row = f'{face.grid[FacePositions.TOP_RIGHT]} {face.grid[FacePositions.MID_RIGHT]} {face.grid[FacePositions.BOTTOM_RIGHT]}'
            
        elif orientation == Orientation.BACK:
            first_row = f'{face.grid[FacePositions.BOTTOM_RIGHT]} {face.grid[FacePositions.MID_RIGHT]} {face.grid[FacePositions.TOP_RIGHT]}'
            second_row = f'{face.grid[FacePositions.BOTTOM_CENTER]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.TOP_CENTER]}'
            third_row = f'{face.grid[FacePositions.BOTTOM_LEFT]} {face.grid[FacePositions.MID_LEFT]} {face.grid[FacePositions.TOP_LEFT]}'
            
        elif orientation == Orientation.RIGHT:
            first_row = f'{face.grid[FacePositions.BOTTOM_LEFT]} {face.grid[FacePositions.BOTTOM_CENTER]} {face.grid[FacePositions.BOTTOM_RIGHT]}'
            second_row = f'{face.grid[FacePositions.MID_LEFT]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.MID_RIGHT]}'
            third_row = f'{face.grid[FacePositions.TOP_LEFT]} {face.grid[FacePositions.TOP_CENTER]} {face.grid[FacePositions.TOP_RIGHT]}'
        
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
        #TODO: Redo complete function
        ## As long as cube isn't in the currect perspective
        iters = 0
        while True:
            blue_face_orientation = self.get_orientation()
            if Predicates.FacePredicates.is_correct_perspective(self):
                break
            else:
                orientation = self.get_orientation()
                print(orientation)
                if orientation == Orientation.TOP:
                    self.rotate_down()
                elif orientation == Orientation.BOTTOM:
                    self.rotate_up()
                elif orientation == Orientation.BACK:
                    if Predicates.FacePredicates.is_white_face_top(self.current_perspective, self.white_face):
                        self.invert_cube(Axes.VERTICAL)
                    else:
                        self.invert_cube(Axes.HORIZONTAL)
                elif orientation == Orientation.LEFT:
                    self.rotate_right(Axes.VERTICAL)
                elif orientation == Orientation.RIGHT:
                    self.rotate_left(Axes.VERTICAL)
                else:
                    if iters > 5:
                        raise Exception('Invalid Cube! Exiting Infinite Loop')
                    else:
                        self.rotate_left(Axes.HORIZONTAL)
                iters += 1
            
            pass
        pass
    
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
    
    
    
    
    #     while True:
    #         # print(self.is_correct_perspective())
    #         print(f'\n{self.is_correct_perspective()}')
    #         print(self.is_right_face())
    #         print(self.is_left_face())
    #         print(self.is_top_face())
    #         print(self.is_bottom_face())
    #         print(f'{self.is_front_back_faces_inverted()}\n')
            
    #         #? Does is_correct_perspective() return the right logic?
    #         if self.is_correct_perspective():
    #             break
    #         elif self.is_front_back_faces_inverted():
    #             self.invert_cube()
    #         elif self.is_right_face():
    #             self.rotate_left(Axes.VERTICAL)
    #         elif self.is_left_face():
    #             self.rotate_right(Axes.VERTICAL)
    #         elif self.is_top_face():
    #             self.rotate_down()
    #         elif self.is_bottom_face():
    #             self.rotate_up()
    #         else:
    #             self.rotate_left(Axes.HORIZONTAL)

    
    # def is_correct_perspective(self):
    #     return (self.current_perspective.center_colour == Colours.BLUE and \
    #         self.current_perspective.top.center_colour == Colours.WHITE and \
    #             self.current_perspective.left.center_colour == Colours.RED)
        
    # def is_front_back_faces_inverted(self):
    #     return self.current_perspective.opposite.center_colour == Colours.BLUE
    
    # def is_right_face(self):
    #     return self.current_perspective.right.center_colour == Colours.BLUE
    
    # def is_left_face(self):
    #     return self.current_perspective.left.center_colour == Colours.BLUE
    
    # def is_top_face(self):
    #     return self.current_perspective.top.center_colour == Colours.BLUE
    
    # def is_bottom_face(self):
    #     return self.current_perspective.bottom.center_colour == Colours.BLUE

    

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
        
    
    def set_right_face(self, face):
        self.right = face
        
    def set_left_face(self, face):
        self.left = face
        
    def set_top_face(self, face):
        self.top = face
        
    def set_bottom_face(self, face):
        self.bottom = face
        
    def copy(self):
        return Face(self.center_colour, self.right, self.left, self.top, self.bottom, self.front, self.back, self.opposite, self.is_side_face, is_copy=True, grid=self.grid.copy())
        
    def initialize_center_pieces(self):
        
        center_piece = Piece(FacePositions.MID_CENTER, self, PieceType.CENTER)
        
        grid = [
            [1, 2, 3],
            [4, center_piece, 6],
            [7, 8, 9]
        ]
        
        return np.array(grid)


class Row:
    def __init__(self, left, center, right):
        self.left = left
        self.center = center
        self.right = right
        pass
    pass


class Column:
    def __init__(self, top, center, bottom):
        self.top = top
        self.center = center
        self.bottom = bottom
        pass
    pass


class Piece:
    def __init__(self, face_position, face:Face, piece_type:PieceType, complements=()):
        self.face_position = face_position
        self.face = face
        self.colour = self.face.center_colour
        self.piece_type = piece_type
        self.complements = complements
    pass

if __name__ == "__main__":
    cube = Cube()
    cube.print_cube_grid()
    cube.rotate_down()
    cube.rotate_left(Axes.HORIZONTAL)
    # cube.rotate_right(Axes.HORIZONTAL)
    # cube.rotate_left(Axes.VERTICAL)
    # cube.rotate_right(Axes.VERTICAL)
    # cube.rotate_up()
    cube.print_cube_grid()
    cube.reset_perspective()
    cube.print_cube_grid()
    
