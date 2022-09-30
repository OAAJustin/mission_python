from multiprocessing.context import SpawnProcess
import pgzrun

WIDTH = 800
HEIGHT = 600
player_x = 700
player_y = 125

take_off_checklist = ["Put on suit", 
                      "Seal hatch",
                      "Check cabin pressure",
                      "Fasten seatbelt"]

spacewalk_checklist = ["Put on suit",
                       "Check oxygen",
                       "Seal helmet",
                       "Test radio",
                       "Open airlock"]

def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (50, 50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (650,50))
    
def game_loop():
    global player_x, player_y
    if keyboard.right:
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    elif keyboard.up:
        player_y -= 10
    elif keyboard.down:
        player_y += 10

clock.schedule_interval(game_loop, 0.03)
    
    
    


for index in range(len(spacewalk_checklist)):
    value = spacewalk_checklist[index]
    print(index,value)








pgzrun.go()