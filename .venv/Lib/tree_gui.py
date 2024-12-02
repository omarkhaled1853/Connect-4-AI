import tkinter as tk
import threading
import time

class Node:
    def __init__(self, val: int):
        self.val = val
        self.childs = []

    def add_child(self, Node):
        self.childs.append(Node)

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

        self.canvas.create_text(x, y, text=str(node.val), font=("Arial", 5))

        if node.childs:
            dis = (end - start) / len(node.childs)

            for child in node.childs:
                childStart = start
                childEnd = start + dis
                childX = childStart + (childEnd - childStart) / 2

                self.canvas.create_line(x, y + self.node_radius, childX,
                                        y + self.level_gap - self.node_radius,
                                        arrow=tk.LAST)

                self.draw_treet(child, start, start + dis, y + self.level_gap, (turn + 1) % 2)

                start += dis



def tree_visualize(root):
    app = TreeVisualizer(root)
    app.mainloop()


# root = Node(0)
# child1 = Node(1)
# child2 = Node(2)
# child3 = Node(3)
# child4 = Node(4)
# child5 = Node(5)
# child6 = Node(6)
# child7 = Node(7)
# child8 = Node(8)
# child9 = Node(9)
#
#
# child10 = Node(10)
# child11 = Node(11)
# child12 = Node(12)
# child13 = Node(13)
# child14 = Node(14)
# child15 = Node(15)
# child16 = Node(16)
# child17 = Node(17)
# child18 = Node(18)
# child19 = Node(19)
# child20 = Node(20)
# child21 = Node(20)
# child22 = Node(20)
# child23 = Node(20)
# child24 = Node(20)
# child25 = Node(20)
# child26 = Node(20)
# child27 = Node(20)
# child28 = Node(20)
# child29 = Node(20)
# child30 = Node(20)
# child31 = Node(20)
# child32 = Node(20)
# child33 = Node(20)
# child34 = Node(20)
# child35 = Node(20)
#
#
#
# root.add_child(child1)
# root.add_child(child2)
# root.add_child(child3)
# root.add_child(child4)
# root.add_child(child5)
# root.add_child(child6)
# root.add_child(child7)


# thread = threading.Thread(target=show_tree, kwargs={'root': root})
# thread.start()
#
# thread.join()

# if __name__ == "__main__":
#
#     root = Node(0)
#     child1 = Node(1)
#     child2 = Node(2)
#     child3 = Node(3)
#     child4 = Node(4)
#     child5 = Node(5)
#     child6 = Node(6)
#     child7 = Node(7)
#     child8 = Node(8)
#     child9 = Node(9)
#
#
#     child10 = Node(10)
#     child11 = Node(11)
#     child12 = Node(12)
#     child13 = Node(13)
#     child14 = Node(14)
#     child15 = Node(15)
#     child16 = Node(16)
#     child17 = Node(17)
#     child18 = Node(18)
#     child19 = Node(19)
#     child20 = Node(20)
#     child21 = Node(20)
#     child22 = Node(20)
#     child23 = Node(20)
#     child24 = Node(20)
#     child25 = Node(20)
#     child26 = Node(20)
#     child27 = Node(20)
#     child28 = Node(20)
#     child29 = Node(20)
#     child30 = Node(20)
#     child31 = Node(20)
#     child32 = Node(20)
#     child33 = Node(20)
#     child34 = Node(20)
#     child35 = Node(20)
#
#
#
#     root.add_child(child1)
#     root.add_child(child2)
#     root.add_child(child3)
#     root.add_child(child4)
#     root.add_child(child5)
#     root.add_child(child6)
#     root.add_child(child7)
#
#
#     #
#     # child1.add_child(child8)
#     # child1.add_child(child9)
#     #
#     # child2.add_child(child10)
#     # child2.add_child(child11)
#     #
#     #
#     # child3.add_child(child12)
#     # child3.add_child(child13)
#     #
#     # child4.add_child(child14)
#     # child4.add_child(child15)
#     #
#     #
#     # child5.add_child(child16)
#     # child5.add_child(child17)
#     # child5.add_child(child18)
#     # child5.add_child(child19)
#     #
#     # child6.add_child(child20)
#     # child6.add_child(child21)
#     # child6.add_child(child22)
#     # child6.add_child(child23)
#     # child6.add_child(child24)
#     # child6.add_child(child25)
#     # child6.add_child(child26)
#     #
#     # child7.add_child(child27)
#     # child7.add_child(child28)
#     # child7.add_child(child29)
#     # child7.add_child(child30)
#     # child7.add_child(child31)
#
#     child8.add_child(child32)
#     child8.add_child(child33)
#     child8.add_child(child34)
#     child8.add_child(child35)
#
#     # child1.add_child(child10)
#     # child1.add_child(child11)
#     #
#     # child2.add_child(child12)
#     # child2.add_child(child13)
#     #
#     # child3.add_child(child14)
#     # child4.add_child(child15)
#     # child4.add_child(child17)
#     #
#     # child5.add_child(child16)
#     #
#     # child15.add_child(child18)
#     # child15.add_child(child19)
#     #
#     # child18.add_child(child20)
#
#     #
#     #
#     # app = TreeVisualizer(root)
#     # app.mainloop()
#
#     app = TreeVisualizer(root)
#     app.mainloop()