from typing import List, Optional
from collections import deque  # Use deque for efficient BFS queue
from utils.node import Node

def print_tree_bfs(root: Node, file):
    if root is None:
        return
    queue = deque([root])

    while queue:
        current = queue.popleft()  # Pop node from the front of the queue

        file.write(f"Node: {current.get_value()}, Children: ")

        if current.get_children():
            file.write(", ".join(str(child.get_value()) for child in current.get_children()))

        file.write("\n")

        queue.extend(current.get_children())


def write_tree_to_file_bfs(root: Node, filename: str):
    # Write the tree to a file using BFS traversal
    with open(filename, 'w') as file:
        print_tree_bfs(root, file)
    print("Tree has been written to file.")