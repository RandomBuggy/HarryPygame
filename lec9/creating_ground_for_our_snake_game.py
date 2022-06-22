import pygame

pygame.init()

#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

gameWindow = pygame.display.set_mode((450, 250))
pygame.display.set_caption("Snake Game")
pygame.display.update()

exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

    gameWindow.fill(white)
    pygame.display.update()

pygame.quit()
quit()
