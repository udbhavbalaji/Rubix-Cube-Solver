from enum import Enum, auto

class Colours(Enum):
    # YOUR CODE HERE
    BLUE = auto()
    WHITE = auto()
    GREEN = auto()
    YELLOW = auto()
    RED = auto()
    ORANGE = auto()


class Orientation(Enum):
    # YOUR CODE HERE
    FRONT = auto()
    BACK = auto()
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()
pass


class FacePositions():
    
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
    BOTTOM_ROW = 2
    
    LEFT_COL = 0
    RIGHT_COL = 2
    
    

class PieceType(Enum):
    # YOUR CODE HERE
    CENTER = auto()
    EDGE = auto()
    CORNER = auto()
    
    
class PossibleRotations(Enum):
    # YOUR CODE HERE
    ROTATE_DOWN = 'Rotating Cube Down'
    ROTATE_UP = 'Rotating Cube Up'
    ROTATE_LEFT_VERTICALLY = 'Rotating Cube Left Vertically'
    ROTATE_LEFT_HORIZONTALLY = 'Rotating Cube Left Horizontally'
    ROTATE_RIGHT_VERTICALLY = 'Rotating Cube Right Vertically'
    ROTATE_RIGHT_HORIZONTALLY = 'Rotating Cube Right Horizontally'
    INVERT_VERTICALLY = 'Inverting Cube Vertically'
    INVERT_HORIZONTALLY = 'Inverting Cube Horizontally'
    

class PossibleShifts(Enum):
    # YOUR CODE HERE
    RIGHT_COL_UP = 'Shifting Right Column Up'
    RIGHT_COL_DOWN = 'Shifting Right Column Down'
    LEFT_COL_UP = 'Shifting Left Column Up'
    LEFT_COL_DOWN = 'Shifting Left Column Down'
    TOP_ROW_LEFT = 'Shifting Top Row Left'
    TOP_ROW_RIGHT = 'Shifting Top Row Right'
    BOTTOM_ROW_LEFT = 'Shifting Bottom Row Left'
    BOTTOM_ROW_RIGHT = 'Shifting Bottom Row Right'
    
    
POSSIBLE_ROTATIONS = [PossibleRotations.ROTATE_UP, PossibleRotations.ROTATE_DOWN, PossibleRotations.ROTATE_LEFT_VERTICALLY,
                      PossibleRotations.ROTATE_LEFT_HORIZONTALLY, PossibleRotations.ROTATE_RIGHT_VERTICALLY,
                      PossibleRotations.ROTATE_RIGHT_HORIZONTALLY, PossibleRotations.INVERT_VERTICALLY, PossibleRotations.INVERT_HORIZONTALLY]

POSSIBLE_SHIFTS = [PossibleShifts.RIGHT_COL_UP, PossibleShifts.RIGHT_COL_DOWN, PossibleShifts.LEFT_COL_UP, PossibleShifts.LEFT_COL_DOWN,
                   PossibleShifts.TOP_ROW_LEFT, PossibleShifts.TOP_ROW_RIGHT, PossibleShifts.BOTTOM_ROW_LEFT, PossibleShifts.BOTTOM_ROW_RIGHT]
    
COLOURS = [Colours.BLUE, Colours.RED, Colours.ORANGE, Colours.WHITE, Colours.GREEN, Colours.YELLOW]