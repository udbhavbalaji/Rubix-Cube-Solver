from __future__ import annotations
from typing import TYPE_CHECKING
import numpy as np
from Constraints import Axes, FacePositions, Orientation
import icecream as ic

if TYPE_CHECKING:
    from cube_init import RubixCube, Face, Piece, CornerPiece, EdgePiece

class GridTransformations: 
    
    def update_piece_positions(face: Face, is_test: bool = False) -> None:
        if not is_test:
            top_left_piece = face.grid[FacePositions.TOP_LEFT]
            top_center_piece = face.grid[FacePositions.TOP_CENTER]
            top_right_piece = face.grid[FacePositions.TOP_RIGHT]
            mid_left_piece = face.grid[FacePositions.MID_LEFT]
            mid_center_piece = face.grid[FacePositions.MID_CENTER]
            mid_right_piece = face.grid[FacePositions.MID_RIGHT]
            bottom_left_piece = face.grid[FacePositions.BOTTOM_LEFT]
            bottom_center_piece = face.grid[FacePositions.BOTTOM_CENTER]
            bottom_right_piece = face.grid[FacePositions.BOTTOM_RIGHT]
            
            top_left_piece.face_position = FacePositions.TOP_LEFT
            top_center_piece.face_position = FacePositions.TOP_CENTER
            top_right_piece.face_position = FacePositions.TOP_RIGHT
            mid_left_piece.face_position = FacePositions.MID_LEFT
            mid_center_piece.face_position = FacePositions.MID_CENTER
            mid_right_piece.face_position = FacePositions.MID_RIGHT
            bottom_left_piece.face_position = FacePositions.BOTTOM_LEFT
            bottom_center_piece.face_position = FacePositions.BOTTOM_CENTER
            bottom_right_piece.face_position = FacePositions.BOTTOM_RIGHT
            
            top_left_piece.face = face
            top_center_piece.face = face
            top_right_piece.face = face
            mid_left_piece.face = face
            mid_center_piece.face = face
            mid_right_piece.face = face
            bottom_left_piece.face = face
            bottom_center_piece.face = face
            bottom_right_piece.face = face

    
    class ColumnUpAndDown:
        
        #* GRID TRANSFORMATIONS FOR COLUMN UP AND DOWN
        
        # UnitTest Added
        def transform_left_face(current_front: Face, is_rotate_down: bool = True, is_test: bool = False) -> np.ndarray:
            return GridTransformations.UpAndDown.transform_left_face(current_front, is_rotate_down=is_rotate_down, is_test=is_test)
        
        # UnitTest Added
        def transform_right_face(current_front: Face, is_rotate_down: bool = True, is_test: bool = False) -> np.ndarray:
            return GridTransformations.UpAndDown.transform_right_face(current_front, is_rotate_down=is_rotate_down, is_test=is_test)
        
        # UnitTest Added
        def transform_front_face(current_front: Face, is_rotate_down: bool = True, is_right_col: bool = True, is_test: bool = False) -> np.ndarray:
            front_face = current_front.copy()
            old_face = front_face.copy()
            
            if is_rotate_down:
                top_face = old_face.top.copy()
                
                if is_right_col:
                    top_col = top_face.grid[:,FacePositions.RIGHT_COL].copy()
                    front_face.grid[:,FacePositions.RIGHT_COL] = top_col
                else:
                    top_col = top_face.grid[:,FacePositions.LEFT_COL].copy()
                    front_face.grid[:,FacePositions.LEFT_COL] = top_col
                
            else:
                bottom_face = old_face.bottom.copy()
                
                if is_right_col:
                    bottom_col = bottom_face.grid[:,FacePositions.RIGHT_COL].copy()
                    front_face.grid[:,FacePositions.RIGHT_COL] = bottom_col
                else:
                    bottom_col = bottom_face.grid[:,FacePositions.LEFT_COL].copy()
                    front_face.grid[:,FacePositions.LEFT_COL] = bottom_col
                    
            GridTransformations.update_piece_positions(front_face, is_test=is_test)
                
            return front_face.grid
        
        def transform_top_face(current_front: Face, is_rotate_down: bool = True, is_right_col: bool = True, is_test: bool = False) -> np.ndarray:
            top_face = current_front.top.copy()
            old_face = top_face.copy()
            
            if is_rotate_down:
                back_face = old_face.back.copy()
                
                if is_right_col:
                    back_left_col = back_face.grid[:,FacePositions.LEFT_COL].copy()
                    top_face.grid[:,FacePositions.RIGHT_COL] = np.flip(back_left_col)
                else:
                    back_right_col = back_face.grid[:,FacePositions.RIGHT_COL].copy()
                    top_face.grid[:,FacePositions.LEFT_COL] = np.flip(back_right_col)
            else:
                front_face = old_face.front.copy()
                
                if is_right_col:
                    front_right_col = front_face.grid[:,FacePositions.RIGHT_COL].copy()
                    top_face.grid[:,FacePositions.RIGHT_COL] = front_right_col
                else:
                    front_left_col = front_face.grid[:,FacePositions.LEFT_COL].copy()
                    top_face.grid[:,FacePositions.LEFT_COL] = front_left_col
                    
            GridTransformations.update_piece_positions(top_face, is_test=is_test)

            return top_face.grid
        
        def transform_bottom_face(current_front: Face, is_rotate_down: bool = True, is_right_col: bool = True, is_test: bool = False) -> np.ndarray:
            bottom_face = current_front.bottom.copy()
            old_face = bottom_face.copy()
            
            if is_rotate_down:
                front_face = old_face.front.copy()
                
                if is_right_col:
                    front_right_col = front_face.grid[:,FacePositions.RIGHT_COL].copy()
                    bottom_face.grid[:,FacePositions.RIGHT_COL] = front_right_col
                else:
                    front_left_col = front_face.grid[:,FacePositions.LEFT_COL].copy()
                    bottom_face.grid[:,FacePositions.LEFT_COL] = front_left_col
            else:
                back_face = old_face.back.copy()
                
                if is_right_col:
                    back_left_col = back_face.grid[:,FacePositions.LEFT_COL].copy()
                    bottom_face.grid[:,FacePositions.RIGHT_COL] = np.flip(back_left_col)
                else:
                    back_right_col = back_face.grid[:,FacePositions.RIGHT_COL].copy()
                    bottom_face.grid[:,FacePositions.LEFT_COL] = np.flip(back_right_col)
                    
            GridTransformations.update_piece_positions(bottom_face, is_test=is_test)
            
            return bottom_face.grid
        
        # Added UnitTest
        def transform_back_face(current_front: Face, is_rotate_down: bool = True, is_right_col: bool = True, is_test: bool = False) -> np.ndarray:
            back_face = current_front.opposite.copy()
            old_face = back_face.copy()
            
            if is_rotate_down:
                bottom_face = old_face.bottom.copy()
                
                if is_right_col:
                    bottom_right_col = bottom_face.grid[:,FacePositions.RIGHT_COL].copy()
                    back_face.grid[:,FacePositions.LEFT_COL] = np.flip(bottom_right_col)
                else:
                    bottom_left_col = bottom_face.grid[:,FacePositions.LEFT_COL].copy()
                    back_face.grid[:,FacePositions.RIGHT_COL] = np.flip(bottom_left_col)
            else:
                top_face = old_face.top.copy()
                
                if is_right_col:
                    top_right_col = top_face.grid[:,FacePositions.RIGHT_COL].copy()
                    back_face.grid[:,FacePositions.LEFT_COL] = np.flip(top_right_col)
                else:
                    top_left_col = top_face.grid[:,FacePositions.LEFT_COL].copy()
                    back_face.grid[:,FacePositions.RIGHT_COL] = np.flip(top_left_col)
                    
            GridTransformations.update_piece_positions(back_face, is_test=is_test)
            
            return back_face.grid
        
    
    class RowRightAndLeft:
        
        def transform_top_face(current_front: Face, is_rotate_left: bool = True, is_test: bool = False) -> np.ndarray:
            ic.ic(current_front)
            return GridTransformations.LeftAndRight.transform_top_face(current_front, Axes.VERTICAL, is_left=is_rotate_left, is_test=is_test)
        
        def transform_bottom_face(current_front: Face, is_rotate_left: bool = True, is_test: bool = False) -> np.ndarray:
            ic.ic(current_front)
            return GridTransformations.LeftAndRight.transform_bottom_face(current_front, Axes.VERTICAL, is_left=is_rotate_left, is_test=is_test)
        
        def transform_front_back_left_right_faces(current_front: Face, orientation: str, is_rotate_left: bool = True, is_top_row: bool = True, is_test: bool = False) -> np.ndarray:
            if orientation == Orientation.FRONT:
                face = current_front.copy()
            elif orientation == Orientation.BACK:
                face = current_front.opposite.copy()
            elif orientation == Orientation.LEFT:
                face = current_front.left.copy()
            elif orientation == Orientation.RIGHT:
                face = current_front.right.copy()
            else:
                raise Exception('Don\'t have valid Orientation! Exiting Program')
            
            if is_rotate_left:
                right_face = face.right.copy()
                
                if is_top_row:
                    right_top_row = right_face.grid[FacePositions.TOP_ROW].copy()
                    face.grid[FacePositions.TOP_ROW] = right_top_row
                else:
                    right_bottom_row = right_face.grid[FacePositions.BOTTOM_ROW].copy()
                    face.grid[FacePositions.BOTTOM_ROW] = right_bottom_row
            else:
                left_face = face.left.copy()
                
                if is_top_row:
                    left_top_row = left_face.grid[FacePositions.TOP_ROW].copy()
                    face.grid[FacePositions.TOP_ROW] = left_top_row
                else:
                    left_bottom_row = left_face.grid[FacePositions.BOTTOM_ROW].copy()
                    face.grid[FacePositions.BOTTOM_ROW] = left_bottom_row
                    
            GridTransformations.update_piece_positions(face, is_test=is_test)
            
            return face.grid
        
    class UpAndDown:
        
        # * GRID TRANSFORMATIONS FOR UP & DOWN ROTATIONS
        
        # UnitTest Added
        def transform_left_face(current_front: Face, is_rotate_down: bool = True, is_test: bool = False) -> np.ndarray:
            left_face = current_front.left.copy()
            old_face = left_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if is_rotate_down:
                left_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                left_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                left_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                left_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
            else:
                left_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                left_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                left_face.grid[FacePositions.TOP_ROW] = old_right_col
                left_face.grid[FacePositions.BOTTOM_ROW] = old_left_col
                
            GridTransformations.update_piece_positions(left_face, is_test=is_test)
                
            return left_face.grid
        
        # UnitTest Added
        def transform_right_face(current_front: Face, is_rotate_down: bool = True, is_test: bool = False) -> np.ndarray:
            right_face = current_front.right.copy()
            old_face = right_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if is_rotate_down:
                right_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                right_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                right_face.grid[FacePositions.TOP_ROW] = old_right_col
                right_face.grid[FacePositions.BOTTOM_ROW] = old_left_col
            else:
                right_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                right_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                right_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                right_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
                
            GridTransformations.update_piece_positions(right_face, is_test=is_test)
                
            return right_face.grid
        
        # UnitTest Added
        def transform_back_face(current_front: Face, is_rotate_down: bool = True, is_test: bool = False) -> np.ndarray:
            back_face = current_front.opposite.copy()
            old_face = back_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if is_rotate_down:
                back_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                back_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                back_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                back_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
            else:
                back_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                back_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                back_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                back_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(back_face, is_test=is_test)
            
            return back_face.grid
        
        # UnitTest Added
        def transform_top_face(current_front: Face, is_rotate_down: bool = True, is_test: bool = False) -> np.ndarray:
            top_face = current_front.top.copy()
            old_face = top_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if not is_rotate_down:
                top_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                top_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                top_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(top_face, is_test=is_test)
            
            return top_face.grid
        
        # UnitTest Added
        def transform_bottom_face(current_front: Face, is_rotate_down: bool = True, is_test: bool = False) -> np.ndarray:
            bottom_face = current_front.bottom.copy()
            old_face = bottom_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if is_rotate_down:
                bottom_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                bottom_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(bottom_face, is_test=is_test)
            
            return bottom_face.grid
        
    
    class LeftAndRight:
        
        # * GRID TRANSFORMATIONS FOR LEFT & RIGHT ROTATIONS
        
        # UnitTest Added
        def transform_left_face(current_front: Face, axis: str, is_left: bool = True, is_test: bool = False) -> np.ndarray:
            left_face = current_front.left.copy()
            old_face = left_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.HORIZONTAL:
                if is_left:
                    left_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                    left_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                    left_face.grid[FacePositions.TOP_ROW] = (old_right_col)
                    left_face.grid[FacePositions.BOTTOM_ROW] = (old_left_col)
                else:
                    left_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                    left_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                    left_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                    left_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
                    
            GridTransformations.update_piece_positions(left_face, is_test=is_test)
            
            return left_face.grid
        
        # UnitTest Added
        def transform_right_face(current_front: Face, axis: str, is_left: bool = True, is_test: bool = False) -> np.ndarray:
            right_face = current_front.right.copy()
            old_face = right_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.HORIZONTAL:
                if is_left:
                    right_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                    right_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                    right_face.grid[FacePositions.TOP_ROW] = (old_right_col)
                    right_face.grid[FacePositions.BOTTOM_ROW] = (old_left_col)
                else:
                    right_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                    right_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                    right_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                    right_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
                    
            GridTransformations.update_piece_positions(right_face, is_test=is_test)
            
            return right_face.grid
        
        # UnitTest Added
        def transform_front_face(current_front: Face, axis: str, is_left: bool = True, is_test: bool = False) -> np.ndarray:
            front_face = current_front.copy()
            old_face = front_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.HORIZONTAL:
                if is_left:
                    front_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                    front_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                    front_face.grid[FacePositions.TOP_ROW] = (old_right_col)
                    front_face.grid[FacePositions.BOTTOM_ROW] = (old_left_col)
                else:
                    front_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                    front_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                    front_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                    front_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
                    
            GridTransformations.update_piece_positions(front_face, is_test=is_test)
            
            return front_face.grid
        
        # UnitTest Added
        def transform_back_face(current_front: Face, axis: str, is_left: bool = True, is_test: bool = False) -> np.ndarray:
            back_face = current_front.opposite.copy()
            old_face = back_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.HORIZONTAL:
                if is_left:
                    back_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                    back_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                    back_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                    back_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
                else:
                    back_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                    back_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                    back_face.grid[FacePositions.TOP_ROW] = (old_right_col)
                    back_face.grid[FacePositions.BOTTOM_ROW] = (old_left_col)
                    
            GridTransformations.update_piece_positions(back_face, is_test=is_test)

            return back_face.grid
        
        # UnitTest Added
        def transform_top_face(current_front: Face, axis: str, is_left: bool = True, is_test: bool = False) -> np.ndarray:
            top_face = current_front.top.copy()
            old_face = top_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.VERTICAL:
                if is_left:
                    top_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                    top_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                    top_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                    top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
                else:
                    top_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                    top_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                    top_face.grid[FacePositions.TOP_ROW] = (old_right_col)
                    top_face.grid[FacePositions.BOTTOM_ROW] = (old_left_col)
            else:
                if is_left:
                    top_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                    top_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                    top_face.grid[FacePositions.TOP_ROW] = (old_right_col)
                    top_face.grid[FacePositions.BOTTOM_ROW] = (old_left_col)
                else:
                    top_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                    top_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                    top_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                    top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
                    
            GridTransformations.update_piece_positions(top_face, is_test=is_test)
            
            return top_face.grid
        
        # UnitTest Added
        def transform_bottom_face(current_front: Face, axis: str, is_left: bool = True, is_test: bool = False) -> np.ndarray:
            bottom_face = current_front.bottom.copy()
            old_face = bottom_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if is_left:
                bottom_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_bottom_row)
                bottom_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_top_row)
                bottom_face.grid[FacePositions.TOP_ROW] = (old_right_col)
                bottom_face.grid[FacePositions.BOTTOM_ROW] = (old_left_col)
            else:
                bottom_face.grid[:,FacePositions.RIGHT_COL] = (old_top_row)
                bottom_face.grid[:,FacePositions.LEFT_COL] = (old_bottom_row)
                bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_left_col)
                bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_right_col)
                
            GridTransformations.update_piece_positions(bottom_face, is_test=is_test)
                    
            return bottom_face.grid
    
        
    class Inversion:
        
        # * GRID TRANSFORMATIONS FOR CUBE INVERSION
        
        # UnitTest Added
        def transform_left_face(current_front: Face, axis: str, is_test: bool = False) -> np.ndarray:
            left_face = current_front.left.copy()
            old_face = left_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.HORIZONTAL:
                left_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                left_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                left_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                left_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(left_face, is_test=is_test)
            
            return left_face.grid
        
        # UnitTest Added
        def transform_right_face(current_front: Face, axis: str, is_test: bool = False) -> np.ndarray:
            right_face = current_front.right.copy()
            old_face = right_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.HORIZONTAL:
                right_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                right_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                right_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                right_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(right_face, is_test=is_test)
        
            return right_face.grid
        
        # UnitTest Added
        def transform_top_face(current_front: Face, axis: str, is_test: bool = False) -> np.ndarray:
            top_face = current_front.top.copy()
            old_face = top_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.VERTICAL:
                top_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                top_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                top_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
            else:
                top_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                top_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                top_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                top_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(top_face, is_test=is_test)
                
            return top_face.grid
        
        # UnitTest Added 
        def transform_bottom_face(current_front: Face, axis: str, is_test: bool = False) -> np.ndarray:
            bottom_face = current_front.bottom.copy()
            old_face = bottom_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.VERTICAL:
                bottom_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                bottom_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
            else:
                bottom_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                bottom_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                bottom_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                bottom_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(bottom_face, is_test=is_test)
            
            return bottom_face.grid
        
        # UnitTest Added
        def transform_front_face(current_front: Face, axis: str, is_test: bool = False) -> np.ndarray:
            front_face = current_front.copy()
            old_face = front_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.HORIZONTAL:
                front_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                front_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                front_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                front_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(front_face, is_test=is_test)
            
            return front_face.grid
        
        # UnitTest Added
        def transform_back_face(current_front: Face, axis: str, is_test: bool = False) -> np.ndarray:
            back_face = current_front.opposite.copy()
            old_face = back_face.copy()
            
            old_top_row = old_face.grid[FacePositions.TOP_ROW].copy()
            old_bottom_row = old_face.grid[FacePositions.BOTTOM_ROW].copy()
            old_left_col = old_face.grid[:,FacePositions.LEFT_COL].copy()
            old_right_col = old_face.grid[:,FacePositions.RIGHT_COL].copy()
            
            if axis == Axes.HORIZONTAL:
                back_face.grid[:,FacePositions.RIGHT_COL] = np.flip(old_left_col)
                back_face.grid[:,FacePositions.LEFT_COL] = np.flip(old_right_col)
                back_face.grid[FacePositions.TOP_ROW] = np.flip(old_bottom_row)
                back_face.grid[FacePositions.BOTTOM_ROW] = np.flip(old_top_row)
                
            GridTransformations.update_piece_positions(back_face, is_test=is_test)
                
            return back_face.grid
        
        
