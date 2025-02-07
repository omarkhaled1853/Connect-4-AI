#Board size
ROW_COUNT = 6
COLUMN_COUNT = 7

def num_of_connect4_in_col(board, col, piece):
    count = 0
    for row in range(ROW_COUNT - 3):
        if board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and board[row + 3][col] == piece:
            count += 1

    return count

def num_of_connect4_in_row(board, row, piece):
    count = 0
    for col in range(COLUMN_COUNT - 3):
        if board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and board[row][col + 3] == piece:
            count += 1

    return count

def num_of_connect4_in_pos_diagonal(board, row, col, piece):
    while row > 0 and col > 0:
        row -= 1
        col -= 1

    count = 0
    while row + 3 < ROW_COUNT and col + 3 < COLUMN_COUNT:
        if board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and board[row + 3][col + 3] == piece:
            count += 1
        row += 1
        col += 1

    return count

def num_of_connect4_in_neg_diagonal(board, row, col, piece):
    while row > 0 and col < COLUMN_COUNT - 1:
        row -= 1
        col += 1

    count = 0
    while row + 3 < ROW_COUNT and col - 3 >= 0:
        if board[row][col] == piece and board[row + 1][col - 1] == piece and board[row + 2][col - 2] == piece and board[row + 3][col - 3] == piece:
            count += 1
        row += 1
        col -= 1

    return count

def gain_from_one_piece(board, row, col, piece):
    board[row][col] = 0

    count_col_before = num_of_connect4_in_col(board, col, piece)
    count_row_before = num_of_connect4_in_row(board, row, piece)
    count_pos_diagonal_before = num_of_connect4_in_pos_diagonal(board, row, col, piece)
    count_neg_diagonal_before = num_of_connect4_in_neg_diagonal(board, row, col, piece)

    board[row][col] = piece

    count_col_after = num_of_connect4_in_col(board, col, piece)
    count_row_after = num_of_connect4_in_row(board, row, piece)
    count_pos_diagonal_after = num_of_connect4_in_pos_diagonal(board, row, col, piece)
    count_neg_diagonal_after = num_of_connect4_in_neg_diagonal(board, row, col, piece)

    gain = (count_col_after - count_col_before) + (count_row_after - count_row_before) + (count_pos_diagonal_after - count_pos_diagonal_before) + (count_neg_diagonal_after - count_neg_diagonal_before)
    return gain