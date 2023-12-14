from Constraints import FacePositions, PieceType
import Predicates


def get_num_edge_pieces(face):
    counter = 0
    for position in FacePositions.POSITIONS:
        
        pass
    pass

def get_count_complements(piece):
    if piece.piece_type == PieceType.CORNER:
        try:
            if len(piece.complements) == 2:
                return 2
            else:
                raise ValueError(f'Number of complements = {len(piece.complements)} ≠ 2')
        except(TypeError):
            raise TypeError(f'Received Type: {piece}\nExpected Type: tuple')
    else:
        pass
    pass
