from chess.coord import Coord
from chess.enum_types import Color, Piece
from chess.chessman import Chessman
from chess.game import Game
# import timeit
#
# setup = """from chess.coord import Coord
# from chess.enum_types import Color, Piece
# from chess.chessman import Chessman
# from chess.game import Game
# test = [
#     Chessman(5, 1, Piece.king, Color.white),
#     Chessman(5, 8, Piece.king, Color.black),
#     Chessman(4, 5, Piece.queen, Color.white),
#     Chessman(1, 1, Piece.queen, Color.black)]
# game = Game(test, Color.black)"""
#
# code1 = "game.check_obstacle(Chessman(1, 1, Piece.queen, Color.black), Coord(8, 8))"
# code2 = "game.check_obstacle2(Chessman(1, 1, Piece.queen, Color.black), Coord(8, 8))"
#
# if __name__ == '__main__':
#     print(timeit.timeit(setup=setup, stmt=code1, number=100000))
#     print(timeit.timeit(setup=setup, stmt=code2, number=100000))
#     # point = Coord(1, 2)
#     # queen = Chessman(1, 1, Piece.queen, Color.white)
#     # queen2 = Chessman(1, 1, Piece.queen, Color.black)
#     # queen3 = Chessman(1, 1, Piece.queen, Color.white)
#     # if queen != queen2:
#     #     print('test1')
#     # if queen == queen3:
#     #     print('test2')
#     # for i in range(8):
#     #     point.iterate_right_up()
#     #     print(str(point))
#     # for item in point:
#     #     print(item)
