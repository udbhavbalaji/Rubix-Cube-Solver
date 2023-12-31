from enum import Enum

class PieceType(Enum):
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
    
    
class Axes(Enum):
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
    
    
class Orientation(Enum):
    FRONT = 'Front'
    BACK = 'Back'
    LEFT = 'Left'
    RIGHT = 'Right'
    TOP = 'Top'
    BOTTOM = 'Bottom'


class PossibleOperations:
    
    ROTATE_LEFT_VERTICALLY = 'Rotating Left Vertically'
    ROTATE_RIGHT_VERTICALLY = 'Rotating Right Vertically'
    ROTATE_UP = 'Rotating Up'
    ROTATE_DOWN = 'Rotating Down'
    ROTATE_LEFT_HORIZONTALLY = 'Rotating Left Horizontally'
    ROTATE_RIGHT_HORIZONTALLY = 'Rotating Right Horizontally'
    INVERT_CUBE_VERTICALLY = 'Inverting Cube Vertically'
    INVERT_CUBE_HORIZONTALLY = 'Inverting Cube Horizontally'
    
    RIGHT_COL_UP = 'Rotating Right Column Up'
    LEFT_COL_UP = 'Rotating Left Column Up'
    RIGHT_COL_DOWN = 'Rotating Right Column Down'
    LEFT_COL_DOWN = 'Rotating Left Column Down'
    TOP_ROW_LEFT = 'Rotating Top Row Left'
    TOP_ROW_RIGHT = 'Rotating Top Row Right'
    BOTTOM_ROW_LEFT = 'Rotating Bottom Row Left'
    BOTTOM_ROW_RIGHT = 'Rotating Bottom Row Right'
    
    RESET_PERSPECTIVE = 'Resetting Cube Perspective'
    
    SHUFFLE_CUBE = 'Shuffling Cube'
    
    MOVES = [ROTATE_LEFT_VERTICALLY, ROTATE_RIGHT_VERTICALLY, ROTATE_UP, ROTATE_DOWN,
             ROTATE_LEFT_HORIZONTALLY, ROTATE_RIGHT_HORIZONTALLY, INVERT_CUBE_VERTICALLY, INVERT_CUBE_HORIZONTALLY,
             RIGHT_COL_UP, LEFT_COL_UP, RIGHT_COL_DOWN, LEFT_COL_DOWN,
             TOP_ROW_LEFT, TOP_ROW_RIGHT, BOTTOM_ROW_LEFT, BOTTOM_ROW_RIGHT,
             RESET_PERSPECTIVE, SHUFFLE_CUBE]
    