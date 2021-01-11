import pygame as pg
import random
pg.init()
Win = pg.display.set_mode((500,500))
pg.display.set_caption("First Game")

font = pg.font.SysFont(None,30)
def setScore(text,color,x,y):
    Stext = font.render(text,True,color)
    Win.blit(Stext,[x,y])
def plot_snake(Win,color,snk_list,snake_sizex,snake_sizey):
    for x,y in snk_list:
         pg.draw.rect(Win,color,(x,y,snake_sizex,snake_sizey))

def Welcome():
    run = False
    pg.time.delay(100)
    while not run:
        Win.fill((255,255,255))
        setScore("Welcome To Snake Game",(0,0,0),125,200)
        setScore("Press Space To Play",(0,0,0),150,240)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    GameOver()
        pg.display.update()
    

def GameOver():
    #snake starting position
    snake_x = 45
    snake_y = 55
    #snake starting size
    snake_sizex = 10
    snake_sizey = 10
    #snake starting velocity
    vel_x = 0
    vel_y = 0
    initVelo = 8
    #food size
    food_size = 6
    food_x = random.randint(5,495)
    food_y = random.randint(50,495)
    score = 0
    run = True
    snk_list = []
    snk_length = 1
    gameover = False
    with open("highscore.txt","r") as f:
        HighScore = f.read()

    while run:
        pg.time.delay(100)
        if gameover:
            with open("highscore.txt","w") as f:
                f.write(str(HighScore))
            Win.fill((255,255,255))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            setScore("Game over! Press Enter To Continue",(255,0,0),70,250)
            keys1 = pg.key.get_pressed()
            if keys1[pg.K_RETURN]:
                GameOver()

        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                vel_x = -initVelo
                vel_y = 0 
            if keys[pg.K_RIGHT]:
                vel_x = initVelo
                vel_y = 0
            if keys[pg.K_UP]:
                vel_y = -initVelo
                vel_x = 0
            if keys[pg.K_DOWN]:
                vel_y = initVelo
                vel_x = 0
            if keys[pg.K_s]:
                score +=100
                if score>int(HighScore):
                     HighScore = score
                setScore("Score :"+str(score)+"    High-Score :"+str(HighScore),(0,0,255),120,5)
            snake_x += vel_x
            snake_y += vel_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                 score += 10
                 food_x = random.randint(5,495)
                 food_y = random.randint(50,495)
                 snk_length += 3
                 if score>int(HighScore):
                     HighScore = score
                     

            Win.fill((255,255,255))
            setScore("Score :"+str(score)+"    High-Score :"+str(HighScore),(0,0,255),120,5)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                gameover = True
            if snake_x<0 or snake_x>500 or snake_y<0 or snake_y>500:
                gameover = True
            
            pg.draw.rect(Win,(255,0,0),(food_x,food_y,food_size,food_size))
            plot_snake(Win,(0,0,0),snk_list,snake_sizex,snake_sizey)

        pg.display.update()
        
Welcome()            
pg.quit()
        
