import numpy as np
from Constraints import Axes, FacePositions

class GridTransformations: 
    
    class UpAndDown:
        
        # * GRID TRANSFORMATIONS FOR UP & DOWN ROTATIONS
        
        def transform_left_face(current_front, is_rotate_down=True):
            left_face = current_front.left
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
                
            return left_face.grid
        
        def transform_right_face(current_front, is_rotate_down):
            right_face = current_front.right
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
                
            return right_face.grid
        
        def transform_back_face(current_front, is_rotate_down=True):
            back_face = current_front.opposite
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
            
            return back_face.grid
        
        def transform_top_face(current_front, is_rotate_down=True):
            top_face = current_front.top
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
            
            return top_face.grid
        
        def transform_bottom_face(current_front, is_rotate_down=True):
            bottom_face = current_front.bottom
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
                
            
            return bottom_face.grid
        
    
    class LeftAndRight:
        
        # * GRID TRANSFORMATIONS FOR LEFT & RIGHT ROTATIONS
        
        def transform_left_face(current_front, axis, is_left=True):
            left_face = current_front.left
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
            
            return left_face.grid
        
        def transform_right_face(current_front, axis, is_left=True):
            right_face = current_front.right
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
            
            return right_face.grid
        
        def transform_front_face(current_front, axis, is_left=True):
            front_face = current_front
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
            
            return front_face.grid
        
        def transform_back_face(current_front, axis, is_left=True):
            back_face = current_front.opposite
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

            return back_face.grid
        
        def transform_top_face(current_front, axis, is_left=True):
            top_face = current_front.top
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
            
            return top_face.grid
        
        def transform_bottom_face(current_front, axis, is_left=True):
            bottom_face = current_front.bottom
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
                    
            return bottom_face.grid
    
        
    class Inversion:
        
        # * GRID TRANSFORMATIONS FOR CUBE INVERSION
        
        def transform_left_face(current_front, axis):
            left_face = current_front.left
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
            
            return left_face.grid
        
        def transform_right_face(current_front, axis):
            right_face = current_front.right
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
        
            return right_face.grid
        
        def transform_top_face(current_front, axis):
            top_face = current_front.top
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
                
            return top_face.grid
                
        def transform_bottom_face(current_front, axis):
            bottom_face = current_front.bottom
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
            
            return bottom_face.grid
        
        def transform_front_face(current_front, axis):
            front_face = current_front
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
            
            return front_face.grid
        
        def transform_back_face(current_front, axis):
            back_face = current_front.opposite
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
                
            return back_face.grid
        
        
class FaceTransformations:
    
    class UpAndDown:
        
        # * FACE TRANSFORMATIONS FOR UP & DOWN ROTATIONS
    
        def transform_right_face(current_front, is_rotate_down=True):
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
        
        def transform_left_face(current_front, is_rotate_down=True):
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
        
        def transform_front_back_faces(current_front, is_front=True, is_rotate_down=True):
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
        
        def transform_top_bottom_faces(current_front, is_top=True, is_rotate_down=True):
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
        
        def transform_right_face(current_front, is_left=False):
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
        
        def transform_left_face(current_front, is_left=False):
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
        
        def transform_front_back_faces(current_front, is_front=True, is_left=True):
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
        
        def transform_top_bottom_faces(current_front, axis, is_top=True, is_left=True):
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
                # TODO: Have to add another if statement to handle bottom face (not same updates as for top face)
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
        
        def transform_top_bottom_faces(current_front, axis, is_top=True):
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
        
        def transform_front_back_faces(current_front, is_front=True):
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
        
        def transform_right_left_faces(current_front, is_left_face=True):
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
            