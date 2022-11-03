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

    def is_legal(self, move: Coord, piece: Chessman):
        print("Move -> is_legal: ", piece.is_legal(move))
        if not piece.is_legal(move):
            return False
        check = False
        if self.turn == Color.white:
            if piece not in self.whites:
                return False
            for piece in self.whites:
                if piece.coord == move:
                    return False
            # new method which check if there are pieces between two figures
            # if true return false
            id = self.whites.index(piece)
            # for piece in self.blacks:
            #     if piece.is_legal(self.whites[0].coord):
            #         check = True
            # if check:
            self.move(move, id)
            print(piece)
            print(piece.is_legal(self.blacks[0].coord))
            for piece in self.blacks:
                if piece.is_legal(self.whites[0].coord):
                    self.undo_last_move()
                    return False
        if self.turn == Color.black:
            if piece not in self.blacks:
                print('Checking if piece exist...')
                return False
            for piece in self.blacks:
                if piece.coord == move:
                    print('Checking if black piece is already on that square...')
                    return False
            # new method which check if there are pieces between two figures
            # if true return false
            id = self.blacks.index(piece)
            print(id)
            # for piece in self.whites:
            #     if piece.is_legal(self.blacks[0].coord):
            #         check = True
            # if check:
            self.move(move, id)
            for piece in self.whites:
                print(piece)
                print(piece.is_legal(self.blacks[0].coord))
                if piece.is_legal(self.blacks[0].coord):
                    self.undo_last_move()
                    return False
        return True

    def move(self, move: Coord, id: int):
        self.last_move = {'piece': self.whites[id], "taken": None}
        if self.turn == Color.white:
            self.whites[id].coord = move
            for piece in self.blacks:
                if piece.coord == move:
                    self.last_move['taken'] = piece
                    self.blacks.remove(piece)
            self.turn = Color.black
        if self.turn == Color.black:
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
        if self.turn == Color.black:
            for piece in self.whites:
                if taken:
                    if taken.coord == piece.coord:
                        self.blacks.append(taken)
                piece.coord = l_piece.coord
            self.turn = Color.white
        self.last_move = {'piece': None, "taken": None}
