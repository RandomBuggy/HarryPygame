import pygame
pygame.init()

gameWindow = pygame.display.set_mode((750, 345))
pygame.display.set_caption("My first Game")

exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_AMPERSAND:
                print("You pressed & key")

pygame.quit()
quit()
