import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Text Input Example")

player = pygame.Rect((300, 250, 50, 50))

text_font = pygame.font.SysFont("Arial", 20)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

block_width = 50
block_height = 20

block_x = (SCREEN_WIDTH - block_width) / 2
block_y = 0

block_speed = 1

font = pygame.font.SysFont(None, 50)

text = "Hello World"

clock = pygame.time.Clock()

input_text = ""

run = True

while run:

    screen.fill((0, 0, 0))

    #draw_text("Hello World", text_font, white, 20, 530)

    pygame.draw.rect(screen, (255, 0, 0), player)

    block_y += block_speed
    if block_y > SCREEN_HEIGHT:
        block_y = -block_height

    pygame.draw.rect(screen, blue, [block_x, block_y, block_width, block_height])

    #text_surface = font.render(text, True, white)
    text_x = block_x + (block_width - text_font.size(text)[0]) / 2
    text_y = block_y + (block_height - text_font.size(text)[1]) / 2
    draw_text(text, text_font, white, text_x, text_y)

    clock.tick(60)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    text_surface = font.render(input_text, True, white)
    screen.blit(text_surface, (20, SCREEN_HEIGHT - text_surface.get_height() - 20))

    pygame.display.update()

pygame.quit()
