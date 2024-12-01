from abc import ABC, abstractmethod

# Abstract class for all different search algorithms
class Search(ABC):
    def __init__(self, piece: int, depth: int, rows: int = 6, cols: int = 7) -> None:
        self._piece= piece
        self._depth = depth
        self._rows = rows
        self._cols = cols
        self._board = []
        self._human_score = 0
        self._agent_score = 0
    
    @abstractmethod
    def solve(self) -> dict:
        """Abstract method to be implemented by subclasses"""
        pass

    def get_board(self) -> list[list[chr]]:
        """Getter for board"""
        return self._board
    
    def set_board(self, board: list[list[chr]]):
        """Setter for board"""
        self._board = board
    
    def get_human_score(self) -> int:
        """Getter for human score"""
        return self._human_score
    
    def set_human_score(self, human_score):
        """Setter for human score"""
        self._human_score = human_score
    
    def get_agent_score(self) -> int:
        """Getter for agent score"""
        return self._agent_score
    
    def set_agent_score(self, agent_score):
        """Setter for agent score"""
        self._agent_score = agent_score