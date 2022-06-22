import random
import pygame

pygame.init()

screen_width = 450
screen_height = 250

#colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.clock()
font = pygame.font.SysFont(None, 35)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    size = 10
    fps = 30
    snake_list = []
    snake_length = 1

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over!\nPress Enter to Continue", red, screen_width / 2, screen_height / 2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocity_x = init_velocity
                    velocity_y = 0
                if event.key == pygame.K_LEFT:
                    velocity_x = -init_velocity
                    velocity_y = 0
                if event.key == pygame.K_UP:
                    velocity_y = -init_velocity
                    velocity_x = 0
                if event.key == pygame.K_DOWN:
                    velocity_y = init_velocity
                    velocity_x = 0

        snake_x += velocity_x
        snake_y += velocity_y

        if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
            score += 1
            food_x = random.randint(20, screen_width / 2)
            food_y = random.randint(20, screen_height / 2)
            snake_length += 5

        gameWindow.fill(white)
        text_screen("score: " + str(score * 10), red, 5, 5)
        pygame.draw.rect(gameWindow, red, [food_x, food_y, size, size])
        head = []
        head.append(snake_x)
        head.append(snake_y)
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        if head in snake_list[:-1]:
            game_over = True
        if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
            game_over = True
        #pygame.draw.rect(gameWindow, black, [snake_x, snake_y, size, size])
        plot_snake(gameWindow, black, snake_list, size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()
