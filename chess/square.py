from chess.coord import Coord
from chessman import Chessman


class Square(Coord):
    def __init__(self, x: int, y: int, chessman: Chessman = None):
        super().__init__(x, y)
        self.chessman = chessman

    def get_piece(self):
        return self.chessman

    def has_piece(self):
        if self.chessman:
            return True
        else:
            return False

    def set_null(self):
        self.chessman = None

    def capture_piece(self):
        self.chessman = None
