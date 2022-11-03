from chess import *


# queen is_legal() test
def test_queen_is_legal_1():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert queen.is_legal(Coord(1, 1))


def test_queen_is_legal_2():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert queen.is_legal(Coord(8, 8))


def test_queen_is_legal_3():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert not queen.is_legal(Coord(1, 8))


def test_queen_is_legal_4():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert not queen.is_legal(Coord(8, 1))


def test_queen_is_legal_5():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert queen.is_legal(Coord(1, 4))


def test_queen_is_legal_6():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert queen.is_legal(Coord(4, 8))


def test_queen_is_legal_7():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert not queen.is_legal(Coord(3, 6))


def test_queen_is_legal_8():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert not queen.is_legal(Coord(3, 6))


def test_queen_is_legal_9():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert queen.is_legal(Coord(4, 5))


def test_queen_is_legal_10():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert queen.is_legal(Coord(4, 6))


def test_queen_is_legal_11():
    queen = Chessman(4, 4, Piece.queen, Color.white)
    assert queen.is_legal(Coord(4, 7))


def test_queen_is_legal_12():
    queen = Chessman(7, 6, Piece.queen, Color.white)
    assert queen.is_legal(Coord(7, 7))


# king is_legal() test
def test_king_is_legal_1():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert king.is_legal(Coord(4, 5))


def test_king_is_legal_2():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert king.is_legal(Coord(5, 4))


def test_king_is_legal_3():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert king.is_legal(Coord(5, 5))


def test_king_is_legal_4():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert king.is_legal(Coord(3, 4))


def test_king_is_legal_5():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert king.is_legal(Coord(4, 3))


def test_king_is_legal_6():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert king.is_legal(Coord(3, 5))


def test_king_is_legal_7():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert king.is_legal(Coord(5, 3))


def test_king_is_legal_8():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert king.is_legal(Coord(3, 3))


def test_king_is_legal_9():
    king = Chessman(4, 4, Piece.king, Color.white)
    assert not king.is_legal(Coord(6, 4))


def test_king_is_legal_10():
    king = Chessman(8, 8, Piece.king, Color.white)
    assert not king.is_legal(Coord(9, 8))


# knight is_legal() test
def test_knight_is_legal_1():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert knight.is_legal(Coord(6, 3))


def test_knight_is_legal_2():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert knight.is_legal(Coord(6, 5))


def test_knight_is_legal_3():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert knight.is_legal(Coord(2, 3))


def test_knight_is_legal_4():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert knight.is_legal(Coord(2, 5))


def test_knight_is_legal_5():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert knight.is_legal(Coord(5, 2))


def test_knight_is_legal_6():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert knight.is_legal(Coord(3, 2))


def test_knight_is_legal_7():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert knight.is_legal(Coord(3, 6))


def test_knight_is_legal_8():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert knight.is_legal(Coord(5, 6))


def test_knight_is_legal_9():
    knight = Chessman(4, 4, Piece.knight, Color.white)
    assert not knight.is_legal(Coord(4, 5))


def test_knight_is_legal_10():
    knight = Chessman(5, 8, Piece.knight, Color.white)
    assert not knight.is_legal(Coord(7, 9))


