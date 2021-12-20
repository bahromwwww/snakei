import random
import pygame

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102, 128)
red = (213, 50, 80)
green = (0, 100, 0)
pink = (222, 155, 155)
grey = (100, 100, 100)
dis_width = 900
dis_height = 900

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

probel = ("  ")
r = 30
snake_speed = 8

font_style = pygame.font.SysFont("TimesNewRoman", 25)
score_font = pygame.font.SysFont("TimesNewRoman", 25)


def Score(score):
    value = score_font.render(probel + "Score: " + str(score), True, yellow)
    value.set_alpha(200)
    dis.blit(value, [0, 0])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [50, 450])


def our_snake(r, snakelist):
    head = snakelist[-1]
    pygame.draw.circle(dis, red, [head[0], head[1]], r)
    pygame.draw.circle(dis, (0, 0, 0), [head[0], head[1]], r, 2)
    h = 30

    l = round(random.randrange(0, 255))
    m = round(random.randrange(0, 255))
    k = round(random.randrange(0, 255))

    for x in snakelist[0:-1]:
        k1 = k
        l1 = l
        m1 = m
        pygame.draw.circle(dis, (l1, m1, k1), [x[0], x[1]], r, r - 10)
        pygame.draw.circle(dis, grey, [x[0], x[1]], r, 2)
        l = round(random.randrange(0, 255))
        m = round(random.randrange(0, 255))
        k = round(random.randrange(0, 255))


def game():
    game_over = False
    game_close = False

    x_snake = 450
    y_snake = 450

    deltax_snake = 0
    deltay_snake = 0

    snakelist = []
    Length_of_snake = 1

    foodx = random.randrange(r, dis_width - r + 1, 60)
    foody = random.randrange(r, dis_height - r + 1, 60)
    while not game_over:
        while game_close == True:
            dis.fill(pink)
            message("Произошло досадное недоразумение. Начать заново - С. Покинуть игру - Q.", red)
            Score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    deltax_snake = -2 * r
                    deltay_snake = 0
                elif event.key == pygame.K_a:
                    deltax_snake = -2 * r
                    deltay_snake = 0
                elif event.key == pygame.K_RIGHT:
                    deltax_snake = 2 * r
                    deltay_snake = 0
                elif event.key == pygame.K_d:
                    deltax_snake = 2 * r
                    deltay_snake = 0
                elif event.key == pygame.K_UP:
                    deltay_snake = -2 * r
                    deltax_snake = 0
                elif event.key == pygame.K_w:
                    deltay_snake = -2 * r
                    deltax_snake = 0
                elif event.key == pygame.K_DOWN:
                    deltay_snake = 2 * r
                    deltax_snake = 0
                elif event.key == pygame.K_s:
                    deltay_snake = 2 * r
                    deltax_snake = 0

        if x_snake >= dis_width or x_snake <= 0 or y_snake >= dis_height or y_snake < 0:
            game_close = True
        x_snake += deltax_snake
        y_snake += deltay_snake
        dis.fill(pink)
        for i in range(0, 900, 60):
            for j in range(0, 900, 60):
                pygame.draw.line(dis, grey, (i, 0), (i, dis_width), 2)
                pygame.draw.line(dis, grey, (0, j), (dis_height, j), 2)
        pygame.draw.circle(dis, green, [foodx, foody], 0.6 * r)
        Score(Length_of_snake - 1)
        snake_Head = [x_snake, y_snake]

        if [x_snake, y_snake] in snakelist[0:-1]:
            game_close = True

        snakelist.append(snake_Head)
        if len(snakelist) > Length_of_snake:
            del snakelist[0]

        our_snake(r, snakelist)
        pygame.display.update()
        if x_snake == foodx and y_snake == foody:
            foodx = random.randrange(r, dis_width - r + 1, 2 * r)
            foody = random.randrange(r, dis_height - r + 1, 2 * r)

            while [foodx, foody] in snakelist:
                foodx = random.randrange(r, dis_width - r + 1, 2 * r)
                foody = random.randrange(r, dis_height - r + 1, 2 * r)
            Length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


game()