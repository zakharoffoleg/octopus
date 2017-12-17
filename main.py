import pygame, sys, time
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0

map_data = [(5, 6, "2"), (8, 2, "3")]

for x in range(10):
    for y in range(6):
        map_data.append((x, y, "1"))

for x in range(10, 15):
    for y in range(6, 10):
        map_data.append((x, y, "2"))



fps_font = pygame.font.Font("fonts/Verdana.ttf", 20)

sky = pygame.image.load("graphics/sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Yellow)
    window.blit(fps_overlay, (0, 0))


def create_window():
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "Best RPG game ever"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_fps():
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS




create_window()

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Globals.camera_move = 1
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                
        elif event.type == pygame.KEYUP:
            Globals.camera_move = 0


    # LOGIC
    if Globals.camera_move == 1:
        Globals.camera_y += 100 * deltatime
    elif Globals.camera_move == 2:
        Globals.camera_y -= 100 * deltatime
    elif Globals.camera_move == 3:
        Globals.camera_x += 100 * deltatime
    elif Globals.camera_move == 4:
        Globals.camera_x -= 100 * deltatime

    

    # RENDER GRAPHICS
    window.blit(Sky, (0,0))

    # Render Simple Terrain Grid
    for x in range(0, 640, Tiles.Size):
        for y in range(0, 480, Tiles.Size):
            for i in map_data:
                tile = (i[0] * Tiles.Size, i[1] * Tiles.Size)
                if (x, y) == tile:
                    window.blit(Tiles.Texture_Tags[i[2]], (x + Globals.camera_x, y + Globals.camera_y))

    #show_fps()

    pygame.display.update()

    count_fps()

pygame.quit()
sys.exit()







