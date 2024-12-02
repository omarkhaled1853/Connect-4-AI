import math

class Node:
    def __init__(self, board: list[list[chr]]) -> None:
        self.__board = board
        self.__children = []
        self.__heurstic_value = 0
        self.__alpha = -math.inf
        self.__beta = math.inf
    
    @classmethod
    def chance_node(cls):
        """
        Alternative constructor to create a Node with only a heuristic value.
        """
        node = cls(board=[])  # Initialize with an empty board
        return node

    def get_board(self) -> list[list[chr]]:
        return self.__board
    
    def get_children(self) -> list:
        return self.__children
    
    def add_child(self, node: 'Node'):
        self.__children.append(node)
    
    def get_heurstic_value(self) -> int:
        return self.__heurstic_value

    def set_heuristic_value(self, heurstic_value: float):
        self.__heurstic_value = heurstic_value
    
    def get_alpha(self) -> int:
        return self.__alpha
    
    def set_alpha(self, alpha: int):
        self.__alpha = alpha
    
    def get_beta(self) -> int:
        return self.__beta
    
    def set_beta(self, beta: int):
        self.__beta = beta