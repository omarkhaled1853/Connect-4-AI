from typing import List, Optional
from collections import deque  # Use deque for efficient BFS queue
from tree_gui import Node

def print_tree_bfs(root: Node, file):
    queue = deque([root])

    while queue:
        current = queue.popleft()  # Pop node from the front of the queue

        file.write(f"Node: {current.val}, Childs: ")

        if current.childs:
            file.write(", ".join(str(child.val) for child in current.childs))

        file.write("\n")

        queue.extend(current.childs)


def write_tree_to_file_bfs(root: Node, filename: str):
    # Write the tree to a file using BFS traversal
    with open(filename, 'w') as file:
        print_tree_bfs(root, file)
    print("Tree has been written to file.")