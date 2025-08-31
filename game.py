import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball and Paddle Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Ball setup
x, y = 300, 200
speed_x, speed_y = 3, 2
radius = 20

# Paddle setup
paddle_width, paddle_height = 100, 15
paddle_x, paddle_y = WIDTH // 2 - paddle_width // 2, HEIGHT - 30
paddle_speed = 6

# Score setup
score = 0
font = pygame.font.SysFont("Arial", 24)

# 🔹 Load sounds
bounce_sound = pygame.mixer.Sound("bounce.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")

# Game loop
def game_loop():
    global x, y, speed_x, speed_y, paddle_x, score  # allows reset

    # Reset ball and paddle positions and score
    x, y = 300, 200
    speed_x, speed_y = 3, 2
    paddle_x = WIDTH // 2 - paddle_width // 2
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
            paddle_x += paddle_speed

        # Move the ball
        x += speed_x
        y += speed_y

        # Bounce on walls
        if x - radius < 0 or x + radius > WIDTH:
            speed_x = -speed_x
            bounce_sound.play()
        if y - radius < 0:
            speed_y = -speed_y
            bounce_sound.play()

        # Bounce on paddle
        if (paddle_x < x < paddle_x + paddle_width) and (paddle_y < y + radius < paddle_y + paddle_height):
            speed_y = -speed_y
            score += 1
            bounce_sound.play()

        # Game over
        if y > HEIGHT:
            gameover_sound.play()
            show_game_over()  # call the restart screen

        # Draw everything
        BACKGROUND_COLOR = (193, 105, 180)
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.circle(screen, RED, (x, y), radius)
        pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

        # Draw score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.delay(20)
def show_game_over():
    BACKGROUND_COLOR = (200, 230, 255)  # light blue
    screen.fill(BACKGROUND_COLOR)
    game_over_text = font.render("Game Over! Press R to Restart or Q to Quit", True, RED)
    screen.blit(game_over_text, (50, HEIGHT // 2 - 20))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart
                    waiting = False
                    game_loop()
                if event.key == pygame.K_q:  # Quit
                    pygame.quit()
                    sys.exit()
game_loop()
if (paddle_x < x < paddle_x + paddle_width) and (paddle_y < y + radius < paddle_y + paddle_height):
    speed_y = -speed_y
    score += 1
    bounce_sound.play()

    # 🔹 Increase difficulty
    if score % 5 == 0:  # every 5 points
        if speed_x > 0:
            speed_x += 1
        else:
            speed_x -= 1
        if speed_y > 0:
            speed_y += 1
        else:
            speed_y -= 1

