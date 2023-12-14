"""
This module contains the RubixCube, Face, Piece, EdgePiece and CornerPiece classes. It creates a Rubix Cube, 
allowing all possible operations that can be done to a Rubix Cube in real life.
"""
from __future__ import annotations
# Importing installed modules
import numpy as np
# Importing built-in modules
import random
# Importing (from) local modules
from Constraints import Axes, Colours, FacePositions, Orientation, PieceType, PossibleOperations
from Operations import shuffle_cube, OPERATIONS

class RubixCube():
    
    """
    This is a class representing the Rubix Cube. A cube has 6 faces (type=FaceObject). It is initialized with the blue 
    face in front, red face on the left, orange face on the right, green face on the back, white face 
    on the top and yellow face on the bottom.
    
    All side faces (Front, Left, Right, Back) have Face().top set as the top (white) face and Face().bottom set as the 
    bottom (yellow) face. Additionally, for all side faces, accessing the left/right attribute 4 times will bring you back to
    the initial perspective (hence, making it cyclic). The top (white) and bottom (yellow) faces have Face().top and 
    Face().bottom set to None. To correctly map their representation in the cube, they have Face().front = the current 
    front face and Face().back = the current back face.
    
    All faces have a 3 X 3 grid holding pieces (type=PieceObject). These are stored in a numpy array. For all side faces, 
    the orientation is identical to face orientations discussed above. For the top (white) face, the top row corresponds to
    the edge Face().back (green), the left and right columns correspond to edges Face().left (red) and Face().right (orange) and 
    the bottom row corresponds to the edge Face().front (blue). Similarly, for the bottom (yellow) face, the top row corresponds to
    the edge Face().front (blue), the left and right columns correspond to edges Face().left (red) and Face().right (orange) and 
    the bottom row corresponds to the edge Face().back (green).
    
    Class Attributes:
        NUM_FACES (int): Literal value to store number of faces in the Rubix Cube
        COLOURS (list): List of face colour literals

    Instance Attributes:
        current_perspective: Pointer to the Face Object that is currently in front
        blue_face: Pointer to the blue face in the cube
        white_face: Pointer to the white face in the cube
        yellow_face: Pointer to the yellow face in the cube
        red_face: Pointer to the red face in the cube
        orange_face: Pointer to the orange face in the cube
        green_face: Pointer to the green face in the cube
        _kwargs_dict: Dictionary property mapping possible moves to operation functions and corresponding kwargs
        
    Instance Methods:
        copy: Creates a duplicate instance of the Cube class with the same values
        initialize_random_cube: Creates the cube structure
        init_kwargs: Initializes operation functions and corresponding kwargs
        get_kwargs: Decorator method that maps the required operation function and kwargs dict based on the requested operation
        move: Performs the specified operation
        assign_complements: Assigns corresponding complement value for each piece on a face
        get_2D_cube_grid: Translates each face's grid into a 2D representation for graphing
    """
    
    NUM_FACES = 6
    # $ Face Order: Front, Right, Back, Left, Top, Bottom
    # $ Colour Order: Blue, Orange, Green, Red, White, Yellow
    COLOURS = [Colours.BLUE, Colours.ORANGE, Colours.GREEN, Colours.RED, Colours.WHITE, Colours.YELLOW]
    
    def __init__(self, 
                 current: Face = None, initial: Face = None, blue: Face = None, white: Face = None, 
                 yellow: Face = None, red: Face = None, orange: Face = None, green: Face = None, 
                 is_copy: bool = False) -> None:
        """
        Constructor method for the Cube class.

        Args:
            current (Face, optional): Face instance that is currently in front. Defaults to None.
            initial (_type_, optional): _description_. Defaults to None.
            blue (Face, optional): Face instance for the blue face. Defaults to None.
            white (Face, optional): Face instance for the white face. Defaults to None.
            yellow (Face, optional): Face instance for the yellow face. Defaults to None.
            red (Face, optional): Face instance for the red face. Defaults to None.
            orange (Face, optional): Face instance for the orange face. Defaults to None.
            green (Face, optional): Face instance for the green face. Defaults to None.
            is_copy (bool, optional): bool to show if current Cube object is copied from another Cube object. Defaults to False.
        """
        self.current_perspective = current
        self.initial_perspective = initial
        
        self.blue_face = blue
        self.white_face = white
        self.yellow_face = yellow
        self.red_face = red
        self.orange_face = orange
        self.green_face = green
        
        self._kwargs_dict = self.init_kwargs()
                
        if not is_copy:
            self.initialize_random_cube()
            
        self.kwargs_dict = self.init_kwargs()
                        
    def __str__(self) -> str:
        """
        This method is called to return the string representation of the cube. It is represented as a 2D grid, 
        as shown below.
        
        Every face's grid = [[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]]
                              
        The output representation is as follows:
        
             Left Face
              _______   Bottom Face
              |3 2 1|   /
              |6 5 4|  /
              |9 8 7| /
        _____________L___________
        |1 4 7|1 4 7|9 6 3|1 4 7|
Front   |2 5 8|2 5 8|8 5 2|2 5 8| Top
Face    |3 6 9|3 6 9|7 4 1|3 6 9| Face
        -------------------------
              |7 8 9|   \
              |4 5 6|    \
              |1 2 3|    Back Face
              -------
             Right Face
        

        Returns:
            output (str): A string that is formatted to output the above structure
        """
        front = self.current_perspective.copy()
        
        left_grid = self.get_2D_cube_grid(front.left, Orientation.LEFT)
        right_grid = self.get_2D_cube_grid(front.right, Orientation.RIGHT)
        top_grid = self.get_2D_cube_grid(front.top, Orientation.TOP)
        bottom_grid = self.get_2D_cube_grid(front.bottom, Orientation.BOTTOM)
        back_grid = self.get_2D_cube_grid(front.opposite, Orientation.BACK)
        front_grid = self.get_2D_cube_grid(front, Orientation.FRONT)
        
        output = f'      ______\n'
        output += f'     !{left_grid[0]}|\n     !{left_grid[1]}|\n     !{left_grid[2]}|\n'
        output += '________________________\n'
        output += f'{front_grid[0]}|{bottom_grid[0]}|{back_grid[0]}|{top_grid[0]}|\n'
        output += f'{front_grid[1]}|{bottom_grid[1]}|{back_grid[1]}|{top_grid[1]}|\n'
        output += f'{front_grid[2]}|{bottom_grid[2]}|{back_grid[2]}|{top_grid[2]}|\n'
        output += '________________________\n'
        output += f'     !{right_grid[0]}|\n     !{right_grid[1]}|\n     !{right_grid[2]}|\n'
        output += f'      ______'
        
        return output
            
    def init_kwargs(self) -> dict:
        """
        This method initializes the operation functions and corresponding kwargs for each of the 
        possible operations.

        Returns:
            kwargs_dict (dict): A dictionary containing tuples for each possible operation. The 
                                tuple contains the operation function and the corresponding kwargs.
        """
        kwargs_template = {
            'cube': None,
            'axis': None,
            'current_front': None
        }
        kwargs_dict = {}
        
        for i in range(len(PossibleOperations.MOVES)):
            kwargs = kwargs_template.copy()
            if i < 8 or i > 15:
                kwargs['cube'] = self
                if i in [0, 1, 6]:
                    kwargs['axis'] = Axes.VERTICAL
                elif i in [4, 5, 7]:
                    kwargs['axis'] = Axes.HORIZONTAL
            else:
                kwargs['current_front'] = self.current_perspective
                
            operation = OPERATIONS[i]
            kwargs_dict[PossibleOperations.MOVES[i]] = (operation, kwargs)
        
        return kwargs_dict
            
    @property
    def kwargs_dict(self) -> dict:
        """
        This is a getter method for the property Cube().kwargs_dict. It returns the dict that is stored in
        Cube()._kwargs_dict. 

        Returns:
            dict: Returns the dict stored in Cube()._kwargs_dict
        """
        return self._kwargs_dict
    
    @kwargs_dict.setter
    def kwargs_dict(self, new_dict: dict) -> None:
        """
        This is a setter method to internally re-assign the property (if required). It overrides the current dict
        withnew_dict.

        Args:
            new_dict (dict): New dict containing kwargs for all possible operations.
        """
        self._kwargs_dict = new_dict
    
    def copy(self) -> RubixCube:
        """
        This method creates and returns a copy of the current object (Cube) with all attribute values duplicated.

        Returns:
            Cube: A copy of the current instance is created and returned.
        """
        return RubixCube(self.current_perspective, self.initial_perspective, self.blue_face, self.white_face, self.yellow_face, \
                    self.red_face, self.orange_face, self.green_face, is_copy=True)
    
    def initialize_random_cube(self) -> None:
        """
        This method initializes the Rubix Cube. The faces are created, edges are joined and positional attributes 
        assigned. All complements values are assigned for each piece (type=PieceType) in each face (type=FaceType).
        
        Side Faces Initialization:
                                               
                                             (Top)
                                    (Left Col)   (Right Col)
                                             ^   ^
                                             |   |
                                            _______
                                            |1 2 3|-> (Top Row)
                            (Left)          |4 5 6|                  (Right)
                                            |7 8 9|-> (Bottom Row)
                                            -------
                                            
                                            (Bottom)
                                            
        Top Face Initialization:
                                              
                                             (Back)
                                    (Left Col)   (Right Col)
                                             ^   ^
                                             |   |
                                            _______
                                            |1 2 3|-> (Top Row)
                            (Left)          |4 5 6|                  (Right)
                                            |7 8 9|-> (Bottom Row)
                                            -------
                                            
                                            (Front)
                                            
        Bottom Face Initialization:
                                              
                                             (Front)
                                    (Left Col)   (Right Col)
                                             ^   ^
                                             |   |
                                            _______
                                            |1 2 3|-> (Top Row)
                            (Left)          |4 5 6|                  (Right)
                                            |7 8 9|-> (Bottom Row)
                                            -------
                                            
                                            (Back)
        """
        
        #* Creating the faces
        
        self.blue_face = Face(self.COLOURS[0])
        self.orange_face = Face(self.COLOURS[1])
        self.green_face = Face(self.COLOURS[2])
        self.red_face = Face(self.COLOURS[3])
        self.white_face = Face(self.COLOURS[4], is_side_face=False)
        self.yellow_face = Face(self.COLOURS[5], is_side_face=False)
        
        ## Joining the faces to make a cube
        self.current_perspective = self.blue_face
        
        ## Joining the side faces
        self.blue_face.left = self.red_face
        self.blue_face.right = self.orange_face
        
        self.orange_face.left = self.blue_face
        self.orange_face.right = self.green_face
        
        self.green_face.left = self.orange_face
        self.green_face.right = self.red_face
        
        self.red_face.left = self.green_face
        self.red_face.right = self.blue_face
        
        ## Joining the top face
        self.white_face.front = self.blue_face
        self.blue_face.top = self.white_face
        
        self.white_face.right = self.orange_face
        self.orange_face.top = self.white_face
        
        self.white_face.back = self.green_face
        self.green_face.top = self.white_face
        
        self.white_face.left = self.red_face
        self.red_face.top = self.white_face
        
        ## Joining the bottom face
        self.yellow_face.front = self.blue_face
        self.blue_face.bottom = self.yellow_face
        
        self.yellow_face.right = self.orange_face
        self.orange_face.bottom = self.yellow_face
        
        self.yellow_face.back = self.green_face
        self.green_face.bottom = self.yellow_face
        
        self.yellow_face.left = self.red_face
        self.red_face.bottom = self.yellow_face
        
        ## Connecting opposite faces
        self.white_face.opposite = self.yellow_face
        self.yellow_face.opposite = self.white_face
        
        self.blue_face.opposite = self.green_face
        self.green_face.opposite = self.blue_face
        
        self.red_face.opposite = self.orange_face
        self.orange_face.opposite = self.red_face
        
        ## Initializing complements
        # Blue Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY, verbose=False)
        # Orange Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY, verbose=False)
        # Green Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY, verbose=False)
        # Red Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_LEFT_VERTICALLY, verbose=False)
        # Back to Blue Face
        self.move(PossibleOperations.ROTATE_DOWN, verbose=False)
        # White Face
        self.assign_complements(self.current_perspective)
        self.move(PossibleOperations.ROTATE_DOWN, verbose=False)
        self.move(PossibleOperations.ROTATE_DOWN, verbose=False)
        # Yellow Face
        self.assign_complements(self.current_perspective)
        
        # Back to Blue Face
        self.move(PossibleOperations.RESET_PERSPECTIVE, verbose=False)
        
    def assign_complements(self, face: "Face") -> None:
        """
        This method assigns the complements for each piece in the face. EdgePiece and CornerPiece classes
        have instance attributes (EdgePiece().complement and CornerPiece().complements respectively) that hold 
        the pointers to the complement pieces.
        
        Example: Consider an edge piece in between the blue face and white face. According to current perspective,
        this would make the top_center piece in the front (blue) face and the bottom_center piece in the top (white)
        face complements. Similarly, in corner pieces, all 3 pieces that make up each corner are each others' complements.

        Args:
            face (Face): Face representing the current perspective of the cube
        """
        ## Assigning complements of edge pieces
        face.grid[FacePositions.TOP_CENTER].complement = face.top.grid[FacePositions.BOTTOM_CENTER]
        face.grid[FacePositions.MID_LEFT].complement = face.left.grid[FacePositions.MID_RIGHT]
        face.grid[FacePositions.MID_RIGHT].complement = face.right.grid[FacePositions.MID_LEFT]
        face.grid[FacePositions.BOTTOM_CENTER].complement = face.bottom.grid[FacePositions.TOP_CENTER]
        
        ## Assigning complements for corner pieces
        face.grid[FacePositions.TOP_LEFT].complements = (face.top.grid[FacePositions.BOTTOM_LEFT], face.left.grid[FacePositions.TOP_RIGHT])
        face.grid[FacePositions.TOP_RIGHT].complements = (face.top.grid[FacePositions.BOTTOM_RIGHT], face.right.grid[FacePositions.TOP_LEFT])
        face.grid[FacePositions.BOTTOM_LEFT].complements = (face.bottom.grid[FacePositions.TOP_LEFT], face.left.grid[FacePositions.BOTTOM_RIGHT])
        face.grid[FacePositions.BOTTOM_RIGHT].complements = (face.bottom.grid[FacePositions.TOP_RIGHT], face.right.grid[FacePositions.BOTTOM_LEFT])
        
    def get_kwargs(original_func: function) -> function:
        """
        This is a decorator method that selects operation function and kwargs based on the requested operation.

        Args:
            original_func (func): Function to be executed within the wrapper function.
            
        Returns:
            perform_operation (func): Wrapper function that performs the operation
        """
        
        def perform_operation(self, operation: str, verbose: bool = True) -> list:
            """
            This is the wrapper function for the get_kwargs decorator method. It obtains the correct operation function
            and executes it before calling the Cube().move method.

            Args:
                operation (str): String literal representing a possible operation.
                verbose (bool, optional): bool value that determines if the operation should output logs. Defaults to True.
            """
            shift, kwargs = self.kwargs_dict[operation]
            op_stack = shift(**kwargs)
            original_func(self, operation, verbose)
            if op_stack is not None:
                return op_stack
            return []
        
        return perform_operation
        
    @get_kwargs
    def move(self, operation: str, verbose: bool = True) -> None:
        """
        This function performs the operation requested/specified.

        Args:
            operation (str): String literal representing a possible operation
            verbose (bool, optional): bool value that determines if the operation should output logs. Defaults to True.
        """
        if verbose:
            print(operation)
        
    def get_2D_cube_grid(self, face: Face, orientation: str) -> tuple:
        """
        This method builds the transformed grids to be used in the string representation of the cube. 

        Args:
            face (Face): face instance that the grid is being transformed for
            orientation (str): String literal showing if the face is left, right, top, bottom, back or front of Cube().current_perspective

        Returns:
            tuple: The tuple contains the string output for each row/column in the grid
        """
        if orientation == Orientation.LEFT:
            first_row = f'{face.grid[FacePositions.TOP_RIGHT].colour[0]} {face.grid[FacePositions.TOP_CENTER].colour[0]} {face.grid[FacePositions.TOP_LEFT].colour[0]}'
            second_row = f'{face.grid[FacePositions.MID_RIGHT].colour[0]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.MID_LEFT].colour[0]}'
            third_row = f'{face.grid[FacePositions.BOTTOM_RIGHT].colour[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour[0]} {face.grid[FacePositions.BOTTOM_LEFT].colour[0]}'
            
        elif orientation in [Orientation.FRONT, Orientation.BOTTOM, Orientation.TOP]:
            first_row = f'{face.grid[FacePositions.TOP_LEFT].colour[0]} {face.grid[FacePositions.MID_LEFT].colour[0]} {face.grid[FacePositions.BOTTOM_LEFT].colour[0]}'
            second_row = f'{face.grid[FacePositions.TOP_CENTER].colour[0]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour[0]}'
            third_row = f'{face.grid[FacePositions.TOP_RIGHT].colour[0]} {face.grid[FacePositions.MID_RIGHT].colour[0]} {face.grid[FacePositions.BOTTOM_RIGHT].colour[0]}'
            
        elif orientation == Orientation.BACK:
            first_row = f'{face.grid[FacePositions.BOTTOM_RIGHT].colour[0]} {face.grid[FacePositions.MID_RIGHT].colour[0]} {face.grid[FacePositions.TOP_RIGHT].colour[0]}'
            second_row = f'{face.grid[FacePositions.BOTTOM_CENTER].colour[0]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.TOP_CENTER].colour[0]}'
            third_row = f'{face.grid[FacePositions.BOTTOM_LEFT].colour[0]} {face.grid[FacePositions.MID_LEFT].colour[0]} {face.grid[FacePositions.TOP_LEFT].colour[0]}'
            
        elif orientation == Orientation.RIGHT:
            first_row = f'{face.grid[FacePositions.BOTTOM_LEFT].colour[0]} {face.grid[FacePositions.BOTTOM_CENTER].colour[0]} {face.grid[FacePositions.BOTTOM_RIGHT].colour[0]}'
            second_row = f'{face.grid[FacePositions.MID_LEFT].colour[0]} {face.grid[FacePositions.MID_CENTER].colour[0]} {face.grid[FacePositions.MID_RIGHT].colour[0]}'
            third_row = f'{face.grid[FacePositions.TOP_LEFT].colour[0]} {face.grid[FacePositions.TOP_CENTER].colour[0]} {face.grid[FacePositions.TOP_RIGHT].colour[0]}'
        
        return (first_row, second_row, third_row)
    
    def print_cube_structure_2D(self) -> None:
        front = self.current_perspective.copy()
        # Printing Format
        #       Left
        # Front Bottom Back Top
        #       Right
        print('\n            Left')
        print('Front    Bottom     Back    Top')
        print('            Right\n')
        print(f'\n          {front.left.center_colour}')
        print(f'{front.center_colour}    {front.bottom.center_colour}    {front.opposite.center_colour}    {front.top.center_colour}')
        print(f'          {front.right.center_colour}\n')
        
    def get_attributes(self) -> None:
        front = self.current_perspective
        right_face = front.right
        left_face = front.left
        top_face = front.top
        bottom_face = front.bottom
        opposite_face = front.opposite
        
        print('\nFront Attributes')
        print(f'Front: {front}, Left: {left_face}, Right: {right_face}, Top: {top_face}, Bottom: {bottom_face}, \
                Back: {opposite_face}')
        print('Front Colours')
        print(f'Front: {front.center_colour}, Left: {front.left.center_colour}, Right: {front.right.center_colour}, \
                Top: {front.top.center_colour}, Bottom: {front.bottom.center_colour}, Back: {front.opposite.center_colour}\n')
        

