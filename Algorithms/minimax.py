from search import Search
from node import Node
import math
import random

class Minimax(Search):
    def __init__(self, piece: int, rows: int = 6, cols: int = 7) -> None:
        super().__init__(piece, rows, cols)
    
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
            for row in range(self._rows - 1, -1):
                if board[row][col] == '0':
                    valid_positions.append((row, col))
                    break
        return valid_positions
    
    def __update_board(self, board: list[list[chr]], position: tuple):
        """ Update board with agent piece """
        board[position] = self._piece

    def minimax(self, node: Node, depth: int = 42, maximizing_player: bool = True) -> tuple:
        """ Get best position to play with its value
            based on it is maximization node or minimization node
        """
        # get board
        board = node.get_board()
        # get valid positions
        valid_positions = self.__get_valid_positions()
        # check terminal node
        is_terminal = self.__is_terminal_node(board)
        if depth == 0 or is_terminal:
            node.set_heuristic_value(math.inf)
            # return heurstic value
            # dummy
            return (None, math.inf)
        
        if maximizing_player:
            value = -math.inf
            best_position = random.choice(valid_positions)
            for position in valid_positions:
                board_copy = board.copy()
                self.__update_board(board_copy, position)
                
                new_node = Node(board_copy)
                temp_value = self.minimax(new_node, depth - 1, False)
                if (temp_value > value):
                    value = temp_value
                    best_position = position
                new_node.set_heuristic_value(value)
                node.add_child(new_node)
            
            return (best_position, value)
        else: #minimizing player
            value = math.inf
            best_position = random.choice(valid_positions)
            for position in valid_positions:
                board_copy = board.copy()
                self.__update_board(board_copy, position)
                
                new_node = Node(board_copy)
                temp_value = self.minimax(new_node, depth - 1, True)
                if (temp_value < value):
                    value = temp_value
                    best_position = position
                new_node.set_heuristic_value(value)
                node.add_child(new_node)
            
            return (best_position, value)


    def solve(self) -> dict:
        node = Node(self._board)
        best_position, _ = self.minimax(node, self._depth)
        pass