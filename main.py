from chess.coord import *
from chess.enum_types import *
from chess.chessman import Chessman


if __name__ == '__main__':
    point = Coord(1, 2)
    queen = Chessman(1, 1, Piece.queen, Color.white)
    queen2 = Chessman(1, 1, Piece.queen, Color.black)
    queen3 = Chessman(1, 1, Piece.queen, Color.white)
    if queen != queen2:
        print('test1')
    if queen == queen3:
        print('test2')
    for i in range(8):
        point.iterate_right_up()
        print(str(point))
    for item in point:
        print(item)
