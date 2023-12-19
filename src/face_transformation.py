from __future__ import annotations
from typing import Protocol, TYPE_CHECKING
# from cube_init_m import Face

from constants import Orientation

if TYPE_CHECKING:
    from cube_init_m import Face

class FaceTransformationProtocol(Protocol):
    # YOUR CODE HERE
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        ...
        
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        ...
        
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        ...
        
    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        ...
        
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        ...
        
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        ...


class RotateUp:
    
    # YOUR CODE HERE
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.copy()
        old_face = face.copy()
        
        face.back = old_face.top
        face.front = old_face.bottom
                    
        face.top = None
        face.bottom = None
        
        # face.is_side_face=False
        face.orientation_to_cube = Orientation.TOP
        
        return face
        
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.opposite.copy()
        old_face = face.copy()
        
        face.back = old_face.top
        face.front = old_face.bottom
        
        face.right = old_face.left
        face.left = old_face.right
            
        face.top = None
        face.bottom = None
        
        # face.is_side_face=False
        face.orientation_to_cube = Orientation.BOTTOM
        
        return face
        
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        left_face = current_front.left.copy()
        old_face = left_face.copy()
        
        left_face.top = old_face.right
        left_face.bottom = old_face.left
        
        left_face.left = old_face.top
        left_face.right = old_face.bottom
        
        return left_face
        
    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        right_face = current_front.right.copy()
        old_face = right_face.copy()
        
        right_face.right = old_face.top
        right_face.left = old_face.bottom
        
        right_face.top = old_face.left
        right_face.bottom = old_face.right
        
        return right_face
        
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.top.copy()
        old_face = face.copy()
        
        face.top = old_face.front
        face.bottom = old_face.back
            
        face.right = old_face.left
        face.left = old_face.right
        
        face.front = None
        face.back = None
        
        # face.is_side_face = True
        face.orientation_to_cube = Orientation.BACK
        
        return face
        
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.bottom.copy()
        old_face = face.copy()
        
        face.top = old_face.front
        face.bottom = old_face.back
                
        face.front = None
        face.back = None
        
        # face.is_side_face = True
        face.orientation_to_cube = Orientation.FRONT
        
        return face
    
    
class RotateDown:
    
    # YOUR CODE HERE
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.copy()
        old_face = face.copy()
        
        face.front = old_face.top
        face.back = old_face.bottom
        
        face.top = None
        face.bottom = None
        
        # face.is_side_face=False
        face.orientation_to_cube = Orientation.BOTTOM
        
        return face
        
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.opposite.copy()
        old_face = face.copy()
        
        face.front = old_face.top
        face.back = old_face.bottom
        
        face.right = old_face.left
        face.left = old_face.right

        face.top = None
        face.bottom = None
        
        # face.is_side_face=False
        face.orientation_to_cube = Orientation.TOP
        
        return face
        
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        left_face = current_front.left.copy()
        old_face = left_face.copy()
        
        left_face.right = old_face.top
        left_face.left = old_face.bottom
        
        left_face.top = old_face.left
        left_face.bottom = old_face.right
        
        return left_face
        
    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        right_face = current_front.right.copy()
        old_face = right_face.copy()
        
        right_face.left = old_face.top
        right_face.right = old_face.bottom
        
        right_face.bottom = old_face.left
        right_face.top = old_face.right
        
        return right_face
        
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.top.copy()
        old_face = face.copy()
        
        face.top = old_face.back
        face.bottom = old_face.front
                
        face.front = None
        face.back = None
        
        # face.is_side_face = True
        face.orientation_to_cube = Orientation.FRONT
        
        return face
        
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.bottom.copy()
        old_face = face.copy()
        
        face.top = old_face.back
        face.bottom = old_face.front
        
        face.left = old_face.right
        face.right = old_face.left
        
        face.front = None
        face.back = None
        
        # face.is_side_face = True
        face.orientation_to_cube = Orientation.BACK
        
        return face
    
    