class Face:
    
    """
    This is a class representing a Face of a Rubix Cube (type=CubeType). Each face has a 3 X 3 grid
    representing each of the 9 pieces (type=PieceType) on the face of a Rubix Cube. The Piece().colour
    is set to the face's center colour (since the center piece cannot be moved from the face). 
    
    Instance Attributes:
        center_colour (str, optional): String literal assigning a colour to the face's center piece. Defaults to None
        right (Face, optional): Face instance that is to the right of the current face in the Cube class. Defaults to None
        left (Face, optional): Face instance that is to the left of the current face in the Cube class. Defaults to None
        top (Face, optional): Face instance that is to the top of the current face in the Cube class. Becomes None if face is not a side face. Defaults to None
        bottom (Face, optional): Face instance that is to the bottom of the current face in the Cube class. Becomes None if face is not a side face. Defaults to None
        front (Face, optional): Face instance that is to the front of the current face in the Cube class. Becomes None if face is a side face. Defaults to None
        back (Face, optional): Face instance that is to the back of the current face in the Cube class. Becomes None if face is a side face. Defaults to None
        opposite (Face, optional): Face instance that points to the opposite face to the current face in the Cube class. Defaults to None
        is_side_face (bool, optional): bool value storing if the current face is a side face. Defaults to None
        grid (numpy.array, optional): 3 X 3 matrix that stores the pieces for the current face. Defaults to None
        
    Instance Methods:
        copy: Creates a duplicate instance of the Face class with the same values
        initialize_pieces: Initializes the face instance's grid
    """
    
    def __init__(self, 
                 colour: str = None, right: Face = None, left: Face = None, top: Face = None, bottom: Face = None, 
                 front: Face = None, back: Face = None, opposite: Face = None, is_side_face: bool = True, 
                 is_copy: bool = False, grid: np.ndarray = None) -> None:
        """
        Constructor method for the Face class.

        Args:
            colour (str, optional): String literal representing the colour of the face. Defaults to None.
            right (Face, optional): Face instance that is to the right of the current face in the Cube class. Defaults to None.
            left (Face, optional): Face instance that is to the left of the current face in the Cube class. Defaults to None.
            top (Face, optional): Face instance that is to the top of the current face in the Cube class. Becomes None 
                                  if current face instance is not a side face in the Cube class. Defaults to None.
            bottom (Face, optional): Face instance that is to the bottom of the current face in the Cube class. Becomes None 
                                  if current face instance is not a side face in the Cube class. Defaults to None.
            front (Face, optional): Face instance that is to the front of the current face in the Cube class. Becomes None 
                                  if the current face instance is a side face in the Cube class. Defaults to None.
            back (Face, optional): Face instance that is to the back of the current face in the Cube class. Becomes None 
                                  if the current face instance is a side face in the Cube class. Defaults to None.
            opposite (Face, optional): Face instance that is opposite to the current face in the Cube class. Defaults to None.
            is_side_face (bool, optional): bool value storing if the current face instance is a side face. Defaults to True.
            is_copy (bool, optional): bool value storing if the current Face instance is a copied version. Defaults to False.
            grid (numpy.array, optional): 3 X 3 matrix representing the pieces on the current Face instance. Defaults to None.
        """
        self.center_colour = colour
        self.right = right
        self.left = left
        self.top = top
        self.bottom = bottom
        self.front = front
        self.back = back
        self.opposite = opposite
        self.is_side_face = is_side_face
        
        if is_copy:
            self.grid = grid
        else:
            self.grid = self.initialize_pieces()
        
    def copy(self) -> Face:
        """
        This method creates and returns a duplicate Face instance with all attributes values copied.

        Returns:
            Face: Newly created Face instance with all attribute values copied
        """
        return Face(self.center_colour, self.right, self.left, self.top, self.bottom, self.front, self.back, self.opposite, self.is_side_face, is_copy=True, grid=self.grid.copy())
        
    def initialize_pieces(self) -> np.ndarray:
        """
        This method initializes the grid for the current face instance. It is represented by a 3 X 3 matrix.

        Returns:
            numpy.array: 3 X 3 matrix/array representing the grid for the current face instance.
        """
        ## Creating center piece
        center_piece = Piece(FacePositions.MID_CENTER, self, PieceType.CENTER)
        # colour = center_piece.colour[0]
        
        ## Creating edge pieces
        top_center_piece = EdgePiece(FacePositions.TOP_CENTER, self, PieceType.EDGE)
        mid_left_piece = EdgePiece(FacePositions.MID_LEFT, self, PieceType.EDGE)
        bottom_center_piece = EdgePiece(FacePositions.BOTTOM_CENTER, self, PieceType.EDGE)
        mid_right_piece = EdgePiece(FacePositions.MID_RIGHT, self, PieceType.EDGE)
        
        ## Creating corner pieces
        top_left_piece = CornerPiece(FacePositions.TOP_LEFT, self, PieceType.CORNER)
        top_right_piece = CornerPiece(FacePositions.TOP_RIGHT, self, PieceType.CORNER)
        bottom_left_piece = CornerPiece(FacePositions.BOTTOM_LEFT, self, PieceType.CORNER)
        bottom_right_piece = CornerPiece(FacePositions.BOTTOM_RIGHT, self, PieceType.CORNER)
        
        ## Creating the grid
        grid = [
            [top_left_piece, top_center_piece, top_right_piece],
            [mid_left_piece, center_piece, mid_right_piece],
            [bottom_left_piece, bottom_center_piece, bottom_right_piece]
        ]
        
        return np.array(grid)


