"""
This module contains the RubixCube, Face, Piece, EdgePiece and CornerPiece classes. It creates a Rubix Cube, 
allowing all possible operations that can be done to a Rubix Cube in real life.
"""

from __future__ import annotations
from typing import Optional, Union
import numpy as np
from constants import (
    Colours,
    FacePositions,
    Orientation,
    PieceType,
    PossibleRotations,
    PossibleShifts,
    POSSIBLE_ROTATIONS,
    POSSIBLE_SHIFTS,
)
from operations import Operation, Rotations, Shifts, ROTATIONS, SHIFTS
from predicate import CubePredicate, FacePredicate
from error import CubeIntegrityError, InvalidOperationError
from validity_check import CubeValidity
import helper as hp
import icecream as ic


class RubixCube:

    """
    This is a class representing the Rubix Cube. A cube has 6 faces (type=FaceObject). It is initialized with the blue
    face in front, red face on the left, orange face on the right, green face on the back, white face
    on the top and yellow face on the bottom.

    All side faces (Front, Left, Right, Back) have Face().top set as the top (white) face and Face().bottom set as the
    bottom (yellow) face. Additionally, for all side faces, accessing the left/right attribute 4 times will bring you back to
    the initial perspective (hence, making it cyclic). The top (white) and bottom (yellow) faces have Face().top and
    Face().bottom set to None. To correctly map their representation in the cube, they have Face().front = the current
    front face and Face().back = the current back face.

    All faces have a 3 X 3 grid holding pieces (type=PieceObject). These are stored in a numpy array. For all side faces,
    the orientation is identical to face orientations discussed above. For the top (white) face, the top row corresponds to
    the edge Face().back (green), the left and right columns correspond to edges Face().left (red) and Face().right (orange) and
    the bottom row corresponds to the edge Face().front (blue). Similarly, for the bottom (yellow) face, the top row corresponds to
    the edge Face().front (blue), the left and right columns correspond to edges Face().left (red) and Face().right (orange) and
    the bottom row corresponds to the edge Face().back (green).

    ATTRIBUTES:
        current_perspective: Pointer to the Face Object that is currently in front
        blue_face: Pointer to the blue face in the cube
        white_face: Pointer to the white face in the cube
        yellow_face: Pointer to the yellow face in the cube
        red_face: Pointer to the red face in the cube
        orange_face: Pointer to the orange face in the cube
        green_face: Pointer to the green face in the cube
        current_operation: Represents the current operation performed on the cube
        op_stack: Stack containing all operations performed on the cube

    METHODS:
        create_cube: Creates the cube structure
        get_2D_cube_grid: Translates each face's grid into a 2D representation for graphing
        copy: Creates a duplicate instance of the Cube class with the same values
        assign_complements: Assigns corresponding complement value for each piece on a face
        integrity_check: Decorator function that performs integrity checks on the cube after each operation
        rotate: Performs the specified rotation operation
        shift: Performs the specified shift operation
        reset_perspective: Resets cube perspective to get the blue face front and white face top
        shuffle_cube: Shuffles cube

    PROPERTIES:
        faces: List of all the faces in the cube


    """

    def __init__(
        self,
        blue_face: Face = None,
        red_face: Face = None,
        orange_face: Face = None,
        green_face: Face = None,
        white_face: Face = None,
        yellow_face: Face = None,
        is_copy: bool = False,
    ) -> None:
        """
        Constructor method for the Cube class.

        Args:
            blue_face (Face, optional): Face instance for the blue face. Defaults to None.
            red_face (Face, optional): Face instance for the red face. Defaults to None.
            orange_face (Face, optional): Face instance for the orange face. Defaults to None.
            green_face (Face, optional): Face instance for the green face. Defaults to None.
            white_face (Face, optional): Face instance for the white face. Defaults to None.
            yellow_face (Face, optional): Face instance for the yellow face. Defaults to None.
            is_copy (bool, optional): bool to show if current Cube object is copied from another Cube object. Defaults to False.
        """
        # YOUR CODE HERE
        self.blue_face = blue_face
        self.red_face = red_face
        self.orange_face = orange_face
        self.green_face = green_face
        self.white_face = white_face
        self.yellow_face = yellow_face

        self.current_operation: Optional[Operation] = None
        self.op_stack: list = []

        if not is_copy:
            self.create_cube()
        else:
            self.current_perspective = self.blue_face
        pass

    # YOUR CODE HERE

    @property
    def faces(self) -> list[Face]:
        return [
            self.blue_face,
            self.red_face,
            self.green_face,
            self.orange_face,
            self.yellow_face,
            self.white_face,
        ]

    def __str__(self) -> str:
        """
        This method is called to return the string representation of the cube. It is represented as a 2D grid, 
        as shown below.
        
        Every face's grid = [[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]]
                              
        The output representation is as follows:
        
             Left Face
              _______   Bottom Face
              |3 2 1|   /
              |6 5 4|  /
              |9 8 7| /
        _____________L___________
        |1 4 7|1 4 7|9 6 3|1 4 7|
Front   |2 5 8|2 5 8|8 5 2|2 5 8| Top
Face    |3 6 9|3 6 9|7 4 1|3 6 9| Face
        -------------------------
              |7 8 9|   \
              |4 5 6|    \
              |1 2 3|    Back Face
              -------
             Right Face
        

        Returns:
            output (str): A string that is formatted to output the above structure
        """
        front = self.current_perspective.copy()

        left_grid = self.get_2D_cube_grid(front.left, Orientation.LEFT)
        right_grid = self.get_2D_cube_grid(front.right, Orientation.RIGHT)
        top_grid = self.get_2D_cube_grid(front.top, Orientation.TOP)
        bottom_grid = self.get_2D_cube_grid(front.bottom, Orientation.BOTTOM)
        back_grid = self.get_2D_cube_grid(front.opposite, Orientation.BACK)
        front_grid = self.get_2D_cube_grid(front, Orientation.FRONT)

        output = f"     _______\n"
        output += (
            f"     !{left_grid[0]}|\n     !{left_grid[1]}|\n     !{left_grid[2]}|\n"
        )
        output += "------------------------\n"
        output += f"{front_grid[0]}|{bottom_grid[0]}|{back_grid[0]}|{top_grid[0]}|\n"
        output += f"{front_grid[1]}|{bottom_grid[1]}|{back_grid[1]}|{top_grid[1]}|\n"
        output += f"{front_grid[2]}|{bottom_grid[2]}|{back_grid[2]}|{top_grid[2]}|\n"
        output += "------------------------\n"
        output += (
            f"     !{right_grid[0]}|\n     !{right_grid[1]}|\n     !{right_grid[2]}|\n"
        )
        output += f"     -------"

        return output

    def get_2D_cube_grid(
        self, face: Face, orientation: Orientation
    ) -> tuple[str, str, str]:
        """
        This method builds the transformed grids to be used in the string representation of the cube.

        Args:
            face (Face): face instance that the grid is being transformed for
            orientation (str): String literal showing if the face is left, right, top, bottom, back or front of Cube().current_perspective

        Returns:
            tuple: The tuple contains the string output for each row/column in the grid
        """
        if orientation == Orientation.LEFT:
            first_row = f"{face.grid[FacePositions.TOP_RIGHT].colour.value[0]} {face.grid[FacePositions.TOP_CENTER].colour.value[0]} {face.grid[FacePositions.TOP_LEFT].colour.value[0]}"
            second_row = f"{face.grid[FacePositions.MID_RIGHT].colour.value[0]} {face.grid[FacePositions.MID_CENTER].colour.value[0]} {face.grid[FacePositions.MID_LEFT].colour.value[0]}"
            third_row = f"{face.grid[FacePositions.BOTTOM_RIGHT].colour.value[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour.value[0]} {face.grid[FacePositions.BOTTOM_LEFT].colour.value[0]}"

        elif orientation in [Orientation.FRONT, Orientation.BOTTOM, Orientation.TOP]:
            first_row = f"{face.grid[FacePositions.TOP_LEFT].colour.value[0]} {face.grid[FacePositions.MID_LEFT].colour.value[0]} {face.grid[FacePositions.BOTTOM_LEFT].colour.value[0]}"
            second_row = f"{face.grid[FacePositions.TOP_CENTER].colour.value[0]} {face.grid[FacePositions.MID_CENTER].colour.value[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour.value[0]}"
            third_row = f"{face.grid[FacePositions.TOP_RIGHT].colour.value[0]} {face.grid[FacePositions.MID_RIGHT].colour.value[0]} {face.grid[FacePositions.BOTTOM_RIGHT].colour.value[0]}"

        elif orientation == Orientation.BACK:
            first_row = f"{face.grid[FacePositions.BOTTOM_RIGHT].colour.value[0]} {face.grid[FacePositions.MID_RIGHT].colour.value[0]} {face.grid[FacePositions.TOP_RIGHT].colour.value[0]}"
            second_row = f"{face.grid[FacePositions.BOTTOM_CENTER].colour.value[0]} {face.grid[FacePositions.MID_CENTER].colour.value[0]} {face.grid[FacePositions.TOP_CENTER].colour.value[0]}"
            third_row = f"{face.grid[FacePositions.BOTTOM_LEFT].colour.value[0]} {face.grid[FacePositions.MID_LEFT].colour.value[0]} {face.grid[FacePositions.TOP_LEFT].colour.value[0]}"

        elif orientation == Orientation.RIGHT:
            first_row = f"{face.grid[FacePositions.BOTTOM_LEFT].colour.value[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour.value[0]} {face.grid[FacePositions.BOTTOM_RIGHT].colour.value[0]}"
            second_row = f"{face.grid[FacePositions.MID_LEFT].colour.value[0]} {face.grid[FacePositions.MID_CENTER].colour.value[0]} {face.grid[FacePositions.MID_RIGHT].colour.value[0]}"
            third_row = f"{face.grid[FacePositions.TOP_LEFT].colour.value[0]} {face.grid[FacePositions.TOP_CENTER].colour.value[0]} {face.grid[FacePositions.TOP_RIGHT].colour.value[0]}"

        return (first_row, second_row, third_row)

    def create_cube(self) -> None:
        """
        This method initializes the Rubix Cube. The faces are created, edges are joined and positional attributes
        assigned. All complements values are assigned for each piece (type=PieceType) in each face (type=FaceType).

        Side Faces Initialization:

                                             (Top)
                                    (Left Col)   (Right Col)
                                             ^   ^
                                             |   |
                                            _______
                                            |1 2 3|-> (Top Row)
                            (Left)          |4 5 6|                  (Right)
                                            |7 8 9|-> (Bottom Row)
                                            -------

                                            (Bottom)

        Top Face Initialization:

                                             (Back)
                                    (Left Col)   (Right Col)
                                             ^   ^
                                             |   |
                                            _______
                                            |1 2 3|-> (Top Row)
                            (Left)          |4 5 6|                  (Right)
                                            |7 8 9|-> (Bottom Row)
                                            -------

                                            (Front)

        Bottom Face Initialization:

                                             (Front)
                                    (Left Col)   (Right Col)
                                             ^   ^
                                             |   |
                                            _______
                                            |1 2 3|-> (Top Row)
                            (Left)          |4 5 6|                  (Right)
                                            |7 8 9|-> (Bottom Row)
                                            -------

                                            (Back)
        """
        # YOUR CODE HERE
        # Creating the Cube Faces
        self.blue_face = Face(Colours.BLUE, orientation_to_cube=Orientation.FRONT)
        self.red_face = Face(Colours.RED, orientation_to_cube=Orientation.LEFT)
        self.orange_face = Face(Colours.ORANGE, orientation_to_cube=Orientation.RIGHT)
        self.yellow_face = Face(Colours.YELLOW, orientation_to_cube=Orientation.BOTTOM)
        self.green_face = Face(Colours.GREEN, orientation_to_cube=Orientation.BACK)
        self.white_face = Face(Colours.WHITE, orientation_to_cube=Orientation.TOP)

        # Setting current perspective (front) as the blue face
        self.current_perspective = self.blue_face

        # Joining side faces
        self.blue_face.right = self.orange_face
        self.blue_face.left = self.red_face

        self.red_face.right = self.blue_face
        self.red_face.left = self.green_face

        self.green_face.right = self.red_face
        self.green_face.left = self.orange_face

        self.orange_face.right = self.green_face
        self.orange_face.left = self.blue_face

        # Joining top face
        self.blue_face.top = self.white_face
        self.white_face.front = self.blue_face

        self.orange_face.top = self.white_face
        self.white_face.right = self.orange_face

        self.green_face.top = self.white_face
        self.white_face.back = self.green_face

        self.red_face.top = self.white_face
        self.white_face.left = self.red_face

        # Joining the bottom face
        self.blue_face.bottom = self.yellow_face
        self.yellow_face.front = self.blue_face

        self.orange_face.bottom = self.yellow_face
        self.yellow_face.right = self.orange_face

        self.green_face.bottom = self.yellow_face
        self.yellow_face.back = self.green_face

        self.red_face.bottom = self.yellow_face
        self.yellow_face.left = self.red_face

        # Connecting opposite faces
        self.blue_face.opposite = self.green_face
        self.green_face.opposite = self.blue_face

        self.red_face.opposite = self.orange_face
        self.orange_face.opposite = self.red_face

        self.white_face.opposite = self.yellow_face
        self.yellow_face.opposite = self.white_face

        ## Initializing complements
        self.assign_complements()

    def copy(self) -> RubixCube:
        # YOUR CODE HERE
        return RubixCube(
            self.blue_face,
            self.red_face,
            self.orange_face,
            self.green_face,
            self.white_face,
            self.yellow_face,
            is_copy=True,
        )

    def assign_complements(self) -> None:
        """
        This method assigns the complements for each piece in the face. EdgePiece and CornerPiece classes
        have instance attributes (EdgePiece().complement and CornerPiece().complements respectively) that hold
        the pointers to the complement pieces.

        Example: Consider an edge piece in between the blue face and white face. According to current perspective,
        this would make the top_center piece in the front (blue) face and the bottom_center piece in the top (white)
        face complements. Similarly, in corner pieces, all 3 pieces that make up each corner are each others' complements.
        """
        # YOUR CODE HERE
        current = self.current_perspective

        # Assigning Edge Piece Complements
        current.grid[FacePositions.TOP_CENTER].complement = current.top.grid[
            FacePositions.BOTTOM_CENTER
        ]
        current.top.grid[FacePositions.BOTTOM_CENTER].complement = current.grid[
            FacePositions.TOP_CENTER
        ]

        current.grid[FacePositions.MID_LEFT].complement = current.left.grid[
            FacePositions.MID_RIGHT
        ]
        current.left.grid[FacePositions.MID_RIGHT].complement = current.grid[
            FacePositions.MID_LEFT
        ]

        current.grid[FacePositions.MID_RIGHT].complement = current.right.grid[
            FacePositions.MID_LEFT
        ]
        current.right.grid[FacePositions.MID_LEFT].complement = current.grid[
            FacePositions.MID_RIGHT
        ]

        current.grid[FacePositions.BOTTOM_CENTER].complement = current.bottom.grid[
            FacePositions.TOP_CENTER
        ]
        current.bottom.grid[FacePositions.TOP_CENTER].complement = current.grid[
            FacePositions.BOTTOM_CENTER
        ]

        current.top.grid[FacePositions.MID_LEFT].complement = current.left.grid[
            FacePositions.TOP_CENTER
        ]
        current.left.grid[FacePositions.TOP_CENTER].complement = current.top.grid[
            FacePositions.MID_LEFT
        ]

        current.top.grid[FacePositions.MID_RIGHT].complement = current.right.grid[
            FacePositions.TOP_CENTER
        ]
        current.right.grid[FacePositions.TOP_CENTER].complement = current.top.grid[
            FacePositions.MID_RIGHT
        ]

        current.bottom.grid[FacePositions.MID_LEFT].complement = current.left.grid[
            FacePositions.BOTTOM_CENTER
        ]
        current.left.grid[FacePositions.BOTTOM_CENTER].complement = current.bottom.grid[
            FacePositions.MID_LEFT
        ]

        current.bottom.grid[FacePositions.MID_RIGHT].complement = current.right.grid[
            FacePositions.BOTTOM_CENTER
        ]
        current.right.grid[
            FacePositions.BOTTOM_CENTER
        ].complement = current.bottom.grid[FacePositions.MID_RIGHT]

        current.opposite.grid[FacePositions.TOP_CENTER].complement = current.top.grid[
            FacePositions.TOP_CENTER
        ]
        current.top.grid[FacePositions.TOP_CENTER].complement = current.opposite.grid[
            FacePositions.TOP_CENTER
        ]

        current.opposite.grid[FacePositions.MID_LEFT].complement = current.right.grid[
            FacePositions.MID_RIGHT
        ]
        current.right.grid[FacePositions.MID_RIGHT].complement = current.opposite.grid[
            FacePositions.MID_LEFT
        ]

        current.opposite.grid[FacePositions.MID_RIGHT].complement = current.left.grid[
            FacePositions.MID_LEFT
        ]
        current.left.grid[FacePositions.MID_LEFT].complement = current.opposite.grid[
            FacePositions.MID_RIGHT
        ]

        current.opposite.grid[
            FacePositions.BOTTOM_CENTER
        ].complement = current.bottom.grid[FacePositions.BOTTOM_CENTER]
        current.bottom.grid[
            FacePositions.BOTTOM_CENTER
        ].complement = current.opposite.grid[FacePositions.BOTTOM_CENTER]

        # Assigning corner piece complements
        # Front Corners
        current.grid[FacePositions.TOP_LEFT].complements = set(
            [
                current.top.grid[FacePositions.BOTTOM_LEFT],
                current.left.grid[FacePositions.TOP_RIGHT],
            ]
        )
        current.top.grid[FacePositions.BOTTOM_LEFT].complements = set(
            [
                current.grid[FacePositions.TOP_LEFT],
                current.left.grid[FacePositions.TOP_RIGHT],
            ]
        )
        current.left.grid[FacePositions.TOP_RIGHT].complements = set(
            [
                current.grid[FacePositions.TOP_LEFT],
                current.top.grid[FacePositions.BOTTOM_LEFT],
            ]
        )

        current.grid[FacePositions.TOP_RIGHT].complements = set(
            [
                current.top.grid[FacePositions.BOTTOM_RIGHT],
                current.right.grid[FacePositions.TOP_LEFT],
            ]
        )
        current.top.grid[FacePositions.BOTTOM_RIGHT].complements = set(
            [
                current.grid[FacePositions.TOP_RIGHT],
                current.right.grid[FacePositions.TOP_LEFT],
            ]
        )
        current.right.grid[FacePositions.TOP_LEFT].complements = set(
            [
                current.top.grid[FacePositions.BOTTOM_RIGHT],
                current.grid[FacePositions.TOP_RIGHT],
            ]
        )

        current.grid[FacePositions.BOTTOM_LEFT].complements = set(
            [
                current.bottom.grid[FacePositions.TOP_LEFT],
                current.left.grid[FacePositions.BOTTOM_RIGHT],
            ]
        )
        current.bottom.grid[FacePositions.TOP_LEFT].complements = set(
            [
                current.grid[FacePositions.BOTTOM_LEFT],
                current.left.grid[FacePositions.BOTTOM_RIGHT],
            ]
        )
        current.left.grid[FacePositions.BOTTOM_RIGHT].complements = set(
            [
                current.grid[FacePositions.BOTTOM_LEFT],
                current.bottom.grid[FacePositions.TOP_LEFT],
            ]
        )

        current.grid[FacePositions.BOTTOM_RIGHT].complements = set(
            [
                current.bottom.grid[FacePositions.TOP_RIGHT],
                current.right.grid[FacePositions.BOTTOM_LEFT],
            ]
        )
        current.bottom.grid[FacePositions.TOP_RIGHT].complements = set(
            [
                current.grid[FacePositions.BOTTOM_RIGHT],
                current.right.grid[FacePositions.BOTTOM_LEFT],
            ]
        )
        current.right.grid[FacePositions.BOTTOM_LEFT].complements = set(
            [
                current.grid[FacePositions.BOTTOM_RIGHT],
                current.bottom.grid[FacePositions.TOP_RIGHT],
            ]
        )

        # Back Corners
        current.opposite.grid[FacePositions.TOP_LEFT].complements = set(
            [
                current.top.grid[FacePositions.TOP_RIGHT],
                current.right.grid[FacePositions.TOP_RIGHT],
            ]
        )
        current.top.grid[FacePositions.TOP_RIGHT].complements = set(
            [
                current.opposite.grid[FacePositions.TOP_LEFT],
                current.right.grid[FacePositions.TOP_RIGHT],
            ]
        )
        current.right.grid[FacePositions.TOP_RIGHT].complements = set(
            [
                current.top.grid[FacePositions.TOP_RIGHT],
                current.opposite.grid[FacePositions.TOP_LEFT],
            ]
        )

        current.opposite.grid[FacePositions.TOP_RIGHT].complements = set(
            [
                current.top.grid[FacePositions.TOP_LEFT],
                current.left.grid[FacePositions.TOP_LEFT],
            ]
        )
        current.top.grid[FacePositions.TOP_LEFT].complements = set(
            [
                current.opposite.grid[FacePositions.TOP_RIGHT],
                current.left.grid[FacePositions.TOP_LEFT],
            ]
        )
        current.left.grid[FacePositions.TOP_LEFT].complements = set(
            [
                current.top.grid[FacePositions.TOP_LEFT],
                current.opposite.grid[FacePositions.TOP_RIGHT],
            ]
        )

        current.opposite.grid[FacePositions.BOTTOM_LEFT].complements = set(
            [
                current.bottom.grid[FacePositions.BOTTOM_RIGHT],
                current.right.grid[FacePositions.BOTTOM_RIGHT],
            ]
        )
        current.bottom.grid[FacePositions.BOTTOM_RIGHT].complements = set(
            [
                current.opposite.grid[FacePositions.BOTTOM_LEFT],
                current.right.grid[FacePositions.BOTTOM_RIGHT],
            ]
        )
        current.right.grid[FacePositions.BOTTOM_RIGHT].complements = set(
            [
                current.bottom.grid[FacePositions.BOTTOM_RIGHT],
                current.opposite.grid[FacePositions.BOTTOM_LEFT],
            ]
        )

        current.opposite.grid[FacePositions.BOTTOM_RIGHT].complements = set(
            [
                current.bottom.grid[FacePositions.BOTTOM_LEFT],
                current.left.grid[FacePositions.BOTTOM_LEFT],
            ]
        )
        current.bottom.grid[FacePositions.BOTTOM_LEFT].complements = set(
            [
                current.opposite.grid[FacePositions.BOTTOM_RIGHT],
                current.left.grid[FacePositions.BOTTOM_LEFT],
            ]
        )
        current.left.grid[FacePositions.BOTTOM_LEFT].complements = set(
            [
                current.bottom.grid[FacePositions.BOTTOM_LEFT],
                current.opposite.grid[FacePositions.BOTTOM_RIGHT],
            ]
        )

    def integrity_check(func: function) -> function:
        """
        This is a decorator method that performs checks the integrity of the cube after each operation.

        Args:
            func (function): Function to be executed within the wrapper function

        Returns:
            (function): Wrapper function that performs operation, followed by the integrity check
        """

        def wrapper(
            self,
            operation: Union[PossibleRotations, PossibleShifts],
            internal_req: bool = False,
        ) -> None:
            """
            This is the wrapper function for the decorator. It performs the operation, as well as the
            integrity check after performing each operation.

            Args:
                operation (Union[PossibleRotations, PossibleShifts]): Operation requested
                internal_req (bool, optional): Flag representing whether the operation was requested by
                                               user or a built-in function. Defaults to False.

            Raises:
                CubeIntegrityError: If the requested operation causes a break in cube integrity, exception is raised
            """
            ic.ic(operation)
            func(operation, internal_req)
            if not CubeValidity.is_cube_valid(self):
                raise CubeIntegrityError(
                    f"Operation '{operation.value}' has broken integrity of the cube! Exiting Porgram Now!"
                )

        return wrapper

    @integrity_check
    def rotate(self, rotation: PossibleRotations, internal_req: bool = False) -> None:
        """
        This method performs the requested rotation operation.

        Args:
            rotation (PossibleRotations): String literal indicating the rotation operation requested
            internal_req (bool, optional): bool flag indicating whether the operation was requested by
                                           user or a buit-in function. Defaults to False.

        Raises:
            InvalidOperationError: If requested operation is not a rotation, exception is raised.
        """
        # YOUR CODE HERE
        for op, func in zip(POSSIBLE_ROTATIONS, ROTATIONS):
            if rotation == op:
                self.current_operation = rotation
                # print(rotation)
                func(self, internal_req)
                break
        else:
            raise InvalidOperationError(
                f"Invalid Rotation Operation Requested! Requested Operation is {rotation}"
            )

    @integrity_check
    def shift(self, shift: PossibleShifts, internal_req: bool = None) -> None:
        """
        This method performs the requested shift operation.

        Args:
            shift (PossibleShifts): String literal indicating the shift operation requested
            internal_req (bool, optional): bool flag indicating whether the operation was requested by
                                           user or a buit-in function. Defaults to None.

        Raises:
            InvalidOperationError: If requested operation is not a shift, exception is raised
        """
        # YOUR CODE HERE
        for op, func in zip(POSSIBLE_SHIFTS, SHIFTS):
            if shift == op:
                self.current_operation = shift
                # print(shift, internal_req)
                func(self, internal_req)
                break
        else:
            raise InvalidOperationError("Invalid Shift Operation Requested!")

    def reset_perspective(self) -> None:
        """
        This method resets the perspective of the cube to its initial orientation. Initial
        orientation is reached when the blue face is in front, white face on top and
        red face on the left.

        Raises:
            CubeIntegrityError: If the blue face doesn't have a valid orientation, raise an exception
        """
        iters = 0
        while True:
            if CubePredicate.is_correct_perspective(self):
                break
            else:
                orientation = self.blue_face.orientation_to_cube
                if orientation == Orientation.TOP:
                    self.rotate(PossibleRotations.ROTATE_DOWN, internal_req=True)
                elif orientation == Orientation.BOTTOM:
                    self.rotate(PossibleRotations.ROTATE_UP, internal_req=True)
                elif orientation == Orientation.BACK:
                    if CubePredicate.is_white_face_top(
                        self.current_perspective, self.white_face
                    ):
                        self.rotate(
                            PossibleRotations.INVERT_VERTICALLY, internal_req=True
                        )
                    else:
                        self.rotate(
                            PossibleRotations.INVERT_HORIZONTALLY,
                            internal_req=True,
                        )
                elif orientation == Orientation.LEFT:
                    self.rotate(
                        PossibleRotations.ROTATE_RIGHT_VERTICALLY, internal_req=True
                    )
                elif orientation == Orientation.RIGHT:
                    self.rotate(
                        PossibleRotations.ROTATE_LEFT_VERTICALLY, internal_req=True
                    )
                else:
                    if iters > 5:
                        raise CubeIntegrityError("Invalid Cube! Exiting Infinite Loop")
                    else:
                        self.rotate(
                            PossibleRotations.ROTATE_LEFT_HORIZONTALLY,
                            internal_req=True,
                        )
                iters += 1

    def shuffle_cube(self) -> list[Union[PossibleRotations, PossibleShifts]]:
        """
        This method shuffles the cube by performing random operations.

        Returns:
            list[Union[PossibleRotations, PossibleShifts]]: _description_
        """
        error_stack = []
        num_operations = np.random.randint(100, 200)
        for i in range(num_operations):
            p = np.random.random()
            if p > 0.7:
                rand_idx = np.random.randint(len(ROTATIONS))
                try:
                    ROTATIONS[rand_idx](self, internal_req=True)
                    # self.op_stack.append(POSSIBLE_ROTATIONS[rand_idx])
                except:
                    # YOUR CODE HERE
                    error_stack.append(POSSIBLE_ROTATIONS[rand_idx])
                    continue
            else:
                rand_idx = np.random.randint(len(SHIFTS))
                try:
                    SHIFTS[rand_idx](self, internal_req=True)
                    # self.op_stack.append(POSSIBLE_SHIFTS[rand_idx])
                except:
                    # YOUR CODE HERE
                    error_stack.append(POSSIBLE_SHIFTS[rand_idx])
                    continue

        return error_stack

    def set_perspective(self, face: Face) -> None:
        orientation = face.orientation_to_cube

        if orientation == Orientation.BACK:
            self.rotate(PossibleRotations.INVERT_VERTICALLY, internal_req=True)
        elif orientation == Orientation.LEFT:
            self.rotate(PossibleRotations.ROTATE_RIGHT_VERTICALLY, internal_req=True)
        elif orientation == Orientation.RIGHT:
            self.rotate(PossibleRotations.ROTATE_LEFT_VERTICALLY, internal_req=True)
        elif orientation == Orientation.TOP:
            self.rotate(PossibleRotations.ROTATE_DOWN, internal_req=True)
        elif orientation == Orientation.BOTTOM:
            self.rotate(PossibleRotations.ROTATE_UP, internal_req=True)

    def unshuffle_cube(self) -> None:
        inverse_op_stack = hp.reverse_stack(self.op_stack)
        for op in inverse_op_stack:
            op()  # Add operation call with internal_req
            pass
        pass


