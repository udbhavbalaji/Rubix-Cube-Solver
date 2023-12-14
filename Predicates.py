from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cube_init import RubixCube, Face, Piece, EdgePiece, CornerPiece

import numpy as np
from Constraints import FacePositions, Axes, PieceType
from errors import ArgumentTypeError


class CubePredicates:
    
    def is_valid_cube():
        pass
    
    def are_cubes_equal(cube1: RubixCube, cube2: RubixCube) -> bool:
        return cube1 == cube2
    
    pass


class FacePredicates:
    
    def is_correct_perspective(cube: RubixCube) -> bool:
        
        return (FacePredicates.is_blue_face_front(cube.current_perspective, cube.blue_face) and \
                FacePredicates.is_white_face_top(cube.current_perspective, cube.white_face) and \
                FacePredicates.is_orange_face_right(cube.current_perspective, cube.orange_face) and \
                FacePredicates.is_red_face_left(cube.current_perspective, cube.red_face) and \
                FacePredicates.is_green_face_back(cube.current_perspective, cube.green_face) and \
                FacePredicates.is_yellow_face_bottom(cube.current_perspective, cube.yellow_face))
    
    
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
    
    def are_faces_equal(face: Face, target_face: Face) -> bool:
        return face == target_face
    
    def are_num_edge_pieces_correct():
        
        pass


class GridPredicates:
    
    def are_grids_equal(grid_one: np.ndarray, grid_two: np.ndarray) -> bool:
        try:
            for position in FacePositions.POSITIONS:
                if grid_one[position] != grid_two[position]:
                    return False
            return True
        except ArgumentTypeError:
            raise ArgumentTypeError('Datatype Received is incorrect!')
    
    pass


class PiecePredicates:
    
    def are_pieces_equal(piece_one: Piece, piece_two: Piece) -> bool:
        return piece_one == piece_two
    
    def is_edge_piece(piece: Piece) -> bool:
        return piece.piece_type == PieceType.EDGE
    
    def is_corner_piece(piece: Piece) -> bool:
        return piece.piece_type == PieceType.CORNER
    
    def is_center_piece(piece: Piece) -> bool:
        return piece.piece_type == PieceType.CENTER
    
    def is_num_complements_corner_correct(piece):
        # return get_count_complements(piece) == 2
        pass