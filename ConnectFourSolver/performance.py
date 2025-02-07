import time
from utils.factory import Factory

AGENT_PIECE = '1'
HUMAN_PIECE = '2'

AGENT_TURN = 0
HUMAN_TURN = 1


def __count_winning_moves(board, piece):
    """
    Counts all occurrences of connected 4s for the given piece
    """
    count = 0
    # Horizontal check
    for r in range(6):
        row_array = board[r]
        for c in range(4):
            window = list(row_array[c:c + 4])
            if window.count(piece) == 4:
                count += 1

    # Vertical check
    for c in range(7):
        col_array = [row[c] for row in board] 
        for r in range(3):
            window = list(col_array[r:r + 4])
            if window.count(piece) == 4:
                count += 1

    # Diagonal check
    for r in range(3):
        for c in range(4):
            window = list([board[r + i][c + i] for i in range(4)])
            if window.count(piece) == 4:
                count += 1

    # Reversed diagonal check
    for r in range(6):
        for c in range(4):
            window = list([board[r + 3 - i][c + i] for i in range(4)])
            if window.count(piece) == 4:
                count += 1

    return count

def performance_test(board: list[list[chr]], turn: int) -> int:
    human_score = __count_winning_moves(board, HUMAN_PIECE)
    agent_score = __count_winning_moves(board, AGENT_PIECE)

    if turn == AGENT_TURN:
        search = Factory.get_technique("Minimax_alpha_beta", AGENT_PIECE, HUMAN_PIECE, 6)
        start_time = time.time()
        res = search.solve(board, human_score, agent_score)
        end_time = time.time()
        print(f"Time: {end_time - start_time} seconds")
        return res['best_position'][0]
    else:
        search = Factory.get_technique("Minimax_alpha_beta", HUMAN_PIECE, AGENT_PIECE, 6)
        start_time = time.time()
        res = search.solve(board, human_score, agent_score)
        end_time = time.time()
        print(f"Time: {end_time - start_time} seconds")
        return res['best_position'][0]