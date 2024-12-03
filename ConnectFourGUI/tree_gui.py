import tkinter as tk
import threading
from ConnectFourSolver.utils.node import Node
import time


class TreeVisualizer(tk.Tk):
    def __init__(self, root):
        super().__init__()
        self.title("Tree Visualizer")
        self.width = 1500
        self.height = 1900
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()
        self.root = root
        self.node_radius = 10
        self.y_offset = 50
        self.level_gap = 50
        self.turn = 0

        self.draw_treet(root, 0, self.width, self.y_offset, self.turn)

    def draw_treet(self, node: Node, start, end, y, turn):
        x = start + (end - start) / 2

        color = "lightblue"
        if turn == 1:
            color = "orange"

        self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                x + self.node_radius, y + self.node_radius,
                                fill=color, outline="black")

        self.canvas.create_text(x, y, text=str(node.get_value()), font=("Arial", 5))

        if node.get_children():
            dis = (end - start) / len(node.get_children())
            children = node.get_children()
            for child in children:
                childStart = start
                childEnd = start + dis
                childX = childStart + (childEnd - childStart) / 2

                self.canvas.create_line(x, y + self.node_radius, childX,
                                        y + self.level_gap - self.node_radius,
                                        arrow=tk.LAST)

                self.draw_treet(child, start, start + dis, y + self.level_gap, (turn + 1) % 2)

                start += dis


def tree_visualize(root: Node):
    if root is None:
        return
    app = TreeVisualizer(root)
    app.mainloop()