class FaceTransformations:
    
    class UpAndDown:
        
        # * FACE TRANSFORMATIONS FOR UP & DOWN ROTATIONS
    
        def transform_right_face(current_front: Face, is_rotate_down: bool = True) -> Face:
            right_face = current_front.right.copy()
            old_face = right_face.copy()
            
            if is_rotate_down:
                right_face.left = old_face.top
                right_face.right = old_face.bottom
                
                right_face.bottom = old_face.left
                right_face.top = old_face.right
            else:
                right_face.right = old_face.top
                right_face.left = old_face.bottom
                
                right_face.top = old_face.left
                right_face.bottom = old_face.right
            
            return right_face
        
        def transform_left_face(current_front: Face, is_rotate_down: bool = True) -> Face:
            left_face = current_front.left.copy()
            old_face = left_face.copy()
            
            if is_rotate_down:
                left_face.right = old_face.top
                left_face.left = old_face.bottom
                
                left_face.top = old_face.left
                left_face.bottom = old_face.right
            else:
                left_face.top = old_face.right
                left_face.bottom = old_face.left
                
                left_face.left = old_face.top
                left_face.right = old_face.bottom
            
            return left_face
        
        def transform_front_back_faces(current_front: Face, is_front: bool = True, is_rotate_down: bool = True) -> Face:
            if is_front:
                face = current_front.copy()
            else:
                face = current_front.opposite.copy()
                
            old_face = face.copy()
            
            if is_rotate_down:
                face.front = old_face.top
                face.back = old_face.bottom
                
                if not is_front:
                    face.right = old_face.left
                    face.left = old_face.right
                
            else:
                face.back = old_face.top
                face.front = old_face.bottom
                
                if not is_front:
                    face.right = old_face.left
                    face.left = old_face.right
                
            face.top = None
            face.bottom = None
            
            face.is_side_face=False
            
            return face
        
        def transform_top_bottom_faces(current_front: Face, is_top: bool = True, is_rotate_down: bool = True) -> Face:
            if is_top:
                face = current_front.top.copy()
            else:
                face = current_front.bottom.copy()
                
            old_face = face.copy()
            
            if is_rotate_down:
                face.top = old_face.back
                face.bottom = old_face.front
                
                if not is_top:
                    face.left = old_face.right
                    face.right = old_face.left
            else:
                face.top = old_face.front
                face.bottom = old_face.back
                
                if is_top:
                    face.right = old_face.left
                    face.left = old_face.right
            
            face.front = None
            face.back = None
            
            face.is_side_face = True
            
            return face
    
        
    class LeftAndRight:
        
        # * FACE TRANSFORMATIONS FOR LEFT & RIGHT ROTATIONS
        
        def transform_right_face(current_front: Face, is_left: bool = False) -> Face:
            right_face = current_front.right.copy()
            old_face = right_face.copy()
            
            if is_left:
                right_face.right = old_face.bottom
                right_face.left = old_face.top
            else:
                right_face.right = old_face.top
                right_face.left = old_face.bottom
                
            right_face.front = old_face.left
            right_face.back = old_face.right
                
            right_face.top = None
            right_face.bottom = None
            
            right_face.is_side_face = False
                
            return right_face
        
        def transform_left_face(current_front: Face, is_left: bool = False) -> Face:
            left_face = current_front.left.copy()
            old_face = left_face.copy()
            
            if is_left:
                left_face.left = old_face.top
                left_face.right = old_face.bottom
            else:
                left_face.right = old_face.top
                left_face.left = old_face.bottom
                
            left_face.front = old_face.right
            left_face.back = old_face.left
                
            left_face.top = None
            left_face.bottom = None
            
            left_face.is_side_face = False
                
            return left_face
        
        def transform_front_back_faces(current_front: Face, is_front: bool = True, is_left: bool = True) -> Face:
            if is_front:
                face = current_front.copy()
            else:
                face = current_front.opposite.copy()
                
            old_face = face.copy()
            
            if is_left:
                if is_front:
                    face.left = old_face.top
                    face.right = old_face.bottom
                    
                    face.top = old_face.right
                    face.bottom = old_face.left
                else:
                    face.top = old_face.left
                    face.bottom = old_face.right
                    
                    face.left = old_face.bottom
                    face.right = old_face.top
            else:
                if is_front:
                    face.right = old_face.top
                    face.left = old_face.bottom
                    
                    face.top = old_face.left
                    face.bottom = old_face.right
                else:
                    face.left = old_face.top
                    face.right = old_face.bottom
                    
                    face.top = old_face.right
                    face.bottom = old_face.left
                    
            return face
        
        def transform_top_bottom_faces(current_front: Face, axis: str, is_top: bool = True, is_left: bool = True) -> Face:
            if is_top:
                face = current_front.top.copy()
            else:
                face = current_front.bottom.copy()
                
            old_face = face.copy()
            
            if axis == Axes.VERTICAL:
                if is_left:
                    face.left = old_face.front
                    face.right = old_face.back
                    
                    face.front = old_face.right
                    face.back = old_face.left
                else:
                    face.front = old_face.left
                    face.back = old_face.right
                    
                    face.left = old_face.back
                    face.right = old_face.front
            else:
                if is_left:
                    if not is_top:
                        face.right = old_face.back
                        face.left = old_face.front
                    else:
                        face.right = old_face.front
                        face.left = old_face.back
                    
                    face.top = old_face.right
                    face.bottom = old_face.left
                else:
                    if not is_top:
                        face.right = old_face.front
                        face.left = old_face.back
                    else:
                        face.right = old_face.back
                        face.left = old_face.front
                    
                    face.top = old_face.left
                    face.bottom = old_face.right
                    
                face.front = None
                face.back = None
                
                face.is_side_face = True
            
            return face
        
        
    class Inversion:
        
        # * FACE TRANSFORMATIONS FOR CUBE INVERSION
        
        def transform_top_bottom_faces(current_front: Face, axis: str, is_top: bool = True) -> Face:
            if is_top:
                face = current_front.top.copy()
            else:
                face = current_front.bottom.copy()
                
            old_face = face.copy()
            
            if axis == Axes.VERTICAL:
                face.back = old_face.front
                face.front = old_face.back
                
                face.left = old_face.right
                face.right = old_face.left
            else:
                face.front = old_face.back
                face.back = old_face.front
            
            return face
        
        def transform_front_back_faces(current_front: Face, is_front: bool = True) -> Face:
            if is_front:
                face = current_front.copy()
            else:
                face = current_front.opposite.copy()
                
            old_face = face.copy()
            
            face.left = old_face.right
            face.right = old_face.left
                
            face.bottom = old_face.top
            face.top = old_face.bottom
            
            return face
        
        def transform_right_left_faces(current_front: Face, is_left_face: bool = True) -> Face:
            if is_left_face:
                face = current_front.left.copy()
            else:
                face = current_front.right.copy()
            old_face = face.copy()
            
            face.left = old_face.right
            face.right = old_face.left
            
            face.top = old_face.bottom
            face.bottom = old_face.top
            
            return face
            