#! DeprecationWarning: Class Row will not be used for this project and will be subsequently removed in future versions.
class Row:
    def __init__(self, left, center, right):
        self.left = left
        self.center = center
        self.right = right
        pass
    pass


#! DeprecationWarning: Class Column will not be used for this project and will be subsequently removed in future versions.
class Column:
    def __init__(self, top, center, bottom):
        self.top = top
        self.center = center
        self.bottom = bottom
        pass
    pass


class Piece:
    
    """
    This is a class that represents each piece on each face of the Rubix Cube.
    
    Instance Attributes:
        face_position (tuple): a tuple representing the index for the piece in the current face instance's grid
        face (Face): a pointer to the piece's current face instance
        _colour (str): a string property that stores the colour that is on the current piece instance
        _piece_type (str): a string property that stores the piece's type (Center, Edge, Corner)
    """
    
    def __init__(self, face_position: tuple, face: Face, piece_type: str) -> None:
        """
        Constructor method for the Piece Class.

        Args:
            face_position (tuple): tuple containing index position of current piece instance in current face instance
            face (Face): Face instance that contains the current Piece instance
            piece_type (str): String literal storing the type of piece the current Piece instance is
        """
        self.face_position = face_position
        self.face = face
        self._colour = self.face.center_colour
        self._piece_type = piece_type
        
    @property
    def colour(self) -> str:
        """
        This is a getter method for the Piece()._colour property. It returns the string literal stored in
        Piece()._colour.

        Returns:
            str: String literal storing the piece instance's colour
        """
        return self._colour
    
    @property
    def piece_type(self) -> str:
        """
        This is a getter method for the Piece()._piece_type property. It returns the string literal stored
        in Piece()._piece_type. 

        Returns:
            str: String literal storing the piece instance's type
        """
        return self._piece_type
        

