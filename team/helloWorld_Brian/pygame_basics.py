import pygame # all available pygame submodules are automatically imported
import time # ? 

pygame.init() #initializes all imported pygame modules

#color constants, easy to go to website to get RGB
black = (0,0,0) 
white = (255, 255, 255)
red = (255, 0, 0)

#makes the display size easy to modify by using variables
display_width = 600
display_height = 800

#create Display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Turkey Trot')
clock = pygame.time.Clock()  #Neccessary

#create idleImg
idleImgs = [pygame.image.load('png/Idle (1).png'),
           pygame.image.load('png/idle (2).png'),
           pygame.image.load('png/idle (3).png'),
           pygame.image.load('png/idle (4).png'),
           pygame.image.load('png/idle (5).png'),
           pygame.image.load('png/idle (6).png'),
           pygame.image.load('png/idle (7).png'),
           pygame.image.load('png/idle (8).png'),
           pygame.image.load('png/idle (9).png'),
           pygame.image.load('png/idle (10).png'),
           pygame.image.load('png/idle (11).png'),
           pygame.image.load('png/idle (12).png'),
           pygame.image.load('png/idle (13).png'),
           pygame.image.load('png/idle (14).png'),
           pygame.image.load('png/idle (15).png'),
           pygame.image.load('png/idle (16).png')]

walkingImgs = [pygame.image.load('png/Idle (1).png'),
           pygame.image.load('png/idle (2).png'),
           pygame.image.load('png/idle (3).png'),
           pygame.image.load('png/idle (4).png'),
           pygame.image.load('png/idle (5).png'),
           pygame.image.load('png/idle (6).png'),
           pygame.image.load('png/idle (7).png'),
           pygame.image.load('png/idle (8).png'),
           pygame.image.load('png/idle (9).png'),
           pygame.image.load('png/idle (10).png'),
           pygame.image.load('png/idle (11).png'),
           pygame.image.load('png/idle (12).png'),
           pygame.image.load('png/idle (13).png'),
           pygame.image.load('png/idle (14).png'),
           pygame.image.load('png/idle (15).png'),
           pygame.image.load('png/idle (16).png')]


for i in range(16):
    idleImgs[i] = pygame.transform.scale(idleImgs[i], (104,114)) #scale image

idle_count = 0

def idle(x,y): #calling this function displays image
    global idle_count
    gameDisplay.blit(idleImgs[idle_count], (x,y))

    if idle_count + 1 >= 16:
        idle_count= 0

    idle_count += 1
    print (idle_count)
        
    pygame.display.update() #updates the display
    

        

    
        

def text_objects(text,font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

    

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2, display_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update() #updates the display

def hello_world():
    message_display('Hello World')

def game_loop():
    x = (display_width * .43)
    y = (display_height * .6)

    x_change = 0
    y_change = 0

    #animation


    


    #event handling
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True

            #KEY PRESS EVENTS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change =  -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                elif event.key == pygame.K_DOWN:
                    y_change = 10
                elif event.key == pygame.K_UP:
                    y_change = -10

                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

                
        x += x_change
        y += y_change
                
        gameDisplay.fill(white)
        idle(x,y)
        hello_world()
        

        if x < 0 or x > display_width - 100: #Border
            gameExit = True

        if y < 0 or y > display_height - 120:
            gameExit = True

        pygame.display.update() #updates the display
        clock.tick(30)

        
game_loop()
pygame.quit()
quit()

