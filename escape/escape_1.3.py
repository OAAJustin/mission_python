import pgzrun

WIDTH = 800
HEIGHT = 600
player_x = 700
player_y = 125


def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.ship, (130,150))
    screen.blit(images.mars, (50, 50))
    

pgzrun.go()