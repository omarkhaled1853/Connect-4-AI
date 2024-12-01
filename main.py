from Algorithms.minimax import Minimax

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

    search = Minimax(AGENT_PIECE, HUMAN_PIECE)
    res = search.solve(board, human_score, agent_score)
    print(res['best_position'])
