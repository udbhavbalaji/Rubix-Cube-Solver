from __future__ import annotations
from typing import TYPE_CHECKING
import random
import math
import Predicates
from Transformations import FaceTransformations, GridTransformations
from Constraints import Axes, FacePositions, Orientation, PossibleOperations

if TYPE_CHECKING:
    from cube_init import RubixCube, Face, Piece, CornerPiece, EdgePiece


def shuffle_cube(cube: RubixCube = None, axis: str = None, current_front: Face = None) -> tuple(list, list):
    op_stack = []
    error_stack = []
    num_operations = round(math.pow(random.randint(10, 100), (random.random()*2)))
    print(num_operations)
    rotations = PossibleOperations.MOVES[:8]
    shifts = PossibleOperations.MOVES[8:16]
    for i in range(num_operations):
        if i%10 == 0:
            random_index = random.randrange(0, len(rotations))
            operation = rotations[random_index]
        else:
            random_index = random.randrange(0, len(shifts))
            operation = shifts[random_index]
            
        print(operation)

        op, op_kwargs = cube.kwargs_dict[operation]
        # print(op, op_kwargs)
        try:
            op(**op_kwargs)
            op_stack.append(operation)
        except(AttributeError):
            # error_stack.append(operation)
            cube.get_attributes()
            raise Exception
        # op(**op_kwargs)
        # op_stack.append(operation)
    
    return op_stack, error_stack


