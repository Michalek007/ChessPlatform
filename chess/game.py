from chess.enum_types import *
from chess.chessman import Chessman
from chess.coord import Coord
from chess.square import Square
from chess.king import King
from chess.queen import Queen
from chess.bishop import Bishop
from chess.knight import Knight
from chess.pawn import Pawn
from chess.rook import Rook


class Game:

    def __init__(self, pieces, turn: Color = Color.white):
        # self.whites = []
        # self.blacks = []
        # for piece in pieces:
        #     if piece.color == Color.white:
        #         self.whites.append(piece)
        #     if piece.color == Color.black:
        #         self.blacks.append(piece)
        self.turn = turn
        # self.last_move = dict(piece=None, move=None, taken=None)
        self.last_move = {}
        self.game_record = []
        # self.board = [[]]
        self.board = pieces
        self.white_king = Coord(4, 1)
        self.black_king = Coord(4, 8)

    def __str__(self):
        # print('Whites: ')
        # for piece in self.whites:
        #     print(piece)
        # print('Blacks: ')
        # for piece in self.whites:
        #     print(piece)
        # print(f'Turn: {self.turn')
        # print(self.game_record)
        return str(self.game_record) + " " + str(self.turn)

    # @staticmethod
    # def init():
    #     list_of_pieces = [
    #         Chessman(5, 1, Piece.king, Color.white),
    #         Chessman(5, 8, Piece.king, Color.black),
    #         Chessman(4, 1, Piece.queen, Color.white),
    #         Chessman(4, 8, Piece.queen, Color.black),
    #         Chessman(3, 1, Piece.bishop, Color.white),
    #         Chessman(6, 1, Piece.bishop, Color.white),
    #         Chessman(3, 8, Piece.bishop, Color.black),
    #         Chessman(6, 8, Piece.bishop, Color.black),
    #         Chessman(2, 1, Piece.knight, Color.white),
    #         Chessman(7, 1, Piece.knight, Color.white),
    #         Chessman(2, 8, Piece.knight, Color.black),
    #         Chessman(7, 8, Piece.knight, Color.black),
    #         Chessman(1, 1, Piece.rook, Color.white),
    #         Chessman(8, 8, Piece.rook, Color.white),
    #         Chessman(1, 1, Piece.rook, Color.black),
    #         Chessman(8, 8, Piece.rook, Color.black),
    #         Chessman(1, 2, Piece.pawn, Color.white),
    #         Chessman(2, 2, Piece.pawn, Color.white),
    #         Chessman(3, 2, Piece.pawn, Color.white),
    #         Chessman(4, 2, Piece.pawn, Color.white),
    #         Chessman(5, 2, Piece.pawn, Color.white),
    #         Chessman(6, 2, Piece.pawn, Color.white),
    #         Chessman(7, 2, Piece.pawn, Color.white),
    #         Chessman(8, 2, Piece.pawn, Color.white),
    #         Chessman(1, 7, Piece.pawn, Color.black),
    #         Chessman(2, 7, Piece.pawn, Color.black),
    #         Chessman(3, 7, Piece.pawn, Color.black),
    #         Chessman(4, 7, Piece.pawn, Color.black),
    #         Chessman(5, 7, Piece.pawn, Color.black),
    #         Chessman(6, 7, Piece.pawn, Color.black),
    #         Chessman(7, 7, Piece.pawn, Color.black),
    #         Chessman(8, 7, Piece.pawn, Color.black)
    #     ]
    #     return list_of_pieces
    #
    # def get_piece_id(self, square: Coord):
    #     for piece in self.whites:
    #         if piece.coord == square:
    #             return self.whites.index(piece)
    #     for piece in self.blacks:
    #         if piece.coord == square:
    #             return self.blacks.index(piece)
    #     return None
    #
    # def make_move(self, move: Coord, id: int):
    #     try:
    #         piece = self.whites[id]
    #     except IndexError:
    #         try:
    #             piece = self.blacks[id]
    #         except IndexError:
    #             return False
    #     if not self.is_legal(move=move, piece=piece):
    #         return False
    #     if self.turn == Color.white:
    #         self.game_record.append({'piece': self.whites[id], 'move': move, 'taken': None)
    #         self.whites[id].coord = move
    #         for piece in self.blacks:
    #             if piece.coord == move:
    #                 self.game_record[-1]['taken'] = piece
    #                 self.blacks.remove(piece)
    #         self.last_move = self.game_record[-1]
    #         self.turn = Color.black
    #     else:
    #         self.game_record.append({'piece': self.blacks[id], 'move': move, 'taken': None)
    #         self.blacks[id].coord = move
    #         for piece in self.whites:
    #             if piece.coord == move:
    #                 self.game_record[-1]['taken'] = piece
    #                 self.whites.remove(piece)
    #         self.last_move = self.game_record[-1]
    #         self.turn = Color.white
    #
    # def is_legal(self, move: Coord, piece: Chessman):
    #     # print("Move -> is_legal: ", piece.is_legal(move))
    #     if not piece.is_legal(move):
    #         breakpoint()
    #         return False
    #     if self.turn == Color.white:
    #         if piece not in self.whites:
    #             return False
    #         for item in self.whites:
    #             if item.coord == move:
    #                 return False
    #         # new method which check if there are pieces between two figures
    #         # if True return False
    #         if self.check_obstacle(piece=piece, move=move):
    #             return False
    #         id = self.whites.index(piece)
    #         self.move(move, id)
    #         for item in self.blacks:
    #             if not item.is_legal(self.whites[0].coord):
    #                 continue
    #             if not self.check_obstacle(piece=item, move=self.whites[0].coord):
    #                 self.undo_last_move()
    #                 return False
    #     else:
    #         if piece not in self.blacks:
    #             print('Piece is not in blacks')
    #             return False
    #         for item in self.blacks:
    #             if item.coord == move:
    #                 print('Black piece is already on that square...')
    #                 return False
    #         # new method which check if there are pieces between two figures
    #         # if True return False
    #         if self.check_obstacle(piece=piece, move=move):
    #             return False
    #         id = self.blacks.index(piece)
    #         self.move(move, id)
    #         for item in self.whites:
    #             if not item.is_legal(self.blacks[0].coord):
    #                 continue
    #             if not self.check_obstacle(piece=item, move=self.blacks[0].coord):
    #                 self.undo_last_move()
    #                 return False
    #     return True
    #
    # def move(self, move: Coord, id: int):
    #     if self.turn == Color.white:
    #         self.last_move = {'piece': self.whites[id], "taken": None
    #         self.whites[id].coord = move
    #         for piece in self.blacks:
    #             if piece.coord == move:
    #                 self.last_move['taken'] = piece
    #                 self.blacks.remove(piece)
    #         self.turn = Color.black
    #     else:
    #         self.last_move = {'piece': self.blacks[id], "taken": None
    #         self.blacks[id].coord = move
    #         for piece in self.whites:
    #             if piece.coord == move:
    #                 self.last_move['taken'] = piece
    #                 self.whites.remove(piece)
    #         self.turn = Color.white
    #
    # def undo_last_move(self):
    #     taken = self.last_move['taken']
    #     l_piece = self.last_move['piece']
    #     if not l_piece:
    #         return
    #     # undo blacks move
    #     if self.turn == Color.white:
    #         for piece in self.blacks:
    #             if taken:
    #                 if taken.coord == piece.coord:
    #                     self.whites.append(taken)
    #             piece.coord = l_piece.coord
    #         self.turn = Color.black
    #
    #     # undo whites move
    #     else:
    #         for piece in self.whites:
    #             if taken:
    #                 if taken.coord == piece.coord:
    #                     self.blacks.append(taken)
    #             piece.coord = l_piece.coord
    #         self.turn = Color.white
    #     if self.game_record:
    #         self.last_move = self.game_record[-1]
    #     else:
    #         self.last_move = {'piece': None, 'move': None, 'taken': None
    #
    # def check_square(self, iter: Coord):
    #     # if next((x for x in self.blacks if x.coord == iter), None):
    #     #     return True
    #     # if next((x for x in self.whites if x.coord == iter), None):
    #     #     return True
    #     for item in self.blacks:
    #         if iter == item.coord:
    #             return True
    #     for item in self.whites:
    #         if iter == item.coord:
    #             return True
    #     return False
    #
    # def check_obstacle(self, piece, move):
    #     if piece.type == Piece.knight or piece.type == Piece.king:
    #         return False
    #     iter = Coord(piece.coord.x, piece.coord.y)
    #     if piece.type == Piece.pawn:
    #         if move.x != piece.coord.x:
    #             if piece.color == Color.white:
    #                 for item in self.blacks:
    #                     if move.x == item.coord.x:
    #                         return False
    #             if piece.color == Color.black:
    #                 for item in self.whites:
    #                     if move.x == item.coord.x:
    #                         return False
    #             if piece.color == Color.white and piece.coord.x != 5:
    #                 return True
    #             if piece.color == Color.black and piece.coord.x != 4:
    #                 return True
    #             if self.last_move['piece'].type != Piece.pawn:
    #                 return True
    #             if self.last_move['move'].y == 5 and self.last_move['piece'].coord.y == 7:
    #                 if move.x == self.last_move['piece'].coord.x:
    #                     return False
    #             if self.last_move['move'].y == 4 and self.last_move['piece'].coord.y == 2:
    #                 if move.x == self.last_move['piece'].coord.x:
    #                     return False
    #             return True
    #         if move.y == piece.coord.y + 2:
    #             if piece.coord.y != 2:
    #                 return True
    #             for item in self.whites:
    #                 if move.y + 1 == item.coord.y:
    #                     return True
    #             for item in self.blacks:
    #                 if move.y + 1 == item.coord.y:
    #                     return True
    #             return False
    #         if move.y == piece.coord.y - 2:
    #             if piece.coord.y != 7:
    #                 return True
    #             for item in self.whites:
    #                 if move.y - 1 == item.coord.y:
    #                     return True
    #             for item in self.blacks:
    #                 if move.y - 1 == item.coord.y:
    #                     return True
    #             return False
    #         return False
    #     if piece.coord > move:
    #         while True:
    #             iter.iterate_left_down()
    #             if iter == move:
    #                 break
    #             if self.check_square(iter):
    #                 return True
    #     if piece.coord < move:
    #         iter.x, iter.y = (piece.coord.x, piece.coord.y)
    #         while True:
    #             iter.iterate_right_up()
    #             if iter == move:
    #                 break
    #             if self.check_square(iter):
    #                 return True
    #     if piece.coord.x > move.x and piece.coord.y < move.y:
    #         iter.x, iter.y = (piece.coord.x, piece.coord.y)
    #         while True:
    #             iter.iterate_left_up()
    #             if iter == move:
    #                 break
    #             if self.check_square(iter):
    #                 return True
    #     if piece.coord.x < move.x and piece.coord.y > move.y:
    #         while True:
    #             iter.iterate_right_down()
    #             if iter == move:
    #                 break
    #         if not self.check_square(iter):
    #             return False
    #     if piece.coord.x == move.x and piece.coord.y > move.y:
    #         iter.x, iter.y = (piece.coord.x, piece.coord.y)
    #         while True:
    #             iter.iterate_down()
    #             if iter == move:
    #                 break
    #             if self.check_square(iter):
    #                 return True
    #     if piece.coord.x == move.x and piece.coord.y < move.y:
    #         iter.x, iter.y = (piece.coord.x, piece.coord.y)
    #         while True:
    #             iter.iterate_up()
    #             if iter == move:
    #                 break
    #             if self.check_square(iter):
    #                 return True
    #     if piece.coord.x > move.x and piece.coord.y == move.y:
    #         iter.x, iter.y = (piece.coord.x, piece.coord.y)
    #         while True:
    #             iter.iterate_left()
    #             if iter == move:
    #                 break
    #             if self.check_square(iter):
    #                 return True
    #     if piece.coord.x < move.x and piece.coord.y == move.y:
    #         iter.x, iter.y = (piece.coord.x, piece.coord.y)
    #         while True:
    #             iter.iterate_right()
    #             if iter == move:
    #                 break
    #             if self.check_square(iter):
    #                 return True
    #     return False
    def is_legal_override(self, start: Coord, end: Coord):
        piece = self.get_piece(start)
        if piece is None:
            return False
        if piece.get_symbol() == "P":
            if not piece.is_legal(start, end):
                return False
            if piece.is_white():
                if start.x == end.x:
                    if self.get_square(end).has_piece():
                        if self.get_piece(end).is_white():
                            return False
                if not self.get_square(end).has_piece():
                    return False
                if self.get_piece(end).is_white():
                    return False
                return True
            else:
                if start.x == end.x:
                    if self.get_square(end).has_piece():
                        if not self.get_piece(end).is_white():
                            return False
                if not self.get_square(end).has_piece():
                    return False
                if not self.get_piece(end).is_white():
                    return False
                return True
        else:
            return piece.is_legal(start, end)

    def is_legal(self, start: Coord, end: Coord):
        if not self.is_legal_override(start, end):
            return False
        if self.get_square(end).has_piece():
            if self.get_piece(start).get_color() == self.get_piece(end).get_color():
                return False
        # check obstacles
        if self.piece_between(start, end):
            return False
        # make move and check if king is under attack
        self.make_move(start, end)
        if self.get_piece(start).is_white():
            if self.can_be_captured(self.white_king):
                return False
        else:
            if self.can_be_captured(self.black_king):
                return False
        # undo move
        self.undo_last_move()
        return True

    def can_be_captured(self, start: Coord):
        end_coords = [
            start.get_last_coord(Direction.up),
            start.get_last_coord(Direction.down),
            start.get_last_coord(Direction.right),
            start.get_last_coord(Direction.down),
            start.get_last_coord(Direction.right_up),
            start.get_last_coord(Direction.right_down),
            start.get_last_coord(Direction.left_up),
            start.get_last_coord(Direction.left_down)]
        for end in end_coords:
            direction = start.get_direction(end)
            if direction == Direction.up:
                for i in range(8-start.y):
                    iter = start.up()
                    if self.get_square(iter).get_piece() is not None:
                        if self.is_legal_override(iter, start):
                            return True
            if direction == Direction.down:
                for i in range(start.y - 1):
                    iter = start.down()
                    if self.get_square(iter).get_piece() is not None:
                        if self.is_legal_override(iter, start):
                            return True
            if direction == Direction.right:
                for i in range(8-start.x):
                    iter = start.right()
                    if self.get_square(iter).get_piece() is not None:
                        if self.is_legal_override(iter, start):
                            return True
            if direction == Direction.left:
                for i in range(start.x - 1):
                    iter = start.left()
                    if self.get_square(iter).get_piece() is not None:
                        if self.is_legal_override(iter, start):
                            return True
            if direction == Direction.right_up:
                for i in range(start.x_axis_distance(end)):
                    iter = start.right_up()
                    if self.get_square(iter).get_piece() is not None:
                        if self.is_legal_override(iter, start):
                            return True
            if direction == Direction.right_down:
                for i in range(start.x_axis_distance(end)):
                    iter = start.right_down()
                    if self.get_square(iter).get_piece() is not None:
                        if self.is_legal_override(iter, start):
                            return True
            if direction == Direction.left_up:
                for i in range(start.x_axis_distance(end)):
                    iter = start.left_up()
                    if self.get_square(iter).get_piece() is not None:
                        if self.is_legal_override(iter, start):
                            return True
            if direction == Direction.left_down:
                for i in range(start.x_axis_distance(end)):
                    iter = start.left_down()
                    if self.get_square(iter).get_piece() is not None:
                        if self.is_legal_override(iter, start):
                            return True
            if direction == Direction.undefined:
                return True
        l_values = ((1, 2), (1, -2), (2, 1), (2, -1),
                    (-1, 2), (-1, -2), (-2, 1), (-2, -1))
        for value in l_values:
            try:
                l_coord = Coord(start.x + value[0], start.y + value[1])
                if self.get_square(l_coord).has_piece():
                    if self.get_piece(l_coord).get_symbol() == "N":
                        return True
            except ValueError:
                continue

    def set_last_move(self, start: str, end: str, taken: str):
        last_move = {'start': start, 'end': end, 'taken': taken}
        self.game_record.append(last_move)

    def piece_between(self, start: Coord, end: Coord):
        if start.is_equal(end):
            return False
        if not start.is_diagonal(end):
            return False
        if start.x_axis_distance(end) < 2 and start.y_axis_distance(end) < 2:
            return False

        direction = start.get_direction(end)
        if direction == Direction.up:
            for i in range(start.y_axis_distance(end)):
                iter = start.up()
                if self.get_square(iter).get_piece() is not None:
                    return True
        if direction == Direction.down:
            for i in range(start.y_axis_distance(end)):
                iter = start.down()
                if self.get_square(iter).get_piece() is not None:
                    return True
        if direction == Direction.right:
            for i in range(start.x_axis_distance(end)):
                iter = start.right()
                if self.get_square(iter).get_piece() is not None:
                    return True
        if direction == Direction.left:
            for i in range(start.x_axis_distance(end)):
                iter = start.left()
                if self.get_square(iter).get_piece() is not None:
                    return True
        if direction == Direction.right_up:
            for i in range(start.x_axis_distance(end)):
                iter = start.right_up()
                if self.get_square(iter).get_piece() is not None:
                    return True
        if direction == Direction.right_down:
            for i in range(start.x_axis_distance(end)):
                iter = start.right_down()
                if self.get_square(iter).get_piece() is not None:
                    return True
        if direction == Direction.left_up:
            for i in range(start.x_axis_distance(end)):
                iter = start.left_up()
                if self.get_square(iter).get_piece() is not None:
                    return True
        if direction == Direction.left_down:
            for i in range(start.x_axis_distance(end)):
                iter = start.left_down()
                if self.get_square(iter).get_piece() is not None:
                    return True
        if direction == Direction.undefined:
            return False
        return True

    def get_last_move(self):
        return self.game_record[-1]

    def undo_last_move(self):
        last_move = self.get_last_move()
        start = self.decode_coord(last_move["start"])
        end = self.decode_coord(last_move["end"])
        self.get_square(start).set_piece(self.get_square(end).get_piece())
        self.get_square(end).set_piece(self.decode_piece(last_move["taken"]))

    def make_move(self, start: Coord, end: Coord):
        begin = self.get_square(start)
        dest = self.get_square(end)
        taken = ""
        if begin.has_piece():
            if begin.has_piece().get_symbol() == 'K':
                if self.turn == Color.white:
                    self.white_king = end
                else:
                    self.black_king = end
                begin.get_piece().has_moved = True
            if begin.get_piece().get_symbol() == 'R':
                begin.get_piece.has_moved = True
            if dest.has_piece():
                taken = dest.get_piece()
            dest.capture_piece()
            dest.set_piece(begin.get_piece())
            begin.set_null()
            self.set_last_move(begin.get_coord_symbol(), dest.get_coord_symbol(), taken)
            self.change_turn()

    def change_turn(self):
        if self.turn == Color.white:
            self.turn = Color.black
        else:
            self.turn = Color.white

    def get_square(self, coord: Coord):
        return self.board[coord.x - 1][coord.y - 1]

    def get_piece(self, coord: Coord):
        return self.board[coord.x - 1][coord.y - 1].get_piece()

    def decode_piece(self, piece: str):
        if not piece:
            return None
        if self.turn == Color.white:
            color = Color.black
        else:
            color = Color.white
        if piece[0] == "K":
            return King(1, 1, Piece.king, color)
        if piece[0] == "Q":
            return Queen(1, 1, Piece.queen, color)
        if piece[0] == "B":
            return Bishop(1, 1, Piece.bishop, color)
        if piece[0] == "R":
            return Rook(1, 1, Piece.rook, color)
        if piece[0] == "N":
            return Knight(1, 1, Piece.knight, color)
        if piece[0] == "P":
            return Pawn(1, 1, Piece.pawn, color)
        return None

    @staticmethod
    def decode_coord(coord: str):
        if not coord:
            return None
        x = int(coord[0])
        y = int(coord[1])
        return Coord(x, y)

    @staticmethod
    def init():
        a1 = Square(1, 1, Rook(1, 1, Piece.rook, Color.white))
        b1 = Square(2, 1, Knight(2, 1, Piece.knight, Color.white))
        c1 = Square(3, 1, Bishop(3, 1, Piece.bishop, Color.white))
        d1 = Square(4, 1, Queen(4, 1, Piece.queen, Color.white))
        e1 = Square(5, 1, King(5, 1, Piece.king, Color.white))
        f1 = Square(6, 1, Bishop(6, 1, Piece.bishop, Color.white))
        g1 = Square(7, 1, Pawn(7, 1, Piece.knight, Color.white))
        h1 = Square(8, 1, Pawn(8, 1, Piece.rook, Color.white))

        a2 = Square(1, 2, Pawn(1, 2, Piece.pawn, Color.white))
        b2 = Square(2, 2, Pawn(2, 2, Piece.pawn, Color.white))
        c2 = Square(3, 2, Pawn(3, 2, Piece.pawn, Color.white))
        d2 = Square(4, 2, Pawn(4, 2, Piece.pawn, Color.white))
        e2 = Square(5, 2, Pawn(5, 2, Piece.pawn, Color.white))
        f2 = Square(6, 2, Pawn(6, 2, Piece.pawn, Color.white))
        g2 = Square(7, 2, Pawn(7, 2, Piece.pawn, Color.white))
        h2 = Square(8, 2, Pawn(8, 2, Piece.pawn, Color.white))

        a3 = Square(1, 3)
        b3 = Square(2, 3)
        c3 = Square(3, 3)
        d3 = Square(4, 3)
        e3 = Square(5, 3)
        f3 = Square(6, 3)
        g3 = Square(7, 3)
        h3 = Square(8, 3)

        a4 = Square(1, 4)
        b4 = Square(2, 4)
        c4 = Square(3, 4)
        d4 = Square(4, 4)
        e4 = Square(5, 4)
        f4 = Square(6, 4)
        g4 = Square(7, 4)
        h4 = Square(8, 4)

        a5 = Square(1, 5)
        b5 = Square(2, 5)
        c5 = Square(3, 5)
        d5 = Square(4, 5)
        e5 = Square(5, 5)
        f5 = Square(6, 5)
        g5 = Square(7, 5)
        h5 = Square(8, 5)

        a6 = Square(1, 6)
        b6 = Square(2, 6)
        c6 = Square(3, 6)
        d6 = Square(4, 6)
        e6 = Square(5, 6)
        f6 = Square(6, 6)
        g6 = Square(7, 6)
        h6 = Square(8, 6)

        a7 = Square(1, 7, Pawn(1, 7, Piece.pawn, Color.black))
        b7 = Square(2, 7, Pawn(2, 7, Piece.pawn, Color.black))
        c7 = Square(3, 7, Pawn(3, 7, Piece.pawn, Color.black))
        d7 = Square(4, 7, Pawn(4, 7, Piece.pawn, Color.black))
        e7 = Square(5, 7, Pawn(5, 7, Piece.pawn, Color.black))
        f7 = Square(6, 7, Pawn(6, 7, Piece.pawn, Color.black))
        g7 = Square(7, 7, Pawn(7, 7, Piece.pawn, Color.black))
        h7 = Square(8, 7, Pawn(8, 7, Piece.pawn, Color.black))

        a8 = Square(1, 8, Rook(1, 8, Piece.rook, Color.black))
        b8 = Square(2, 8, Knight(2, 8, Piece.knight, Color.black))
        c8 = Square(3, 8, Bishop(3, 8, Piece.bishop, Color.black))
        d8 = Square(4, 8, Queen(4, 8, Piece.queen, Color.black))
        e8 = Square(5, 8, King(5, 8, Piece.king, Color.black))
        f8 = Square(6, 8, Bishop(6, 8, Piece.bishop, Color.black))
        g8 = Square(7, 8, Pawn(7, 8, Piece.knight, Color.black))
        h8 = Square(8, 8, Pawn(8, 8, Piece.rook, Color.black))

        row1 = [a1, a2, a3, a4, a5, a6, a7, a8]
        row2 = [b1, b2, b3, b4, b5, b6, b7, b8]
        row3 = [c1, c2, c3, c4, c5, c6, c7, c8]
        row4 = [d1, d2, d3, d4, d5, d6, d7, d8]
        row5 = [e1, e2, e3, e4, e5, e6, e7, e8]
        row6 = [f1, f2, f3, f4, f5, f6, f7, f8]
        row7 = [g1, g2, g3, g4, g5, g6, g7, g8]
        row8 = [h1, h2, h3, h4, h5, h6, h7, h8]
        board = [row1, row2, row3, row4, row5, row6, row7, row8]
        return board

    @staticmethod
    def empty_init():
        a1 = Square(1, 1)
        b1 = Square(2, 1)
        c1 = Square(3, 1)
        d1 = Square(4, 1)
        e1 = Square(5, 1)
        f1 = Square(6, 1)
        g1 = Square(7, 1)
        h1 = Square(8, 1)

        a2 = Square(1, 2)
        b2 = Square(2, 2)
        c2 = Square(3, 2)
        d2 = Square(4, 2)
        e2 = Square(5, 2)
        f2 = Square(6, 2)
        g2 = Square(7, 2)
        h2 = Square(8, 2)

        a3 = Square(1, 3)
        b3 = Square(2, 3)
        c3 = Square(3, 3)
        d3 = Square(4, 3)
        e3 = Square(5, 3)
        f3 = Square(6, 3)
        g3 = Square(7, 3)
        h3 = Square(8, 3)

        a4 = Square(1, 4)
        b4 = Square(2, 4)
        c4 = Square(3, 4)
        d4 = Square(4, 4)
        e4 = Square(5, 4)
        f4 = Square(6, 4)
        g4 = Square(7, 4)
        h4 = Square(8, 4)

        a5 = Square(1, 5)
        b5 = Square(2, 5)
        c5 = Square(3, 5)
        d5 = Square(4, 5)
        e5 = Square(5, 5)
        f5 = Square(6, 5)
        g5 = Square(7, 5)
        h5 = Square(8, 5)

        a6 = Square(1, 6)
        b6 = Square(2, 6)
        c6 = Square(3, 6)
        d6 = Square(4, 6)
        e6 = Square(5, 6)
        f6 = Square(6, 6)
        g6 = Square(7, 6)
        h6 = Square(8, 6)

        a7 = Square(1, 7)
        b7 = Square(2, 7)
        c7 = Square(3, 7)
        d7 = Square(4, 7)
        e7 = Square(5, 7)
        f7 = Square(6, 7)
        g7 = Square(7, 7)
        h7 = Square(8, 7)

        a8 = Square(1, 8)
        b8 = Square(2, 8)
        c8 = Square(3, 8)
        d8 = Square(4, 8)
        e8 = Square(5, 8)
        f8 = Square(6, 8)
        g8 = Square(7, 8)
        h8 = Square(8, 8)

        row1 = [a1, a2, a3, a4, a5, a6, a7, a8]
        row2 = [b1, b2, b3, b4, b5, b6, b7, b8]
        row3 = [c1, c2, c3, c4, c5, c6, c7, c8]
        row4 = [d1, d2, d3, d4, d5, d6, d7, d8]
        row5 = [e1, e2, e3, e4, e5, e6, e7, e8]
        row6 = [f1, f2, f3, f4, f5, f6, f7, f8]
        row7 = [g1, g2, g3, g4, g5, g6, g7, g8]
        row8 = [h1, h2, h3, h4, h5, h6, h7, h8]
        board = [row1, row2, row3, row4, row5, row6, row7, row8]
        return board

    def print(self):
        for vec in self.board:
            for square in vec:
                if square.has_piece():
                    print(square.get_piece().get_symbol())
                else:
                    print(".")
                print("\n")
