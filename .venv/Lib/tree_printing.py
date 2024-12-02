from typing import List, Optional
from collections import deque  # Use deque for efficient BFS queue
from utils.node import Node

from collections import deque


def print_tree_bfs(root: Node, file):
    if root is None:
        return

    queue = deque([root])
    node_counter = 1
    node_mapping = {}

    while queue:
        current = queue.popleft()

        node_mapping[current] = node_counter

        children = current.get_children()
        queue.extend(children)

        node_counter += 1  # Increment the node counter

    queue = deque([(root, 0)])  # Reinitialize the queue for the second pass
    current_level = 0  # Track of the current level

    while queue:
        current, level = queue.popleft()

        if level > current_level:
            file.write("\n")
            current_level = level

        file.write(f"Node {node_mapping.get(current)}: {current.get_value()}, Children: ")

        children = current.get_children()
        if children:
            # Get the node numbers of the children
            child_numbers = [str(node_mapping.get(child)) for child in children if child in node_mapping]
            file.write(", ".join(child_numbers))
        else:
            file.write("None")

        file.write("\n")

        queue.extend([(child, level + 1) for child in children])


def write_tree_to_file_bfs(root: Node, filename: str):
    # Write the tree to a file using BFS traversal
    with open(filename, 'w') as file:
        print_tree_bfs(root, file)
    print("Tree has been written to file.")