#####
# def test_1queen_is_legal_1():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(1, 1))
#
#
# def test_quee1n_is_legal_2():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(8, 8))
#
#
# def test_que1en_is_legal_3():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(1, 8))
#
#
# def test_qu1een_is_legal_4():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(8, 1))
#
#
# def test_q1ueen_is_legal_5():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(1, 4))
#
#
# def test_1queen_is_legal_6():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 8))
#
#
# def test_queen_is_legal_71():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(3, 6))
#
#
# def test_queen_is_legal_18():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(3, 6))
#
#
# def test_queen_is_legal1_9():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 5))
#
#
# def test_queen_is_lega1l_10():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 6))
#
#
# def test_queen_is_leg1al_11():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 7))
#
#
# def test_queen_is_le1gal_12():
#     queen = Chessman(7, 6, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(7, 7))
#
#
# # king is_legal() test
# def test_king_is_le1gal_1():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(4, 5))
#
#
# def test_king_is_l1egal_2():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 4))
#
#
# def test_king_is_1legal_3():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 5))
#
#
# def test_king_is1_legal_4():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 4))
#
#
# def test_king_i1s_legal_5():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(4, 3))
#
#
# def test_king_1is_legal_6():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 5))
#
#
# def test_king1_is_legal_7():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 3))
#
#
# def test_kin1g_is_legal_8():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 3))
#
#
# def test_ki1ng_is_legal_9():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert not king.is_legal(Coord(6, 4))
#
#
# def test_k1ing_is_legal_10():
#     king = Chessman(8, 8, Piece.king, Color.white)
#     assert not king.is_legal(Coord(9, 8))
#
#
# # knight is_legal() test
# def test_1knight_is_legal_1():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(6, 3))
#
#
# def test_knight_is_legal_21():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(6, 5))
#
#
# def test_knight_is_legal_13():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(2, 3))
#
#
# def test_knight_is_legal1_4():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(2, 5))
#
#
# def test_knight_is_lega1l_5():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(5, 2))
#
#
# def test_knight_is_leg1al_6():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(3, 2))
#
#
# def test_knight_is_le1gal_7():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(3, 6))
#
#
# def test_knight_is_l1egal_8():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(5, 6))
#
#
# def test_knight_is_1legal_9():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert not knight.is_legal(Coord(4, 5))
#
#
# def test_knight_is1_legal_10():
#     knight = Chessman(5, 8, Piece.knight, Color.white)
#     assert not knight.is_legal(Coord(7, 9))
#
#
# def test_queen_is1_legal_1():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(1, 1))
#
#
# def test_queen_i1s_legal_2():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(8, 8))
#
#
# def test_queen_1is_legal_3():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(1, 8))
#
#
# def test_queen1_is_legal_4():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(8, 1))
#
#
# def test_quee1n_is_legal_5():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(1, 4))
#
#
# def test_que1en_is_legal_6():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 8))
#
#
# def test_qu1een_is_legal_7():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(3, 6))
#
#
# def test_q1ueen_is_legal_8():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(3, 6))
#
#
# def test_1queen_is_legal_9():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 5))
#
#
# def test_queen_is_legal_101():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 6))
#
#
# def test_queen_is_legal_111():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 7))
#
#
# def test_queen_is_legal_112():
#     queen = Chessman(7, 6, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(7, 7))
#
#
# # king is_legal() test
# def test_king_is_legal_11():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(4, 5))
#
#
# def test_king_is_legal1_2():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 4))
#
#
# def test_king_is_lega1l_3():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 5))
#
#
# def test_king_is_legal_14():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 4))
#
#
# def test_king_is_legal_15():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(4, 3))
#
#
# def test_king_is_legal_16():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 5))
#
#
# def test_king_is_legal1_7():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 3))
#
#
# def test_king_is_lega1l_8():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 3))
#
#
# def test_king_is_leg1al_9():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert not king.is_legal(Coord(6, 4))
#
#
# def test_king_is_le1gal_10():
#     king = Chessman(8, 8, Piece.king, Color.white)
#     assert not king.is_legal(Coord(9, 8))
#
#
# # knight is_legal() test
# def test_knight_is1_legal_1():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(6, 3))
#
#
# def test_knight_i1s_legal_2():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(6, 5))
#
#
# def test_knight_1is_legal_3():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(2, 3))
#
#
# def test_knight1_is_legal_4():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(2, 5))
#
#
# def test_knigh1t_is_legal_5():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(5, 2))
#
#
# def test_knig1ht_is_legal_6():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(3, 2))
#
#
# def test_kni1ght_is_legal_7():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(3, 6))
#
#
# def test_kn1ight_is_legal_8():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(5, 6))
#
#
# def test_k1night_is_legal_9():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert not knight.is_legal(Coord(4, 5))
#
#
# def test_1knight_is_legal_10():
#     knight = Chessman(5, 8, Piece.knight, Color.white)
#     assert not knight.is_legal(Coord(7, 9))
#
#
# def test_q2ueen_is_legal_11():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(1, 1))
#
#
# def test_2queen_is_legal_12():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(8, 8))
#
#
# def test_queen_is_legal1_3():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(1, 8))
#
#
# def test_queen_is_lega1l_4():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(8, 1))
#
#
# def test_queen_is_leg1al_5():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(1, 4))
#
#
# def test_queen_is_le1gal_6():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 8))
#
#
# def test_queen_is_l1egal_7():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(3, 6))
#
#
# def test_queen_is_1legal_8():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert not queen.is_legal(Coord(3, 6))
#
#
# def test_queen_is1_legal_9():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 5))
#
#
# def test_queen_i1s_legal_10():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 6))
#
#
# def test_queen_1is_legal_11():
#     queen = Chessman(4, 4, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(4, 7))
#
#
# def test_queen1_is_legal_12():
#     queen = Chessman(7, 6, Piece.queen, Color.white)
#     assert queen.is_legal(Coord(7, 7))
#
#
# # king is_legal() test
# def test_king1_is_legal_1():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(4, 5))
#
#
# def test_kin1g_is_legal_2():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 4))
#
#
# def test_ki1ng_is_legal_3():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 5))
#
#
# def test_k1ing_is_legal_4():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 4))
#
#
# def test_1king_is_legal_5():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(4, 3))
#
#
# def test_king_is_legal_216():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 5))
#
#
# def test_king_is_legal21_7():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(5, 3))
#
#
# def test_king_is_lega21l_8():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert king.is_legal(Coord(3, 3))
#
#
# def test_king_is_leg21al_9():
#     king = Chessman(4, 4, Piece.king, Color.white)
#     assert not king.is_legal(Coord(6, 4))
#
#
# def test_king_is_le21gal_10():
#     king = Chessman(8, 8, Piece.king, Color.white)
#     assert not king.is_legal(Coord(9, 8))
#
#
# # knight is_legal() test
# def test_knight_is21_legal_1():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(6, 3))
#
#
# def test_knight_i21s_legal_2():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(6, 5))
#
#
# def test_knight_21is_legal_3():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(2, 3))
#
#
# def test_knight21_is_legal_4():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(2, 5))
#
#
# def test_knigh21t_is_legal_5():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(5, 2))
#
#
# def test_knig21ht_is_legal_6():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(3, 2))
#
#
# def test_kni21ght_is_legal_7():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(3, 6))
#
#
# def test_kn21ight_is_legal_8():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert knight.is_legal(Coord(5, 6))
#
#
# def test_k21night_is_legal_9():
#     knight = Chessman(4, 4, Piece.knight, Color.white)
#     assert not knight.is_legal(Coord(4, 5))
#
#
# def test_21knight_is_legal_10():
#     knight = Chessman(5, 8, Piece.knight, Color.white)
#     assert not knight.is_legal(Coord(7, 9))
