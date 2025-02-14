import pygame
import sys
import random
from pygame.locals import *
import settings
import music

game_settings = settings.load_settings()

# Initialize Pygame
pygame.init()




# Screen dimensions
WIDTH, HEIGHT = 1200, 1100
LINE_WIDTH = 15
MARK_SIZE = 80

# Colors
BG_COLOR = (28, 170, 100)
LINE_COLOR = (23, 145, 135)
MARK_COLOR = (84, 84, 84)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (126, 87, 194)
BUTTON_HOVER_COLOR = (0, 180, 80)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe: Three Marks")
screen.fill(BG_COLOR)

# Draw the grid
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT // 3 * i), (WIDTH, HEIGHT // 3 * i), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH // 3 * i, 0), (WIDTH // 3 * i, HEIGHT), LINE_WIDTH)

# Draw a mark (X or O)
def draw_mark(row, col, mark):
    font = pygame.font.Font(None, 120)
    text = font.render(mark, True, MARK_COLOR)
    text_rect = text.get_rect(center=(col * WIDTH // 3 + WIDTH // 6, row * HEIGHT // 3 + HEIGHT // 6))
    screen.blit(text, text_rect)


# Draw a button
def draw_button(x, y, width, height, text, hover):
    color = BUTTON_HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font(None, 40)
    text_surf = font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)

#rules
def display_rules():
    while True:
        screen.fill(BG_COLOR)
        font = pygame.font.Font(None, 40)
        rules = [
            "Rules:",
            ' ',
            "1. Players take turns placing marks (X or O).",
            ' ',
            "2. Each player can only have three marks on the board at a time.",
            ' ',
            "3. When a fourth mark is placed, the oldest mark is removed.",
            ' ',
            "4. The first player to align three marks in a row, column,\n     or diagonal wins.",
            
        ]
        for i, rule in enumerate(rules):
            text = font.render(rule, True, TEXT_COLOR)
            screen.blit(text, (150, HEIGHT // 4 + i * 40))
        
        draw_button(WIDTH // 2 - 75, HEIGHT - 100, 150, 50, "Back", False)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH // 2 - 75 <= event.pos[0] <= WIDTH // 2 + 75 and HEIGHT - 100 <= event.pos[1] <= HEIGHT - 50:
                    return

# Ask for game mode
def ask_game_mode():
    single_player_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 100, 150, 50)
    multiplayer_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, 150, 50)
    rules_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 100, 150, 50)

    while True:
        screen.fill(BG_COLOR)
        font = pygame.font.Font(None, 60)
        text = font.render("Choose Game Mode", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(text, text_rect)

        mouse_pos = pygame.mouse.get_pos()
        single_hover = single_player_button.collidepoint(mouse_pos)
        multi_hover = multiplayer_button.collidepoint(mouse_pos)
        rules_hover = rules_button.collidepoint(mouse_pos)

        draw_button(single_player_button.x, single_player_button.y, 200, 50, "Single-Player", single_hover)
        draw_button(multiplayer_button.x, multiplayer_button.y, 200, 50, "Multi-Player", multi_hover)
        draw_button(rules_button.x, rules_button.y, 150, 50, "Rules", rules_hover)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if single_player_button.collidepoint(event.pos):
                    return "single"
                if multiplayer_button.collidepoint(event.pos):
                    return "multi"
                if rules_button.collidepoint(event.pos):
                    display_rules()


# Check for a win
def check_win(mark):
    if len(moves_x) < 3 and len(moves_o) < 3:  # No need to check if fewer than 3 marks
        return False
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == mark:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False


# Display a message and wait for a rematch decision
def display_popup(message):
    popup_width, popup_height = 400, 200
    popup_x, popup_y = (WIDTH - popup_width) // 2, (HEIGHT - popup_height) // 2
    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)

    rematch_button = pygame.Rect(popup_x + 30, popup_y + 120, 150, 50)
    quit_button = pygame.Rect(popup_x + 250, popup_y + 120, 110, 50)

    while True:
        pygame.draw.rect(screen, (50, 50, 50), popup_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, rematch_button)
        pygame.draw.rect(screen, BUTTON_COLOR, quit_button)
        
        font = pygame.font.Font(None, 50)
        text = font.render(message, True, TEXT_COLOR)
        screen.blit(text, (popup_x + 145, popup_y + 50))

        font_small = pygame.font.Font(None, 40)
        rematch_text = font_small.render("Rematch", True, BUTTON_TEXT_COLOR)
        quit_text = font_small.render("Quit", True, BUTTON_TEXT_COLOR)
        screen.blit(rematch_text, (rematch_button.x + 13, rematch_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 22, quit_button.y + 10))

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rematch_button.collidepoint(event.pos):
                    return True
                if quit_button.collidepoint(event.pos):
                    return False

# Reset the game state
def reset_game():
    global board, moves_x, moves_o, current_mark
    board = [[None] * 3 for _ in range(3)]
    moves_x = []
    moves_o = []
    current_mark = 'X'
    draw_grid()
    screen.fill(BG_COLOR)
    

# Make a random computer move
def computer_move():
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] is None]
    if available_moves:
        return random.choice(available_moves)
    return None