class EdgePiece(Piece):
    
    """
    This is a class that represents each edge piece on each face of the Rubix Cube. This class inherits from
    the Piece class, inheriting some properties and attributes.
    
    Instance Attributes:
        face_position (tuple): a tuple representing the index for the piece in the current face instance's grid
        face (Face): a pointer to the piece's current face instance
        _colour (str): a string property that stores the colour that is on the current piece instance
        _piece_type (str): a string property that stores the piece's type (Center, Edge, Corner)
        _complement (EdgePiece): a pointer property to the Piece instance that is the current Piece instance's complement
    """
    
    def __init__(self, face_position: tuple, face: Face, piece_type: str, complement: Face = None) -> None:
        """
        Constructor method for the EdgePiece class.

        Args:
            face_position (tuple): tuple containing index position of current piece instance in current face instance
            face (Face): Face instance that contains the current Piece instance
            piece_type (str): String literal storing the type of piece the current Piece instance is
            complement (Piece, optional): A Piece instance pointing to the complement Piece instance. Defaults to None.
        """
        super().__init__(face_position, face, piece_type)
        self._complement = complement
        
    @property
    def complement(self) -> Face:
        """
        This is a getter method for the EdgePiece()._complement property. It returns the Piece object instance stored in
        CornerPiece()._complement.

        Returns:
            Piece: a Piece object property containing the Piece instance that is the current 
                   Piece instance's complement
        """
        return self._complement
    
    @complement.setter
    def complement(self, new_complement: Face) -> None:
        """
        This is a setter method for the EdgePiece()._complement property. It overrides the current value in
        EdgePiece()._complement with the value in new_complement.

        Args:
            new_complements (Piece): a Piece object property containing the Piece instance that is the current
                                     Piece instance's complement.
        """
        self._complement = new_complement
        
        
