from enum_types import Direction


class Coord:
    MAX = 8
    MIN = 1

    def __init__(self, x: int = 1, y: int = 1):
        if x > 8 or x < 1 or y > 8 or y < 1:
            raise ValueError
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __iter__(self):
        yield self.x
        yield self.y

    def __bool__(self):
        if self.x > self.MAX or self.x < self.MIN:
            return False
        if self.y > self.MAX or self.y < self.MIN:
            return False
        return True


    def is_equal(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def x_axis_distance(self, other):
        return abs(self.x - other.x)

    def y_axis_distance(self, other):
        return abs(self.y - other.y)

    def is_diagonal(self, other):
        if self.x_axis_distance(other) == self.y_axis_distance(other):
            return True
        return False

    def get_direction(self, other):
        if self.is_equal(other):
            return Direction.undefined
        if self.x == other.x():
            if self.y > other.y:
                return Direction.down
            else:
                return Direction.up
        if self.y == other.y:
            if self.x > other.x:
                return Direction.left
            else:
                return Direction.right
        if self.is_diagonal(other):
            return Direction.undefined
        if self.x > other.x and self.y > other.y:
            return Direction.left_down
        if self.x < other.x and self.y < other.get_y():
            return Direction.right_up
        if self.x > other.x and self.y < other.y:
            return Direction.left_up
        if self.x < other.x and self.y > other.y:
            return Direction.right_down
        return Direction.undefined

    def up(self):
        return Coord(self.x, self.y + 1)

    def down(self):
        return Coord(self.x, self.y - 1)

    def left(self):
        return Coord(self.x - 1, self.y)

    def right(self):
        return Coord(self.x + 1, self.y)

    def right_up(self):
        return Coord(self.x + 1, self.y + 1)

    def right_down(self):
        return Coord(self.x + 1, self.y - 1)

    def left_up(self):
        return Coord(self.x - 1, self.y + 1)

    def left_down(self):
        return Coord(self.x - 1, self.y - 1)

    def get_last_coord(self, direction: Direction):
        if direction == Direction.up:
            return Coord(self.x , 8)
        if direction == Direction.down:
            return Coord(self.x, 1)
        if direction == Direction.right:
            return Coord(8, self.y)
        if direction == Direction.left:
            return Coord(1, self.y)
        if direction == Direction.right_up:
            if self.y >= self.x:
                value = 8 - self.y
            else:
                value = 8 - self.x
            return Coord(self.x + value, self.y + value)
        if direction == Direction.right_down:
            if self.y >= 0:
               value = self.x-1
            else:
                value = self.y-1
            return Coord(self.x - value, self.y - value)
        if direction == Direction.left_up:
            if self.y >= 0:
                value = self.x-1
            else:
                value = self.y-1
            return Coord(self.x - value, self.y - value)
        if direction == Direction.left_down:
            if self.y >= self.x:
                value = self.x-1
            else:
                value = self.x-1
            return Coord(self.x - value, self.y - value)
        if direction == Direction.undefined:
            return Coord()

    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        return False

    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False

    def distance(self, square):
        if self.x == square.x:
            pass
        if self.y == square.x:
            pass
        if abs(self.x-square.x) == abs(self.y-square.y):
            return abs(self.x-square.x)
        return None
    # @property
    # def x(self):
    #     return self._x
    #
    # @x.setter
    # def x(self, x: int):
    #     if x > self.MAX or x < self.MIN:
    #         # raise ValueError
    #         print('dupa')
    #     else:
    #         self._x = x
    #
    # @property
    # def y(self):
    #     return self._y
    #
    # @y.setter
    # def y(self, y: int):
    #     if y > self.MAX or y < self.MIN:
    #         raise ValueError
    #     self._y = y

    def queen(self, square):
        if not square:
            return False
        if self.x == square.x:
            return True
        if self.y == square.y:
            return True
        if abs(self.x-square.x) == abs(self.y-square.y):
            return True
        return False

    def rook(self, square):
        if not square:
            return False
        if self.x == square.x:
            return True
        if self.y == square.y:
            return True
        return False

    def bishop(self, square):
        if not square:
            return False
        if abs(self.x - square.x) == abs(self.y - square.y):
            return True
        return False

    def knight(self, move):
        iter = Coord(self.x, self.y)
        iter.iterate_up()
        iter.iterate_up()
        if iter.iterate_right():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        iter.iterate_up()
        iter.iterate_up()
        if iter.iterate_left():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        iter.iterate_down()
        iter.iterate_down()
        if iter.iterate_right():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        iter.iterate_down()
        iter.iterate_down()
        if iter.iterate_left():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        iter.iterate_right()
        iter.iterate_right()
        if iter.iterate_up():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        iter.iterate_right()
        iter.iterate_right()
        if iter.iterate_down():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        iter.iterate_left()
        iter.iterate_left()
        if iter.iterate_up():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        iter.iterate_left()
        iter.iterate_left()
        if iter.iterate_down():
            if iter == move:
                return True

    def king(self, move):
        iter = Coord(self.x, self.y)
        if iter.iterate_up():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        if iter.iterate_down():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        if iter.iterate_right():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        if iter.iterate_left():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        if iter.iterate_right_up():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        if iter.iterate_right_down():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        if iter.iterate_left_up():
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        if iter.iterate_left_down():
            if iter == move:
                return True

    def iterate_diagonal(self, move):
        iter = Coord(self.x, self.y)
        while True:
            if not iter.iterate_right_up():
                break
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        while True:
            if not iter.iterate_right_down():
                break
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        while True:
            if not iter.iterate_left_up():
                break
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        while True:
            if not iter.iterate_left_down():
                break
            if iter == move:
                return True
        return False

    def iterate_vertical(self, move):
        squares = []
        iter = Coord(self.x, self.y)
        while True:
            if not iter.iterate_up():
                break
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        while True:
            if not iter.iterate_down():
                break
            squares.append(Coord(iter.x, iter.y))
            if iter == move:
                return True

    def iterate_horizontal(self, move):
        iter = Coord(self.x, self.y)
        while True:
            if not iter.iterate_right():
                break
            if iter == move:
                return True
        iter.x, iter.y = (self.x, self.y)
        while True:
            if not iter.iterate_left():
                break
            if iter == move:
                return True
        return False

    # def iterate(self, direction: D, coord):
    #     if direction == D.up:
    #         for i in range(self.max):
    #             self.iterate_up()
    #             if self == coord:
    #                 return True
    #     if direction == D.down:
    #         for i in range(self.max):
    #             self.iterate_down()
    #             if self == coord:
    #                 return True
    #     if direction == D.right:
    #         for i in range(self.max):
    #             self.iterate_right()
    #             if self == coord:
    #                 return True
    #     if direction == D.left:
    #         for i in range(self.max):
    #             self.iterate_left()
    #             if self == coord:
    #                 return True
    #     if direction == D.right_up:
    #         for i in range(self.max):
    #             self.iterate_right_up()
    #             if self == coord:
    #                 return True
    #     if direction == D.right_down:
    #         for i in range(self.max):
    #             self.iterate_right_down()
    #             if self == coord:
    #                 return True
    #     if direction == D.left_up:
    #         for i in range(self.max):
    #             self.iterate_left_up()
    #             if self == coord:
    #                 return True
    #     if direction == D.left_down:
    #         for i in range(self.max):
    #             self.iterate_left_down()
    #             if self == coord:
    #                 return True
    #     return False

    def iterate_right_up(self):


        if self.x + 1 > Coord.MAX:
            return False
        if self.y + 1 > Coord.MAX:
            return False
        self.x += 1
        self.y += 1
        return True

    def iterate_right_down(self):
        if self.x + 1 > Coord.MAX:
            return False
        if self.y - 1 < Coord.MIN:
            return False
        self.x += 1
        self.y -= 1
        return True

    def iterate_left_up(self):
        if self.x - 1 < Coord.MIN:
            return False
        if self.y + 1 > Coord.MAX:
            return False
        self.x -= 1
        self.y += 1
        return True

    def iterate_left_down(self):
        if self.x - 1 < Coord.MIN:
            return False
        if self.y - 1 < Coord.MIN:
            return False
        self.x -= 1
        self.y -= 1
        return True

    def iterate_left(self):
        if self.x - 1 < Coord.MIN:
            return False
        self.x -= 1
        return True

    def iterate_right(self):
        if self.x + 1 > Coord.MAX:
            return False
        self.x += 1
        return True

    def iterate_down(self):
        if self.y - 1 < Coord.MIN:
            return False
        self.y -= 1
        return True

    def iterate_up(self):
        if self.y + 1 > Coord.MAX:
            return False
        self.y += 1
        return True
