import pygame

pygame.init()

gameWindow = pygame.display.set_mode((544, 344))
pygame.display.set_caption("My First Game")

exit_game = False
game_over = False

#game loop

while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()
