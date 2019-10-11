from pico2d import *
import turtle
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

#x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
charX, charY = KPU_WIDTH // 2, KPU_HEIGHT // 2

def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8,0.9,0)
    turtle.dot(15)
    turtle.write('     '+str(p))
    
def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())
    
#def move_character_to_points(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):
        #global frame

def prepare_turtle_canvas():
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.speed(100)

    turtle.onkey(stop, 'Escape')
    turtle.listen()
        
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

process = True
chardir = 1
size = 10
frame = 0
points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(size)]
#turtle.setup(1280, 1024)
while process:
    #clear_canvas()
    #kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    #move_character_to_points(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7],points[8],points[9])
    #character.clip_draw(frame * 100, 100 * chardir, 100, 100, charX, charY)
    #update_canvas()
    #frame = (frame + 1) % 8
    
        # draw p1-p2
    if points[0][0] < points[1][0]:
        chardir = 1
    elif points[0][0] > points[1][0]:
        chardir = 0
            
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[0][0] + (3*t**3 - 5*t**2 + 2)*points[1][0] + (-3*t**3 + 4*t**2 + t)*points[2][0] + (t**3 - t**2)*points[3][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[0][1] + (3*t**3 - 5*t**2 + 2)*points[1][1] + (-3*t**3 + 4*t**2 + t)*points[2][1] + (t**3 - t**2)*points[3][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p2)
    if points[1][0] < points[2][0]:
         chardir = 1
    elif points[1][0] > points[2][0]:
         chardir = 0
            
    # draw p2-p3
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[1][0] + (3*t**3 - 5*t**2 + 2)*points[2][0] + (-3*t**3 + 4*t**2 + t)*points[3][0] + (t**3 - t**2)*points[4][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[1][1] + (3*t**3 - 5*t**2 + 2)*points[2][1] + (-3*t**3 + 4*t**2 + t)*points[3][1] + (t**3 - t**2)*points[4][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p3)
    if points[2][0] < points[3][0]:
        chardir = 1
    elif points[2][0] > points[3][0]:
        chardir = 0
        

    # draw p3-p4
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[2][0] + (3*t**3 - 5*t**2 + 2)*points[3][0] + (-3*t**3 + 4*t**2 + t)*points[4][0] + (t**3 - t**2)*points[5][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[2][1] + (3*t**3 - 5*t**2 + 2)*points[3][1] + (-3*t**3 + 4*t**2 + t)*points[4][1] + (t**3 - t**2)*points[5][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p4)
    if points[3][0] < points[4][0]:
        chardir = 1
    elif points[3][0] > points[4][0]:
        chardir = 0

    # draw p4-p5
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[3][0] + (3*t**3 - 5*t**2 + 2)*points[4][0] + (-3*t**3 + 4*t**2 + t)*points[5][0] + (t**3 - t**2)*points[6][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[3][1] + (3*t**3 - 5*t**2 + 2)*points[4][1] + (-3*t**3 + 4*t**2 + t)*points[5][1] + (t**3 - t**2)*points[6][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p5)
    if points[4][0] < points[5][0]:
        chardir = 1
    elif points[4][0] > points[5][0]:
        chardir = 0
    
    # draw p5-p6
    for i in range(0, 500, 2):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[4][0] + (3*t**3 - 5*t**2 + 2)*points[5][0] + (-3*t**3 + 4*t**2 + t)*points[6][0] + (t**3 - t**2)*points[7][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[4][1] + (3*t**3 - 5*t**2 + 2)*points[5][1] + (-3*t**3 + 4*t**2 + t)*points[6][1] + (t**3 - t**2)*points[7][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p6)
    if points[5][0] < points[6][0]:
        chardir = 1
    elif points[5][0] > points[6][0]:
        chardir = 0

    # draw p6-p7
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[5][0] + (3*t**3 - 5*t**2 + 2)*points[6][0] + (-3*t**3 + 4*t**2 + t)*points[7][0] + (t**3 - t**2)*points[8][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[5][1] + (3*t**3 - 5*t**2 + 2)*points[6][1] + (-3*t**3 + 4*t**2 + t)*points[7][1] + (t**3 - t**2)*points[8][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p7)
    if points[6][0] < points[7][0]:
        chardir = 1
    elif points[6][0] > points[7][0]:
        chardir = 0

    # draw p7-p8
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[6][0] + (3*t**3 - 5*t**2 + 2)*points[7][0] + (-3*t**3 + 4*t**2 + t)*points[8][0] + (t**3 - t**2)*points[9][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[6][1] + (3*t**3 - 5*t**2 + 2)*points[7][1] + (-3*t**3 + 4*t**2 + t)*points[8][1] + (t**3 - t**2)*points[9][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p8)
    if points[7][0] < points[8][0]:
        chardir = 1
    elif points[7][0] > points[8][0]:
        chardir = 0

    # draw p8-p9
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[7][0] + (3*t**3 - 5*t**2 + 2)*points[8][0] + (-3*t**3 + 4*t**2 + t)*points[9][0] + (t**3 - t**2)*points[0][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[7][1] + (3*t**3 - 5*t**2 + 2)*points[8][1] + (-3*t**3 + 4*t**2 + t)*points[9][1] + (t**3 - t**2)*points[0][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p9)
    if points[8][0] < points[9][0]:
        chardir = 1
    elif points[8][0] > points[9][0]:
        chardir = 0

    # draw p9-p10
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[8][0] + (3*t**3 - 5*t**2 + 2)*points[9][0] + (-3*t**3 + 4*t**2 + t)*points[0][0] + (t**3 - t**2)*points[1][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[8][1] + (3*t**3 - 5*t**2 + 2)*points[9][1] + (-3*t**3 + 4*t**2 + t)*points[0][1] + (t**3 - t**2)*points[1][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p10)
    if points[9][0] < points[0][0]:
        chardir = 1
    elif points[9][0] > points[0][0]:
        chardir = 0

    # draw p10-p1
    for i in range(0, 500, 1):
        t = i / 500
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        x = ((-t**3 + 2*t**2 - t)*points[9][0] + (3*t**3 - 5*t**2 + 2)*points[0][0] + (-3*t**3 + 4*t**2 + t)*points[1][0] + (t**3 - t**2)*points[2][0])/2
        y = ((-t**3 + 2*t**2 - t)*points[9][1] + (3*t**3 - 5*t**2 + 2)*points[0][1] + (-3*t**3 + 4*t**2 + t)*points[1][1] + (t**3 - t**2)*points[2][1])/2
        character.clip_draw(frame * 100, 100 * chardir, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
    #draw_point(p1)
    

close_canvas()




