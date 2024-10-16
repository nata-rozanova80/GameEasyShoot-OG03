# со счетчиком гиф и запросом о продолжении

import pygame
import random
from PIL import Image

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("C:\\Users\\Иван\\Documents\\GitHub\\GameEasyShoot\\image\\icon.jpeg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("image\\target.png")
target_width = 50
target_height = 50


def load_gif(filename):
    """Загружает GIF и возвращает список кадров."""
    image = Image.open(filename)
    frames = []

    try:
        while True:
            # Преобразуем кадр в Pygame Surface
            frame = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
            frames.append(frame)
            image.seek(image.tell() + 1)  # Переход к следующему кадру
    except EOFError:
        pass

    return frames


def show_continue_prompt():
    prompt_font = pygame.font.Font(None, 50)
    screen.fill((0, 0, 0))  # Черный фон для окна
    text = prompt_font.render("Продолжить игру? (Нажмите Y или N)", True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:  # Y для продолжения
                    return True
                elif event.key == pygame.K_n:  # N для выхода
                    return False


# Загрузка GIF с конфетти
confetti_gif_frames = load_gif("image\\konfetti-49.gif")
# Загрузка PNG с кубком
cup_img = pygame.image.load("image\\cup100.png")

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

hit_count = 0
font = pygame.font.Font(None, 74)
running = True
game_won = False
display_win_message = False

# Объявляем переменные для анимации
current_confetti_frame = 0
confetti_frame_delay = 100  # Задержка в миллисекундах между кадрами
last_confetti_update = pygame.time.get_ticks()  # Время последнего обновления кадра

# Объявляем переменные для анимации
current_confetti_frame = 0
confetti_frame_delay = 100  # Задержка в миллисекундах между кадрами
last_confetti_update = pygame.time.get_ticks()  # Время последнего обновления кадра
confetti_display_count = 0  # Счетчик отображений GIF

while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_won:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hit_count += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

            if hit_count >= 5:
                game_won = True
                display_win_message = True

    if game_won:
        # Устанавливаем цвет фона (белый)
        background_color = (255, 255, 255)  # RGB код для белого
        screen.fill(background_color)
        if display_win_message:
            text = font.render("Ты победил!", True, (255, 0, 0))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(1000)  # Задержка для отображения сообщения победы
            display_win_message = False  # Скрываем сообщение победы

        # Обновляем кадры конфетти
        if pygame.time.get_ticks() - last_confetti_update > confetti_frame_delay:
            current_confetti_frame = (current_confetti_frame + 1) % len(confetti_gif_frames)  # Переход к следующему кадру
            last_confetti_update = pygame.time.get_ticks()  # Обновляем время последнего обновления кадра
            confetti_display_count += 1  # Увеличиваем счетчик отображений

        # Отображаем текущий кадр конфетти
        screen.blit(confetti_gif_frames[current_confetti_frame], (130, 0))
        screen.blit(cup_img, (340, 300))  # Отображаем кубок

        # Если конфетти было показано 3 раза, показываем запрос на продолжение
        if confetti_display_count >= 125:
            pygame.time.delay(1000)  # Задержка перед запросом
            game_won = False  # Сбрасываем состояние игры
            confetti_display_count = 0  # Сбрасываем счетчик
            if not show_continue_prompt():
                running = False  # Выход из игры, если игрок нажимает N

    else:
        screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

pygame.quit()

while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_won:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hit_count += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

            if hit_count >= 5:
                game_won = True
                display_win_message = True

    if game_won:
        # Устанавливаем цвет фона (белый)
        background_color = (255, 255, 255)  # RGB код для белого
        screen.fill(background_color)
        if display_win_message:
            text = font.render("Ты победил!", True, (255, 0, 0))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(1000)  # Задержка для отображения сообщения победы
            display_win_message = False  # Скрываем сообщение победы
        count = 0
        # Обновляем кадры конфетти
        if pygame.time.get_ticks() - last_confetti_update > confetti_frame_delay:
            current_confetti_frame = (current_confetti_frame + 1) % len(confetti_gif_frames)  # Переход к следующему кадру
            last_confetti_update = pygame.time.get_ticks()  # Обновляем время последнего обновления кадра
            count += 1
            if count > 2:
                print (count)
                show_continue_prompt()
        screen.blit(confetti_gif_frames[current_confetti_frame], (130, 0))  # Отображаем текущий кадр конфетти
       # screen.blit(cup_img, (SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 - 60))  # Отображаем кубок в центре
        screen.blit(cup_img, (340, 300))  # Отображаем кубок

    else:
        screen.blit(target_img, (target_x, target_y))

    pygame.display.update()



#pygame.quit()
