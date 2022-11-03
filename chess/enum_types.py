import enum


class Piece(enum.Enum):

    pawn = 0
    knight = 1
    bishop = 2
    rook = 3
    queen = 4
    king = 5


class Direction(enum.Enum):

    right = 0
    left = 1
    up = 2
    down = 3
    right_up = 4
    right_down = 5
    left_up = 6
    left_down = 7


class Color(enum.Enum):

    black = 0
    white = 1
