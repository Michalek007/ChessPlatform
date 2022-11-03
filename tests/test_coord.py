from chess.coord import *


def test_iterate_right():
    coord = Coord(8, 6)
    assert not coord.iterate_right()


def test_iterate_left():
    coord = Coord(1, 6)
    assert not coord.iterate_left()


def test_iterate_up():
    coord = Coord(7, 8)
    assert not coord.iterate_up()


def test_iterate_down():
    coord = Coord(7, 1)
    assert not coord.iterate_down()


def test_iterate_right_up_1():
    coord = Coord(7, 8)
    assert not coord.iterate_right_up()


def test_iterate_right_up_2():
    coord = Coord(8, 2)
    assert not coord.iterate_right_up()


def test_iterate_right_down_1():
    coord = Coord(8, 6)
    assert not coord.iterate_right_down()


def test_iterate_right_down_2():
    coord = Coord(7, 1)
    assert not coord.iterate_right_down()


def test_iterate_left_up_1():
    coord = Coord(1, 6)
    assert not coord.iterate_left_up()


def test_iterate_left_up_2():
    coord = Coord(7, 8)
    assert not coord.iterate_left_up()


def test_iterate_left_down_1():
    coord = Coord(7, 1)
    assert not coord.iterate_left_down()


def test_iterate_left_down_2():
    coord = Coord(1, 6)
    assert not coord.iterate_left_down()


def test_distance():
    coord = Coord(1, 3)
    assert coord.iterate_diagonal(Coord(4, 6))


def test_distance2():
    coord = Coord(1, 3)
    assert coord.distance(Coord(4, 6))


def test_value_error():
    x = Coord(2, 2)
    assert not x.queen(Coord(-1, 2))


def test_value_error2():
    x = Coord(2, 2)
    assert not x.queen(Coord(9, 1))


def test_value_error3():
    x = Coord(2, 2)
    assert not x.queen(Coord(2, -1))


def test_value_error4():
    x = Coord(2, 2)
    assert not x.queen(Coord(-1, 2))
# def test_value_error():
#     x = Coord(9, 12)
#     x._x = -23
#     print(x._x)
    # assert ValueError
