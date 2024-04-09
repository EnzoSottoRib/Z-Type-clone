import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

text_font = pygame.font.SysFont("Arial", 50)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


black = (0, 0, 0)
blue = (0, 0, 255)

block_width = 50
block_height = 20

block_x = (SCREEN_WIDTH - block_width) / 2
block_y = 0

block_speed = 1

clock = pygame.time.Clock()

run = True

while run:

    screen.fill((0, 0, 0))

    draw_text("Hello World", text_font, (120, 0, 0), 20, 530)

    pygame.draw.rect(screen, (255, 0, 0), player)

    block_y += block_speed
    if block_y > SCREEN_HEIGHT:
        block_y = -block_height

    pygame.draw.rect(screen, blue, [block_x, block_y, block_width, block_height])

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



    pygame.display.update()

pygame.quit()
