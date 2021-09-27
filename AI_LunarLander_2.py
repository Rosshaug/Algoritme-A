# Lunar Lander: AI-controlled play

# Instructions:
#   Land the rocket on the platform within a distance of plus/minus 20, 
#   with a horizontal and vertical speed less than 20
#
# Controlling the rocket:
#    arrows  : Turn booster rockets on and off
#    r       : Restart game
#    q / ESC : Quit

from LunarLander import *
import statistics
import math
fuel_list = []
env = LunarLander()
env.reset()
exit_program = False
while not exit_program: 
    env.render()
    (x, y, xspeed, yspeed), reward, done = env.step((boost, left, right)) 

    # Process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                exit_program = True
            if event.key == pygame.K_UP:
                boost = True
            if event.key == pygame.K_DOWN:
                boost = False
            if event.key == pygame.K_RIGHT:
                left = False if right else True
                right = False
            if event.key == pygame.K_LEFT:
                right = False if left else True
                left = False
            if event.key == pygame.K_r:
                boost = False        
                left = False
                right = False
                env.reset()


    



    if abs(x) < 20:
        if yspeed > 18:
            boost = True
        if yspeed < 5:
            boost = False
        if y > 200:
            boost = False

    elif y < 400 and yspeed > -20:
        boost = True
    else:
        boost = False
        
    
    if abs(x) < 20 and xspeed == 0:
        right = False
        left = False
    if x > 0:
        right = True
        left = False
        if xspeed < -5 and x < 25:
            left = True
            right = False
        elif xspeed < -15 and x < 150:
            left = True
            right = False
    elif x < 0:
        left = True
        right = False
        if xspeed > 5 and x > -25:
            left = False
            right = True
        elif xspeed > 15 and x > -150:
            left = False
            right = True

    if env.won == True and len(fuel_list) <= 1000:
        right = False
        left = False
        fuel_list.append(int(env.rocket.fuel))
        if len(fuel_list) > 1:
            print(str(sum(fuel_list)/len(fuel_list)) + ' +- ' + str(1.96 * math.sqrt(statistics.variance(fuel_list)/len(fuel_list))))
        env.reset()
            
        
 




env.close()