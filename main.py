import math
import pygame
from robot import Graphics,Robot,Ultrasonic

MAP_DIMENSIONS = (600,1200)


#env
gfx = Graphics(MAP_DIMENSIONS,'robot.png','map.png')

#robot
start = (200,200)
robot = Robot(start,0.01*3779.52)

#sensor
sensor_range = 250, math.radians(40)
ultra_sonic = Ultrasonic(sensor_range,gfx.map)

dt=0
last_time=pygame.time.get_ticks()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    dt=(pygame.time.get_ticks()-last_time)/1000
    last_time=pygame.time.get_ticks()

    gfx.map.blit(gfx.map_img,(0,0))

    robot.kinematics(dt)
    gfx.draw_robot(robot.x,robot.y,robot.heading)
    point_cloud= ultra_sonic.sense_obstacles(robot.x,robot.y,robot.heading)
    robot.avoid_obstacles(point_cloud,dt)
    gfx.draw_sensor_data(point_cloud)
    pygame.display.update()

    
