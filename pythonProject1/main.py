import pygame
import random
import sys  #用于退出操作

pygame.init()

WIDTH,HEIGHT=800,600
#面积
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("贪吃蛇游戏")

#颜色定义
BLACK = (0,0,0)
WHITE=(255,255,255)
GREEN =(0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

clock=pygame.time.Clock()
FPS = 10

#第二步
GRID_SIZE =20  #网格大小

GRID_WIDTH=WIDTH //GRID_SIZE
GRID_HEIGHT=HEIGHT //GRID_SIZE


snake =[
    (WIDTH//2,HEIGHT//2),
    (WIDTH//2-GRID_SIZE,HEIGHT//2),
    (WIDTH//2-2*GRID_SIZE,HEIGHT//2)
]
direction = (GRID_SIZE,0)


def generate_food():
    while True:
        x = random.randint(0,GRID_WIDTH - 1)*GRID_SIZE
        y = random.randint(0,GRID_HEIGHT- 1)*GRID_SIZE
        food_pos = (x,y)

        if food_pos not in snake:
            return food_pos

food = generate_food()





def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen,GREEN,(segment[0],segment[1],GRID_SIZE-1,GRID_SIZE-1))

def draw_food():
    pygame.draw.rect(screen,RED,(food[0],food[1],GRID_SIZE - 1,GRID_SIZE - 1))




running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        # 处理键盘操作
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction !=(0,GRID_SIZE):
                direction = (0,-GRID_SIZE)
            if event.key == pygame.K_DOWN and direction !=(0,-GRID_SIZE):
                direction = (0,GRID_SIZE)
            if event.key == pygame.K_LEFT and direction !=(GRID_SIZE,0):
                direction = (-GRID_SIZE,0)
            if event.key == pygame.K_RIGHT and direction !=(-GRID_SIZE,0):
                direction = (GRID_SIZE,0)
                #if event.key==pygame.K_DOWN and direction !=(0,-GRID_SIZE)
                    #direction = (0,GRID_SIZE)  向下


    head_x,head_y=snake[0]
    new_head = (head_x + direction[0],head_y+direction[1])

    snake.insert(0,new_head)

    #检测是否吃到了食物
    if new_head == food:

      food = generate_food()
    else:

      snake.pop()




    screen.fill(BLACK)
    draw_food()
    draw_snake()

    #将绘制内容显示到窗口上
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

sys.exit()