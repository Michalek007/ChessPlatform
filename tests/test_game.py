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


# def test_is_legal_queen_king_9():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_is_legal_queen_king_10():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_is_legal_queen_king_11():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_legal_queen_king_12():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_legal_queen_king_13():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_is_legal_two_queens_14():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_legal_two_queens_15():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_taken16():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.bishop, Color.white)]
#     game = Game(test, Color.black)
#     game.move(Coord(6, 8), game.blacks.index(test[1]))
#     assert len(game.whites) == 2
#
# def test_is_legal_queen_king_17():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_is_legal_queen_king_18():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_is_legal_queen_king_19():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_legal_queen_king_20():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_legal_queen_king_21():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_is_legal_two_queens_22():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_legal_two_queens_23():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_taken24():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.bishop, Color.white)]
#     game = Game(test, Color.black)
#     game.move(Coord(6, 8), game.blacks.index(test[1]))
#     assert len(game.whites) == 2
#
# def test_is_legal_queen_king_25():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_is_legal_queen_king_26():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_is_legal_queen_king_27():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_legal_queen_king_28():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_legal_queen_king_29():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_is_legal_two_queens_30():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_legal_two_queens_31():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_taken32():
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
# def test_is_legal_queen_king_33():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_is_legal_queen_king_34():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_is_legal_queen_king_35():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_legal_queen_king_36():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_legal_two_queens_39():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_taken40():
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
# def test_is_legal_queen_king_37():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_is_legal_two_queens_38():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
#
#
# def test_2is_legal_queen_king_1():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_2is_legal_queen_king_2():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_2is_legal_queen_king_3():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_lega2l_queen_king_4():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_leg2al_queen_king_5():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_is_le2gal_two_queens_1():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_l2egal_two_queens_2():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_tak2en():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.bishop, Color.white)]
#     game = Game(test, Color.black)
#     game.move(Coord(6, 8), game.blacks.index(test[1]))
#     assert len(game.whites) == 2
#
# def test_is_legal2_queen_king_9():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_is_lega2l_queen_king_10():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_is_leg2al_queen_king_11():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_le2gal_queen_king_12():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_l2egal_queen_king_13():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_is_2legal_two_queens_14():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is2_legal_two_queens_15():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_t2aken16():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.bishop, Color.white)]
#     game = Game(test, Color.black)
#     game.move(Coord(6, 8), game.blacks.index(test[1]))
#     assert len(game.whites) == 2
#
# def test_is_lega2l_queen_king_17():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_is_leg2al_queen_king_18():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_is_le2gal_queen_king_19():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_l2egal_queen_king_20():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_2legal_queen_king_21():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_is2_legal_two_queens_22():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
#
#
# def test_i2s_legal_two_queens_23():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_2taken24():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.bishop, Color.white)]
#     game = Game(test, Color.black)
#     game.move(Coord(6, 8), game.blacks.index(test[1]))
#     assert len(game.whites) == 2
#
# def test_is_lega2l_queen_king_25():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_is_leg2al_queen_king_26():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_is_le2gal_queen_king_27():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_l2egal_queen_king_28():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_2legal_queen_king_29():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_is2_legal_two_queens_30():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
#
#
# def test_i2s_legal_two_queens_31():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_2taken32():
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
# def test_is_lega2l_queen_king_33():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 8), test[1])
#
#
# def test_is_leg2al_queen_king_34():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 7), test[1])
#
#
# def test_is_le2gal_queen_king_35():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(5, 7), test[1])
#
#
# def test_is_l2egal_queen_king_36():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_is_2legal_two_queens_39():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert game.is_legal(Coord(6, 8), test[1])
#
#
# def test_ta2ken40():
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
# def test_i2s_legal_queen_king_37():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(4, 7), test[1])
#
#
# def test_2is_legal_two_queens_38():
#     test = [
#         Chessman(5, 1, Piece.king, Color.white),
#         Chessman(5, 8, Piece.king, Color.black),
#         Chessman(4, 5, Piece.queen, Color.white),
#         Chessman(6, 8, Piece.queen, Color.black)]
#     game = Game(test, Color.black)
#     assert not game.is_legal(Coord(6, 8), test[1])
