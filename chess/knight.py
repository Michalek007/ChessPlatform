from chess.chessman import Chessman
from chess.enum_types import *
from chess.coord import Coord


class Knight(Chessman):
    def __init__(self, x: int, y: int, piece_type: Piece, color: Color):
        super().__init__(x, y, piece_type, color)

    def is_legal(self, start: Coord, end: Coord):
        if start.is_equal(end):
            return False
        if start.is_diagonal(end):
            return False
        if start.x_axis_distance(end) == 1 and start.y_axis_distance(end) == 2:
            return True
        if start.x_axis_distance(end) == 2 and start.y_axis_distance(end) == 1:
            return True
        return False

    @staticmethod
    def get_symbol():
        return "N"