class RotateLeftHorizontal:
    
    # YOUR CODE HERE
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.copy()
        old_face = face.copy()
        
        face.left = old_face.top
        face.right = old_face.bottom
        
        face.top = old_face.right
        face.bottom = old_face.left
                
        return face
        
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.opposite.copy()
        old_face = face.copy()
        
        face.top = old_face.left
        face.bottom = old_face.right
        
        face.left = old_face.bottom
        face.right = old_face.top

        return face
        
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        left_face = current_front.left.copy()
        old_face = left_face.copy()
        
        left_face.left = old_face.top
        left_face.right = old_face.bottom
            
        left_face.front = old_face.right
        left_face.back = old_face.left
            
        left_face.top = None
        left_face.bottom = None
        
        # left_face.is_side_face = False
        left_face.orientation_to_cube = Orientation.BOTTOM
            
        return left_face
        
    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        right_face = current_front.right.copy()
        old_face = right_face.copy()
        
        right_face.right = old_face.bottom
        right_face.left = old_face.top
            
        right_face.front = old_face.left
        right_face.back = old_face.right
            
        right_face.top = None
        right_face.bottom = None
        
        # right_face.is_side_face = False
        right_face.orientation_to_cube = Orientation.TOP
            
        return right_face
        
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.top.copy()
        old_face = face.copy()
        
        face.right = old_face.front
        face.left = old_face.back
        
        face.top = old_face.right
        face.bottom = old_face.left
            
        face.front = None
        face.back = None
        
        # face.is_side_face = True
        face.orientation_to_cube = Orientation.LEFT
    
        return face
        
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.bottom.copy()
        old_face = face.copy()
        
        face.right = old_face.back
        face.left = old_face.front
        
        face.top = old_face.right
        face.bottom = old_face.left
            
        face.front = None
        face.back = None
        
        # face.is_side_face = True
        face.orientation_to_cube = Orientation.RIGHT
        
        return face
    
    
class RotateLeftVertical:
    
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        front_face = current_front.copy()
        front_face.orientation_to_cube = Orientation.LEFT
        return front_face
    
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        back_face = current_front.opposite.copy()
        back_face.orientation_to_cube = Orientation.RIGHT
        return back_face

    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        right_face = current_front.right.copy()
        right_face.orientation_to_cube = Orientation.FRONT
        return right_face
    
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        left_face = current_front.left.copy()
        left_face.orientation_to_cube = Orientation.BACK
        return left_face
    
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.top.copy()
        old_face = face.copy()
        
        face.left = old_face.front
        face.right = old_face.back
        
        face.front = old_face.right
        face.back = old_face.left
        
        return face
    
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.bottom.copy()
        old_face = face.copy()
        
        face.left = old_face.front
        face.right = old_face.back
        
        face.front = old_face.right
        face.back = old_face.left

        return face
    
    
class RotateRightVertical:
    
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        front_face = current_front.copy()
        front_face.orientation_to_cube = Orientation.RIGHT
        return front_face
    
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        back_face = current_front.opposite.copy()
        back_face.orientation_to_cube = Orientation.LEFT
        return back_face
    
    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        right_face = current_front.right.copy()
        right_face.orientation_to_cube = Orientation.BACK
        return right_face
    
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        left_face = current_front.left.copy()
        left_face.orientation_to_cube = Orientation.FRONT
        return left_face
    
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.top.copy()
        old_face = face.copy()
        
        face.front = old_face.left
        face.back = old_face.right
        
        face.left = old_face.back
        face.right = old_face.front
        
        return face
    
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.bottom.copy()
        old_face = face.copy()
        
        face.front = old_face.left
        face.back = old_face.right
        
        face.left = old_face.back
        face.right = old_face.front
        
        return face
    
    
