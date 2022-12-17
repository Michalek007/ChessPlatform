from chess.chessman import Chessman
from chess.enum_types import *
from chess.coord import Coord


class Bishop(Chessman):
    def __init__(self, x: int, y: int, piece_type: Piece, color: Color):
        super().__init__(x, y, piece_type, color)

    def is_legal(self, start: Coord, end: Coord):
        if start.is_equal(end):
            return False
        if start.is_diagonal(end):
            return True
        return False

    @staticmethod
    def get_symbol():
        return "B"
