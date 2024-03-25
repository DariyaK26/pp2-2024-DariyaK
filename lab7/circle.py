import pygame

size=w, h=300,300
pygame.init()
screen=pygame.display.set_mode(size)
run=True

x=25
y=25

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN and (event.key==pygame.K_UP or event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT or event.key==pygame.K_DOWN):
            pressed=pygame.key.get_pressed()
            
            if pressed[pygame.K_UP]: y-=20
            if pressed[pygame.K_DOWN]: y+=20   
            if pressed[pygame.K_LEFT]: x-=20
            if pressed[pygame.K_RIGHT]: x+=20
        if x>w-25:
            x=25
        if y>h-25:
            y=25
        if x<25:
            x=w-25
        if y<25:
            y=h-25

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (x,y),25 )
    pygame.display.flip()



