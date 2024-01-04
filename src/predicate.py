from __future__ import annotations
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from cube_init_m import Face, RubixCube, Piece, CornerPiece, EdgePiece


class PiecePredicate:
    def are_pieces_equal(
        piece1: Union[Piece, CornerPiece, EdgePiece],
        piece2: Union[Piece, CornerPiece, EdgePiece],
    ) -> bool:
        return piece1 == piece2


class FacePredicate:
    def are_faces_equal(face1: Face, face2: Face):
        return face1 == face2

    pass


class CubePredicate:
    def is_correct_perspective(cube: RubixCube) -> bool:
        return (
            CubePredicate.is_blue_face_front(cube.current_perspective, cube.blue_face)
            and CubePredicate.is_white_face_top(
                cube.current_perspective, cube.white_face
            )
            and CubePredicate.is_orange_face_right(
                cube.current_perspective, cube.orange_face
            )
            and CubePredicate.is_red_face_left(cube.current_perspective, cube.red_face)
            and CubePredicate.is_green_face_back(
                cube.current_perspective, cube.green_face
            )
            and CubePredicate.is_yellow_face_bottom(
                cube.current_perspective, cube.yellow_face
            )
        )

    def is_blue_face_front(current_front: Face, blue_face: Face) -> bool:
        return current_front == blue_face

    def is_white_face_top(current_front: Face, white_face: Face) -> bool:
        return current_front.top == white_face

    def is_orange_face_right(current_front: Face, orange_face: Face) -> bool:
        return current_front.right == orange_face

    def is_red_face_left(current_front: Face, red_face: Face) -> bool:
        return current_front.left == red_face

    def is_green_face_back(current_front: Face, green_face: Face) -> bool:
        return current_front.opposite == green_face

    def is_yellow_face_bottom(current_front: Face, yellow_face: Face) -> bool:
        return current_front.bottom == yellow_face
