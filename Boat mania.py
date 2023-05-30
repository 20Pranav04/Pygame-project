#Arcade Pygame Workshop project(inspired from a pygame car race tutorial on Google)
#Submitted by Pranav(S2 ECE)

import pygame,sys
pygame.init() 
from pygame.locals import* 
import random
import math
import time
clock=pygame.time.Clock()


screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Boat mania')


   
def countdown():
    font2 = pygame.font.Font('freesansbold.ttf', 85)
    countdownBacground = pygame.image.load('bg.jpg')
    three = font2.render('3',True, (0,0,0))
    two =   font2.render('2',True, (0,0,0))
    one =   font2.render('1',True, (0,0,0))
    go =    font2.render('GO!!!',True, (0,0,0))
    
    

    screen.blit(countdownBacground, (0,0))
    pygame.display.update()

    ###### Displaying  three (3) ######
    screen.blit(three,(350,250))
    pygame.display.update()
    time.sleep(1)

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(1)

        ###### Displaying  two (2) ######
    screen.blit(two,(350,250))
    pygame.display.update()
    time.sleep(1)

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(1)

        ###### Displaying  one (1) ######
    screen.blit(one,(350,250))
    pygame.display.update()
    time.sleep(1)

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0,0))
    pygame.display.update()
    time.sleep(1)

        ###### Displaying  Go!!! ######
    screen.blit(go,(350,250))
    pygame.display.update()
    time.sleep(1)
    gameloop() 
    clock.tick(60)
    pygame.display.update()



def gameloop():
    


 
    score_value = 0
    font1= pygame.font.Font("freesansbold.ttf",25)

    def show_score(x,y):
        score = font1.render("SCORE: "+ str(score_value), True, (255,255,255))
        screen.blit(score, (x,y))

   
   

    def gameover():
        gameoverImg = pygame.image.load("gameover.png")
        run = True
        while run:

            screen.blit(gameoverImg,(0,0))
            time.sleep(0.5)
            show_score(325,415)
            time.sleep(0.5)
            pygame.display.update()
            
            for event in pygame.event.get():
             if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    countdown()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
    
    bg = pygame.image.load('bg.jpg')
    clock.tick(60)
    
    
    boat = pygame.image.load('boat.png')
    boatX = 350
    boatY = 495
    boatX_change = 0
    boatY_change = 0

  
    dinghy = pygame.image.load('dinghy.png')
    dinghyX = random.randint(178,570)
    dinghyY = 100
    dinghyYchange = 10  

    branch = pygame.image.load('branch.png')
    branchX = random.randint(178,570)
    branchY = 100
    branchYchange = 10

    log = pygame.image.load('log.png')
    logX = random.randint(178,570)
    logY = 100
    logYchange = 10
      

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

         
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT:
                    boatX_change += 5
            
                if event.key == pygame.K_LEFT:
                    boatX_change -= 5
                
                if event.key == pygame.K_UP:
                    boatY_change -= 5
                    
                if event.key == pygame.K_DOWN:
                    boatY_change += 5

             
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_RIGHT:
                    boatX_change = 0
            
                if event.key == pygame.K_LEFT:
                    boatX_change = 0
                
                if event.key == pygame.K_UP:
                    boatY_change = 0
                    
                if event.key == pygame.K_DOWN:
                   boatY_change = 0            
    
        #setting boundary for our boat
        if boatX < 178:
            boatX = 178
        if boatX > 570:
            boatX = 570
        
        if boatY < 0:
            boatY = 0
        if boatY > 495:
            boatY = 495


    
        screen.fill((0,0,0))

       
        screen.blit(bg,(0,0))

        
        screen.blit(boat,(boatX,boatY))

        screen.blit(dinghy,(dinghyX,dinghyY))
        screen.blit(branch,(branchX,branchY))
        screen.blit(log,(logX,logY))
          
        show_score(650,280)
        

        
        
        #updating the values
        boatX += boatX_change
        boatY += boatY_change

        #movement of the enemies
        dinghyY += dinghyYchange
        branchY += branchYchange
        logY += logYchange
        #moving enemies infinitely
        if dinghyY > 670:
            dinghyY = -100
            dinghyX = random.randint(178,490)
            score_value += 1
        if branchY > 670:
            branchY = -150
            branchX = random.randint(178,490)
            score_value += 1
        if logY > 670:
            logY = -200
            logX = random.randint(178,490)
            score_value += 1

        clock.tick(60)
        

          
         


        #DETECTING COLLISIONS 

        
        def iscollision(dinghyX,dinghyY,boatX,boatY):
            distance = math.sqrt(math.pow(dinghyX- boatX,2) + math.pow(dinghyY - boatY,2)) 

           
            if distance < 50: 
                return True
            else:
                return False

       
        def iscollision(branchX,branchY,boatX,boatY):
            distance = math.sqrt(math.pow(branchX-boatX,2) + math.pow(branchY - boatY,2))

          
            if distance < 50:
                return True
            else:
                return False

      
        def iscollision(logX,logY,boatX,boatY):
            distance = math.sqrt(math.pow(logX-boatX,2) + math.pow(logY - boatY,2))

           
            if distance < 50:
                return True
            else:
                return False
      

       
        coll1 = iscollision(dinghyX,dinghyY,boatX,boatY) 

        
        coll2 = iscollision(branchX,branchY,boatX,boatY) 

       
        coll3 = iscollision(logX,logY,boatX,boatY) 

        if coll1: 
            
            
            dinghyYchange = 0
            branchYchange = 0
            logYchange = 0
            dinghyY = 0
            branchY = 0
            logY = 0
            boatX_change = 0
            boatY_change = 0
          
     
            time.sleep(1)
            gameover()
          
           
            
        
     
        if coll2:
           
            
            dinghyYchange = 0
            branchYchange = 0
            logYchange = 0
            dinghyY = 0
            branchY = 0
            logY = 0
            boatX_change = 0
            boatY_change = 0
            
            time.sleep(1)
            gameover()
           

        if coll3:
            
           
            dinghyYchange = 0
            branchYchange = 0
            logYchange = 0
            dinghyY = 0
            branchY = 0
            logY = 0
            boatX_change = 0
            boatY_change = 0
         
            time.sleep(1)
            gameover()
        
        if dinghyYchange == 0 and branchYchange == 0 and logYchange == 0 :
          pass
        pygame.display.update()
            
         

pygame.display.update()

gameloop()