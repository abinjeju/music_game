import pygame
import random
from pygame.rect import *
import pygame.font
import sys

#pygame 초기화
pygame.init()
pygame.display.set_caption("rhythm game")

#노래 불러오기
pygame.mixer.music.load("NewJeans_-_Hype_Boy.mp3")
pygame.mixer.music.play()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

lives = 3

direction = []

floor_rect = pygame.Rect(0, screen_height - 50, screen_width, 50)
pygame.draw.rect(screen, (255, 255, 255), floor_rect)

for direction in direction:
    if direction['rect'].colliderect(floor_rect):
        done = True
        lives -= 1

    mtext = mtext.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(mtext, (10, 10))



    if lives == 0:
        game_over = True

#키 이벤트 처리하기
def resultProcess(direction):
    global isColl, score, DrawResult, result_ticks



# 충돌했을 때 방향과 충돌값이 모두 맞을 경우,
    if isColl and CollDirection.direction == direction:
        score += 10 
        CollDirection.y = -1 
        DrawResult = 1 
    else:
        DrawResult = 2 
    result_ticks = pygame.time.get_ticks() 
def eventProcess(): 
    global isActive, score
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                isActive = False

                
            
            if event.key == pygame.K_UP: 
                resultProcess(0)
            if event.key == pygame.K_LEFT:  # 1
                resultProcess(1)
            if event.key == pygame.K_DOWN:  # 2
                resultProcess(2)
            if event.key == pygame.K_RIGHT:  # 3
                resultProcess(3)

            if event.key == pygame.K_SPACE: 
                score = 0 #스코어 0
                for direc in Directions:
                    direc.y = -1

class Direction(object):
    def __init__(self):
        self.pos = None 
        self.direction = 0
        self.image = pygame.image.load(f"direction.png")            
        self.image = pygame.transform.scale(self.image, (100, 100))   
        self.rotated_image = pygame.transform.rotate(self.image, 0) 
        self.y = -1  
         

    def rotate(self, direction=0):
        self.direction = direction
        self.rotated_image = pygame.transform.rotate(
            self.image, 90*self.direction)  # 0도, 90도, 180도, 270도 회전
        if (self.direction == 1):
            self.x = 50 
        if (self.direction == 0):
            self.x = 153  
        if (self.direction == 2):
            self.x = 256  
        if (self.direction == 3):
            self.x = 360 
    def draw(self):
        if self.y >= SCREEN_HEIGHT:
            self.y = -1   
            return True
        elif self.y == -1:
            return False
        else:
            self.y += 1   
            self.pos = screen.blit(self.rotated_image, (self.x, self.y))
            return False
        
#방향 아이콘 생성과 그리기
def drawIcon(): 
    global start_ticks,chance

    elapsed_time = (pygame.time.get_ticks() - start_ticks) 
    if elapsed_time > 800: 
        start_ticks = pygame.time.get_ticks()
        for direc in Directions: 
            if direc.y == -1: 
                direc.y = 0
                direc.rotate(direction=random.randint(0, 3))
                break

    for direc in Directions:  
        if direc.draw():        
            continue   

def draw_targetArea():
    global isColl, CollDirection
    isColl = False
    for direc in Directions:
        if direc.y == -1:
            continue 
        if direc.pos.colliderect(targetArea1): 
            isColl = True
            CollDirection = direc 
            pygame.draw.rect(screen, (80, 186, 169), targetArea1) 
            break
        if direc.pos.colliderect(targetArea2):
            isColl = True
            CollDirection = direc 
            pygame.draw.rect(screen, (80, 186, 169), targetArea2) 
            break
        if direc.pos.colliderect(targetArea3): 
            isColl = True
            CollDirection = direc 
            pygame.draw.rect(screen, (80, 186, 169), targetArea3) 
            break
        if direc.pos.colliderect(targetArea4): 
            isColl = True
            CollDirection = direc 
            pygame.draw.rect(screen, (80, 186, 169), targetArea4) 
            break
    pygame.draw.rect(screen, (35, 35, 91), targetArea1, 5)
    pygame.draw.rect(screen, (35, 35, 91), targetArea2, 5)
    pygame.draw.rect(screen, (35, 35, 91), targetArea3, 5)
    pygame.draw.rect(screen, (35, 35, 91), targetArea4, 5)

#문자 넣기
def setText():
    global score, chance
    mFont = pygame.font.SysFont("굴림", 40)

    mtext = mFont.render(f'score : {score}', True, 'black')  
    screen.blit(mtext, (10, 10, 0, 0))

#결과 이모티콘 그리기
def drawResult():
    global DrawResult, result_ticks  
    if result_ticks > 0:   
        elapsed_time = (pygame.time.get_ticks() - result_ticks)  
        if elapsed_time > 800:
            result_ticks = 0
            DrawResult = 0
    screen.blit(resultImg[DrawResult], resultImgRec)

isActive = True
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
score = 0
isColl = False
CollDirection = 0
DrawResult, result_ticks = 0,0 
start_ticks = pygame.time.get_ticks()
start_time = pygame.time.get_ticks()

clock = pygame.time.Clock()
total_time = 180
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
#배경
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#방향 아이콘
Directions = [Direction() for i in range(0, 10)]  
#타겟 박스
targetArea1 = Rect(60, 400, 85, 80)  
targetArea2 = Rect(160, 400, 85, 80)
targetArea3 = Rect(262, 400, 85, 80)
targetArea4 = Rect(362, 400, 85, 80)
#결과 이모티콘
resultFileNames = ["normal.png", "good.png", "bad.png"]
resultImg = []
for i, name in enumerate(resultFileNames):
    resultImg.append(pygame.image.load(name))
    resultImg[i] = pygame.transform.scale(resultImg[i], (100, 120))

#표시되는 이미지의 위치
resultImgRec = resultImg[0].get_rect()
resultImgRec.centerx = 250
resultImgRec.centery = 100

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


while(isActive):
    screen.fill((255, 255, 255))  
    screen.blit(background, (0, 0))
    eventProcess()
    # Directions[0].y = 100
    # Directions[0].rotate(1)
    # Directions[0].draw()
    draw_targetArea()
    drawIcon()
    setText()
    drawResult()
    remain_time = (pygame.time.get_ticks() - start_time) / 1000
    mFont = pygame.font.SysFont("굴림", 35)
    timer = mFont.render(str(int(total_time - remain_time)), True, 'black')
    screen.blit(timer, (350,50))
    if total_time - remain_time <= 0:
        isActive = False
    pygame.display.update()
    clock.tick(800)  

    pygame.display.update()