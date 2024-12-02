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




# def create_sample_tree() -> Node:
#     # Create a sample tree
#     root = Node(1)
#     child1 = Node(2)
#     child2 = Node(3)
#     child3 = Node(4)
#
#     root.add_child(child1)
#     root.add_child(child2)
#     child1.add_child(child3)
#
#     return root
#
#
# # Create the sample tree
# root = create_sample_tree()
#
# # Write the tree to a file in BFS order
# write_tree_to_file_bfs(root, 'tree_bfs.txt')




# from treeDemo import *
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
# root.add_child(child1)
# root.add_child(child2)
# root.add_child(child3)
# root.add_child(child4)
# root.add_child(child5)
# root.add_child(child6)
# root.add_child(child7)
#
#
# app = TreeVisualizer(root)
# app.mainloop()

# import pygame
# import sys
# import numpy as np
# import tkinter as tk
# from tkinter import messagebox
#
# root = tk.Tk()
# C = tk.Canvas(root, width=600, height=500)
#
# C.create_oval(80, 30, 140, 150)
#
# oval = C.create_oval(80, 30, 140,
#                      150,
#                      fill="blue")
#
# C.create_text(110, 90, text="hello world", fill="black", font=('Helvetica 5 bold'))
#
#
# C.pack()
# tk.mainloop()
#
# # # Initialize Pygame
# # pygame.init()
# #
# # # Constants
# # ROW_COUNT = 6
# # COLUMN_COUNT = 7
# # SQUARESIZE = 100
# # RADIUS = int(SQUARESIZE / 2 - 5)
# # BLUE = (0, 0, 255)
# # BLACK = (0, 0, 0)
# # RED = (255, 0, 0)
# # NEWCOLOR = (122, 132, 1)
# # YELLOW = (255, 255, 0)
# # MY_BLUE = (0, 0, 128)
# # FONT = pygame.font.SysFont("monospace", 75)
# #
# # def create_board():
# #     board = np.zeros((ROW_COUNT, COLUMN_COUNT))
# #     return board
# #
# # # Drop a piece in the board
# # def drop_piece(board, row, col, piece):
# #     board[row][col] = piece
# #
# # # Draw the game board
# # def draw_board(board):
# #     for c in range(COLUMN_COUNT):
# #         for r in range(ROW_COUNT):
# #             pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
# #             pygame.draw.circle(screen, BLACK, (c*SQUARESIZE + SQUARESIZE//2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE//2), RADIUS)
# #
# #             if board[r][c] == 1:
# #                 pygame.draw.circle(screen, RED, (c*SQUARESIZE + SQUARESIZE//2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE//2), RADIUS)
# #             elif board[r][c] == 2:
# #                 pygame.draw.circle(screen, YELLOW, (c*SQUARESIZE + SQUARESIZE//2, r*SQUARESIZE + SQUARESIZE + SQUARESIZE//2), RADIUS)
# #
# #     pygame.display.update()
# #
# # # Get the next available row in a column
# # def get_next_open_row(board, col):
# #     for r in range(ROW_COUNT-1, -1, -1):
# #         if board[r][col] == 0:
# #             return r
# #
# # # Check if a player wins
# # def winning_move(board, piece):
# #     # Check horizontal locations
# #     for c in range(COLUMN_COUNT-3):
# #         for r in range(ROW_COUNT):
# #             if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
# #                 return True
# #
# #     # Check vertical locations
# #     for c in range(COLUMN_COUNT):
# #         for r in range(ROW_COUNT-3):
# #             if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
# #                 return True
# #
# #     # Check positively sloped diagonals
# #     for c in range(COLUMN_COUNT-3):
# #         for r in range(ROW_COUNT-3):
# #             if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
# #                 return True
# #
# #     # Check negatively sloped diagonals
# #     for c in range(COLUMN_COUNT-3):
# #         for r in range(3, ROW_COUNT):
# #             if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
# #                 return True
# #
# # # Function to get user settings before starting the game
# # def get_user_settings():
# #     root = tk.Tk()
# #     root.withdraw()  # Hide the root window
# #
# #     # Create a new top-level window for the settings
# #     settings_window = tk.Toplevel(root)
# #     settings_window.title("Game Settings")
# #
# #     # Label for the start choice
# #     start_label = tk.Label(settings_window, text="Who will start first?")
# #     start_label.pack(pady=10)
# #
# #     # Dropdown menu for who starts first (Player or Computer)
# #     start_choice = tk.StringVar(value="Player")  # Default to Player
# #     start_menu = tk.OptionMenu(settings_window, start_choice, "Player", "Computer")
# #     start_menu.pack(pady=10)
# #
# #     # Label for Minimax depth 'k'
# #     k_label = tk.Label(settings_window, text="Enter Max Depth (k) for Minimax Algorithm:")
# #     k_label.pack(pady=10)
# #
# #     # Dropdown menu for selecting the Max Depth 'k' (between 1 and 42)
# #     k_value = tk.IntVar(value=1)  # Default to 1
# #     k_menu = tk.OptionMenu(settings_window, k_value, *range(1, 43))  # Range from 1 to 42
# #     k_menu.pack(pady=10)
# #
# #     # Button to proceed to the next step
# #     def proceed_to_next_page():
# #         settings_window.quit()
# #         settings_window.destroy()
# #
# #     next_button = tk.Button(settings_window, text="Start Game", command=proceed_to_next_page)
# #     next_button.pack(pady=20)
# #
# #     settings_window.mainloop()
# #
# #     # Get the value from the dropdown menu
# #     start_choice_value = start_choice.get()
# #     k_depth_value = k_value.get()
# #
# #     return start_choice_value, k_depth_value
# #
# # # Initialize the window and game variables
# # screen = pygame.display.set_mode((COLUMN_COUNT*SQUARESIZE, (ROW_COUNT+1)*SQUARESIZE))
# # pygame.display.set_caption("Connect 4")
# # board = create_board()
# # turn = 0  # 0 for player 1 (RED), 1 for player 2 (YELLOW)
# #
# # # Get user settings before starting the game
# # start_choice, k_depth = get_user_settings()
# #
# # print(start_choice)
# # print(k_depth)
# #
# # if start_choice.lower() == 'player':
# #     turn = 0  # Player 1 starts
# # else:
# #     turn = 1  # Computer starts
# #
# # draw_board(board)
# # pygame.display.update()
# #
# # game_over = False
# # while not game_over:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             game_over = True
# #
# #         if event.type == pygame.MOUSEMOTION:
# #             pygame.draw.rect(screen, MY_BLUE, (0, 0, COLUMN_COUNT*SQUARESIZE, SQUARESIZE))
# #             posx = event.pos[0]
# #             pygame.draw.circle(screen, NEWCOLOR, (posx, int(SQUARESIZE/2)), RADIUS)
# #
# #         pygame.display.update()
# #
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             posx = event.pos[0]
# #             col = int(posx // SQUARESIZE)
# #
# #
# #             if board[0][col] == 0:
# #                 row = get_next_open_row(board, col)
# #                 if turn % 2 == 0:
# #                     drop_piece(board, row, col, 1)
# #                     if winning_move(board, 1):
# #                         label = FONT.render("Player 1 wins!!", 1, RED)
# #                         screen.blit(label, (40, 10))
# #                         game_over = True
# #                 else:
# #                     drop_piece(board, row, col, 2)
# #                     if winning_move(board, 2):
# #                         label = FONT.render("Player 2 wins!!", 1, YELLOW)
# #                         screen.blit(label, (40, 10))
# #                         game_over = True
# #
# #                 turn += 1
# #                 draw_board(board)
# #
# #                 if game_over:
# #                     pygame.time.wait(3000)
# #                     game_over = False
# #                     board = create_board()
# #                     draw_board(board)
# #
# # pygame.quit()
# # sys.exit()
# #
# #
# # def drop_disc_with_animation(board, col, player):
# #     # Starting position (top of the screen)
# #     start_y = 0
# #     end_y = 0
# #     for r in range(ROWS-1, -1, -1):
# #         if board[r][col] == 0:
# #             end_y = r * SQUARESIZE + SQUARESIZE  # Calculate the drop position
# #             board[r][col] = player
# #             break
# #
# #     # Animate the disc falling
# #     y_pos = start_y
# #     while y_pos < end_y:
# #         screen.fill(BLUE)
# #         draw_board()
# #         pygame.draw.circle(screen, RED if player == 1 else YELLOW, (col * SQUARESIZE + SQUARESIZE // 2, y_pos), RADIUS)
# #         pygame.display.update()
# #         pygame.time.wait(20)  # Pause for a short time to create the effect
# #         y_pos += 5  # Move the disc down
# #
# #     draw_board()  # Redraw the board after the disc has settled
# #
