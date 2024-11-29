from Algorithms.minimax import Minimax

if __name__ == '__main__':
    AGENT = 1
    HUMAN = 2
    
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

    search = Minimax(AGENT)
    search.set_board(board)
    search.set_human_score(human_score)
    search.set_agent_score(agent_score)

    print(f'{search.get_board()}\n{search.get_human_score()}\n{search.get_agent_score()}')
