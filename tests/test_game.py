from chess.game import *


# Chessman(8, 4, Piece.queen, Color.black)


def test_is_legal_queen_king_1():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(4, 5, Piece.queen, Color.white)]
    game = Game(test, Color.black)
    assert not game.is_legal(Coord(4, 8), test[1])


def test_is_legal_queen_king_2():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(4, 5, Piece.queen, Color.white)]
    game = Game(test, Color.black)
    assert not game.is_legal(Coord(6, 7), test[1])


def test_is_legal_queen_king_3():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(4, 5, Piece.queen, Color.white)]
    game = Game(test, Color.black)
    assert game.is_legal(Coord(5, 7), test[1])


def test_is_legal_queen_king_4():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(4, 5, Piece.queen, Color.white)]
    game = Game(test, Color.black)
    assert game.is_legal(Coord(6, 8), test[1])


def test_is_legal_queen_king_5():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(4, 5, Piece.queen, Color.white)]
    game = Game(test, Color.black)
    assert not game.is_legal(Coord(4, 7), test[1])


def test_is_legal_two_queens_1():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(4, 5, Piece.queen, Color.white),
        Chessman(6, 8, Piece.queen, Color.black)]
    game = Game(test, Color.black)
    assert not game.is_legal(Coord(6, 8), test[1])


def test_is_legal_two_queens_2():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(4, 5, Piece.queen, Color.white),
        Chessman(6, 8, Piece.queen, Color.white)]
    game = Game(test, Color.black)
    assert game.is_legal(Coord(6, 8), test[1])


def test_taken():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(4, 5, Piece.queen, Color.white),
        Chessman(6, 8, Piece.bishop, Color.white)]
    game = Game(test, Color.black)
    game.move(Coord(6, 8), game.blacks.index(test[1]))
    assert len(game.whites) == 2


def test_check_obstacle_1():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(1, 3, Piece.queen, Color.white),
        Chessman(3, 5, Piece.bishop, Color.white)]
    game = Game(test, Color.white)
    assert not game.is_legal(Coord(5, 7), test[2])


def test_check_obstacle_2():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(1, 3, Piece.queen, Color.white),
        Chessman(3, 5, Piece.bishop, Color.white)]
    game = Game(test, Color.white)
    assert not game.is_legal(Coord(6, 8), test[2])


def test_check_obstacle_3():
    test = [
        Chessman(5, 1, Piece.king, Color.white),
        Chessman(5, 8, Piece.king, Color.black),
        Chessman(1, 3, Piece.queen, Color.white),
        Chessman(3, 5, Piece.bishop, Color.white)]
    print(test[2])
    game = Game(test, Color.white)
    assert game.is_legal(Coord(2, 4), test[2])

