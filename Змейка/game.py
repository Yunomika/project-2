import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

width = 600
height = 400

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color, position):
    font = pygame.font.SysFont('Arial', 16)
    text_surface = font.render(msg, True, color)
    text_rect = text_surface.get_rect(center=position)
    dis.blit(text_surface, text_rect)

def draw_button(text, x, y, width, height, color):
    pygame.draw.rect(dis, color, [x, y, width, height])
    mesg = font_style.render(text, True, black)
    dis.blit(mesg, [x + (width / 6), y + (height / 4)])

def main_menu():
    while True:
        dis.fill(white)
        message("Добро пожаловать в Змейку!", black, (width // 2, height // 4))

        button_width = 200
        button_height = 50
        button_spacing = 20

        draw_button("Играть", width / 3, height / 3, button_width, button_height, green)
        draw_button("Правила", width / 3, height / 3 + button_height + button_spacing, button_width, button_height, red)
        draw_button("Предыстория", width / 3, height / 3 + 2 * (button_height + button_spacing), button_width, button_height, green)
        draw_button("Выход", width / 3, height / 3 + 3 * (button_height + button_spacing), button_width, button_height, red)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if width / 3 <= mouse_x <= width / 3 + button_width and height / 3 <= mouse_y <= height / 3 + button_height:
                    gameLoop()
                elif width / 3 <= mouse_x <= width / 3 + button_width and height / 3 + button_height + button_spacing <= mouse_y <= height / 3 + button_height + button_spacing + button_height:
                    show_rules()
                elif width / 3 <= mouse_x <= width / 3 + button_width and height / 3 + 2 * (button_height + button_spacing) <= mouse_y <= height / 3 + 2 * (button_height + button_spacing) + button_height:
                    show_backstory()
                elif width / 3 <= mouse_x <= width / 3 + button_width and height / 3 + 3 * (button_height + button_spacing) <= mouse_y <= height / 3 + 3 * (button_height + button_spacing) + button_height:
                    pygame.quit()
                    quit()

def show_backstory():
    backstory_image = pygame.image.load("photo/babushka.png")
    backstory_image = pygame.transform.scale(backstory_image, (width, height))

    while True:
        dis.fill(white)
        dis.blit(backstory_image, (0, 0))
        message("Нажмите пробел для следующего изображения", black, (width // 2, height - 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_second_image()

def show_second_image():
    # Загружаем второе изображение
    second_image = pygame.image.load("photo/telephone.png")
    second_image = pygame.transform.scale(second_image, (width, height)) # Масштабируем изображение под окно

    while True:
        dis.fill(white)
        dis.blit(second_image, (0, 0)) # Отображаем второе изображение
        message("Нажмите Q для выхода в меню", black, (width // 2, height - 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    main_menu()

        clock.tick(10)

def show_rules():
    rules = [
        "Правила игры:",
        "1. Управляйте змейкой стрелками.",
        "2. Собирайте яблоки для увеличения длины.",
        "3. Если столкнетесь с собой - вернетесь к старту.",
        "Нажмите Q для выхода в меню."
    ]

    while True:
        dis.fill(white)

        for i, rule in enumerate(rules):
            message(rule, black, (width // 2, height // 4 + i * 30))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return

        clock.tick(10)
        
def display_score(score):
    font = pygame.font.SysFont("comicsansms", 35)
    score_text = font.render("Счёт: " + str(score), True, black)
    dis.blit(score_text, [0, 0])

def generate_food():
    size_type = random.choice([(10, green, 1), (15, red, 2), (20, yellow, 3)])
    food_size, food_color, food_points = size_type
    foodx = round(random.randrange(0, width - food_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - food_size) / 10.0) * 10.0
    return foodx, foody, food_size, food_color, food_points

def gameLoop():  
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    score = 0 

    foodx, foody, food_size, food_color, food_points = generate_food()

    while not game_over:
        while game_close:
            dis.fill(white)
            display_score(score) 
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        pygame.draw.rect(dis, food_color, [foodx, foody, food_size, food_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        display_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody, food_size, food_color, food_points = generate_food()
            Length_of_snake += food_points
            score += food_points

        clock.tick(snake_speed)

    pygame.quit()
    quit()
main_menu()
