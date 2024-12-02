
# factory class to returun specific search alogrithm
class Factory:
    @staticmethod
    def get_technique(algorithm_name: str, agent_piece: chr, human_piece: chr,
                       depth: int = 42, rows: int = 6, cols: int = 7) -> Search:
        if algorithm_name == 'Minimax':
            return Minimax(agent_piece, human_piece, depth, rows, cols)
        elif algorithm_name == 'MiniMax_alpha_beta':
            return MiniMax_alpha_beta(agent_piece, human_piece, depth, rows, cols)
        elif algorithm_name == 'Expected_minimax':
            return Expected_minimax(agent_piece, human_piece, depth, rows, cols)
        else: None