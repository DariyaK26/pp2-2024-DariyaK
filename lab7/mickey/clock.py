import pygame as pg

import datetime
pg.init()
W = 450
H = 400
run=True
screen = pg.display.set_mode((W, H))
screen.fill((255, 255, 255))

clock = pg.image.load('lab7/mickey/mainclock.png').convert()
clock=pg.transform.rotate(clock,2)
left=pg.image.load('lab7/mickey/leftarm.png')
right=pg.image.load('lab7/mickey/rightarm.png')

pg.display.update()

a_left=0
a_right=0
left1=pg.transform.scale(left,(19, left.get_height()//3-15))
right1=pg.transform.scale(right,(right.get_width()//3, right.get_height()//3))
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run=False
    x=datetime.datetime.now()
    minutes=x.minute
    second=x.second

    
    clock1=pg.transform.scale(clock,(clock.get_width()//3, clock.get_height()//3))
    rot = pg.transform.rotate(right1,-45)
    screen.blit(clock1,(0,0))

    rotateleft=pg.transform.rotate(left1,a_left)
    rotaterleft=rotateleft.get_rect(center=(236,178))
    
    rotateright=pg.transform.rotate(right1,a_right-50)
    rotaterright=rotateright.get_rect(center=(237,178))
    
    screen.blit(rotateleft,rotaterleft.topleft)
    screen.blit(rotateright,rotaterright.topleft)
    
    a_left=second*(-6)
    a_right=minutes*(-6)

    
    pg.display.update()
    pg.display.flip()