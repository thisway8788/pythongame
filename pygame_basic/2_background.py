import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480   # 가로 크기
screen_height = 640  # 세로 크기

screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Tofu to the World")

# 배경 이미지 불러오기
background = pygame.image.load('background.png')
# 창이 꺼지지 않게 하기위해 이벤트 루프를 하자
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():   # 어떤 이벤트가 발생하였는가 체크
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 게임이 진행중이 아님

    # screen.fill((0,0,255)
    screen.blit(background, (0, 0))  # 배경 그리기
    pygame.display.update()  # 게임화면 다시그리기!



# pygame 종료
pygame.quit()
