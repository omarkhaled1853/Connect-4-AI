import pygame
import sys
import pygame_menu as pm
import numpy as np
import random
from queue import Queue
from tree_gui import *
from turn_gain import *
from tree_printing import *
from utils.factory import Factory
from Algorithms.search import Search

#Board size
ROW_COUNT = 6
COLUMN_COUNT = 7

# Screen
SQUARESIZE = 100
SHOW_TREE_BUTTON_HEIGHT = 40
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE + SHOW_TREE_BUTTON_HEIGHT
RADIUS = int(SQUARESIZE / 2 - 5)
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)

#RGB colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
LIGHTBLUE = (173, 216, 230)
ORANGE = (255, 165, 0)

#Game setting. 3 level and player start first are the default values of the game
LEVEL = 3
START_FIRST = 'player'
SEARCH_METHOD = 'Alpha_Beta'
FULL_BOARD = 42
PLAYER_PIECE = '1'
COMPUTER_PIECE = '2'




def generate_number():
    return random.randint(0, 6)

def create_board():
    board = np.full((ROW_COUNT, COLUMN_COUNT), '0')
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == '0'

def get_next_open_row(board, col):
    for row in reversed(range(ROW_COUNT)):
        if board[row][col] == '0':
            return row


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[r][c] == '0':
                pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == '1':
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    pygame.display.update()


def show_tree(root: Node):
    def write_tree_task(q):
        write_tree_to_file_bfs(root, 'tree_bfs.txt')
        q.put("done")

    q = Queue()
    thread = threading.Thread(target=write_tree_task, args=(q,))
    thread.start()

    # Wait for the thread to finish
    while True:
        result = q.get()
        if result == "done":
            break

    tree_visualize(root)  # GUI operations remain in the main thread

def draw_tree_button():
	pygame.draw.rect(screen, ORANGE, (0, HEIGHT - SHOW_TREE_BUTTON_HEIGHT, WIDTH, SHOW_TREE_BUTTON_HEIGHT))
	myfont = pygame.font.SysFont("monospace", 35)
	label = myfont.render("Show tree", 1, BLACK)
	screen.blit(label, (250, HEIGHT - SHOW_TREE_BUTTON_HEIGHT))


def start_game(search: Search):
	step_num = 0
	board = create_board()
	pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
	draw_tree_button()
	draw_board(board)
	pygame.display.update()

	turn = 0 # player turn
	if START_FIRST == 'computer':
		turn = 1

	player_score = 0
	computer_score = 0
	root = None
	game_over = False

	while not game_over:
		if turn == 1: # computer turn
			play_data = search.solve(board, player_score, computer_score)
			position = play_data['best_position']
			root = play_data['node']

			row = position[0]
			computer_col = position[1]
			drop_piece(board, row, computer_col, COMPUTER_PIECE)
			computer_score += gain_from_one_piece(board, row, computer_col, COMPUTER_PIECE)
			draw_board(board)
			turn = (turn + 1) % 2
			step_num += 1
			print(f"player: {player_score}")
			print(f"computer: {computer_score}")

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEMOTION:
				pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))

				posx = event.pos[0]
				if turn == 0:
					if PLAYER_PIECE == '1':
						pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
					else:
						pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)

				pygame.display.update()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.pos[1] > HEIGHT - SHOW_TREE_BUTTON_HEIGHT:
					show_tree(root)
					continue

				pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
				posx = event.pos[0]
				col = int(posx // SQUARESIZE)

				if turn == 0 and is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, PLAYER_PIECE)
					player_score += gain_from_one_piece(board, row, col, PLAYER_PIECE)
					draw_board(board)
					turn = (turn + 1) % 2
					step_num += 1

					print(f"player: {player_score}")
					print(f"computer: {computer_score}")

		if step_num == FULL_BOARD:
			if player_score > computer_score:
				winfont = pygame.font.SysFont("monospace", 40)
				label = winfont.render("Congratulations you wins!!!", 1, RED)
				screen.blit(label, (30, 10))
			elif computer_score > player_score:
				winfont = pygame.font.SysFont("monospace", 50)
				label = winfont.render("Agent win!!", 1, YELLOW)
				screen.blit(label, (170, 10))
			else:
				winfont = pygame.font.SysFont("monospace", 75)
				label = winfont.render("Draw!", 1, LIGHTBLUE)
				screen.blit(label, (220, 10))

			pygame.display.update()
			game_over = True


		if game_over:
			pygame.time.wait(3000)


def main_menu():
	pygame.init()

	start_first = [("Player", "player"), ("Computer", "computer")]
	player_color = [("Red", "1"), ("Yellow", "2")]
	level = [(str(i), str(i)) for i in range(1, 43)]
	search_method = [("Alpha_Beta", "Minimax_alpha_beta"), ("Minmax", "Minimax"), ("Expected minmax", "Expected_minimax")]

	# Creating the settings menu
	settings = pm.Menu(title="CONNECT4 GAME",
					   width=WIDTH,
					   height=HEIGHT,
					   theme=pm.themes.THEME_DARK)

	# Adjusting the default values
	settings._theme.widget_font_size = 25
	settings._theme.widget_font_color = ORANGE

	def setSetting():
		# Updating defaul variables based on user selection
		data = settings.get_input_data()
		global START_FIRST, PLAYER_PIECE, COMPUTER_PIECE, LEVEL, SEARCH_METHOD
		START_FIRST = data.get("start_first")[0][1]
		PLAYER_PIECE = data.get("player_color")[0][1]
		LEVEL = int(data.get("level")[0][1])
		SEARCH_METHOD = data.get("search_method")[0][1]

		if PLAYER_PIECE == '1':
			COMPUTER_PIECE = '2'
		else:
			COMPUTER_PIECE = '1'

		print(START_FIRST)
		print(PLAYER_PIECE)
		print(COMPUTER_PIECE)
		print(LEVEL)
		print(SEARCH_METHOD)
		search = Factory.get_technique(SEARCH_METHOD, COMPUTER_PIECE, PLAYER_PIECE, LEVEL)
		start_game(search)


	settings.add.text_input(title="User Name : ", textinput_id="username")

	settings.add.dropselect(title="Start first", items=start_first,
							dropselect_id="start_first", default=0
							)

	settings.add.dropselect(title="Player color", items=player_color,
							dropselect_id="player_color", default=0
							)

	settings.add.dropselect(title="Search method", items=search_method,
							dropselect_id="search_method", default=0
							)

	settings.add.dropselect(title="Minmax level", items=level,
									 dropselect_id="level", default=0)

	settings.add.button(title="Start game", action=setSetting,
						font_color=WHITE, background_color=BLACK)


	settings.mainloop(screen)

main_menu()