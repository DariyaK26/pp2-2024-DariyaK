import pygame
pygame.init()

screen=pygame.display.set_mode((200,400))
i=0
run=True
sounds=['lab7/sounds/pacman.mp3', 'lab7/sounds/rain.mp3', 'lab7/sounds/rickroll.mp3', 'lab7/sounds/ufo.mp3']
play=True
pause=False
while run:



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
            if i==len(sounds)-1:
                i=0
            else:
                i+=1
            
            pause=False
            play=True
        if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
            if i==0:
                i=len(sounds)-1 
            else:
                i-=1
            pause=False
            play=True
        if event.type==pygame.KEYDOWN and play:
            if pause:
                pygame.mixer.music.unpause()
                pause=not pause
            else:
                pygame.mixer.music.load(sounds[i])
                pygame.mixer.music.play(0) 
            play=not play

        elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE and not play:
            pygame.mixer.music.pause()
            play=not play
            pause = not pause

    
    
    
    
    
    pygame.display.flip()