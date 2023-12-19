from __future__ import annotations
from typing import Optional
import numpy as np
from constants import (
    Colours,
    FacePositions,
    Orientation,
    PieceType,
    PossibleRotations,
    PossibleShifts,
    COLOURS,
    POSSIBLE_ROTATIONS,
    POSSIBLE_SHIFTS,
)
from operations import Operation, Rotations, Shifts, ROTATIONS, SHIFTS
from predicate import CubePredicate, FacePredicate
from error import InvalidOperationError


class RubixCube:
    PRINT_DICT = {
        Colours.BLUE: "B",
        Colours.RED: "R",
        Colours.ORANGE: "O",
        Colours.WHITE: "W",
        Colours.GREEN: "G",
        Colours.YELLOW: "Y",
    }

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
        # YOUR CODE HERE
        self.blue_face = blue_face
        self.red_face = red_face
        self.orange_face = orange_face
        self.green_face = green_face
        self.white_face = white_face
        self.yellow_face = yellow_face

        self.current_operation: Optional[Operation] = None

        if not is_copy:
            self.create_cube()
        pass

    # YOUR CODE HERE

    def __str__(self) -> str:
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
            first_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_RIGHT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_LEFT].colour]}"
            second_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.MID_RIGHT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_LEFT].colour]}"
            third_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_RIGHT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_LEFT].colour]}"

        elif orientation in [Orientation.FRONT, Orientation.BOTTOM, Orientation.TOP]:
            first_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_LEFT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_LEFT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_LEFT].colour]}"
            second_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_CENTER].colour]}"
            third_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_RIGHT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_RIGHT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_RIGHT].colour]}"

        elif orientation == Orientation.BACK:
            first_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_RIGHT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_RIGHT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_RIGHT].colour]}"
            second_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_CENTER].colour]}"
            third_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_LEFT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_LEFT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_LEFT].colour]}"

        elif orientation == Orientation.RIGHT:
            first_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_LEFT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.BOTTOM_RIGHT].colour]}"
            second_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.MID_LEFT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.MID_RIGHT].colour]}"
            third_row = f"{RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_LEFT].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_CENTER].colour]} {RubixCube.PRINT_DICT[face.grid[FacePositions.TOP_RIGHT].colour]}"

        return (first_row, second_row, third_row)

    def create_cube(self) -> None:
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

        # TODO: Assign Complements for Pieces
        pass

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

    def assign_complements(self, face: Face) -> None:
        # YOUR CODE HERE
        ## Assigning complements of edge pieces
        face.grid[FacePositions.TOP_CENTER].complement = face.top.grid[
            FacePositions.BOTTOM_CENTER
        ]
        face.grid[FacePositions.MID_LEFT].complement = face.left.grid[
            FacePositions.MID_RIGHT
        ]
        face.grid[FacePositions.MID_RIGHT].complement = face.right.grid[
            FacePositions.MID_LEFT
        ]
        face.grid[FacePositions.BOTTOM_CENTER].complement = face.bottom.grid[
            FacePositions.TOP_CENTER
        ]

        ## Assigning complements for corner pieces
        face.grid[FacePositions.TOP_LEFT].complements = (
            face.top.grid[FacePositions.BOTTOM_LEFT],
            face.left.grid[FacePositions.TOP_RIGHT],
        )
        face.grid[FacePositions.TOP_RIGHT].complements = (
            face.top.grid[FacePositions.BOTTOM_RIGHT],
            face.right.grid[FacePositions.TOP_LEFT],
        )
        face.grid[FacePositions.BOTTOM_LEFT].complements = (
            face.bottom.grid[FacePositions.TOP_LEFT],
            face.left.grid[FacePositions.BOTTOM_RIGHT],
        )
        face.grid[FacePositions.BOTTOM_RIGHT].complements = (
            face.bottom.grid[FacePositions.TOP_RIGHT],
            face.right.grid[FacePositions.BOTTOM_LEFT],
        )

    def rotate(self, rotation: PossibleRotations, internal_req: bool = False) -> None:
        # YOUR CODE HERE
        for op, func in zip(POSSIBLE_ROTATIONS, ROTATIONS):
            if rotation == op:
                self.current_operation = rotation
                # print(rotation)
                func(self, internal_req)
                break
        else:
            raise InvalidOperationError("Invalid Rotation Operation Requested!")

    def shift(self, shift: PossibleShifts, internal_req: bool = None) -> None:
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
        iters = 0
        while True:
            if CubePredicate.is_correct_perspective(self):
                break
            else:
                # orientation = Rotations.get_orientation(cube)
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
                            PossibleRotations.INVERT_CUBE_VERTICALLY, internal_req=True
                        )
                    else:
                        self.rotate(
                            PossibleRotations.INVERT_CUBE_HORIZONTALLY,
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
                        raise Exception("Invalid Cube! Exiting Infinite Loop")
                    else:
                        self.rotate(
                            PossibleRotations.ROTATE_LEFT_HORIZONTALLY,
                            internal_req=True,
                        )
                iters += 1

    def shuffle_cube(self) -> tuple[list, list]:
        op_stack = []
        error_stack = []
        num_operations = np.random.randint(100, 200)
        for i in range(num_operations):
            p = np.random.random()
            if p > 0.7:
                rand_idx = np.random.randint(len(ROTATIONS))
                try:
                    ROTATIONS[rand_idx](self, internal_req=True)
                    op_stack.append(POSSIBLE_ROTATIONS[rand_idx])
                except:
                    # YOUR CODE HERE
                    error_stack.append(POSSIBLE_ROTATIONS[rand_idx])
                    continue
            else:
                rand_idx = np.random.randint(len(SHIFTS))
                try:
                    SHIFTS[rand_idx](self, internal_req=True)
                    op_stack.append(POSSIBLE_SHIFTS[rand_idx])
                except:
                    # YOUR CODE HERE
                    error_stack.append(POSSIBLE_SHIFTS[rand_idx])
                    continue

        return op_stack, error_stack


class Face:
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


class EdgePiece(Piece):
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
                "Complement attribute is already initialized. Cannot override initial value!"
            )


class CornerPiece(Piece):
    def __init__(
        self,
        face: Face,
        face_position: FacePositions,
        piece_type: PieceType,
        complements: Optional[tuple[CornerPiece, CornerPiece]] = None,
    ) -> None:
        # YOUR CODE HERE
        super().__init__(face, face_position, piece_type)
        self._complements = complements

    # YOUR CODE HERE
    @property
    def complements(self) -> tuple[CornerPiece, CornerPiece]:
        return self._complements

    @complements.setter
    def complements(self, new_complements) -> None:
        if self.complements is None:
            self._complements = new_complements
        else:
            raise Exception(
                "'complements' attribute is already initialized. Cannot override initial value!"
            )
