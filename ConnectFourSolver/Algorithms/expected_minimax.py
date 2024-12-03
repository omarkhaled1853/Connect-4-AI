import math
import random
import copy
from Algorithms.search import Search
from utils.node import Node
from utils.heuristic import heuristic_score

class Expected_minimax(Search):
    def __init__(self, agent_piece: chr, human_piece: chr, depth: int = 42, rows: int = 6, cols: int = 7) -> None:
        super().__init__(agent_piece, human_piece, depth, rows, cols)
    
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

    def __is_valid_column(self, board: list[list[chr]], col: int) -> bool:
        """
        Check if the column not full
        """
        return board[0][col] == '0'
    
    def __is_out_of_board(self, col: int) -> bool:
        return col < 0 or col >= self._cols
    
    def get_valid_columns(self, board: list[list[int]]) -> list:
        valid_locations = []
        for col in range(self._cols):
            if self.__is_valid_column(board, col):
                valid_locations.append(col)
        return valid_locations
    
    def get_next_open_row(self, board: list[list[chr]], col: int) -> int:
        for r in range(self._rows -1, -1, -1):
            if board[r][col] == '0':
                return r
        
    def __chance_evaluation(self, board: list[list[chr]], depth: int, human_score: int, agent_score: int, 
                col: int, maximizing_player: bool = True) -> Node:
        
        left = 0.2
        midle = 0.6
        right = 0.2
        res = 0

        chance_node = Node.chance_node()

        # out of board or not valid
        if self.__is_out_of_board(col - 1) or not self.__is_valid_column(board, col - 1): #left
            midle += left
        else:
            # valid left
            board_copy = copy.deepcopy(board)
            row = self.get_next_open_row(board, col - 1)
            position = (row, col - 1)
            self.__update_board(board_copy, position)
            new_node = Node(board_copy)
            _, value = self.minimax(new_node, depth - 1, human_score, agent_score, not maximizing_player)
            
            chance_node.add_child(new_node)

            res += left * value
        
        # out of bound or not valid
        if self.__is_out_of_board(col + 1) or not self.__is_valid_column(board, col + 1): #midle
            midle += right
        # valid or not valid right
        board_copy = copy.deepcopy(board)
        row = self.get_next_open_row(board, col)
        position = (row, col)
        self.__update_board(board_copy, position)
        new_node = Node(board_copy)
        _, value = self.minimax(new_node, depth - 1, human_score, agent_score, not maximizing_player)
        
        chance_node.add_child(new_node)

        res += midle * value

        # not out of bound and valid
        if not self.__is_out_of_board(col + 1) and self.__is_valid_column(board, col + 1): #right
            board_copy = copy.deepcopy(board)
            row = self.get_next_open_row(board, col + 1)
            position = (row, col + 1)
            self.__update_board(board_copy, position)
            new_node = Node(board_copy)
            _, value = self.minimax(new_node, depth - 1, human_score, agent_score, not maximizing_player)
            
            chance_node.add_child(new_node)

            res += right * value
        
        chance_node.set_value(res)
        
        return chance_node

    def minimax(self, node: Node, depth: int, human_score: int, agent_score: int, 
                maximizing_player: bool = True) -> tuple:
        """ 
        Get best position to play with its value
        based on it is maximization node or minimization node
        """
        # get board
        board = node.get_board()
        # get valid columns
        valid_cols = self.get_valid_columns(board)
        # check terminal node
        is_terminal = self.__is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                agent_wins, human_wins = self.__winning_move(board)
                if agent_wins > human_wins:
                    node.set_value(math.inf)
                    return (None, math.inf)
                elif agent_wins < human_wins:
                    node.set_value(-math.inf)
                    return (None, -math.inf)
                else:
                    node.set_value(0)
                    return (None, 0)
            else:
                heurstic_value = heuristic_score(board, self._rows, self._cols, self._agent_piece, self._human_piece,
                                                  self._agent_score, self._human_score)
                node.set_value(heurstic_value)
                return (None, heurstic_value)

        elif maximizing_player:
            value = -math.inf
            best_col = random.choice(valid_cols)
            for col in valid_cols:
                chance_node = self.__chance_evaluation(board, depth - 1, human_score, agent_score, col, maximizing_player)
                # add chance node to the max node
                node.add_child(chance_node)
                chance_value = chance_node.get_value()
                if chance_value > value:
                    value = chance_value
                    best_col = col
            node.set_value(value)
            return best_col, value
        else: #minimizing player
            value = math.inf
            best_col = random.choice(valid_cols)
            for col in valid_cols:
                chance_node = self.__chance_evaluation(board, depth - 1, human_score, agent_score, col, maximizing_player)
                # add chance node to the min node
                node.add_child(chance_node)
                chance_value = chance_node.get_value()
                if chance_value < value:
                    value = chance_value
                    best_col = col
            node.set_value(value)
            return best_col, value


    def solve(self, board: list[list[chr]], human_score: int, agent_score: int) -> dict:
        node = Node(board)
        col, _ = self.minimax(node, self._depth, human_score, agent_score)
        row = self.get_next_open_row(board, col)
        best_position = (row, col)
        return {
            'best_position': best_position,
            'node': node
        }