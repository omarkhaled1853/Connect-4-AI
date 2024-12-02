from utils.factory import Factory
from utils.node import Node

def print_children(node: Node):
    if node == None:
        return
    print(node.get_value())

    for child in node.get_children():
        print_children(child)


def main():

    AGENT_PIECE = '1'
    HUMAN_PIECE = '2'
    
    board = [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '1', '0', '2', '0', '0', '0'],
        ['0', '2', '0', '1', '1', '0', '0'],
        ['2', '2', '0', '1', '2', '0', '0'],
        ['2', '2', '1', '1', '2', '1', '0'],
    ]

    human_score = 0
    agent_score = 0

    search = Factory.get_technique("Minimax", AGENT_PIECE, HUMAN_PIECE, 2)
    res = search.solve(board, human_score, agent_score)
    print(res['best_position'])
    print_children(res['node'])


if __name__ == '__main__':
    main()