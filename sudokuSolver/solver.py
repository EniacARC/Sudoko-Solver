
# import pygame library
import pygame

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((500, 600))

# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
# constant
GRID = 9

x = 0
y = 0
dif = 500 / 9
val = 0

board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

boardP = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

font1 = pygame.font.SysFont("Ariel", 40)
font2 = pygame.font.SysFont("Ariel", 35)


# functions
# check if number is in a row
def check_row(board1, num, row):
    for i in range(GRID):
        if board1[row][i] == num:
            return True
    return False


# check if number is in a column
def check_column(board1, num, col):
    for i in range(GRID):
        if board1[i][col] == num:
            return True
    return False


def check_box(board1, num, row, col):
    # get top left of box
    top_row = row - (row % 3)
    top_col = col - (col % 3)

    for i in range(top_row, top_row + 3):
        for j in range(top_col, top_col + 3):
            if board1[i][j] == num:
                return True
    return False


def valid_spot(board1, num, row, col):
    return not check_row(board1, num, row) and not check_column(board1, num, col) and not check_box(board1, num, row,
                                                                                                    col)


def solve(board1):
    for row in range(GRID):
        for col in range(GRID):
            if board1[row][col] == 0:
                for t in range(1, 10):
                    if valid_spot(board1, t, row, col):
                        board1[row][col] = t
                        if solve(board1):
                            return True
                        else:
                            board1[row][col] = 0
                return False
    return True


def print_board(board1):
    for i in range(GRID):
        print("")
        for j in range(GRID):
            print(board1[i][j], end="|")


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


# Highlight the cell selected
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

    # Function to draw required lines for making Sudoku board        


def draw(board_person):
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                # Fill blue color in already numbered board
                # pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

                # Fill board with default numbers specified
                if board_person[i][j] != 0:
                    text1 = font2.render(str(board[i][j]), 1, (0, 0, 0))
                    screen.blit(text1, (i * dif + 22, j * dif + 20))
                else:
                    text1 = font2.render(str(board[i][j]), 1, (250, 0, 0))
                    screen.blit(text1, (i * dif + 20, j * dif + 15))
    # Draw lines horizontally and vertical form board
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

    # Fill value entered in cell     


# def draw_val(val):
#     text1 = font1.render(str(val), 1, (0, 0, 0))
#     screen.blit(text1, (x * dif + 15, y * dif + 15))


# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))


# Display instruction for the game
def instruction():
    text1 = font2.render("R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER TO SOLVE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 560))


# Display options when solved
def result():
    draw(boardP)
    text1 = font1.render("FINISHED PRESS R", 1, (0, 0, 0))
    screen.blit(text1, (20, 540))


run = True
flag1 = 0
flag2 = 0
rs = 0
bot = 0
error = 0
# The loop thats keep the window running
while run:

    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False
            # Get the mouse position to insert number   
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9
            if event.key == pygame.K_RETURN:
                flag2 = 1
                # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                board = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            # If D is pressed reset the board to default
    if flag2 == 1:
        if not solve(board):
            error = 1
        else:
            rs = 1
        flag2 = 0
    if val != 0:
        # draw_val(val)
        # print(x)
        # print(y)
        if valid_spot(board, val, int(x), int(y)):
            board[int(x)][int(y)] = val
            boardP[int(x)][int(y)] = val
            flag1 = 0
        else:
            board[int(x)][int(y)] = 0
            boardP[int(x)][int(y)] = val
            raise_error2()
        val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    else:
        instruction()
    draw(boardP)
    if flag1 == 1:
        draw_box()
    # instruction()

    # Update window
    pygame.display.update()

# Quit pygame window   
pygame.quit()