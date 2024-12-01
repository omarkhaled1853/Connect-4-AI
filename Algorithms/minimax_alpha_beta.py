from Algorithms.search import Search

class Minimax_alpha_beta(Search):
    def __init__(self, agent_piece: chr, human_piece: chr, depth: int = 42, rows: int = 6, cols: int = 7) -> None:
        super().__init__(agent_piece, human_piece, depth, rows, cols)
    
    def solve(self, board: list[list], human_score: int, agent_score: int) -> dict:
        return super().solve(board, human_score, agent_score)