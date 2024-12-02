import pygame
import sys
import pygame_menu as pm
import numpy as np
import random
from tree_gui import *
from turn_gain import *
from tree_printing import *

root = Node(0)
child1 = Node(1)
child2 = Node(2)
child3 = Node(3)
child4 = Node(4)
child5 = Node(5)
child6 = Node(6)
child7 = Node(7)
child8 = Node(8)
child9 = Node(9)

child10 = Node(10)
child11 = Node(11)
child12 = Node(12)
child13 = Node(13)
child14 = Node(14)
child15 = Node(15)
child16 = Node(16)
child17 = Node(17)
child18 = Node(18)
child19 = Node(19)
child20 = Node(20)
child21 = Node(20)
child22 = Node(20)
child23 = Node(20)
child24 = Node(20)
child25 = Node(20)
child26 = Node(20)
child27 = Node(20)
child28 = Node(20)
child29 = Node(20)
child30 = Node(20)
child31 = Node(20)
child32 = Node(20)
child33 = Node(20)
child34 = Node(20)
child35 = Node(20)

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
root.add_child(child4)
root.add_child(child5)
root.add_child(child6)
root.add_child(child7)


child1.add_child(child8)
child1.add_child(child9)

child2.add_child(child10)
child2.add_child(child11)


child3.add_child(child12)
child3.add_child(child13)

child4.add_child(child14)
child4.add_child(child15)


child5.add_child(child16)
child5.add_child(child17)
child5.add_child(child18)
child5.add_child(child19)

child6.add_child(child20)
child6.add_child(child21)
child6.add_child(child22)
child6.add_child(child23)
child6.add_child(child24)
child6.add_child(child25)
child6.add_child(child26)

child7.add_child(child27)
child7.add_child(child28)
child7.add_child(child29)
child7.add_child(child30)
child7.add_child(child31)

child8.add_child(child32)
child8.add_child(child33)
child8.add_child(child34)
child8.add_child(child35)

child1.add_child(child10)
child1.add_child(child11)

child2.add_child(child12)
child2.add_child(child13)

child3.add_child(child14)
child4.add_child(child15)
child4.add_child(child17)

child5.add_child(child16)

child15.add_child(child18)
child15.add_child(child19)

child18.add_child(child20)


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
	write_tree_to_file_bfs(root, 'tree_bfs.txt')
	thread = threading.Thread(target=tree_visualize, kwargs={'root': root})
	thread.start()
	thread.join()


def draw_tree_button():
	pygame.draw.rect(screen, ORANGE, (0, HEIGHT - SHOW_TREE_BUTTON_HEIGHT, WIDTH, SHOW_TREE_BUTTON_HEIGHT))
	myfont = pygame.font.SysFont("monospace", 35)
	label = myfont.render("Show tree", 1, BLACK)
	screen.blit(label, (250, HEIGHT - SHOW_TREE_BUTTON_HEIGHT))


def start_game():
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
	game_over = False

	while not game_over:
		if turn == 1: # computer turn
			computer_col = generate_number()
			if not is_valid_location(board, computer_col):
				continue
			row = get_next_open_row(board, computer_col)
			drop_piece(board, row, computer_col, COMPUTER_PIECE)
			computer_score += gain_from_one_piece(board, row, computer_col, COMPUTER_PIECE)
			draw_board(board)
			turn = (turn + 1) % 2
			step_num += 1
			print(f"player: {PLAYER_PIECE}")
			print(f"computer: {COMPUTER_PIECE}")

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
	search_method = [("Alpha_Beta", "Alpha_Beta"), ("Minmax", "Minmax"), ("Expected minmax", "Expeced minmax")]

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
		start_game()


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