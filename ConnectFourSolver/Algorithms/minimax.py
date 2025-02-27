import math
import random
import copy
from ConnectFourSolver.Algorithms.search import Search
from ConnectFourSolver.utils.node import Node
from ConnectFourSolver.utils.heuristic import heuristic_score


class Minimax(Search):
    def __init__(self, agent_piece: chr, human_piece: chr, depth: int = 42, rows: int = 6, cols: int = 7) -> None:
        super().__init__(agent_piece, human_piece, depth, rows, cols)
        # Initialize memoization cache
        self.dp = {}

    def __is_terminal_node(self, board: list[list[chr]]) -> bool:
        """ Terminal node if board is full """
        for i in range(self._rows):
            for j in range(self._cols):
                if board[i][j] == '0':
                    return False
        return True

    def __get_valid_positions(self, board: list[list[chr]]) -> list:
        """ Get valid (empty) positions to play """
        valid_positions = []
        for col in range(self._cols):
            for row in range(self._rows - 1, -1, -1):
                if board[row][col] == '0':
                    valid_positions.append((row, col))
                    break
        return valid_positions

    def __update_board(self, board: list[list[chr]], position: tuple):
        """ Update board with agent piece """
        row, col = position
        board[row][col] = self._agent_piece

    def __count_winning_moves(self, board, piece):
        """
        Counts all occurrences of connected 4s for the given piece
        """
        count = 0
        # Horizontal check
        for r in range(self._rows):
            row_array = board[r]
            for c in range(self._cols - 3):
                window = list(row_array[c:c + 4])
                if window.count(piece) == 4:
                    count += 1

        # Vertical check
        for c in range(self._cols):
            col_array = [row[c] for row in board]
            for r in range(self._rows - 3):
                window = list(col_array[r:r + 4])
                if window.count(piece) == 4:
                    count += 1

        # Diagonal check
        for r in range(self._rows - 3):
            for c in range(self._cols - 3):
                window = list([board[r + i][c + i] for i in range(4)])
                if window.count(piece) == 4:
                    count += 1

        # Reversed diagonal check
        for r in range(self._rows - 3):
            for c in range(self._cols - 3):
                window = list([board[r + 3 - i][c + i] for i in range(4)])
                if window.count(piece) == 4:
                    count += 1

        return count

    def __winning_move(self, board: list[list[chr]]):
        """
        Counts connected 4s occurrences for both the agent and the human.
        """
        agent_wins = self.__count_winning_moves(board, self._agent_piece)
        human_wins = self.__count_winning_moves(board, self._human_piece)

        return agent_wins, human_wins

    def minimax(self, node: Node, depth: int, human_score: int, agent_score: int,
                maximizing_player: bool = True) -> tuple:
        """
        Get best position to play with its value
        based on whether it's a maximization node or minimization node
        """
        # Get the board
        board = node.get_board()
        # Convert board to a tuple for memoization (as it needs to be hashable)
        board_tuple = tuple(tuple(row) for row in board)

        # Check if the result for the current board is already cached
        if board_tuple in self.dp:
            return self.dp[board_tuple]

        # Get valid positions
        valid_positions = self.__get_valid_positions(board)
        # Check if it's a terminal node
        is_terminal = self.__is_terminal_node(board)

        # Base case: depth 0 or terminal node
        if depth == 0 or is_terminal:
            if is_terminal:
                agent_wins, human_wins = self.__winning_move(board)
                if agent_wins > human_wins:
                    node.set_value(math.inf)
                    result = (None, math.inf)
                elif agent_wins < human_wins:
                    node.set_value(-math.inf)
                    result = (None, -math.inf)
                else:
                    node.set_value(0)
                    result = (None, 0)
            else:
                heuristic_value = heuristic_score(board, self._rows, self._cols, self._agent_piece, self._human_piece,
                                                  self._agent_score, self._human_score)
                node.set_value(heuristic_value)
                result = (None, heuristic_value)

            # Cache the result
            self.dp[board_tuple] = result
            return result

        # Maximizing player
        if maximizing_player:
            value = -math.inf
            best_position = random.choice(valid_positions)
            for position in valid_positions:
                board_copy = copy.deepcopy(board)
                self.__update_board(board_copy, position)

                new_node = Node(board_copy)
                temp_value = self.minimax(new_node, depth - 1, human_score, agent_score, False)[1]
                if temp_value > value:
                    value = temp_value
                    best_position = position
                new_node.set_value(value)
                node.add_child(new_node)

            # Cache the result
            result = (best_position, value)
            self.dp[board_tuple] = result
            return result
        else:  # Minimizing player
            value = math.inf
            best_position = random.choice(valid_positions)
            for position in valid_positions:
                board_copy = copy.deepcopy(board)
                self.__update_board(board_copy, position)

                new_node = Node(board_copy)
                temp_value = self.minimax(new_node, depth - 1, human_score, agent_score, True)[1]
                if temp_value < value:
                    value = temp_value
                    best_position = position
                new_node.set_value(value)
                node.add_child(new_node)

            # Cache the result
            result = (best_position, value)
            self.dp[board_tuple] = result
            return result

    def solve(self, board: list[list[chr]], human_score: int, agent_score: int) -> dict:
        node = Node(board)
        best_position, value = self.minimax(node, self._depth, human_score, agent_score)
        node.set_value(value)
        return {
            'best_position': best_position,
            'node': node
        }
