from search import Search

class Minimax_alpha_beta(Search):
    def __init__(self, piece: int, rows: int = 6, cols: int = 7) -> None:
        super().__init__(piece, rows, cols)
    
    def solve(self) -> dict:
        return super().solve()