import pygame
from table import Table
pygame.init()
screen = pygame.display.set_mode((1155, 650))
pygame.display.set_caption("Таблица")
table = Table()
table.set_column_num(3)
table.set_row_num(100, 30)
table.resize(316, 500)
for i in range(100):
    for j in range(3):
        table.set_text(i, j, f"{i} {j} ssssssssssssss")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                table.move_data(False)
            elif event.button == 5:
                table.move_data(True)
            elif event.button == 1:
                table.scroll(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                table.scroll(event)
        elif event.type == pygame.MOUSEMOTION:
            table.scroll(event)
    screen.fill((255, 255, 255))
    table.draw(screen)
    pygame.display.flip()
pygame.quit()
