from chess.chessman import Chessman
from chess.enum_types import *
from chess.coord import Coord


class Pawn(Chessman):
    def __init__(self, x: int, y: int, piece_type: Piece, color: Color):
        super().__init__(x, y, piece_type, color)

    def is_legal(self, start: Coord, end: Coord):
        if start.is_equal(end):
            return False
        if self.is_white():
            if start.x == end.x:
                if start.y + 1 == end.y:
                    return True
                if start.y + 2 == end.y:
                    return True
            else:
                if start.y + 1 == end.y:
                    if start.x - 1 == end.x:
                        return True
                    if start.x + 1 == end.x:
                        return True
                return False
        else:
            if start.x == end.x:
                if start.y - 1 == end.y:
                    return True
                if start.y - 2 == end.y:
                    return True
            else:
                if start.y - 1 == end.y:
                    if start.x - 1 == end.x:
                        return True
                if start.x + 1 == end.x:
                    return True
            return False

    @staticmethod
    def get_symbol():
        return "P"
