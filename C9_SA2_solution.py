import pygame,sys,random
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption('Bird Game')
images={}
images["bg1"] = pygame.image.load("bg1.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)
bird=pygame.Rect(100,250,30,30)
groundx=0
while True:
    screen.blit(images["bg1"],[0,0])
    groundx-=5
    if groundx < -330:
        groundx=0
    screen.blit(images["base"],[groundx,550])
    screen.blit(images["bird"],bird)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()   
    clock.tick(30)