class Shifts:
    
    # Defining the methods for each operation
    def right_column_up(cube: RubixCube = None, axis: str = None) -> None:
        current = cube.current_perspective
        
        ## Getting new Right Face Grid
        new_right_grid = GridTransformations.ColumnUpAndDown.transform_right_face(current, is_rotate_down=False)
        
        ## Getting new Front & Back Grids
        new_front_grid = GridTransformations.ColumnUpAndDown.transform_front_face(current, is_rotate_down=False, is_right_col=True)
        new_back_grid = GridTransformations.ColumnUpAndDown.transform_back_face(current, is_rotate_down=False, is_right_col=True)
        
        ## Getting new Top & Bottom Grids
        new_top_grid = GridTransformations.ColumnUpAndDown.transform_top_face(current, is_rotate_down=False, is_right_col=True)
        new_bottom_grid = GridTransformations.ColumnUpAndDown.transform_bottom_face(current, is_rotate_down=False, is_right_col=True)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid
    
    def left_column_up(cube: RubixCube = None, axis: str = None) -> None:
        current = cube.current_perspective
        
        ## Getting new Left Face Grid
        new_left_grid = GridTransformations.ColumnUpAndDown.transform_left_face(current, is_rotate_down=False)
        
        ## Getting new Front & Back Grids
        new_front_grid = GridTransformations.ColumnUpAndDown.transform_front_face(current, is_rotate_down=False, is_right_col=False)
        new_back_grid = GridTransformations.ColumnUpAndDown.transform_back_face(current, is_rotate_down=False, is_right_col=False)
        
        ## Getting new Top & Bottom Grids
        new_top_grid = GridTransformations.ColumnUpAndDown.transform_top_face(current, is_rotate_down=False, is_right_col=False)
        new_bottom_grid = GridTransformations.ColumnUpAndDown.transform_bottom_face(current, is_rotate_down=False, is_right_col=False)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid
    
    def right_column_down(cube: RubixCube = None, axis: str = None) -> None:
        current = cube.current_perspective
        
        ## Getting new Right Face Grid
        new_right_grid = GridTransformations.ColumnUpAndDown.transform_right_face(current, is_rotate_down=True)
        
        ## Getting new Front & Back Grids
        new_front_grid = GridTransformations.ColumnUpAndDown.transform_front_face(current, is_rotate_down=True, is_right_col=True)
        new_back_grid = GridTransformations.ColumnUpAndDown.transform_back_face(current, is_rotate_down=True, is_right_col=True)
        
        ## Getting new Top & Bottom Grids
        new_top_grid = GridTransformations.ColumnUpAndDown.transform_top_face(current, is_rotate_down=True, is_right_col=True)
        new_bottom_grid = GridTransformations.ColumnUpAndDown.transform_bottom_face(current, is_rotate_down=True, is_right_col=True)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid
    
    def left_column_down(cube: RubixCube = None, axis: str = None) -> None:
        
        #! Error flow: left_column_down -> ColumnUpAndDown.transform_front_face (Type: AttributeError - NoneType object has no attribute copy)
        
        current = cube.current_perspective
        
        ## Getting transformed Left Face Grid
        new_left_grid = GridTransformations.ColumnUpAndDown.transform_left_face(current, is_rotate_down=True)
        
        ## Getting transformed Front & Back Grids
        new_front_grid = GridTransformations.ColumnUpAndDown.transform_front_face(current, is_rotate_down=True, is_right_col=False)
        new_back_grid = GridTransformations.ColumnUpAndDown.transform_back_face(current, is_rotate_down=True, is_right_col=False)
        
        ## Getting transformed Top & Bottom Grids
        new_top_grid = GridTransformations.ColumnUpAndDown.transform_top_face(current, is_rotate_down=True, is_right_col=False)
        new_bottom_grid = GridTransformations.ColumnUpAndDown.transform_bottom_face(current, is_rotate_down=True, is_right_col=False)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid
    
    def top_row_right(cube: RubixCube = None, axis: str = None) -> None:
        current = cube.current_perspective
        
        ## Getting transformed Top Grids
        new_top_grid = GridTransformations.RowRightAndLeft.transform_top_face(current, is_rotate_left=False)
        
        ## Getting transformed Left & Right Grids
        new_left_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.LEFT, is_rotate_left=False, is_top_row=True)
        new_right_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.RIGHT, is_rotate_left=False, is_top_row=True)
        
        ## Getting transformed Front & Back Grids
        new_front_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.FRONT, is_rotate_left=False, is_top_row=True)
        new_back_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.BACK, is_rotate_left=False, is_top_row=True)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid

    def top_row_left(cube: RubixCube = None, axis: str = None) -> None:
        current = cube.current_perspective
        
        ## Getting transformed Top Grids
        new_top_grid = GridTransformations.RowRightAndLeft.transform_top_face(current, is_rotate_left=True)
        
        ## Getting transformed Left & Right Grids
        new_left_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.LEFT, is_rotate_left=True, is_top_row=True)
        new_right_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.RIGHT, is_rotate_left=True, is_top_row=True)
        
        ## Getting transformed Front & Back Grids
        new_front_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.FRONT, is_rotate_left=True, is_top_row=True)
        new_back_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.BACK, is_rotate_left=True, is_top_row=True)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
    
    def bottom_row_right(cube: RubixCube = None, axis: str = None) -> None:
        current = cube.current_perspective
        
        ## Getting transformed Top Grids
        new_bottom_grid = GridTransformations.RowRightAndLeft.transform_bottom_face(current, is_rotate_left=False)
        
        ## Getting transformed Left & Right Grids
        new_left_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.LEFT, is_rotate_left=False, is_top_row=False)
        new_right_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.RIGHT, is_rotate_left=False, is_top_row=False)
        
        ## Getting transformed Front & Back Grids
        new_front_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.FRONT, is_rotate_left=False, is_top_row=False)
        new_back_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.BACK, is_rotate_left=False, is_top_row=False)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.bottom.grid = new_bottom_grid
    
    def bottom_row_left(cube: RubixCube = None, axis: str = None) -> None:
        current = cube.current_perspective
        
        ## Getting transformed Top Grids
        new_bottom_grid = GridTransformations.RowRightAndLeft.transform_bottom_face(current, is_rotate_left=True)
        
        ## Getting transformed Left & Right Grids
        new_left_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.LEFT, is_rotate_left=True, is_top_row=False)
        new_right_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.RIGHT, is_rotate_left=True, is_top_row=False)
        
        ## Getting transformed Front & Back Grids
        new_front_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.FRONT, is_rotate_left=True, is_top_row=False)
        new_back_grid = GridTransformations.RowRightAndLeft.transform_front_back_left_right_faces(current, Orientation.BACK, is_rotate_left=True, is_top_row=False)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.right.grid = new_right_grid
        current.opposite.grid = new_back_grid
        current.bottom.grid = new_bottom_grid
    
    
    RIGHT_COL_UP = right_column_up
    LEFT_COL_UP = left_column_up
    RIGHT_COL_DOWN = right_column_down
    LEFT_COL_DOWN = left_column_down
    
    TOP_ROW_LEFT = top_row_left
    TOP_ROW_RIGHT = top_row_right
    BOTTOM_ROW_LEFT = bottom_row_left
    BOTTOM_ROW_RIGHT = bottom_row_right
    

