from Constraints import FacePositions, Axes

class FacePredicates:
    
    def is_correct_perspective(cube):
        
        return (FacePredicates.is_blue_face_front(cube.current_perspective, cube.blue_face) and \
                FacePredicates.is_white_face_top(cube.current_perspective, cube.white_face) and \
                FacePredicates.is_orange_face_right(cube.current_perspective, cube.orange_face) and \
                FacePredicates.is_red_face_left(cube.current_perspective, cube.red_face) and \
                FacePredicates.is_green_face_back(cube.current_perspective, cube.green_face) and \
                FacePredicates.is_yellow_face_bottom(cube.current_perspective, cube.yellow_face))
    
    
    def is_blue_face_front(current_front, blue_face):
        return current_front == blue_face
    
    def is_white_face_top(current_front, white_face):
        return current_front.top == white_face

    def is_orange_face_right(current_front, orange_face):
        return current_front.right == orange_face  
    
    def is_red_face_left(current_front, red_face):
        return current_front.left == red_face
    
    def is_green_face_back(current_front, green_face):
        return current_front.opposite == green_face
    
    def is_yellow_face_bottom(current_front, yellow_face):
        return current_front.bottom == yellow_face  
    
    def are_faces_equal(face, target_face):
        return face == target_face


class GridPredicates:
    
    pass


class PiecePredicates:
    
    def are_pieces_equal(piece_one, piece_two):
        return piece_one == piece_two