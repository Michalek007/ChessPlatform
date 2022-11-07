from chess.enum_types import *
from chess.chessman import Chessman
from chess.coord import Coord


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
        # self.last_move = dict(piece=None, coord=None, taken=None)
        self.last_move = {}
        self.game_record = []

    @staticmethod
    def init():
        list_of_pieces = [
            Chessman(1, 5, Piece.king, Color.white),
            Chessman(8, 5, Piece.king, Color.black),
            Chessman(1, 4, Piece.queen, Color.white),
            Chessman(8, 4, Piece.queen, Color.black),
            Chessman(1, 3, Piece.bishop, Color.white),
            Chessman(1, 6, Piece.bishop, Color.white),
            Chessman(8, 3, Piece.bishop, Color.black),
            Chessman(8, 6, Piece.bishop, Color.black),
            Chessman(1, 2, Piece.knight, Color.white),
            Chessman(1, 7, Piece.knight, Color.white),
            Chessman(8, 2, Piece.knight, Color.black),
            Chessman(8, 7, Piece.knight, Color.black),
            Chessman(1, 1, Piece.rook, Color.white),
            Chessman(1, 8, Piece.rook, Color.white),
            Chessman(8, 1, Piece.rook, Color.black),
            Chessman(8, 8, Piece.rook, Color.black),
            Chessman(2, 1, Piece.pawn, Color.white),
            Chessman(2, 2, Piece.pawn, Color.white),
            Chessman(2, 3, Piece.pawn, Color.white),
            Chessman(2, 4, Piece.pawn, Color.white),
            Chessman(2, 5, Piece.pawn, Color.white),
            Chessman(2, 6, Piece.pawn, Color.white),
            Chessman(2, 7, Piece.pawn, Color.white),
            Chessman(2, 8, Piece.pawn, Color.white),
            Chessman(7, 1, Piece.pawn, Color.black),
            Chessman(7, 2, Piece.pawn, Color.black),
            Chessman(7, 3, Piece.pawn, Color.black),
            Chessman(7, 4, Piece.pawn, Color.black),
            Chessman(7, 5, Piece.pawn, Color.black),
            Chessman(7, 6, Piece.pawn, Color.black),
            Chessman(7, 7, Piece.pawn, Color.black),
            Chessman(7, 8, Piece.pawn, Color.black)
        ]
        return list_of_pieces

    def make_move(self, move: Coord, piece: Chessman):
        if not self.is_legal(move=move, piece=piece):
            return False
        if self.turn == Color.white:
            id = self.whites[self.whites.index(piece)]
            self.last_move = {'piece': self.whites[id], "taken": None}
            self.whites[id].coord = move
            for piece in self.blacks:
                if piece.coord == move:
                    self.last_move['taken'] = piece
                    self.blacks.remove(piece)
            self.turn = Color.black
        else:
            id = self.blacks[self.blacks.index(piece)]
            self.game_record.append({'piece': self.blacks[id], 'coord': move, "taken": None})
            self.last_move = self.game_record[-1]
            self.blacks[id].coord = move
            for piece in self.whites:
                if piece.coord == move:
                    self.game_record[-1]['taken'] = piece
                    self.last_move['taken'] = piece
                    self.whites.remove(piece)
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
            if not self.check_obstacle(piece, move):
                return False
            id = self.whites.index(piece)
            self.move(move, id)
            for item in self.blacks:
                if not item.is_legal(self.whites[0].coord):
                    continue
                if self.check_obstacle(item, self.whites[0].coord):
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
            if not self.check_obstacle(piece, move):
                return False
            id = self.blacks.index(piece)
            self.move(move, id)
            for item in self.whites:
                if not item.is_legal(self.blacks[0].coord):
                    continue
                if self.check_obstacle(item, self.blacks[0].coord):
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
            self.last_move = {'piece': None, "taken": None}

    def check_obstacle(self, piece, move):
        if piece.type == Piece.knight or piece.type == Piece.king:
            return True
        iter = Coord(piece.coord.x, piece.coord.y)
        if piece.type == Piece.pawn:
            if move.x != piece.coord.x:
                if piece.color == Color.white:
                    for item in self.blacks:
                        if move.x == item.coord.x:
                            return True
                if piece.color == Color.black:
                    for item in self.whites:
                        if move.x == item.coord.x:
                            return True
                if piece.color == Color.white and piece.coord.x != 5:
                    return False
                if piece.color == Color.black and piece.coord.x != 4:
                    return False
                if self.last_move['piece'].type != Piece.pawn:
                    return False
                if self.last_move['coord'].y == 5 and self.last_move['piece'].coord.y == 7:
                    if move.x == self.last_move['piece'].coord.x:
                        return True
                if self.last_move['coord'].y == 4 and self.last_move['piece'].coord.y == 2:
                    if move.x == self.last_move['piece'].coord.x:
                        return True
                return False
            if move.y == piece.coord.y + 2:
                if piece.coord.y != 2:
                    return False
                for item in self.whites:
                    if move.y + 1 == item.coord.y:
                        return False
                for item in self.blacks:
                    if move.y + 1 == item.coord.y:
                        return False
                return True
            if move.y == piece.coord.y - 2:
                if piece.coord.y != 7:
                    return False
                for item in self.whites:
                    if move.y - 1 == item.coord.y:
                        return False
                for item in self.blacks:
                    if move.y - 1 == item.coord.y:
                        return False
                return True
            return True
        if piece.coord > move:
            while True:
                iter.iterate_left_down()
                if iter == move:
                    break
                for item in self.blacks:
                    if iter == item.coord:
                        return False
                for item in self.whites:
                    if iter == item.coord:
                        return False
        if piece.coord < move:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_right_up()
                if iter == move:
                    break
                for item in self.blacks:
                    if iter == item.coord:
                        return False
                for item in self.whites:
                    if iter == item.coord:
                        return False
        if piece.coord.x > move.x and piece.coord.y < move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_left_up()
                if iter == move:
                    break
                for item in self.blacks:
                    if iter == item.coord:
                        return False
                for item in self.whites:
                    if iter == item.coord:
                        return False
        if piece.coord.x < move.x and piece.coord.y > move.y:
            while True:
                iter.iterate_right_down()
                if iter == move:
                    break
                for item in self.blacks:
                    if iter == item.coord:
                        return False
                for item in self.whites:
                    if iter == item.coord:
                        return False
        if piece.coord.x == move.x and piece.coord.y > move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_down()
                if iter == move:
                    break
                for item in self.blacks:
                    if iter == item.coord:
                        return False
                for item in self.whites:
                    if iter == item.coord:
                        return False
        if piece.coord.x == move.x and piece.coord.y < move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_up()
                if iter == move:
                    break
                for item in self.blacks:
                    if iter == item.coord:
                        return False
                for item in self.whites:
                    if iter == item.coord:
                        return False
        if piece.coord.x > move.x and piece.coord.y == move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_left()
                if iter == move:
                    break
                for item in self.blacks:
                    if iter == item.coord:
                        return False
                for item in self.whites:
                    if iter == item.coord:
                        return False
        if piece.coord.x < move.x and piece.coord.y == move.y:
            iter.x, iter.y = (piece.coord.x, piece.coord.y)
            while True:
                iter.iterate_right()
                if iter == move:
                    break
                for item in self.blacks:
                    if iter == item.coord:
                        return False
                for item in self.whites:
                    if iter == item.coord:
                        return False
        return True
