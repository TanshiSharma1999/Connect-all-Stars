import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600
TITLE="✨✨✨✨Connect All Stars✨✨✨✨"

stars = []
lines = []
next_satellite = 0

start_time = 0
total_time = 0
end_time = 0

number_of_satellite = 8

def create_stars():
    global start_time
    
    for count in range(0, number_of_satellite):
        satellite = Actor("star2")
        satellite.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        stars.append(satellite)
    
    start_time = time()

def draw():
    global total_time

    screen.blit("background", (0,0))
    
    number = 1
    
    for satellite in stars:
        screen.draw.text(
            str(number),
            (satellite.pos[0]+10, satellite.pos[1] +30)
        )
        
        satellite.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_satellite < number_of_satellite:
        total_time = time() - start_time
        
        screen.draw.text(
            str(round(total_time,1)),
            (10,10),
            fontsize=30
        )
    else:
        screen.draw.text(
            str(round(total_time,1)),
            (10,10),
            fontsize=30
        )

def update():
    pass

def on_mouse_down(pos):
    global next_satellite, lines

    if next_satellite < number_of_satellite:
        
        if stars[next_satellite].collidepoint(pos):
            
            if next_satellite:
                lines.append(
                    (
                        stars[next_satellite-1].pos,
                        stars[next_satellite].pos
                    )
                )

            next_satellite = next_satellite + 1

        else:
            lines = []
            next_satellite = 0

create_stars()

pgzrun.go()