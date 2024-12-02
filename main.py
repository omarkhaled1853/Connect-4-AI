from Algorithms.minimax import Minimax
from Algorithms.minimax_alpha_beta import Minimax_alpha_beta
from Algorithms.expected_minimax import Expected_minimax

if __name__ == '__main__':
    AGENT_PIECE = '1'
    HUMAN_PIECE = '2'
    
    board = [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '1', '0', '2', '0', '0', '0'],
        ['0', '2', '0', '1', '1', '0', '0'],
        ['2', '2', '0', '1', '2', '0', '0'],
        ['2', '2', '1', '1', '2', '1', '0'],
    ]

    human_score = 0
    agent_score = 0

    search = Expected_minimax(AGENT_PIECE, HUMAN_PIECE, 8)
    search.set_agent_score(agent_score)
    search.set_human_score(human_score)
    res = search.solve(board, human_score, agent_score)
    print(res['best_position'])
