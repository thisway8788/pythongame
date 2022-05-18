import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Tofu to the World")

# 배경 이미지 불러오기
background = pygame.image.load('background.png')

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load('character.png')
character_size = character.get_rect().size  # 이미지 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 캐릭터 위치
character_y_pos = screen_height - character_height  # 화면 세로크기 가장 아래


# 창이 꺼지지 않게 하기위해 이벤트 루프를 하자
running = True  # Is gaming running?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가 체크
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # Game is not running

    screen.blit(background, (0, 0))  # Drawing background
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # redrawing game display

# pygame 종료
pygame.quit()


