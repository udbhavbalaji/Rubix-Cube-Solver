import numpy as np
import unittest
from cube_init import Face, Piece, CornerPiece, EdgePiece
from Constraints import Axes, Colours, FacePositions, PieceType
from Transformations import GridTransformations
from Predicates import GridPredicates, PiecePredicates
from errors import ArgumentTypeError

class TestGridPredicates(unittest.TestCase):
    
    def setUp(self):
        self.face = Face('Blue')
        self.test_grid = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.face.grid = np.array(self.test_grid)
        pass
    
    def tearDown(self):
        pass
    
    
    def test_are_grids_equal(self):
        self.assertTrue(GridPredicates.are_grids_equal(self.face.grid, self.face.grid))
        self.assertFalse(GridPredicates.are_grids_equal(self.face.grid, np.flip(self.face.grid)))
        self.assertRaises(ArgumentTypeError, GridPredicates.are_grids_equal, self.face, self.face.grid) 
        
    pass


class TestPiecePredicates(unittest.TestCase):
    
    def setUp(self):
        face = Face('Blue')
        self.piece = Piece(FacePositions.MID_CENTER, face, PieceType.CENTER)
        self.edge_piece = EdgePiece(FacePositions.TOP_CENTER, face, PieceType.EDGE)
        self.corner_piece = CornerPiece(FacePositions.TOP_LEFT, face, PieceType.CORNER)
    
    def tearDown(self):
        pass
    
    
    def test_are_pieces_equal(self):
        self.assertTrue(PiecePredicates.are_pieces_equal(self.piece, self.piece))
        self.assertFalse(PiecePredicates.are_pieces_equal(self.piece, self.edge_piece))
        
        self.assertTrue(PiecePredicates.are_pieces_equal(self.edge_piece, self.edge_piece))
        self.assertFalse(PiecePredicates.are_pieces_equal(self.corner_piece, self.edge_piece))
        
        self.assertTrue(PiecePredicates.are_pieces_equal(self.corner_piece, self.corner_piece))
        self.assertFalse(PiecePredicates.are_pieces_equal(self.piece, self.corner_piece))
        
    def test_is_edge_piece(self):
        self.assertTrue(PiecePredicates.is_edge_piece(self.edge_piece))
        self.assertFalse(PiecePredicates.is_edge_piece(self.piece))
        self.assertFalse(PiecePredicates.is_edge_piece(self.corner_piece))
    
    def test_is_corner_piece(self):
        self.assertTrue(PiecePredicates.is_corner_piece(self.corner_piece))
        self.assertFalse(PiecePredicates.is_corner_piece(self.piece))
        self.assertFalse(PiecePredicates.is_corner_piece(self.edge_piece))
    
    def test_is_center_piece(self):
        self.assertTrue(PiecePredicates.is_center_piece(self.piece))
        self.assertFalse(PiecePredicates.is_center_piece(self.corner_piece))
        self.assertFalse(PiecePredicates.is_center_piece(self.edge_piece))

    @unittest.expectedFailure
    def test_is_num_complements_corner_correct(self):
        self.assertTrue(PiecePredicates.is_num_complements_corner_correct(self.corner_piece))
        self.assertFalse(PiecePredicates.is_num_complements_corner_correct(self.edge_piece))
        self.assertFalse(PiecePredicates.is_num_complements_corner_correct(self.piece))
        self.assertRaises(ArgumentTypeError, PiecePredicates.is_num_complements_corner_correct, Face('White'))

    @unittest.expectedFailure
    def test_is_num_complements_edge_correct(self):
        self.assertTrue(PiecePredicates.is_num_complements_edge_correct(self.edge_piece))
        self.assertFalse(PiecePredicates.is_num_complements_edge_correct(self.corner_piece))
        self.assertFalse(PiecePredicates.is_num_complements_edge_correct(self.piece))
        self.assertRaises(ArgumentTypeError, PiecePredicates.is_num_complements_corner_correct, Face('White'))
        
        pass
    
    pass
