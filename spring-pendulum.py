import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()

WIDTH, HEIGHT = (500 ,500)

mass = 1

mass_force = 9.81 * mass
mass_acc = 0
mass_vel = 0

default_spring_length = 20
spring_length = 20
k = 1
spring_force = 0

g = 9

height = 50
width = 50

screen_pos = [WIDTH/2 - 25, spring_length * 10]

pos = [screen_pos[0]/10, screen_pos[1]/10]


display = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(line_start, line_end, rect_pos, width, height):
    display.fill((255, 255, 255))
    pygame.draw.line(display, (0, 0, 0),(line_start[0], line_start[1]), (line_end[0], line_end[1]))
    pygame.draw.rect(display, (0, 0, 0), (rect_pos[0], rect_pos[1], width, height))

    pygame.display.flip()

while True:

    dt = clock.tick(30)

    mass_force = 9.81 * mass

    diff = spring_length - default_spring_length

    spring_force = -1 * abs(diff) * k
    mass_force += spring_force

    mass_acc = mass / mass_force
    mass_vel += mass_acc / dt
    pos[1] += mass_vel / dt
    spring_length = pos[1]

    screen_pos = [pos[0] * 10, pos[1] * 10]

    print(mass_vel)

    mass_force = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close the program any way you want, or troll users who want to close your program.
            raise SystemExit


    draw([250, 50], [250, spring_length * 10], screen_pos, 50, 50)