class Rotations:
    
    def rotate_left(cube: RubixCube = None, axis: str = None) -> None:
        """
        * This method performs the operation of rotating the cube leftwards. It makes calls to get the 
        * transformed faces of the cube. These values are then transferred into the existing Face object.
        
        @params: axis (ENUM) - The enum is defined in Constraints.Axes . Tells the program along which axis to rotate.
        @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
        @returns: None
        """
        try:
            current = cube.current_perspective
        except:
            raise ValueError('Cube is of NoneType!')
        
        if axis == Axes.VERTICAL:
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
            cube.current_perspective = cube.current_perspective.right
            
            ## Transferring transformed attribute values to original object
            Rotations.transfer_faces(cube.current_perspective.top, new_top_face)
            Rotations.transfer_faces(cube.current_perspective.bottom, new_bottom_face)
        else:
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
            Rotations.transfer_faces(cube.current_perspective, new_front_face)
            Rotations.transfer_faces(cube.current_perspective.left, new_top_face)
            Rotations.transfer_faces(cube.current_perspective.right, new_bottom_face)
            Rotations.transfer_faces(cube.current_perspective.top, new_right_face)
            Rotations.transfer_faces(cube.current_perspective.bottom, new_left_face)
            Rotations.transfer_faces(cube.current_perspective.opposite, new_back_face)
            
    def rotate_right(cube: RubixCube = None, axis: str = None) -> None:
        """
        * This method performs the operation of rotating the cube rightwards. It makes calls to get the 
        * transformed faces of the cube. These values are then transferred into the existing Face object.
        
        @params: axis (ENUM) - The enum is defined in Constraints.Axes . Tells the program along which axis to rotate.
        @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
        @returns: None
        """
        current = cube.current_perspective
        
        if axis == Axes.VERTICAL:
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
            cube.current_perspective = cube.current_perspective.left
            
            ## Transferring transformed attribute values to original object
            Rotations.transfer_faces(cube.current_perspective.top, new_top_face)
            Rotations.transfer_faces(cube.current_perspective.bottom, new_bottom_face)
        else:
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
            Rotations.transfer_faces(cube.current_perspective, new_front_face)
            Rotations.transfer_faces(cube.current_perspective.left, new_bottom_face)
            Rotations.transfer_faces(cube.current_perspective.right, new_top_face)
            Rotations.transfer_faces(cube.current_perspective.top, new_left_face)
            Rotations.transfer_faces(cube.current_perspective.bottom, new_right_face)
            Rotations.transfer_faces(cube.current_perspective.opposite, new_back_face)
            
    def rotate_up(cube: RubixCube = None, axis: str = None) -> None:
        """
        * This method performs the operation of rotating the cube upwards. It makes calls to get the 
        * transformed faces of the cube. These values are then transferred into the existing Face object.
        
        @params: None
        @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
        @returns: None
        """
        current = cube.current_perspective
        
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
        cube.current_perspective = cube.current_perspective.bottom
        
        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective, new_bottom_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.top, new_front_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_back_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_top_face)
    
    def rotate_down(cube: RubixCube = None, axis: str = None) -> None:
        """
        * This method performs the operation of rotating the cube downwards. It makes calls to get the 
        * transformed faces of the cube. These values are then transferred into the existing Face object.
        
        @params: None
        @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
        @returns: None
        """
        current = cube.current_perspective
        
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
        new_back_grid = GridTransformations.UpAndDown.transform_back_face(current, is_rotate_down=True)
        
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
        cube.current_perspective = cube.current_perspective.top
        
        ## Transferring transformed attribute values to original object
        Rotations.transfer_faces(cube.current_perspective, new_top_face)
        Rotations.transfer_faces(cube.current_perspective.right, new_right_face)
        Rotations.transfer_faces(cube.current_perspective.left, new_left_face)
        Rotations.transfer_faces(cube.current_perspective.top, new_back_face)
        Rotations.transfer_faces(cube.current_perspective.bottom, new_front_face)
        Rotations.transfer_faces(cube.current_perspective.opposite, new_bottom_face)
    
    def invert_cube(cube: RubixCube = None, axis: str = None) -> None:
        """
        * This method performs the operation of inverting the cube. It makes calls to get the 
        * transformed faces of the cube. These values are then transferred into the existing Face object.
        
        @params: axis (ENUM) - The enum is defined in Constraints.Axes . Tells the program along which axis to invert.
        @modifies: Face().__getattrs__.* - All attribute values for each of the faces in the Cube object.
        @returns: None
        """
        current = cube.current_perspective
        
        if axis == Axes.VERTICAL:
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
            cube.current_perspective = cube.current_perspective.opposite
            
            ## Transferring transformed attribute values to original object
            Rotations.transfer_faces(cube.current_perspective.top, new_top_face)
            Rotations.transfer_faces(cube.current_perspective.bottom, new_bottom_face)
            
        else:
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
            cube.current_perspective = cube.current_perspective.opposite
            
            ## Transferring transformed attribute values to original object
            Rotations.transfer_faces(cube.current_perspective, new_back_face)
            Rotations.transfer_faces(cube.current_perspective.right, new_right_face)
            Rotations.transfer_faces(cube.current_perspective.left, new_left_face)
            Rotations.transfer_faces(cube.current_perspective.top, new_bottom_face)
            Rotations.transfer_faces(cube.current_perspective.bottom, new_top_face)
            Rotations.transfer_faces(cube.current_perspective.opposite, new_front_face)
            
    def reset_perspective(cube: RubixCube = None, axis: str = None) -> None:
        iters = 0
        while True:
            if Predicates.FacePredicates.is_correct_perspective(cube):
                break
            else:
                orientation = Rotations.get_orientation(cube)
                if orientation == Orientation.TOP:
                    cube.move(PossibleOperations.ROTATE_DOWN)
                elif orientation == Orientation.BOTTOM:
                    cube.move(PossibleOperations.ROTATE_UP)
                elif orientation == Orientation.BACK:
                    if Predicates.FacePredicates.is_white_face_top(cube.current_perspective, cube.white_face):
                        cube.move(PossibleOperations.INVERT_CUBE_VERTICALLY)
                    else:
                        cube.move(PossibleOperations.INVERT_CUBE_HORIZONTALLY)
                elif orientation == Orientation.LEFT:
                    cube.move(PossibleOperations.ROTATE_RIGHT_VERTICALLY)
                elif orientation == Orientation.RIGHT:
                    cube.move(PossibleOperations.ROTATE_LEFT_VERTICALLY)
                else:
                    if iters > 5:
                        raise Exception('Invalid Cube! Exiting Infinite Loop')
                    else:
                        cube.move(PossibleOperations.ROTATE_LEFT_HORIZONTALLY)
                iters += 1
    
    def get_orientation(cube: RubixCube) -> str:
        if Predicates.FacePredicates.are_faces_equal(cube.current_perspective.top, cube.blue_face):
            return Orientation.TOP
        elif Predicates.FacePredicates.are_faces_equal(cube.current_perspective.right, cube.blue_face):
            return Orientation.RIGHT
        elif Predicates.FacePredicates.are_faces_equal(cube.current_perspective.left, cube.blue_face):
            return Orientation.LEFT
        elif Predicates.FacePredicates.are_faces_equal(cube.current_perspective.bottom, cube.blue_face):
            return Orientation.BOTTOM
        elif Predicates.FacePredicates.are_faces_equal(cube.current_perspective.opposite, cube.blue_face):
            return Orientation.BACK
    
    def transfer_faces(old: Face, new: Face) -> None:
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
    

    ROTATE_LEFT_VERTICALLY = rotate_left
    ROTATE_RIGHT_VERTICALLY = rotate_right
    ROTATE_UP = rotate_up
    ROTATE_DOWN = rotate_down
    ROTATE_LEFT_HORIZONTALLY = rotate_left
    ROTATE_RIGHT_HORIZONTALLY = rotate_right
    INVERT_CUBE_VERTICALLY = invert_cube
    INVERT_CUBE_HORIZONTALLY = invert_cube
    RESET_PERSPECTIVE = reset_perspective
    
SHUFFLE_CUBE = shuffle_cube    

OPERATIONS = [Rotations.ROTATE_LEFT_VERTICALLY, Rotations.ROTATE_RIGHT_VERTICALLY, Rotations.ROTATE_UP, Rotations.ROTATE_DOWN, 
              Rotations.ROTATE_LEFT_HORIZONTALLY, Rotations.ROTATE_RIGHT_HORIZONTALLY, Rotations.INVERT_CUBE_VERTICALLY, Rotations.INVERT_CUBE_HORIZONTALLY,
              Shifts.RIGHT_COL_UP, Shifts.LEFT_COL_UP, Shifts.RIGHT_COL_DOWN, Shifts.LEFT_COL_DOWN,
              Shifts.TOP_ROW_LEFT, Shifts.TOP_ROW_RIGHT, Shifts.BOTTOM_ROW_LEFT, Shifts.BOTTOM_ROW_RIGHT,
              Rotations.RESET_PERSPECTIVE, SHUFFLE_CUBE]