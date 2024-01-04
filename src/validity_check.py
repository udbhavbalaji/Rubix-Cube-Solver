from __future__ import annotations
from typing import TYPE_CHECKING
from predicate import FacePredicate, PiecePredicate
from constants import Colours, FacePositions, PossibleRotations
import icecream as ic

if TYPE_CHECKING:
    from cube_init_m import RubixCube


class CubeValidity:
    def is_cube_valid(cube: RubixCube) -> bool:
        if not CubeValidity.are_opposite_faces_correct(cube):
            return False
        if not CubeValidity.is_connection_integrity_maintained(cube):
            return False
        if not CubeValidity.is_num_pieces_colour_correct(cube):
            return False
        if not CubeValidity.are_edge_piece_complements_correct(cube):
            return False
        if not CubeValidity.are_corner_piece_complements_correct(cube):
            return False
        # Add more conditions to ensure structure and integrity of cube is maintained
        return True

    def are_opposite_faces_correct(cube: RubixCube) -> bool:
        cube_copy = cube.copy()
        cube_copy.reset_perspective()

        if not FacePredicate.are_faces_equal(
            cube.current_perspective.opposite.opposite, cube.current_perspective
        ) and not FacePredicate.are_faces_equal(
            cube.current_perspective.opposite, cube.current_perspective.opposite
        ):
            return False

        if not FacePredicate.are_faces_equal(
            cube.current_perspective.left.opposite, cube.current_perspective.right
        ) and not FacePredicate.are_faces_equal(
            cube.current_perspective.right.opposite, cube.current_perspective.left
        ):
            return False

        if not FacePredicate.are_faces_equal(
            cube.current_perspective.top.opposite, cube.current_perspective.bottom
        ) and not FacePredicate.are_faces_equal(
            cube.current_perspective.bottom.opposite, cube.current_perspective.top
        ):
            return False
        return True

    def is_connection_integrity_maintained(cube: RubixCube) -> bool:
        cube_copy = cube.copy()
        cube_copy.reset_perspective()
        # Checking connection between front and right faces
        if not FacePredicate.are_faces_equal(
            cube.right, cube.orange_face
        ) and not FacePredicate.are_faces_equal(cube.right.left, cube.blue_face):
            return False
        # Checking connection between front and left faces
        if not FacePredicate.are_faces_equal(
            cube.left, cube.red_face
        ) and not FacePredicate.are_faces_equal(cube.left.right, cube.blue_face):
            return False
        # Checking connection between front and top faces
        if not FacePredicate.are_faces_equal(
            cube.top, cube.white_face
        ) and not FacePredicate.are_faces_equal(cube.top.front, cube.blue_face):
            return False
        # Checking the connection between front and bottom faces
        if not FacePredicate.are_faces_equal(
            cube.bottom, cube.yellow_face
        ) and not FacePredicate.are_faces_equal(cube.bottom.front, cube.blue_face):
            return False
        # Checking connection between left and back faces
        if not FacePredicate.are_faces_equal(
            cube.left.left, cube.green_face
        ) and not FacePredicate.are_faces_equal(cube.opposite.right, cube.red_face):
            return False
        # Checking connection between right and back faces
        if not FacePredicate.are_faces_equal(
            cube.right.right, cube.green_face
        ) and not FacePredicate.are_faces_equal(cube.opposite.left, cube.orange_face):
            return False
        # Checking connection between back and top faces
        if not FacePredicate.are_faces_equal(
            cube.opposite.top, cube.white_face
        ) and not FacePredicate.are_faces_equal(cube.top.back, cube.green_face):
            return False
        # Checking connection between back and bottom faces
        if not FacePredicate.are_faces_equal(
            cube.opposite.bottom, cube.yellow_face
        ) and not FacePredicate.are_faces_equal(cube.bottom.back, cube.green_face):
            return False
        # Checking connection between left and top faces
        if not FacePredicate.are_faces_equal(
            cube.left.top, cube.white_face
        ) and not FacePredicate.are_faces_equal(cube.top.left, cube.red_face):
            return False
        # Checking connection between left and bottom faces
        if not FacePredicate.are_faces_equal(
            cube.left.bottom, cube.yellow_face
        ) and not FacePredicate.are_faces_equal(cube.bottom.left, cube.red_face):
            return False
        # Checking connection between right and top faces
        if not FacePredicate.are_faces_equal(
            cube.right.top, cube.white_face
        ) and not FacePredicate.are_faces_equal(cube.top.right, cube.orange_face):
            return False
        # Checking connection between right and bottom faces
        if not FacePredicate.are_faces_equal(
            cube.right.bottom, cube.yellow_face
        ) and not FacePredicate.are_faces_equal(cube.bottom.right, cube.orange_face):
            return False

        return True

    def is_num_pieces_colour_correct(cube: RubixCube) -> bool:
        piece_freq = {x: 0 for x in list(Colours)}
        for face in cube.faces:
            for row in face.grid:
                for piece in row:
                    piece_freq[piece.colour] += 1

        for _, value in piece_freq.items():
            if value != 9:
                return False

        return True

    def are_edge_piece_complements_correct(cube: RubixCube) -> bool:
        for face in cube.faces:
            if not face.is_side_face:
                continue
            # Check each of the side faces to make sure that the complements are correct and maintained
            top_edge_piece = face.grid[FacePositions.TOP_CENTER]
            top_edge_complement = face.top.grid[FacePositions.BOTTOM_CENTER]

            left_edge_piece = face.grid[FacePositions.MID_LEFT]
            left_edge_complement = face.left.grid[FacePositions.MID_RIGHT]

            right_edge_piece = face.grid[FacePositions.MID_RIGHT]
            right_edge_complement = face.right.grid[FacePositions.MID_LEFT]

            bottom_edge_piece = face.grid[FacePositions.BOTTOM_CENTER]
            bottom_edge_complement = face.bottom.grid[FacePositions.TOP_CENTER]

            if (
                top_edge_piece.complement != top_edge_complement
                or top_edge_complement.complement != top_edge_piece
            ):
                ic.ic()
                return False
            if (
                left_edge_piece.complement != left_edge_complement
                or left_edge_complement.complement != left_edge_piece
            ):
                ic.ic()
                return False
            if (
                right_edge_piece.complement != right_edge_complement
                or right_edge_complement.complement != right_edge_piece
            ):
                ic.ic()
                return False
            if (
                bottom_edge_piece.complement != bottom_edge_complement
                or bottom_edge_complement.complement != bottom_edge_piece
            ):
                ic.ic()
                return False

            cube.rotate(PossibleRotations.ROTATE_RIGHT_VERTICALLY, internal_req=True)

        return True

    def are_corner_piece_complements_correct(cube: RubixCube) -> bool:
        for face in cube.faces:
            if not face.is_side_face:
                continue

            top_left_piece = face.grid[FacePositions.TOP_LEFT]
            top_left_complement_top = face.top.grid[FacePositions.BOTTOM_LEFT]
            top_left_complement_left = face.left.grid[FacePositions.TOP_RIGHT]

            top_right_piece = face.grid[FacePositions.TOP_RIGHT]
            top_right_complement_top = face.top.grid[FacePositions.BOTTOM_RIGHT]
            top_right_complement_right = face.right.grid[FacePositions.TOP_LEFT]

            bottom_left_piece = face.grid[FacePositions.BOTTOM_LEFT]
            bottom_left_complement_bottom = face.bottom.grid[FacePositions.TOP_LEFT]
            bottom_left_complement_left = face.left.grid[FacePositions.BOTTOM_RIGHT]

            bottom_right_piece = face.grid[FacePositions.BOTTOM_RIGHT]
            bottom_right_complement_bottom = face.bottom.grid[FacePositions.TOP_RIGHT]
            bottom_right_complement_right = face.right.grid[FacePositions.BOTTOM_LEFT]

            if (
                top_left_piece.complements
                != set([top_left_complement_top, top_left_complement_left])
                or top_left_complement_top.complements
                != set([top_left_piece, top_left_complement_left])
                or top_left_complement_left.complements
                != set([top_left_piece, top_left_complement_top])
            ):
                ic.ic()
                return False

            if (
                top_right_piece.complements
                != set([top_right_complement_top, top_right_complement_right])
                or top_right_complement_top.complements
                != set([top_right_piece, top_right_complement_right])
                or top_right_complement_right.complements
                != set([top_right_piece, top_right_complement_top])
            ):
                ic.ic()
                ic.ic(face.colour)
                ic.ic(top_right_piece.colour)
                ic.ic(top_right_complement_top.colour)
                ic.ic(top_right_complement_right.colour)
                ic.ic(top_right_piece.complements)
                ic.ic(top_right_complement_top.complements)
                ic.ic(top_right_complement_right.complements)

                return False

            if (
                bottom_left_piece.complements
                != set([bottom_left_complement_bottom, bottom_left_complement_left])
                or bottom_left_complement_bottom.complements
                != set([bottom_left_piece, bottom_left_complement_left])
                or bottom_left_complement_left.complements
                != set([bottom_left_piece, bottom_left_complement_bottom])
            ):
                ic.ic()
                return False

            if (
                bottom_right_piece.complements
                != set([bottom_right_complement_bottom, bottom_right_complement_right])
                or bottom_right_complement_bottom.complements
                != set([bottom_right_piece, bottom_right_complement_right])
                or bottom_right_complement_right.complements
                != set([bottom_right_piece, bottom_right_complement_bottom])
            ):
                ic.ic()
                return False

            cube.rotate(PossibleRotations.ROTATE_RIGHT_VERTICALLY, internal_req=True)

        return True