class CornerPiece(Piece):
    
    """
    This is a class that represents each corner piece on each face of the Rubix Cube. This class inherits from
    the Piece class, inheriting some properties and attributes.
    
    Instance Attributes:
        face_position (tuple): a tuple representing the index for the piece in the current face instance's grid
        face (Face): a pointer to the piece's current face instance
        _colour (str): a string property that stores the colour that is on the current piece instance
        _piece_type (str): a string property that stores the piece's type (Center, Edge, Corner)
        _complements (tuple): a tuple property containing pointers to the Piece instances that are the 
                              current Piece instance's complements
    """
    
    def __init__(self, face_position: tuple, face: Face, piece_type: str, complements: tuple = ()) -> None:
        """
        Constructor method for the CornerPiece class.

        Args:
            face_position (tuple): tuple containing index position of current piece instance in current face instance
            face (Face): Face instance that contains the current Piece instance
            piece_type (str): String literal storing the type of piece the current Piece instance is
            complements (tuple, optional): A tuple containing Piece instances that point to the current piece 
                                           instance's complements. Defaults to ().
        """
        super().__init__(face_position, face, piece_type)
        self._complements = complements
        
    @property
    def complements(self) -> tuple:
        """
        This is a getter method for the CornerPiece()._complements property. It returns the tuple stored in
        CornerPiece()._complements.

        Returns:
            tuple: a tuple property containing pointers to the Piece instances that are the current 
                   Piece instance's complements
        """
        return self._complements
    
    @complements.setter
    def complements(self, new_complements: tuple) -> None:
        """
        This is a setter method for the CornerPiece()._complements property. It overrides the current value in
        CorenerPiece()._complements with the value in new_complements.

        Args:
            new_complements (tuple): a tuple containing pointers to the Piece instances that are the current
                                     Piece instance's complements.
        """
        self._complements = new_complements
    
    
if __name__ == "__main__":
    cube = RubixCube()
    op_stack, error_stack = cube.move(PossibleOperations.SHUFFLE_CUBE)
    print(cube)
    print(op_stack)
    print(error_stack)
    