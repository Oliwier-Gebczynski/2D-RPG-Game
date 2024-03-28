import pygame

pygame.init()

width = 1500
height = 900
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

font = pygame.font.SysFont("Arial", 32)

number = 0

def draw_button(x, y, width, height, text):
    pygame.draw.rect(screen, black, (x, y, width, height))
    rendered_text = font.render(text, True, white)
    screen.blit(rendered_text, (x + (width - rendered_text.get_width()) // 2, y + (height - rendered_text.get_height()) // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 100 <= mouse_pos[0] <= 300 and 100 <= mouse_pos[1] <= 200:
                number += 1

    screen.fill(white)

    draw_button(100, 100, 200, 100, "Click")

    number_text = str(number)
    rendered_text = font.render(number_text, True, black)
    screen.blit(rendered_text, (400, 100))

    pygame.display.update()