class Face:

    """
    This is a class representing a Face of a Rubix Cube (type=CubeType). Each face has a 3 X 3 grid
    representing each of the 9 pieces (type=PieceType) on the face of a Rubix Cube. The Piece().colour
    is set to the face's center colour (since the center piece cannot be moved from the face).

    ATTRIBUTES:
        _colour (str): Private string literal assigning a colour to the face's center piece
        right (Face, optional): Face instance that is to the right of the current face in the Cube class. Defaults to None.
        left (Face, optional): Face instance that is to the left of the current face in the Cube class. Defaults to None.
        top (Face, optional): Face instance that is to the top of the current face in the Cube class. Becomes None if face is not a side face. Defaults to None
        bottom (Face, optional): Face instance that is to the bottom of the current face in the Cube class. Becomes None if face is not a side face. Defaults to None
        front (Face, optional): Face instance that is to the front of the current face in the Cube class. Becomes None if face is a side face. Defaults to None
        back (Face, optional): Face instance that is to the back of the current face in the Cube class. Becomes None if face is a side face. Defaults to None
        opposite (Face, optional): Face instance that points to the opposite face to the current face in the Cube class. Defaults to None
        orientation_to_cube (Orientation, optional): Orientation of the face with respect to the cube's current perspective. Defaults to None
        grid (numpy.array, optional): 3 X 3 matrix that stores the pieces for the current face. Defaults to None

    METHODS:
        copy: Creates a duplicate instance of the Face class with the same values
        initialize_grid: Initializes the face instance's grid

    PROPERTIES:
        colour: Property to access face's colour
        is_side_face: bool property indicating whether a face is a side face in the cube
    """

    def __init__(
        self,
        colour: Colours,
        left: Face = None,
        right: Face = None,
        top: Face = None,
        bottom: Face = None,
        front: Face = None,
        back: Face = None,
        opposite: Face = None,
        grid: Optional[np.ndarray] = None,
        orientation_to_cube: Optional[Orientation] = None,
        is_copy: bool = False,
    ) -> None:
        # YOUR CODE HERE
        self._colour = colour
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.front = front
        self.back = back
        self.opposite = opposite
        self.orientation_to_cube = orientation_to_cube

        if not is_copy:
            self.grid = self.initialize_grid()
        else:
            self.grid = grid
        pass

    # YOUR CODE HERE
    @property
    def is_side_face(self) -> bool:
        if self.orientation_to_cube in [Orientation.TOP, Orientation.BOTTOM]:
            return False
        return True

    @property
    def colour(self) -> Colours:
        return self._colour

    def copy(self) -> Face:
        # YOUR CODE HERE
        return Face(
            self.colour,
            self.left,
            self.right,
            self.top,
            self.bottom,
            self.front,
            self.back,
            self.opposite,
            self.grid.copy(),
            self.orientation_to_cube,
            is_copy=True,
        )

    def initialize_grid(self) -> np.ndarray:
        # YOUR CODE HERE
        # Initializing center piece
        center_piece = Piece(self, FacePositions.MID_CENTER, PieceType.CENTER)

        # Initializing edge pieces
        top_center_piece = EdgePiece(self, FacePositions.TOP_CENTER, PieceType.EDGE)
        mid_left_piece = EdgePiece(self, FacePositions.MID_LEFT, PieceType.EDGE)
        mid_right_piece = EdgePiece(self, FacePositions.MID_RIGHT, PieceType.EDGE)
        bottom_center_piece = EdgePiece(
            self, FacePositions.BOTTOM_CENTER, PieceType.EDGE
        )

        # Initializing corner pieces
        top_left_piece = CornerPiece(self, FacePositions.TOP_LEFT, PieceType.CORNER)
        top_right_piece = CornerPiece(self, FacePositions.TOP_RIGHT, PieceType.CORNER)
        bottom_left_piece = CornerPiece(
            self, FacePositions.BOTTOM_LEFT, PieceType.CORNER
        )
        bottom_right_piece = CornerPiece(
            self, FacePositions.BOTTOM_RIGHT, PieceType.CORNER
        )

        grid = [
            [top_left_piece, top_center_piece, top_right_piece],
            [mid_left_piece, center_piece, mid_right_piece],
            [bottom_left_piece, bottom_center_piece, bottom_right_piece],
        ]

        return np.array(grid)


