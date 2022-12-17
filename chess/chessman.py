from chess.coord import Coord
from chess.enum_types import *


class Chessman:

    def __init__(self, x: int, y: int, piece_type: Piece, color: Color):
        self.coord = Coord(x, y)
        self.color = color
        self.type = piece_type

    def __eq__(self, other):
        if self.coord == other.coord and self.color == other.color and self.type == other.type:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.coord != other.coord or self.color != other.color or self.type != other.type:
            return True
        else:
            return False

    def __iter__(self):
        yield self.coord.x
        yield self.coord.y
        yield self.type
        yield self.color

    def __str__(self):
        return str(self.color) + ' ' + str(self.type) + ' ' + str(self.coord)

    def is_white(self):
        if self.color == Color.white:
            return True
        else:
            return False

    def is_legal(self, start: Coord, end: Coord):
        return False
    # def is_legal(self, move: Coord):
    #     if self.type == Piece.queen:
    #         return self.coord.queen(move)
    #     if self.type == Piece.rook:
    #         return self.coord.rook(move)
    #     if self.type == Piece.bishop:
    #         return self.coord.bishop(move)
    #     if self.type == Piece.knight:
    #         if self.coord.knight(move):
    #             return True
    #     if self.type == Piece.pawn:
    #         if self.color == Color.white:
    #             iter = Coord(self.coord.x, self.coord.y)
    #             if iter.iterate_up():
    #                 if iter == move:
    #                     return True
    #             if iter.iterate_up():
    #                 if iter == move:
    #                     return True
    #             iter.x, iter.y = (self.coord.x, self.coord.y)
    #             if iter.iterate_right_up():
    #                 if iter == move:
    #                     return True
    #             iter.x, iter.y = (self.coord.x, self.coord.y)
    #             if iter.iterate_left_up():
    #                 if iter == move:
    #                     return True
    #             return False
    #         if self.color == Color.black:
    #             iter = Coord(self.coord.x, self.coord.y)
    #             if iter.iterate_down():
    #                 if iter == move:
    #                     return True
    #             if iter.iterate_down():
    #                 if iter == move:
    #                     return True
    #             iter.x, iter.y = (self.coord.x, self.coord.y)
    #             if iter.iterate_right_down():
    #                 if iter == move:
    #                     return True
    #             iter.x, iter.y = (self.coord.x, self.coord.y)
    #             if iter.iterate_left_down():
    #                 if iter == move:
    #                     return True
    #             return False
    #     if self.type == Piece.king:
    #         if self.coord.king(move):
    #             return True
    #     return False
