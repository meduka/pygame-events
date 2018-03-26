
# Imports
import pygame
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Umbrella Boyos"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (100, 125, 75)
LIGHTER_GREEN = (13, 193, 34)
WHITE = (255, 255, 255)
OFF_WHITE = (234, 237, 239)
BLUE = (75, 200, 255)
DARK_BLUE = (15, 92, 216)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (244, 232, 66)
BLACK = (0, 0, 0)


#image
birbflap1 = pygame.image.load('bird1.png')

lad1 = pygame.image.load('umbrello.png')

lad2 = pygame.image.load('umbrella_down.png')

flag1 = pygame.image.load('banner1.png')
flag2 = pygame.image.load('banner2.png')
flag3 = pygame.image.load('banner3.png')

flagpole = [flag1, flag2, flag3]

# Settings
stormy = True
daytime = False
blackout = False


def draw_birds(fly):
    x = fly[0]
    y = fly[1]
    
    screen.blit(birbflap1,(x, y))

def draw_umbrello(run):
    x = run[0]
    y = run[1]

    screen.blit(lad1, (x, y))

def draw_parasollo(walk):
    x = walk[0]
    y = walk[1]

    screen.blit(lad2, (x, y))

def draw_cloud(loc, color):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])

def draw_raindrop(drop):
    rect = drop[:4]
    pygame.draw.ellipse(screen, DARK_BLUE, rect)


place = [400, 200]


def waving_flag(place, frame):
    x = place[0]
    y = place[1]
    
    screen.blit(flagpole[frame], (x, y))

''' Make clouds '''
num_clouds = 30
near_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 100)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 50
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1000)
    y = random.randrange(-50, 300)
    loc =  [x, y]
    far_clouds.append(loc)

''' Make rain '''

num_drops = 700
rain = []

for i in range(num_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(1, 5)
    stop = random.randrange(400, 700)
    drop = [x, y, r, r, stop]
    rain.append(drop)

''' Make birds '''

num_birds = 10
fly_bird = []

for i in range(num_birds):
    x = random.randrange(0, 1000)
    y = random.randrange(-50, 300)
    fly =  [x, y]
    fly_bird.append(fly)

''' make umbrello '''

num_umbrello = 3
umbrello_move = []

for i in range(num_umbrello):
    x = random.randrange(0, 1000)
    y = random.randrange(400, 550)
    run =  [x, y]
    umbrello_move.append(run)



lightning_timer = 0


# Sound Effects
pygame.mixer.music.load("mario_paint.ogg")

jam = pygame.mixer.Sound("mario_paint.ogg")




# Game loop

pygame.mixer.music.play(-1)

tick = 0
frame = 0

done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                daytime = not daytime
                stormy = not stormy

            if event.key == pygame.K_x:
                blackout = not blackout

        pressed = pygame.key.get_pressed()
        
        reverse = pressed[pygame.K_BACKSPACE]

    # Game logic

    tick += 1
     
    if tick%30 == 0:
        frame += 1
        if frame > 2:
            frame = 0


    ''' move clouds '''
    for c in far_clouds:
        if not reverse:
            c[0] -= 1
        elif reverse:
            c[0] += 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    for c in near_clouds:
        if not reverse:
            c[0] -= 2
        elif reverse:
            c[0] += 2

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)
            
    '''move birds'''

    for b in fly_bird:
        if not reverse:
           b[0] -= 1
        elif reverse:
            b[0] += 1

        if b[0] < -100:
            b[0] = random.randrange(800, 1600)
            b[1] = random.randrange(-50, 200)

    '''move umbrello'''

    for u in umbrello_move:
        if not reverse:
            u[0] -= 2
        elif reverse:
            u[0] += 2

        if u[0] < -100:
            u[0] = random.randrange(800, 1600)
            u[1] = random.randrange(400, 550)


            
    ''' set sky color '''
    if daytime:
        sky = BLUE
        near_cloud_color = WHITE
        far_cloud_color = OFF_WHITE
        grass_color = LIGHTER_GREEN
    else:
        sky = GRAY
        near_cloud_color = NOT_QUITE_DARK_GRAY
        far_cloud_color = DARK_GRAY
        grass_color = GREEN


    ''' move rain '''
    for r in rain:
        
        if not reverse:
            r[0] -= 1
            r[1] += 4
            
        elif reverse:
            r[0] += 1
            r[1] -= 4

        if r[1] > r[4]:
            r[0] = random.randrange(0, 1000)
            r[1] = random.randrange(-100, 0)

    ''' flash lighting '''
    if stormy:
        if random.randrange(0, 150) == 0:
            lightning_timer = 5
        else:
            lightning_timer -= 1
    
    # Drawing code
    ''' sky '''
    if lightning_timer > 0:
        screen.fill(YELLOW)
    else:
        screen.fill(sky)

    ''' sun '''
    if not stormy:
        pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, grass_color, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' clouds '''
    for c in far_clouds:
        draw_cloud(c, near_cloud_color)

    ''' rain '''
    if stormy:
        for r in rain:
            draw_raindrop(r)

    ''' clouds '''
    for c in near_clouds:
        draw_cloud(c, far_cloud_color)

    ''' flagpole'''
    waving_flag(place, frame)
        
    ''' character '''
    
    if not stormy:
        for b in fly_bird:
            draw_birds(b)

    if stormy:
        for u in umbrello_move:
            draw_umbrello(u)
    elif not stormy:
        for u in umbrello_move:
            draw_parasollo(u)

    ''' blackout'''

    if blackout:
        pygame.draw.rect(screen, BLACK, [0, 0, 800, 600])



    jam.play()

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
