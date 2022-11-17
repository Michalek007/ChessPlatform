from chess.chessman import Chessman
from chess.enum_types import *
from chess.coord import Coord


class Pawn(Chessman):
    def __init__(self, x: int, y: int, piece_type: Piece, color: Color):
        super().__init__(x, y, piece_type, color)

    def is_legal(self, move: Coord):
        iter = Coord(self.coord.x, self.coord.y)
        if self.is_white():
            if iter.iterate_up():
                if iter == move:
                    return True
            if iter.iterate_up():
                if iter == move:
                    return True
            iter.x, iter.y = (self.coord.x, self.coord.y)
            if iter.iterate_right_up():
                if iter == move:
                    return True
            iter.x, iter.y = (self.coord.x, self.coord.y)
            if iter.iterate_left_up():
                if iter == move:
                    return True
            return False
        else:
            if iter.iterate_down():
                if iter == move:
                    return True
            if iter.iterate_down():
                if iter == move:
                    return True
            iter.x, iter.y = (self.coord.x, self.coord.y)
            if iter.iterate_right_down():
                if iter == move:
                    return True
            iter.x, iter.y = (self.coord.x, self.coord.y)
            if iter.iterate_left_down():
                if iter == move:
                    return True
            return False

    @staticmethod
    def get_symbol():
        return "P"
