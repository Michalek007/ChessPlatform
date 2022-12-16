from chess.coord import Coord
from chess.chessman import Chessman


class Square(Coord):
    def __init__(self, x: int, y: int, chessman=None):
        super().__init__(x, y)
        self.piece = chessman

    def get_piece(self):
        return self.piece

    def has_piece(self):
        if self.piece:
            return True
        else:
            return False

    def set_null(self):
        self.piece = None

    def capture_piece(self):
        self.piece = None

    def get_piece_symbol(self):
        return self.piece.get_symbol()

    def get_coord_symbol(self):
        return str(self.x) + str(self.y)