class RotateRightHorizontal:
    
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.copy()
        old_face = face.copy()
        
        face.right = old_face.top
        face.left = old_face.bottom
        
        face.top = old_face.left
        face.bottom = old_face.right
            
        return face
    
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.opposite.copy()
        old_face = face.copy()
        
        face.left = old_face.top
        face.right = old_face.bottom
        
        face.top = old_face.right
        face.bottom = old_face.left
                
        return face
    
    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        right_face = current_front.right.copy()
        old_face = right_face.copy()
        
        right_face.right = old_face.top
        right_face.left = old_face.bottom
            
        right_face.front = old_face.left
        right_face.back = old_face.right
            
        right_face.top = None
        right_face.bottom = None
        
        # right_face.is_side_face = False
        right_face.orientation_to_cube = Orientation.BOTTOM
            
        return right_face
    
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        left_face = current_front.left.copy()
        old_face = left_face.copy()
        
        left_face.right = old_face.top
        left_face.left = old_face.bottom
            
        left_face.front = old_face.right
        left_face.back = old_face.left
            
        left_face.top = None
        left_face.bottom = None
        
        # left_face.is_side_face = False
        left_face.orientation_to_cube = Orientation.TOP
            
        return left_face
    
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.top.copy()
        old_face = face.copy()
        
        face.right = old_face.back
        face.left = old_face.front
        
        face.top = old_face.left
        face.bottom = old_face.right
            
        face.front = None
        face.back = None
        
        # face.is_side_face = True
        face.orientation_to_cube = Orientation.RIGHT
        
        return face
    
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.bottom.copy()
        old_face = face.copy()
        
        face.right = old_face.front
        face.left = old_face.back
        
        face.top = old_face.left
        face.bottom = old_face.right
            
        face.front = None
        face.back = None
        
        # face.is_side_face = True
        face.orientation_to_cube = Orientation.LEFT
        
        return face
    
    
class InvertVertical:
    
    # YOUR CODE HERE
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        front_face = current_front.copy()
        front_face.orientation_to_cube = Orientation.BACK
        return front_face
        
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        back_face = current_front.opposite.copy()
        back_face.orientation_to_cube = Orientation.FRONT
        return back_face
        
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        left_face = current_front.left.copy()
        left_face.orientation_to_cube = Orientation.RIGHT
        return left_face
        
    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        right_face = current_front.right.copy()
        right_face.orientation_to_cube = Orientation.LEFT
        return right_face
        
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.top.copy()
        old_face = face.copy()
        
        face.back = old_face.front
        face.front = old_face.back
        
        face.left = old_face.right
        face.right = old_face.left
        
        return face
        
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.bottom.copy()
        old_face = face.copy()
        
        face.back = old_face.front
        face.front = old_face.back
        
        face.left = old_face.right
        face.right = old_face.left
        
        return face
        
        
class InvertHorizontal:
    
    # YOUR CODE HERE
    def transform_front_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.copy()
        old_face = face.copy()
        
        face.left = old_face.right
        face.right = old_face.left
            
        face.bottom = old_face.top
        face.top = old_face.bottom
        
        face.orientation_to_cube = Orientation.BACK
        
        return face
        
    def transform_back_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.opposite.copy()
        old_face = face.copy()
        
        face.left = old_face.right
        face.right = old_face.left
            
        face.bottom = old_face.top
        face.top = old_face.bottom
        
        face.orientation_to_cube = Orientation.FRONT
        
        return face
        
    def transform_left_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.left.copy()
        old_face = face.copy()
        
        face.left = old_face.right
        face.right = old_face.left
        
        face.top = old_face.bottom
        face.bottom = old_face.top
        
        return face
        
    def transform_right_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.right.copy()
        old_face = face.copy()
        
        face.left = old_face.right
        face.right = old_face.left
        
        face.top = old_face.bottom
        face.bottom = old_face.top
        
        return face
        
    def transform_top_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.top.copy()
        old_face = face.copy()
        
        face.front = old_face.back
        face.back = old_face.front
        
        face.orientation_to_cube = Orientation.BOTTOM
        
        return face
        
    def transform_bottom_face(current_front: Face, is_test: bool = False) -> Face:
        face = current_front.bottom.copy()
        old_face = face.copy()
        
        face.front = old_face.back
        face.back = old_face.front
        
        face.orientation_to_cube = Orientation.TOP
        
        return face
    