# Board setup
board = [[None] * 3 for _ in range(3)]
moves_x = []
moves_o = []
current_mark = 'X'

# Ask for the game mode
game_mode = ask_game_mode()
screen.fill(BG_COLOR)
draw_grid()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_mode == "multi":
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // (HEIGHT // 3)
                clicked_col = mouseX // (WIDTH // 3)

                if board[clicked_row][clicked_col] is None:
                    # Update board and moves based on current mark
                    board[clicked_row][clicked_col] = current_mark
                    if current_mark == 'X':
                        moves_x.append((clicked_row, clicked_col))
                        if len(moves_x) > 3:
                            old_row, old_col = moves_x.pop(0)
                            board[old_row][old_col] = None
                    else:
                        moves_o.append((clicked_row, clicked_col))
                        if len(moves_o) > 3:
                            old_row, old_col = moves_o.pop(0)
                            board[old_row][old_col] = None

                    # Check for a win
                    if check_win(current_mark):
                        message = f"{current_mark} won!"
                        if not display_popup(message):
                            running = False
                        else:
                            reset_game()

                    # Redraw screen
                    screen.fill(BG_COLOR)
                    draw_grid()
                    for move in moves_x:
                        draw_mark(move[0], move[1], 'X')
                    for move in moves_o:
                        draw_mark(move[0], move[1], 'O')

                    # Switch turn
                    current_mark = 'O' if current_mark == 'X' else 'X'
        elif game_mode == "single":
            if current_mark == 'X':  # Player's turn
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = event.pos
                    clicked_row = mouseY // (HEIGHT // 3)
                    clicked_col = mouseX // (WIDTH // 3)

                    if board[clicked_row][clicked_col] is None:
                        board[clicked_row][clicked_col] = current_mark
                        moves_x.append((clicked_row, clicked_col))
                        if len(moves_x) > 3:
                            old_row, old_col = moves_x.pop(0)
                            board[old_row][old_col] = None

                        # Check for a win
                        if check_win(current_mark):
                            message = f"{current_mark} won!"
                            if not display_popup(message):
                                running = False
                            else:
                                reset_game()

                        # Redraw screen
                        screen.fill(BG_COLOR)
                        draw_grid()
                        for move in moves_x:
                            draw_mark(move[0], move[1], 'X')
                        for move in moves_o:
                            draw_mark(move[0], move[1], 'O')

                        current_mark = 'O'

            elif current_mark == 'O':  # Computer's turn
                pygame.time.wait(500)  # Delay for a more natural feel
                move = computer_move()
                if move:
                    row, col = move
                    board[row][col] = current_mark
                    moves_o.append((row, col))
                    if len(moves_o) > 3:
                        old_row, old_col = moves_o.pop(0)
                        board[old_row][old_col] = None

                    # Check for a win
                    if check_win(current_mark):
                        message = f"{current_mark} won!"
                        if not display_popup(message):
                            running = False
                        else:
                            reset_game()

                    # Redraw screen
                    screen.fill(BG_COLOR)
                    draw_grid()
                    for move in moves_x:
                        draw_mark(move[0], move[1], 'X')
                    for move in moves_o:
                        draw_mark(move[0], move[1], 'O')

                    current_mark = 'X'

    pygame.display.flip()

pygame.quit()
sys.exit()