class Piece:

    """
    This is a class that represents each piece on each face of the Rubix Cube.

    ATTRIBUTES:
        face_position (FacePositions): a tuple representing the index for the piece in the current face instance's grid
        face (Face): a pointer to the piece's current face instance
        _colour (Colour): a string property that stores the colour that is on the current piece instance
        _piece_type (PieceType): a string property that stores the piece's type (Center, Edge, Corner)

    PROPERTIES:
        colour: Property to access the piece's colour
        piece_type: Property to access the piece's type
        position: Property to access the piece's absolute location in the cube

    """

    def __init__(
        self, face: Face, face_position: FacePositions, piece_type: PieceType
    ) -> None:
        # YOUR CODE HERE
        self.face = face
        self.face_position = face_position
        self._colour = self.face.colour
        self._piece_type = piece_type

    # YOUR CODE HERE
    @property
    def colour(self) -> Colours:
        return self._colour

    @property
    def piece_type(self) -> PieceType:
        return self._piece_type

    @property
    def position(self) -> tuple[Face, FacePositions]:
        return (self.face, self.face_position)


class EdgePiece(Piece):

    """
    This is a class that represents each edge piece on each face of the Rubix Cube. This class inherits from
    the Piece class, inheriting some properties and attributes.

    ATTRIBUTES:
        face_position (FacePositions, inherited): a tuple representing the index for the piece in the current face instance's grid
        face (Face, inherited): a pointer to the piece's current face instance
        _colour (Colour, inherited): a string property that stores the colour that is on the current piece instance
        _piece_type (PieceType, inherited): a string property that stores the piece's type (Center, Edge, Corner)
        _complement (EdgePiece): a pointer property to the Piece instance that is the current Piece instance's complement

    PROPERTIES:
        complement: Property to access the piece's complement piece
    """

    def __init__(
        self,
        face: Face,
        face_position: FacePositions,
        piece_type: PieceType,
        complement: Optional[EdgePiece] = None,
    ) -> None:
        # YOUR CODE HERE
        super().__init__(face, face_position, piece_type)
        self._complement = complement

    # YOUR CODE HERE
    @property
    def complement(self) -> EdgePiece:
        return self._complement

    @complement.setter
    def complement(self, new_complement: EdgePiece) -> None:
        if self.complement is None:
            self._complement = new_complement
        else:
            raise Exception(
                "'complement' attribute is already initialized. Cannot override initial value!"
            )


