from abc import ABC, abstractmethod

# Abstract class for all different search algorithms
class Search(ABC):
    def __init__(self, agent_piece: chr, human_piece: chr, depth: int = 42, rows: int = 6, cols: int = 7) -> None:
        self._agent_piece= agent_piece
        self._human_piece = human_piece
        self._depth = depth
        self._rows = rows
        self._cols = cols
        self._agent_score = 0
        self._human_score = 0
    
    @abstractmethod
    def solve(self, board: list[list[chr]], human_score: int, agent_score: int) -> dict:
        """Abstract method to be implemented by subclasses"""
        pass

    def set_agent_score(self, agent_score):
        self._agent_score = agent_score
    
    def set_human_score(self, human_score):
        self._human_score = human_score