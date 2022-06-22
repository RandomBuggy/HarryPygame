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
snake_x = 45
snake_y = 55
velocity_x = 10
velocity_y = 10
size = 10
fps = 30
clock = pygame.time.clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake_x += 10
            if event.key == pygame.K_LEFT:
                snake_x -= 10
            if event.key == pygame.K_UP:
                snake_y -= 10
            if event.key == pygame.K_DOWN:
                snake_y += 10

    snake_x += velocity_x
    snake_y += velocity_y

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, size, size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
