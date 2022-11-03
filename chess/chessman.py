from chess.coord import Coord
from chess.enum_types import *


class Chessman:
    # def is_legal(self, move: Coord, test):

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

    def is_legal(self, move: Coord):
        if self.type == Piece.queen:
            return self.coord.queen(move)
        if self.type == Piece.rook:
            return self.coord.rook(move)
        if self.type == Piece.bishop:
            return self.coord.bishop(move)
        if self.type == Piece.knight:
            if self.coord.iterate_l(move):
                return True
        if self.type == Piece.pawn:
            if self.color == Color.white:
                iter = Coord(self.coord.x, self.coord.y)
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
            if self.color == Color.black:
                iter = Coord(self.coord.x, self.coord.y)
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
        if self.type == Piece.king:
            if self.coord.iterate_surround(move):
                return True
        return False

# for dir in Chessman.direction:
#     iter = Coord(self.coord.x, self.coord.y)
#     if iter.iterate(dir, move):
#         return True

#     if self.type == Piece.queen:
    #         if self.coord.iterate_horizontal(move):
    #             return True
    #         if self.coord.iterate_vertical(move):
    #             return True
    #         if self.coord.iterate_diagonal(move):
    #             return True
    #     if self.type == Piece.rook:
    #         if self.coord.iterate_horizontal(move):
    #             return True
    #         if self.coord.iterate_vertical(move):
    #             return True
    #     if self.type == Piece.bishop:
    #         if self.coord.iterate_diagonal(move):
    #             return True
    #     if self.type == Piece.knight:
    #         if self.coord.iterate_l(move):
    #             return True
    #     if self.type == Piece.pawn:
    #         iter = Coord(self.coord.x, self.coord.y)
    #         if self.color == Color.white:
    #             iter = Coord(self.coord.x, self.coord.y)
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
    #         if self.coord.iterate_surround(move):
    #             return True
    #     return False

            # iter = Coord(self.coord.x, self.coord.y)
            # while True:
            #     if not iter.iterate_right():
            #         break
            #     if iter == move:
            #         return True
            # iter.x, iter.y = (self.coord.x, self.coord.y)
            # while True:
            #     if not iter.iterate_left():
            #         break
            #     if iter == move:
            #         return True
            # iter.x, iter.y = (self.coord.x, self.coord.y)
            # while True:
            #     if not iter.iterate_up():
            #         break
            #     if iter == move:
            #         return True
            # iter.x, iter.y = (self.coord.x, self.coord.y)
            # while True:
            #     if not iter.iterate_down():
            #         break
            #     if iter == move:
            #         return True
            # iter.x, iter.y = (self.coord.x, self.coord.y)
            # while True:
            #     if not iter.iterate_right_up():
            #         break
            #     if iter == move:
            #         return True
            # iter.x, iter.y = (self.coord.x, self.coord.y)
            # while True:
            #     if not iter.iterate_right_down():
            #         break
            #     if iter == move:
            #         return True
            # iter.x, iter.y = (self.coord.x, self.coord.y)
            # while True:
            #     if not iter.iterate_left_up():
            #         break
            #     if iter == move:
            #         return True
            # iter.x, iter.y = (self.coord.x, self.coord.y)
            # while True:
            #     if not iter.iterate_left_down():
            #         break
            #     if iter == move:
            #         return True
            # return False

            # for dir in Chessman.direction:
            #     iter = Coord(self.coord.x, self.coord.y)
            #     if iter.iterate(dir, move):
            #         return True