class CornerPiece(Piece):

    """
    This is a class that represents each corner piece on each face of the Rubix Cube. This class inherits from
    the Piece class, inheriting some properties and attributes.

    ATTRIBUTES:
        face_position (FacePositions, inherited): a tuple representing the index for the piece in the current face instance's grid
        face (Face, inherited): a pointer to the piece's current face instance
        _colour (Colour, inherited): a string property that stores the colour that is on the current piece instance
        _piece_type (PieceType, inherited): a string property that stores the piece's type (Center, Edge, Corner)
        _complements (set[CornerPiece]): a tuple property containing pointers to the Piece instances that are the
                              current Piece instance's complements

    PROPERTIES:
        complements: Property to access the piece's complement pieces
    """

    def __init__(
        self,
        face: Face,
        face_position: FacePositions,
        piece_type: PieceType,
        complements: Optional[set[CornerPiece]] = None,
    ) -> None:
        # YOUR CODE HERE
        super().__init__(face, face_position, piece_type)
        self._complements = complements

    # YOUR CODE HERE
    @property
    def complements(self) -> set[CornerPiece]:
        return self._complements

    @complements.setter
    def complements(self, new_complements: set[CornerPiece]) -> None:
        if self.complements is None:
            self._complements = new_complements
        else:
            raise Exception(
                "'complements' attribute is already initialized. Cannot override initial value!"
            )
