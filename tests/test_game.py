from chess.game import *


# Chessman(8, 4, Piece.queen, Color.black)

def set_game():
    game = Game(Game.empty_init(), Color.black)
    game.get_square(Coord(5, 1)).piece = King(5, 1, Piece.king, Color.white)
    game.get_square(Coord(5, 8)).piece = King(5, 8, Piece.king, Color.black)
    game.get_square(Coord(4, 5)).piece = Queen(4, 5, Piece.queen, Color.white)
    return game


def test_is_legal_queen_king_1():
    game = set_game()
    assert not game.is_legal(Coord(5, 8), Coord(4, 8))


def test_is_legal_queen_king_2():
    game = set_game()
    assert not game.is_legal(Coord(5, 8), Coord(6, 7))


def test_is_legal_queen_king_3():
    game = set_game()
    assert game.is_legal(Coord(5, 8), Coord(5, 7))


def test_is_legal_queen_king_4():
    game = set_game()
    assert game.is_legal(Coord(5, 8), Coord(6, 8))


def test_is_legal_queen_king_5():
    game = set_game()
    assert not game.is_legal(Coord(5, 8), Coord(4, 7))


# def test_is_legal_two_queens_1():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(Game.empty_init(), Color.black)
#     game.get_square(Coord(5, 1)).piece = King(5, 1, Piece.king, Color.white)
#     game.get_square(Coord(5, 1)).piece = King(5, 8, Piece.king, Color.black)
#     game.get_square(Coord(5, 1)).piece = Queen(4, 5, Piece.queen, Color.white)
#     assert not game.is_legal(Coord(6, 8), test[1])


# def test_is_legal_two_queens_2():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(Game.empty_init(), Color.black)
#     game.get_square(Coord(5, 1)).piece = King(5, 1, Piece.king, Color.white)
#     game.get_square(Coord(5, 1)).piece = King(5, 8, Piece.king, Color.black)
#     game.get_square(Coord(5, 1)).piece = Queen(4, 5, Piece.queen, Color.white)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_taken():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.bishop, Color.white)]
#     game = Game(test, Color.black)
#     game.move(Coord(6, 8), game.blacks.index(test[1]))
#     assert len(game.whites) == 2
#
#
# def test_check_obstacle_1():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(1, 3, Piece.queen, Color.white),
#         Chessman(3, 5, Piece.bishop, Color.white)]
#     game = Game(test, Color.white)
#     assert not game.is_legal(Coord(5, 7), test[2])
#
#
# def test_check_obstacle_2():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(1, 3, Piece.queen, Color.white),
#         Chessman(3, 5, Piece.bishop, Color.white)]
#     game = Game(test, Color.white)
#     assert not game.is_legal(Coord(6, 8), test[2])
#
#
# def test_check_obstacle_3():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(1, 3, Piece.queen, Color.white),
#         Chessman(3, 5, Piece.bishop, Color.white)]
#     game = Game(test, Color.white)
#     assert game.is_legal(Coord(2, 4), test[2])


# def test_check_game_1():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert not game.is_legal(Coord(4, 6), pieces[1])
#
#
# def test_check_game_1_2():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white)]
#     game = Game(pieces, Color.black)
#     assert game.is_legal(Coord(4, 5), pieces[1])
#
#
# def test_check_game_1_3():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white)]
#     game = Game(pieces, Color.black)
#     assert game.is_legal(Coord(4, 6), pieces[1])
#
#
# def test_check_game_1_5():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert not game.is_legal(Coord(4, 5), pieces[1])
#
#
# def test_check_game_1_7():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert not game.is_legal(Coord(4, 6), pieces[1])
#
#
# def test_check_game_2():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert game.is_legal(Coord(5, 6), pieces[2])
#
#
# def test_check_game_2_1():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(5, 6, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white)]
#     game = Game(pieces, Color.white)
#     assert not game.is_legal(Coord(5, 8), pieces[3])
#
#
# def test_check_game_2_2():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 6, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.white)
#     assert not game.is_legal(Coord(5, 8), pieces[4])
#
#
# def test_check_game_2_3():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert game.is_legal(Coord(5, 5), pieces[2])
#
#
# def test_check_game_2_5():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert game.is_legal(Coord(5, 6), pieces[2])
#
#
# def test_check_game_2_7():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(5, 7, Piece.pawn, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert game.is_legal(Coord(5, 5), pieces[2])
#
#
# def test_check_game_3():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(8, 7, Piece.rook, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert not game.is_legal(Coord(5, 7), pieces[0])
#
#
# def test_check_game_3_1():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(8, 7, Piece.rook, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert game.is_legal(Coord(6, 7), pieces[0])
#
#
# def test_check_game_3_2():
#     pieces = [
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 7, Piece.pawn, Color.black),
#         Chessman(8, 7, Piece.rook, Color.black),
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 2, Piece.queen, Color.white),
#         Chessman(2, 5, Piece.bishop, Color.white)]
#     game = Game(pieces, Color.black)
#     assert game.is_legal(Coord(5, 7), pieces[2])
