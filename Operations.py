import numpy as np
from Transformations import FaceTransformations, GridTransformations
from Constraints import Axes, FacePositions


class Shifts:
    
    # Defining the methods for each operation
    def right_column_up(current_front):
        current = current_front
        
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
    
    
    def left_column_up(current_front):
        current = current_front
        
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
    
    
    def right_column_down(current_front):
        current = current_front
        
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
    
    
    def left_column_down(current_front):
        current = current_front
        
        ## Getting new Left Face Grid
        new_left_grid = GridTransformations.ColumnUpAndDown.transform_left_face(current, is_rotate_down=True)
        
        ## Getting new Front & Back Grids
        new_front_grid = GridTransformations.ColumnUpAndDown.transform_front_face(current, is_rotate_down=True, is_right_col=False)
        new_back_grid = GridTransformations.ColumnUpAndDown.transform_back_face(current, is_rotate_down=True, is_right_col=False)
        
        ## Getting new Top & Bottom Grids
        new_top_grid = GridTransformations.ColumnUpAndDown.transform_top_face(current, is_rotate_down=True, is_right_col=False)
        new_bottom_grid = GridTransformations.ColumnUpAndDown.transform_bottom_face(current, is_rotate_down=True, is_right_col=False)
        
        ## Updating grids for all faces where there was a change
        current.grid = new_front_grid
        current.left.grid = new_left_grid
        current.opposite.grid = new_back_grid
        current.top.grid = new_top_grid
        current.bottom.grid = new_bottom_grid
    
    
    def top_row_right():
        pass
    
    
    def top_row_left():
        pass
    
    
    def bottom_row_right():
        pass
    
    
    def bottom_row_left():
        pass
    
        
    # Defining the possible operations
    # RIGHT_COLUMN_UP = right_column_up()
    # LEFT_COLUMN_UP = left_column_up()
    # RIGHT_COLUMN_DOWN = right_column_down()
    # LEFT_COLUMN_DOWN = left_column_down()
    
    # TOP_ROW_RIGHT = top_row_right()
    # TOP_ROW_LEFT = top_row_left()
    # BOTTOM_ROW_RIGHT = bottom_row_right()
    # BOTTOM_ROW_LEFT = bottom_row_left()
    
    pass