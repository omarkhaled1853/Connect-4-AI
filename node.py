class node:
    def __init__(self, board: str) -> None:
        self.__board = board
    
    def get_board(self) -> str:
        return self.__board
    
    def __hash__(self) -> int:
        return hash(self.__board)
    
    def __eq__(self, other) -> bool:
        return self.__board == other.__board