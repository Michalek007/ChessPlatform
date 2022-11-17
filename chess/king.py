from chess.chessman import Chessman
from chess.enum_types import *
from chess.coord import Coord


class King(Chessman):
    def __init__(self, x: int, y: int, piece_type: Piece, color: Color):
        super().__init__(x, y, piece_type, color)

    def is_legal(self, move:Coord):
        return True

    def is_white(self):
        if self.color == Color.white:
            return True
        else:
            return False

    def get_symbol(self):
        return "K"
