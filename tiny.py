import pygame
import random
import time

pygame.init()

red=(255, 0,0)
orange=(255, 127, 0)
yellow=(255, 255, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
violet=(127, 0, 255)
brown=(102, 51, 0)
black=(0,0,0)
white=(255, 255, 255)
pink=(255, 20, 147)

screen_width=600
screen_height=400
game_screen=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Endless Tennis")
font=pygame.font.SysFont("monospace", 75)

ball_x=int(screen_width /2)
ball_y=int(screen_height /2)
ball_xv=5
ball_yv=5
ball_r=20

paddle1_x=10
paddle1_y=10
paddle1_w=25
paddle1_h=100

paddle2_x=screen_width-35
paddle2_y=10
paddle2_w=25
paddle2_h=100

player1_score=0
player2_score=0


pygame.mouse.set_visible(0)
do_main=True
start_time = time.time()
while do_main:
    pressed=pygame.key.get_pressed()
    pygame.key.set_repeat
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            do_main=False
            
    if pressed[pygame.K_ESCAPE]:
        do_main=False
        
    if pressed[pygame.K_w]:
        paddle1_y -=5
    elif pressed[pygame.K_s]:
        paddle1_y +=5
    
    if pressed[pygame.K_UP]:
        paddle2_y -=5
    elif pressed[pygame.K_DOWN]:
        paddle2_y +=5
        


    ball_x +=ball_xv
    ball_y +=ball_yv
    
               
    if ball_y-ball_r <=0 or ball_y+ball_r>=screen_height:
        ball_yv *= -1
        

    if paddle1_y < 0:
        paddle1_y=0
    elif paddle1_y+paddle1_h>screen_height:
        paddle1_y=screen_height-paddle1_h
     
    if paddle2_y<0: 
        paddle2_y=0
    elif paddle2_y+paddle2_h>screen_height:
        paddle2_y=screen_height-paddle2_h
        
    if ball_x<paddle1_x+paddle1_w and ball_y>=paddle1_y and ball_y<=paddle1_y+paddle1_h:
        ball_xv *= -1
        
    if ball_x>paddle2_x and ball_y>=paddle2_y and ball_y<=paddle2_y+paddle2_h:
        ball_xv *=-1
        
    if ball_x<=0:
        player2_score+=2
        ball_x=int(screen_width/2)
        ball_y=int(screen_height/2)
    elif ball_x>= screen_width:
        player1_score+=2
        ball_x=int(screen_width/2)
        ball_y=int(screen_height/2)
        
    
    game_screen.fill(green)
    paddle_1=pygame.draw.rect(game_screen, white, (paddle1_x, paddle1_y, paddle1_w, paddle1_h), 0)
    paddle_2=pygame.draw.rect(game_screen, white, (paddle2_x, paddle2_y, paddle2_w, paddle2_h), 0)
    net=pygame.draw.line(game_screen, blue, (300,5), (300,400))
    ball=pygame.draw.circle(game_screen, blue, (ball_x, ball_y), ball_r, 0)
                              
    score_text=font.render(str(player1_score)+" "+str(player2_score), 1, white)
    game_screen.blit(score_text, (screen_width/2-score_text.get_width()/2, 10))
    
    
    pygame.display.update()
                              
    time.sleep(0.00606000666667)
                                 
pygame.quit()
                
