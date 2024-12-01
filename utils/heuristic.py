def evaluate_window(window: list[list[chr]], piece: chr) -> int:
    """
    Evaluates a single window of 4 and calculates counts for twos, threes, and fours.
    """
    score = 0
    
    if window.count(piece) == 4:
        score += 10000
    elif window.count(piece) == 3 and window.count('0') == 1:
        score += 50
    elif window.count(piece) == 2 and window.count('0') == 2:
        score += 10
        
    return score

def heuristic_score(board: list[list[chr]], rows: int, cols: int, agent_piece: chr, human_piece: chr):
    """
    Calculates the overall heuristic score for the current board state.
    """
    agent_total_score = 0
    human_total_score = 0

    # Score center column
    center_array = [row[cols // 2] for row in board]
    center_count = center_array.count(agent_piece)
    agent_total_score += center_count * 3

    # Horizontal scoring
    for r in range(rows):
        row_array = board[r]
        for c in range(cols - 3):
            window = row_array[c:c + 4]
            agent_score = evaluate_window(window, agent_piece)
            human_score = evaluate_window(window, human_piece)
            agent_total_score += agent_score
            human_total_score += human_score

    # Vertical scoring
    for c in range(cols):
        col_array = [row[c] for row in board] 
        for r in range(rows - 3):
            window = col_array[r:r + 4]
            agent_score = evaluate_window(window, agent_piece)
            human_score = evaluate_window(window, human_piece)
            agent_total_score += agent_score
            human_total_score += human_score

    # Diagonal scoring
    for r in range(rows - 3):
        for c in range(cols - 3):
            window = [board[r + i][c + i] for i in range(4)]
            agent_score = evaluate_window(window, agent_piece)
            human_score = evaluate_window(window, human_piece)
            agent_total_score += agent_score
            human_total_score += human_score

    # Reversed diagonal scoring
    for r in range(rows - 3):
        for c in range(cols - 3):
            window = [board[r + 3 - i][c + i] for i in range(4)]
            agent_score = evaluate_window(window, agent_piece)
            human_score = evaluate_window(window, human_piece)
            agent_total_score += agent_score
            human_total_score += human_score

    # Final heuristic score
    return agent_total_score - human_total_score
    