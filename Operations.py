import numpy as np
from Transformations import FaceTransformations, GridTransformations
from Constraints import Axes, FacePositions, Orientation


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
    
    def top_row_right(current_front):
        current = current_front
        
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

    def top_row_left(current_front):
        current = current_front
        
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
    
    def bottom_row_right(current_front):
        current = current_front
        
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
    
    def bottom_row_left(current_front):
        current = current_front
        
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
    