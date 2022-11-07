from chess.coord import Coord
from chess.enum_types import Color, Piece
from chess.chessman import Chessman
from chess.game import Game

# test = [
#     Chessman(5, 1, Piece.king, Color.white),
#     Chessman(5, 8, Piece.king, Color.black),
#     Chessman(4, 5, Piece.queen, Color.white),
#     Chessman(1, 1, Piece.queen, Color.black)]
# game = Game(test, Color.black)
#
# print(game.check_square(Coord(5, 8)))


game = Game(Game.init())

while True:
    print(game)
    x = int(input())
    y = int(input())
    piece = game.get_piece(Coord(x, y))
    print(piece)
    if not piece:
        continue
    a = int(input())
    b = int(input())
    if not game.make_move(piece=piece, move=Coord(a, b)):
        continue
    print(game)
