import pygame  
import sys

pygame.init()


WIDTH, HEIGHT = 750,750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe game!")


BLACK = (0,0,0)
WHITE = (255, 255, 255) 
YELLOW= (255,255,0)
RED = (255,0,0)
VIOLET=(255,0,255)
GREEN=(0,255,0)
  
 
  

CELL_SIZE = WIDTH // 3
LINE_WIDTH = 5
CIRCLE_RADIUS = CELL_SIZE // 4  
CIRCLE_WIDTH = 15
CROSS_WIDTH = 15
SPACE = CELL_SIZE // 6


board = [["" for _ in range(3)] for _ in range(3)]
player = "X"
game_over = False


score = {"X": 0, "O": 0}
WINNING_SCORE = 5


font = pygame.font.Font(None, 80)
score_font = pygame.font.Font(None, 50)


def draw_grid():
    "Draw the game grid."
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (0, CELL_SIZE * i), (WIDTH, CELL_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, WHITE, (CELL_SIZE * i, 0), (CELL_SIZE * i, HEIGHT), LINE_WIDTH)


def draw_marks():
    "Draw the Xs and Os."
    for row in range(3):
        for col in range(3):
            if board[row][col] == "O":
                pygame.draw.circle(screen, GREEN, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == "X":
                start_pos = (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE)
                end_pos = (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + CELL_SIZE - SPACE)
                pygame.draw.line(screen, RED, start_pos, end_pos, CROSS_WIDTH)
                start_pos = (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE)
                end_pos = (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE)
                pygame.draw.line(screen, RED, start_pos, end_pos, CROSS_WIDTH)


def check_winner():
    "Check if there is a winner."
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    
    if board[0][0] == board[1][1] == board[2][2] != "":      
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    
    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        return "Draw"

    return None


def restart_game():
    "Reset the game board for the next round."
    global board, player, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    player = "X"
    game_over = False


def display_score():
    "Display the current score on the screen."
    score_text = f"X: {score['X']}  |  O: {score['O']}"
    score_surface = score_font.render(score_text, True, VIOLET)
    screen.blit(score_surface, (WIDTH // 2 - score_surface.get_width() // 2, HEIGHT - 50))


def display_final_winner(winner):
    "Display the final winner."
    final_message = f"{winner} won the whole game!"
    
                                                      
    text_surface = font.render(final_message, True, WHITE)
    screen.fill(BLACK)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds before exiting
    pygame.quit()
    sys.exit()



running = True
while running:
    screen.fill(BLACK)
    draw_grid()
    draw_marks()
    display_score()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            row = mouse_y // CELL_SIZE
            col = mouse_x // CELL_SIZE

            
            if board[row][col] == "":
                board[row][col] = player
                winner = check_winner()
                if winner:
                    game_over = True
                    if winner != "Draw":
                        score[winner] += 1
                        
                        if score[winner] >= WINNING_SCORE:
                            display_final_winner(winner)
                player = "O" if player == "X" else "X"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Restart the game when 'R' is pressed
                if game_over:
                    restart_game()

    
    winner = check_winner()
    if winner:
        game_over = True
        message = "Draw!" if winner == "Draw" else f"{winner} won!"
        text = font.render(message, True, YELLOW)
        screen.blit(text, (WIDTH // 2.2- text.get_width() // 2.3, HEIGHT // 2.65- text.get_height() // 3))

    pygame.display.flip()
