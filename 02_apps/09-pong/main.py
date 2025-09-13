# main.py
import pygame
import sys
import random

# -------------------------
# CONFIGURACIÓN INICIAL
# -------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG Clásico")
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paleta
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 5

# Pelota
BALL_RADIUS = 10
BALL_SPEED_X = 4
BALL_SPEED_Y = 4
BALL_SPEED_INCREMENT = 0.5  # para dificultad progresiva

# Puntaje
WINNING_SCORE = 5
FONT = pygame.font.SysFont("comicsans", 40)

# Estados del juego
STATE_MENU = "menu"
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_GAMEOVER = "gameover"


# -------------------------
# CLASES
# -------------------------
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        # Mantener dentro de la pantalla
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, window):
        pygame.draw.rect(window, WHITE, self.rect)


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BALL_RADIUS*2, BALL_RADIUS*2)
        self.reset()

    def reset(self):
        self.rect.center = (WIDTH//2, HEIGHT//2)
        # Dirección aleatoria inicial
        self.speed_x = BALL_SPEED_X * random.choice((-1, 1))
        self.speed_y = BALL_SPEED_Y * random.choice((-1, 1))

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Rebote superior e inferior
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def draw(self, window):
        pygame.draw.ellipse(window, WHITE, self.rect)


# -------------------------
# FUNCIONES
# -------------------------
def draw_window(window, paddles, ball, score1, score2, state):
    window.fill(BLACK)

    if state == STATE_MENU:
        text = FONT.render("PONG - Presiona ESPACIO para iniciar", True, WHITE)
        window.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    elif state == STATE_PAUSED:
        text = FONT.render("PAUSA - Presiona P para continuar", True, WHITE)
        window.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    elif state == STATE_GAMEOVER:
        winner = "Jugador 1" if score1 > score2 else "Jugador 2"
        text = FONT.render(f"¡{winner} ganó! Presiona ESPACIO para reiniciar", True, WHITE)
        window.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
    else:
        # Dibujar marcadores
        score_text = FONT.render(f"{score1} - {score2}", True, WHITE)
        window.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))
        # Dibujar paletas y pelota
        for paddle in paddles:
            paddle.draw(window)
        ball.draw(window)

    pygame.display.update()


def handle_collision(ball, left_paddle, right_paddle):
    # Rebote con paletas
    if ball.rect.colliderect(left_paddle.rect):
        ball.speed_x = abs(ball.speed_x) + BALL_SPEED_INCREMENT
        # Ajustar velocidad vertical aleatoriamente
        ball.speed_y += random.choice([-0.5, 0.5])
    if ball.rect.colliderect(right_paddle.rect):
        ball.speed_x = -abs(ball.speed_x) - BALL_SPEED_INCREMENT
        ball.speed_y += random.choice([-0.5, 0.5])


# -------------------------
# BUCLE PRINCIPAL
# -------------------------
def main():
    clock = pygame.time.Clock()
    run = True

    # Crear objetos
    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2)
    right_paddle = Paddle(WIDTH - 30, HEIGHT//2 - PADDLE_HEIGHT//2)
    ball = Ball(WIDTH//2, HEIGHT//2)
    paddles = [left_paddle, right_paddle]

    score1 = 0
    score2 = 0
    state = STATE_MENU

    while run:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        # -------------------------
        # EVENTOS
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if state == STATE_MENU and event.key == pygame.K_SPACE:
                    state = STATE_PLAYING
                    score1 = 0
                    score2 = 0
                    ball.reset()
                elif state == STATE_GAMEOVER and event.key == pygame.K_SPACE:
                    state = STATE_MENU
                elif state == STATE_PLAYING and event.key == pygame.K_p:
                    state = STATE_PAUSED
                elif state == STATE_PAUSED and event.key == pygame.K_p:
                    state = STATE_PLAYING

        # -------------------------
        # LÓGICA DEL JUEGO
        # -------------------------
        if state == STATE_PLAYING:
            # Movimiento paletas jugador 1 (W/S) y jugador 2 (ARR/ABA)
            if keys[pygame.K_w]:
                left_paddle.move(up=True)
            if keys[pygame.K_s]:
                left_paddle.move(up=False)
            if keys[pygame.K_UP]:
                right_paddle.move(up=True)
            if keys[pygame.K_DOWN]:
                right_paddle.move(up=False)

            # Mover pelota
            ball.move()
            handle_collision(ball, left_paddle, right_paddle)

            # Actualizar puntaje
            if ball.rect.left <= 0:
                score2 += 1
                ball.reset()
            if ball.rect.right >= WIDTH:
                score1 += 1
                ball.reset()

            # Verificar fin de juego
            if score1 >= WINNING_SCORE or score2 >= WINNING_SCORE:
                state = STATE_GAMEOVER

        # -------------------------
        # DIBUJO
        # -------------------------
        draw_window(WINDOW, paddles, ball, score1, score2, state)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
