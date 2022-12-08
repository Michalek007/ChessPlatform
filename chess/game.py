from chess.enum_types import *
from chess.chessman import Chessman
from chess.coord import Coord
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from pawn import Pawn
from rook import Rook


class Game:

    def __init__(self, pieces, turn: Color = Color.white):
        self.whites = []
        self.blacks = []
        for piece in pieces:
            if piece.color == Color.white:
                self.whites.append(piece)
            if piece.color == Color.black:
                self.blacks.append(piece)
        self.turn = turn
        # self.last_move = dict(piece=None, move=None, taken=None)
        self.last_move = {}
        self.game_record = []
        self.board = [[]]

    def __str__(self):
        # print('Whites: ')
        # for piece in self.whites:
        #     print(piece)
        # print('Blacks: ')
        # for piece in self.whites:
        #     print(piece)
        # print(f'Turn: {self.turn}')
        # print(self.game_record)
        return str(self.game_record) + " " + str(self.turn)

    @staticmethod
    def init():
        list_of_pieces = [
            Chessman(5, 1, Piece.king, Color.white),
            Chessman(5, 8, Piece.king, Color.black),
            Chessman(4, 1, Piece.queen, Color.white),
            Chessman(4, 8, Piece.queen, Color.black),
            Chessman(3, 1, Piece.bishop, Color.white),
            Chessman(6, 1, Piece.bishop, Color.white),
            Chessman(3, 8, Piece.bishop, Color.black),
            Chessman(6, 8, Piece.bishop, Color.black),
            Chessman(2, 1, Piece.knight, Color.white),
            Chessman(7, 1, Piece.knight, Color.white),
            Chessman(2, 8, Piece.knight, Color.black),
            Chessman(7, 8, Piece.knight, Color.black),
            Chessman(1, 1, Piece.rook, Color.white),
            Chessman(8, 8, Piece.rook, Color.white),
            Chessman(1, 1, Piece.rook, Color.black),
            Chessman(8, 8, Piece.rook, Color.black),
            Chessman(1, 2, Piece.pawn, Color.white),
            Chessman(2, 2, Piece.pawn, Color.white),
            Chessman(3, 2, Piece.pawn, Color.white),
            Chessman(4, 2, Piece.pawn, Color.white),
            Chessman(5, 2, Piece.pawn, Color.white),
            Chessman(6, 2, Piece.pawn, Color.white),
            Chessman(7, 2, Piece.pawn, Color.white),
            Chessman(8, 2, Piece.pawn, Color.white),
            Chessman(1, 7, Piece.pawn, Color.black),
            Chessman(2, 7, Piece.pawn, Color.black),
            Chessman(3, 7, Piece.pawn, Color.black),
            Chessman(4, 7, Piece.pawn, Color.black),
            Chessman(5, 7, Piece.pawn, Color.black),
            Chessman(6, 7, Piece.pawn, Color.black),
            Chessman(7, 7, Piece.pawn, Color.black),
            Chessman(8, 7, Piece.pawn, Color.black)
        ]
        return list_of_pieces

    def get_piece_id(self, square: Coord):
        for piece in self.whites:
            if piece.coord == square:
                return self.whites.index(piece)
        for piece in self.blacks:
            if piece.coord == square:
                return self.blacks.index(piece)
        return None

    def make_move(self, move: Coord, id: int):
        try:
            piece = self.whites[id]
        except IndexError:
            try:
                piece = self.blacks[id]
            except IndexError:
                return False
        if not self.is_legal(move=move, piece=piece):
            return False
        if self.turn == Color.white:
            self.game_record.append({'piece': self.whites[id], 'move': move, 'taken': None})
            self.whites[id].coord = move
            for piece in self.blacks:
                if piece.coord == move:
                    self.game_record[-1]['taken'] = piece
                    self.blacks.remove(piece)
            self.last_move = self.game_record[-1]
            self.turn = Color.black
        else:
            self.game_record.append({'piece': self.blacks[id], 'move': move, 'taken': None})
            self.blacks[id].coord = move
            for piece in self.whites:
                if piece.coord == move:
                    self.game_record[-1]['taken'] = piece
                    self.whites.remove(piece)
            self.last_move = self.game_record[-1]
            self.turn = Color.white

    def is_legal(self, move: Coord, piece: Chessman):
        # print("Move -> is_legal: ", piece.is_legal(move))
        if not piece.is_legal(move):
            breakpoint()
            return False
        if self.turn == Color.white:
            if piece not in self.whites:
                return False
            for item in self.whites:
                if item.coord == move:
                    return False
            # new method which check if there are pieces between two figures
            # if true return false
            if self.check_obstacle(piece=piece, move=move):
                return False
            id = self.whites.index(piece)
            self.move(move, id)
            for item in self.blacks:
                if not item.is_legal(self.whites[0].coord):
                    continue
                if not self.check_obstacle(piece=item, move=self.whites[0].coord):
                    self.undo_last_move()
                    return False
        else:
            if piece not in self.blacks:
                print('Piece is not in blacks')
                return False
            for item in self.blacks:
                if item.coord == move:
                    print('Black piece is already on that square...')
                    return False
            # new method which check if there are pieces between two figures
            # if true return false
            if self.check_obstacle(piece=piece, move=move):
                return False
            id = self.blacks.index(piece)
            self.move(move, id)
            for item in self.whites:
                if not item.is_legal(self.blacks[0].coord):
                    continue
                if not self.check_obstacle(piece=item, move=self.blacks[0].coord):
                    self.undo_last_move()
                    return False
        return True

    def move(self, move: Coord, id: int):
        if self.turn == Color.white:
            self.last_move = {'piece': self.whites[id], "taken": None}
            self.whites[id].coord = move
            for piece in self.blacks:
                if piece.coord == move:
                    self.last_move['taken'] = piece
                    self.blacks.remove(piece)
            self.turn = Color.black
        else:
            self.last_move = {'piece': self.blacks[id], "taken": None}
            self.blacks[id].coord = move
            for piece in self.whites:
                if piece.coord == move:
                    self.last_move['taken'] = piece
                    self.whites.remove(piece)
            self.turn = Color.white

    def undo_last_move(self):
        taken = self.last_move['taken']
        l_piece = self.last_move['piece']
        if not l_piece:
            return
        # undo blacks move
        if self.turn == Color.white:
            for piece in self.blacks:
                if taken:
                    if taken.coord == piece.coord:
                        self.whites.append(taken)
                piece.coord = l_piece.coord
            self.turn = Color.black

        # undo whites move
        else:
            for piece in self.whites:
                if taken:
                    if taken.coord == piece.coord:
                        self.blacks.append(taken)
                piece.coord = l_piece.coord
            self.turn = Color.white
        if self.game_record:
            self.last_move = self.game_record[-1]
        else:
            self.last_move = {'piece': None, 'move': None, 'taken': None}

    def check_square(self, iter: Coord):
        # if next((x for x in self.blacks if x.coord == iter), None):
        #     return True
        # if next((x for x in self.whites if x.coord == iter), None):
        #     return True
        for item in self.blacks:
            if iter == item.coord:
                return True
        for item in self.whites:
            if iter == item.coord:
                return True
        return False

    def check_obstacle(self, piece, move):
        if piece.type == Piece.knight or piece.type == Piece.king:
            return False
        iter = Coord(piece.coord.x, piece.coord.y)
        if piece.type == Piece.pawn:
            if move.x != piece.coord.x:
                if piece.color == Color.white:
                    for item in self.blacks:
                        if move.x == item.coord.x:
                            return False
                if piece.color == Color.black:
                    for item in self.whites:
                        if move.x == item.coord.x:
                            return False
                if piece.color == Color.white and piece.coord.x != 5:
                    return True
                if piece.color == Color.black and piece.coord.x != 4:
                    return True
                if self.last_move['piece'].type != Piece.pawn:
                    return True
                if self.last_move['move'].y == 5 and self.last_move['piece'].coord.y == 7:
                    if move.x == self.last_move['piece'].coord.x:
                        return False
                if self.last_move['move'].y == 4 and self.last_move['piece'].coord.y == 2:
                    if move.x == self.last_move['piece'].coord.x:
                        return False
                return True
            if move.y == piece.coord.y + 2:
                if piece.coord.y != 2:
                    return True
                for item in self.whites:
                    if move.y + 1 == item.coord.y:
                        return True
                for item in self.blacks:
                    if move.y + 1 == item.coord.y:
                        return True
                return False
            if move.y == piece.coord.y - 2:
                if piece.coord.y != 7:
                    return True
                for item in self.whites:
                    if move.y - 1 == item.coord.y:
                        return True
                for item in self.blacks:
                    if move.y - 1 == item.coord.y:
                        return True
                return False
            return False
        if piece.coord > move:
            while True:
                iter.iterate_left_down()
                if iter == move:
                    break
                if self.check_square(iter):
                    return True
        if piece.coord < move:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_right_up()
                if iter == move:
                    break
                if self.check_square(iter):
                    return True
        if piece.coord.x > move.x and piece.coord.y < move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_left_up()
                if iter == move:
                    break
                if self.check_square(iter):
                    return True
        if piece.coord.x < move.x and piece.coord.y > move.y:
            while True:
                iter.iterate_right_down()
                if iter == move:
                    break
            if not self.check_square(iter):
                return False
        if piece.coord.x == move.x and piece.coord.y > move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_down()
                if iter == move:
                    break
                if self.check_square(iter):
                    return True
        if piece.coord.x == move.x and piece.coord.y < move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_up()
                if iter == move:
                    break
                if self.check_square(iter):
                    return True
        if piece.coord.x > move.x and piece.coord.y == move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_left()
                if iter == move:
                    break
                if self.check_square(iter):
                    return True
        if piece.coord.x < move.x and piece.coord.y == move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_right()
                if iter == move:
                    break
                if self.check_square(iter):
                    return True
        return False

    def change_turn(self):
        if self.turn == Color.white:
            self.turn = Color.black
        else:
            self.turn = Color.white

    def get_square(self, coord: Coord):
        return self.board[coord.x-1][coord.y-1]

    def get_piece(self, coord: Coord):
        return self.board[coord.x-1][coord.y-1].get_piece()

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

    def decode_coord(self, coord: str):
        if not coord:
            return None
        x = int(coord[0])
        y = int(coord[1])
        return Coord(x, y)

    # @staticmethod
    # def init():
    #     a2 = Pawn(1, 2, Piece.pawn, Color.white)
    #     b2 = Pawn(2, 2, Piece.pawn, Color.white)
    #     c2 = Pawn(3, 2, Piece.pawn, Color.white)
    #     d2 = Pawn(4, 2, Piece.pawn, Color.white)
    #     e2 = Pawn(5, 2, Piece.pawn, Color.white)
    #     f2 = Pawn(6, 2, Piece.pawn, Color.white)
    #     g2 = Pawn(7, 2, Piece.pawn, Color.white)
    #     h2 = Pawn(8, 2, Piece.pawn, Color.white)
    #
    #     a2 = Pawn(1, 2, Piece.pawn, Color.white)
    #     b2 = Pawn(2, 2, Piece.pawn, Color.white)
    #     c2 = Pawn(3, 2, Piece.pawn, Color.white)
    #     d2 = Pawn(4, 2, Piece.pawn, Color.white)
    #     e2 = Pawn(5, 2, Piece.pawn, Color.white)
    #     f2 = Pawn(6, 2, Piece.pawn, Color.white)
    #     g2 = Pawn(7, 2, Piece.pawn, Color.white)
    #     h2 = Pawn(8, 2, Piece.pawn, Color.white)
    #
    #     row1 = [a1, a2, a3, a4, a5, a6, a7, a8]
    #     row2 = [b1, b2, b3, b4, b5, b6, b7, b8]
    #     row3 = [c1, c2, c3, c4, c5, c6, c7, c8]
    #     row4 = [d1, d2, d3, d4, d5, d6, d7, d8]
    #     row5=  [e1, e2, e3, e4, e5, e6, e7, e8]
    #     row6 =  [f1, f2, f3, f4, f5, f6, f7, f8]
    #     row7 =  [g1, g2, g3, g4, g5, g6, g7, g8]
    #     row8 =  [h1, h2, h3, h4, h5, h6, h7, h8]
    #     board = [row1, row2, row3, row4, row5, row6, row7, row8]
    #     return board

    def print(self):
        for vec in self.board:
            for square in vec:
                if square.has_piece():
                    print(square.get_piece().get_symbol())
                else:
                    print(".")
                print("\n")
