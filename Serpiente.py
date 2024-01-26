import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Raquetas y pelota
player_width, player_height = 15, 100
opponent_width, opponent_height = 15, 100
ball_size = 20

player_pos = [50, height // 2 - player_height // 2]
opponent_pos = [width - 50 - opponent_width, height // 2 - opponent_height // 2]
ball_pos = [width // 2, height // 2]
ball_speed = [random.choice([-7, 7]), random.choice([-7, 7])]

# Velocidad del jugador
player_speed = 25
opponent_speed = 25

# Reloj y FPS
clock = pygame.time.Clock()
FPS = 60

# Función principal del juego
def game():
    global player_speed, ball_pos, ball_speed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_speed = -7
                elif event.key == pygame.K_DOWN:
                    player_speed = 7
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_speed = 0

        # Actualizar la posición del jugador
        player_pos[1] += player_speed

        # Limitar la posición del jugador dentro de la pantalla
        player_pos[1] = max(0, min(height - player_height, player_pos[1]))

       # Actualizar la posición del oponente (IA mejorada)
        target_y = ball_pos[1] - opponent_height / 2

        if opponent_pos[1] < target_y:
            opponent_pos[1] += min(opponent_speed, target_y - opponent_pos[1])
        elif opponent_pos[1] > target_y:
            opponent_pos[1] -= min(opponent_speed, opponent_pos[1] - target_y)

        # Actualizar la posición de la pelota
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]
        
        # Rebotar la pelota en las raquetas
        if (
            player_pos[0] <= ball_pos[0] <= player_pos[0] + player_width
            and player_pos[1] <= ball_pos[1] <= player_pos[1] + player_height
        ) or (
          opponent_pos[0] <= ball_pos[0] <= opponent_pos[0] + opponent_width
          and opponent_pos[1] <= ball_pos[1] <= opponent_pos[1] + opponent_height
        ):
            ball_speed[0] = -ball_speed[0]
            ball_speed[1] = random.choice([-7, 7])  # Cambia la dirección vertical de la pelota al golpear una raqueta

       # Verificar si la pelota ha salido de la pantalla (anotación de puntos)
        if ball_pos[0] <= 0:
            # Pelota ha salido por el lado izquierdo
            ball_pos[0] = 0  # Ajusta la posición para que la pelota no esté fuera de la pantalla
            ball_speed[0] = abs(ball_speed[0])  # Cambia la dirección horizontal hacia la derecha
        elif ball_pos[0] >= width - ball_size:
            # Pelota ha salido por el lado derecho
             ball_pos[0] = width - ball_size  # Ajusta la posición para que la pelota no esté fuera de la pantalla
             ball_speed[0] = -abs(ball_speed[0])  # Cambia la dirección horizontal hacia la izquierda

        # Verificar si la pelota ha salido por arriba o por abajo
        if ball_pos[1] <= 0 or ball_pos[1] >= height - ball_size:
            ball_speed[1] = -ball_speed[1]  # Invierte la dirección vertical

        # Limpiar la pantalla
        screen.fill(black)

        # Dibujar raquetas y pelota
        pygame.draw.rect(screen, white, (player_pos[0], player_pos[1], player_width, player_height))
        pygame.draw.rect(screen, white, (opponent_pos[0], opponent_pos[1], opponent_width, opponent_height))
        pygame.draw.ellipse(screen, white, (ball_pos[0], ball_pos[1], ball_size, ball_size))

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad del juego
        clock.tick(FPS)

        # Continuar con la próxima iteración del bucle si es necesario
        if 'continue_game' in locals() and continue_game:
            continue

# Iniciar el juego
game()