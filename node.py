class Node:
    def __init__(self, board: list[list[chr]]) -> None:
        self.__board = board
        self.__children = []
        self.__heurstic_value = 0
    
    def get_board(self) -> list[list[chr]]:
        return self.__board
    
    def get_children(self) -> list:
        return self.__children
    
    def add_child(self, node: 'Node'):
        self.__children.append(node)
    
    def get_heurstic_value(self) -> int:
        return self.__heurstic_value

    def set_heuristic_value(self, heurstic_value: int):
        self.__heurstic_value = heurstic_value