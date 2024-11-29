class Node:
    def __init__(self, board: list[list[chr]], children: list['Node'], heurstic_val: int) -> None:
        self.__board = board
        self.__children = children
        self.__heurstic_val = heurstic_val
    
    def get_board(self) -> list[list[chr]]:
        return self.__board
    
    def get_children(self) -> list:
        return self.__children

    def get_heurstic_val(self) -> int:
        return self.__heurstic_val