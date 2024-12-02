from Algorithms.minimax import Minimax
from Algorithms.minimax_alpha_beta import Minimax_alpha_beta

if __name__ == '__main__':
    AGENT_PIECE = '1'
    HUMAN_PIECE = '2'
    
    board = [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ]

    human_score = 0
    agent_score = 0

    search = Minimax_alpha_beta(AGENT_PIECE, HUMAN_PIECE, 4)
    search.set_agent_score(0)
    search.set_human_score(0)
    res = search.solve(board, human_score, agent_score)
    print(res['best_position'])
