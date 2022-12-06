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


    # def decode_piece(self, piece: str):
    #     if piece:
    #         return None
    #     if (color == Color::white){
    #     color = Color::black;
    #
    #         }
    #         else {
    #         color = Color::white;
    #         }
    #         switch(piece[0])
    #         {
    #         case
    #         'K':
    #         return new
    #         King(color);
    #         case
    #         'Q':
    #         return new
    #         Queen(color);
    #         case
    #         'B':
    #         return new
    #         Bishop(color);
    #         case
    #         'N':
    #         return new
    #         Knight(color);
    #         case
    #         'R':
    #         return new
    #         Rook(color);
    #         case
    #         'P':
    #         return new
    #         Pawn(color);
    #         }
    #         return nullptr;
    #         }
    #
    #         Coord
    #         Game::decode_coord(std::string
    #         coord){
    #         int
    #         x = (int)
    #         coord[0] - '0';
    #         int
    #         y = (int)
    #         coord[1] - '0';
    #         std::cout << x << std::endl;
    #         std::cout << y << std::endl;
    #         Coord
    #         result_coord
    #         {x, y};
    #         return result_coord;
    #         }
    #
    #         std::vector < std::vector < Square * >>
    #         *Game::init()
    #         {
    #         auto * a1 = new
    #         Square(1, 1, new
    #         Rook());
    #         auto * a2 = new
    #         Square(1, 2, new
    #         Knight());
    #         auto * a3 = new
    #         Square(1, 3, new
    #         Bishop());
    #         auto * a4 = new
    #         Square(1, 4, new
    #         King());
    #         auto * a5 = new
    #         Square(1, 5, new
    #         Queen());
    #         auto * a6 = new
    #         Square(1, 6, new
    #         Bishop());
    #         auto * a7 = new
    #         Square(1, 7, new
    #         Knight());
    #         auto * a8 = new
    #         Square(1, 8, new
    #         Rook());
    #         auto * b1 = new
    #         Square(2, 1, new
    #         Pawn());
    #         auto * b2 = new
    #         Square(2, 2, new
    #         Pawn());
    #         auto * b3 = new
    #         Square(2, 3, new
    #         Pawn());
    #         auto * b4 = new
    #         Square(2, 4, new
    #         Pawn());
    #         auto * b5 = new
    #         Square(2, 5, new
    #         Pawn());
    #         auto * b6 = new
    #         Square(2, 6, new
    #         Pawn());
    #         auto * b7 = new
    #         Square(2, 7, new
    #         Pawn());
    #         auto * b8 = new
    #         Square(2, 8, new
    #         Pawn());
    #         auto * c1 = new
    #         Square(3, 1);
    #         auto * c2 = new
    #         Square(3, 2);
    #         auto * c3 = new
    #         Square(3, 3);
    #         auto * c4 = new
    #         Square(3, 4);
    #         auto * c5 = new
    #         Square(3, 5);
    #         auto * c6 = new
    #         Square(3, 6);
    #         auto * c7 = new
    #         Square(3, 7);
    #         auto * c8 = new
    #         Square(3, 8);
    #         auto * d1 = new
    #         Square(4, 1);
    #         auto * d2 = new
    #         Square(4, 2);
    #         auto * d3 = new
    #         Square(4, 3);
    #         auto * d4 = new
    #         Square(4, 4);
    #         auto * d5 = new
    #         Square(4, 5);
    #         auto * d6 = new
    #         Square(4, 6);
    #         auto * d7 = new
    #         Square(4, 7);
    #         auto * d8 = new
    #         Square(4, 8);
    #         auto * e1 = new
    #         Square(5, 1);
    #         auto * e2 = new
    #         Square(5, 2);
    #         auto * e3 = new
    #         Square(5, 3);
    #         auto * e4 = new
    #         Square(5, 4);
    #         auto * e5 = new
    #         Square(5, 5);
    #         auto * e6 = new
    #         Square(5, 6);
    #         auto * e7 = new
    #         Square(5, 7);
    #         auto * e8 = new
    #         Square(5, 8);
    #         auto * f1 = new
    #         Square(6, 1);
    #         auto * f2 = new
    #         Square(6, 2);
    #         auto * f3 = new
    #         Square(6, 3);
    #         auto * f4 = new
    #         Square(6, 4);
    #         auto * f5 = new
    #         Square(6, 5);
    #         auto * f6 = new
    #         Square(6, 6);
    #         auto * f7 = new
    #         Square(6, 7);
    #         auto * f8 = new
    #         Square(6, 8);
    #         auto * g1 = new
    #         Square(7, 1, new
    #         Pawn(Color::black));
    #         auto * g2 = new
    #         Square(7, 2, new
    #         Pawn(Color::black));
    #         auto * g3 = new
    #         Square(7, 3, new
    #         Pawn(Color::black));
    #         auto * g4 = new
    #         Square(7, 4, new
    #         Pawn(Color::black));
    #         auto * g5 = new
    #         Square(7, 5, new
    #         Pawn(Color::black));
    #         auto * g6 = new
    #         Square(7, 6, new
    #         Pawn(Color::black));
    #         auto * g7 = new
    #         Square(7, 7, new
    #         Pawn(Color::black));
    #         auto * g8 = new
    #         Square(7, 8, new
    #         Pawn(Color::black));
    #         auto * h1 = new
    #         Square(8, 1, new
    #         Rook(Color::black));
    #         auto * h2 = new
    #         Square(8, 2, new
    #         Knight(Color::black));
    #         auto * h3 = new
    #         Square(8, 3, new
    #         Bishop(Color::black));
    #         auto * h4 = new
    #         Square(8, 4, new
    #         King(Color::black));
    #         auto * h5 = new
    #         Square(8, 5, new
    #         Queen(Color::black));
    #         auto * h6 = new
    #         Square(8, 6, new
    #         Bishop(Color::black));
    #         auto * h7 = new
    #         Square(8, 7, new
    #         Knight(Color::black));
    #         auto * h8 = new
    #         Square(8, 8, new
    #         Rook(Color::black));
    #         std::vector < Square * > row1
    #         {a1, a2, a3, a4, a5, a6, a7, a8};
    #         std::vector < Square * > row2
    #         {b1, b2, b3, b4, b5, b6, b7, b8};
    #         std::vector < Square * > row3
    #         {c1, c2, c3, c4, c5, c6, c7, c8};
    #         std::vector < Square * > row4
    #         {d1, d2, d3, d4, d5, d6, d7, d8};
    #         std::vector < Square * > row5
    #         {e1, e2, e3, e4, e5, e6, e7, e8};
    #         std::vector < Square * > row6
    #         {f1, f2, f3, f4, f5, f6, f7, f8};
    #         std::vector < Square * > row7
    #         {g1, g2, g3, g4, g5, g6, g7, g8};
    #         std::vector < Square * > row8
    #         {h1, h2, h3, h4, h5, h6, h7, h8};
    #         auto * board = new
    #         std::vector < std::vector < Square * >> {row1, row2, row3, row4, row5, row6, row7, row8};
    #         return board;
    #         }
    def print(self):
        for vec in self.board:
            for square in vec:
                if square.has_piece():
                    print(square.get_piece().get_symbol())
                else:
                    print(".")
                print("\n")
