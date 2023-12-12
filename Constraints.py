class PieceType:
    EDGE = 'Edge'
    CENTER = 'Center'
    CORNER = 'Corner'
    
class Colours:
    WHITE = 'White'
    ORANGE = 'Orange'
    GREEN = 'Green'
    RED = 'Red'
    BLUE = 'Blue'
    YELLOW = 'Yellow'
    
class ImpossibleNeighbours:
    WHITE_YELLOW = (Colours.WHITE, Colours.YELLOW)
    ORANGE_RED = (Colours.ORANGE, Colours.RED)
    BLUE_GREEN = (Colours.BLUE, Colours.GREEN)
    
class PossibleEdgePieces:
    WHITE_GREEN = (Colours.WHITE, Colours.GREEN)
    WHITE_BLUE = (Colours.WHITE, Colours.BLUE)
    WHITE_RED = (Colours.WHITE, Colours.RED)
    WHITE_ORANGE = (Colours.WHITE, Colours.ORANGE)
    
    YELLOW_GREEN = (Colours.YELLOW, Colours.GREEN)
    YELLOW_BLUE = (Colours.YELLOW, Colours.BLUE)
    YELLOW_RED = (Colours.YELLOW, Colours.RED)
    YELLOW_ORANGE = (Colours.YELLOW, Colours.ORANGE)
    
    RED_GREEN = (Colours.RED, Colours.GREEN)
    GREEN_ORANGE = (Colours.GREEN, Colours.ORANGE)
    ORANGE_BLUE = (Colours.ORANGE, Colours.BLUE)
    BLUE_RED = (Colours.BLUE, Colours.RED)
    
class PossibleCornerPieces:
    WHITE_RED_BLUE = (Colours.WHITE, Colours.RED, Colours.BLUE)
    WHITE_ORANGE_BLUE = (Colours.WHITE, Colours.ORANGE, Colours.BLUE)
    WHITE_GREEN_RED = (Colours.WHITE, Colours.GREEN, Colours.RED)
    WHITE_GREEN_ORANGE = (Colours.WHITE, Colours.ORANGE, Colours.GREEN)
    
    YELLOW_RED_BLUE = (Colours.YELLOW, Colours.RED, Colours.BLUE)
    YELLOW_ORANGE_BLUE = (Colours.YELLOW, Colours.ORANGE, Colours.BLUE)
    YELLOW_GREEN_RED = (Colours.YELLOW, Colours.GREEN, Colours.RED)
    YELLOW_GREEN_ORANGE = (Colours.YELLOW, Colours.ORANGE, Colours.GREEN)
    
class Axes:
    VERTICAL = 'Vertical'
    HORIZONTAL = 'Horizontal'
    
class FacePositions:
    TOP_LEFT = (0,0)
    TOP_CENTER = (0,1)
    TOP_RIGHT = (0,2)
    MID_LEFT = (1,0)
    MID_CENTER = (1,1)
    MID_RIGHT = (1,2)
    BOTTOM_LEFT = (2,0)
    BOTTOM_CENTER = (2,1)
    BOTTOM_RIGHT = (2,2)

    TOP_ROW = 0
    MID_ROW = 1
    BOTTOM_ROW = 2
    
    LEFT_COL = 0
    CENTER_COL = 1
    RIGHT_COL = 2
    
    POSITIONS = [TOP_LEFT, TOP_CENTER, TOP_RIGHT, MID_LEFT, MID_CENTER, MID_RIGHT, BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT]
    
    def get_colour(face, face_position):
        return face.grid[face_position]
    
    
class Orientation:
    FRONT = 'Front'
    BACK = 'Back'
    LEFT = 'Left'
    RIGHT = 'Right'
    TOP = 'Top'
    BOTTOM = 'Bottom'
