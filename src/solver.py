from __future__ import annotations
from typing import TYPE_CHECKING
from cube_init_m import RubixCube
from constants import (
    Colours,
    FacePositions,
    PossibleRotations,
    PossibleShifts,
    PieceType,
)
from error import ShuffleError, CubeIntegrityError, InvalidEdgePieceError

if TYPE_CHECKING:
    from src.cube_init_m import Face, EdgePiece, CornerPiece, Piece


class RubixCubeSolver:
    def __init__(self) -> None:
        # YOUR CODE HERE
        self.cube = RubixCube()
        error_stack = self.cube.shuffle_cube()
        if len(error_stack) > 0:
            raise ShuffleError(
                "One or more operations weren't successful! Shuffle operation failed!"
            )
        self.cube.reset_perspective()
        pass

    # YOUR CODE HERE
    def solve(self) -> None:
        """
        ALGORITHM:
        1. From initial perspective, complete first layer:
            i. Identify each of the white edge pieces
                a. Loop through each face's grid and find thee required piece
                b. Find the piece's complement to identify where the piece should end up
            ii. For each of the pieces,
        """
        # Looking for edge pieces that are white to build up the first layer
        # face = self.find_edge_piece(Colours.WHITE)
        # self.cube.set_perspective(face)

        while self.count_edge_pieces(Colours.WHITE) != 4:
            # white_edge_piece = self.find_edge_pieces_face(Colours.WHITE)
            # current_face = white_edge_piece.face

            # complement = white_edge_piece.complement
            # complement_colour = complement.colour
            # white_orientation = current_face.orientation_to_cube
            # complement_orientation = complement.face.orientation_to_cube
            white_edge_piece = self.find_edge_piece(Colours.WHITE)
            complement_piece = white_edge_piece.complement

            white_face = white_edge_piece.face
            complement_face = complement_piece.face

            white_orientation = white_edge_piece.face.orientation_to_cube
            complement_orientation = complement_piece.face.orientation_to_cube

            # if complement_piece.colour == complement_face.colour:
            #     pass

            # if complement_piece.colour == white_face.colour:
            #     pass

            if white_face.is_side_face:
                self.cube.set_perspective(white_face)

                if white_edge_piece.face_position == FacePositions.TOP_CENTER:
                    self.cube.rotate(PossibleRotations.ROTATE_LEFT_VERTICALLY)
                    self.cube.shift(PossibleShifts.LEFT_COL_DOWN)
                    self.cube.shift(PossibleShifts.LEFT_COL_DOWN)
                    self.cube.rotate(PossibleRotations.ROTATE_RIGHT_VERTICALLY)

                elif white_edge_piece.face_position == FacePositions.MID_LEFT:
                    self.cube.rotate(PossibleRotations.ROTATE_RIGHT_VERTICALLY)
                    self.cube.shift(PossibleShifts.RIGHT_COL_DOWN)
                    self.cube.shift(PossibleShifts.BOTTOM_ROW_LEFT)
                    self.cube.shift(PossibleShifts.RIGHT_COL_UP)
                    self.cube.shift(PossibleShifts.BOTTOM_ROW_RIGHT)
                    self.cube.rotate(PossibleRotations.ROTATE_LEFT_VERTICALLY)

                elif white_edge_piece.face_position == FacePositions.MID_RIGHT:
                    self.cube.rotate(PossibleRotations.ROTATE_LEFT_VERTICALLY)
                    self.cube.shift(PossibleShifts.LEFT_COL_DOWN)
                    self.cube.shift(PossibleShifts.BOTTOM_ROW_RIGHT)
                    self.cube.shift(PossibleShifts.LEFT_COL_UP)
                    self.cube.shift(PossibleShifts.BOTTOM_ROW_LEFT)
                    self.cube.rotate(PossibleRotations.ROTATE_RIGHT_VERTICALLY)

                else:
                    if white_edge_piece.face_position != FacePositions.BOTTOM_CENTER:
                        raise InvalidEdgePieceError(
                            "Face Position is invalid for an edge piece! Exiting Program!"
                        )

                iters = 0

                while complement_piece.colour != white_face.colour:
                    if iters > 4:
                        raise CubeIntegrityError(
                            "Cube Integrity has been compromised! Exiting program!"
                        )

                    self.cube.shift(PossibleShifts.BOTTOM_ROW_RIGHT)
                    self.cube.rotate(PossibleRotations.ROTATE_LEFT_VERTICALLY)
                    iters += 1

                self.cube.shift(PossibleShifts.BOTTOM_ROW_RIGHT)
                self.cube.shift(PossibleShifts.LEFT_COL_UP)
                self.cube.shift(PossibleShifts.RIGHT_COL_UP)
                self.cube.rotate(PossibleRotations.ROTATE_DOWN)

                self.cube.shift(PossibleShifts.BOTTOM_ROW_LEFT)
                self.cube.shift(PossibleShifts.LEFT_COL_DOWN)
                self.cube.shift(PossibleShifts.RIGHT_COL_DOWN)
                self.cube.rotate(PossibleRotations.ROTATE_UP)

            else:
                self.cube.set_perspective(complement_face)

                iters = 0

                while (
                    complement_face.top.grid[FacePositions.BOTTOM_CENTER].colour
                    == Colours.WHITE
                ):
                    if iters > 4:
                        raise CubeIntegrityError(
                            "Cube Integrity has been compromised! Exiting program!"
                        )

                    self.cube.shift(PossibleShifts.BOTTOM_ROW_RIGHT)
                    self.cube.rotate(PossibleRotations.ROTATE_LEFT_VERTICALLY)
                    iters += 1

                self.cube.shift(PossibleShifts.LEFT_COL_UP)
                self.cube.shift(PossibleShifts.RIGHT_COL_UP)
                self.cube.rotate(PossibleRotations.ROTATE_DOWN)

                self.cube.shift(PossibleShifts.BOTTOM_ROW_RIGHT)

                self.cube.shift(PossibleShifts.LEFT_COL_DOWN)
                self.cube.shift(PossibleShifts.RIGHT_COL_DOWN)
                self.cube.rotate(PossibleRotations.ROTATE_UP)

            self.cube.reset_perspective()

        pass

    def find_edge_piece(self, requested_colour: Colours) -> EdgePiece:
        # faces = [
        #     self.blue_face,
        #     self.red_face,
        #     self.green_face,
        #     self.orange_face,
        #     self.yellow_face,
        #     self.white_face,
        # ]
        for face in self.cube.faces:
            for piece in face.grid:
                if (
                    piece.piece_type == PieceType.EDGE
                    and piece.colour == requested_colour
                ):
                    # return (piece.face, piece.face_position)
                    return piece

    def build_first_layer(self):
        pass

    def count_edge_pieces(self, face: Face) -> int:
        count = 0
        if face.grid[FacePositions.TOP_CENTER].colour == face.colour:
            count += 1
        if face.grid[FacePositions.MID_LEFT].colour == face.colour:
            count += 1
        if face.grid[FacePositions.MID_RIGHT].colour == face.colour:
            count += 1
        if face.grid[FacePositions.BOTTOM_CENTER].colour == face.colour:
            count += 1

        return count


if __name__ == "__main__":
    solver = RubixCubeSolver()
    print(solver.cube)
    solver.solve()
    print(solver.cube)
