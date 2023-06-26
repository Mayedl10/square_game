import libs.collission as collission
import libs.draw as draw

import os
import pygame
import time
import random

pygame.init()       # init pygame
pygame.font.init()  # init font loader
pygame.mixer.init() # init sound loader


FPS = 60                                                                    # framerate
ROOT_N = "Untitled-52 copy"                                                 # window title
WIDTH, HEIGHT = 900, 800                                                    # window size

ROOT = pygame.display.set_mode((WIDTH,HEIGHT))                              # ROOT window object
pygame.display.set_caption(ROOT_N)                                          # set

font = pygame.font.Font(os.path.join("fonts", "game_font.otf"), 40)         # initialize the font

BGCOLOR = (20,20,20)                                                        # background colour

# display text
# ROOT.blit(font.render("Test string.", True, (255,255,255)), (100,100))


class foundSquare:
    def __init__(self, corners:tuple, player:int):
        self.corners = corners
        self.player = player






def draw_5x5_circle_matrix(x, y, win, grid):                                # draws the grid

    xd = 100                    # distance between circles in x
    yd = 100                    # distance between circles in y
    rad = 25                    # radius of the circles

    colour_dict = {             # what colour corresponds to what value in grid[x][y] 
        0 : (200,200,200),
        1 : (0, 200, 200),
        2 : (200, 200, 0)
    }

    for i in range(5):
        for j in range(5):
            draw.draw_circle(win, x + i*xd, y + j*yd, rad, colour_dict[grid[j][i]])             # draw every circle in the correct colour


def find_squares(grid:list, last_placed:tuple, last_player:int):
    if last_player == 1: other_player = 2
    else: other_player = 1
    found = []      # will be filled with foundSquare objects
    for i in range(max(-last_placed[0],-last_placed[1]), 4-max(last_placed[0],last_placed[1])):
        for j in range(max(-last_placed[1],i-4-last_placed[0]), max(last_placed[0],4-i-last_placed[1])):
            try:
                corners = []
                a=i
                b=j
                pointcheck = last_placed
                corners.append(pointcheck)
                quadrat = True
                for k in range(3):
                    pointcheck = (pointcheck[0]+a,pointcheck[1]+b)
                    corners.append(pointcheck)
                    if grid[pointcheck[0]][pointcheck[1]] != last_player:
                            quadrat=False
                    temp = a
                    a=-b
                    b=temp

                if quadrat:
                    print("SQUARE") 
                    print(corners)

                    
            except:
                pass

    return found




def draw_window(grid):
    ROOT.fill(BGCOLOR)                                                      # fill background with BGCOLOR
    
    draw_5x5_circle_matrix(250,250,ROOT, grid)                              # draw grid






    pygame.display.update()                                                 # refresh screen

def main():
    # variables
    current_player = 1              # used for determining the next places circle's colour
    button_cooldown = 15            # so there are no accidents
    scores = {
        1 : 0,
        2 : 0
    }

    lines_to_draw = []              # fill with ((x1, y1), (x2, y2))

    grid =  [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
            ]

    # the positions of all circles
    circle_center_list = [(250, 250), (250, 350), (250, 450), (250, 550), (250, 650), (350, 250), (350, 350), (350, 450), (350, 550), (350, 650), (450, 250), (450, 350), (450, 450), (450, 550), (450, 650), (550, 250), (550, 350), (550, 450), (550, 550), (550, 650), (650, 250), (650, 350), (650, 450), (650, 550), (650, 650)]

    # what position corresponds to what index(es)
    circle_positions = {
        circle_center_list[0]: (0,0),
        circle_center_list[1]: (0,1),
        circle_center_list[2]: (0,2),
        circle_center_list[3]: (0,3),
        circle_center_list[4]: (0,4),
        
        circle_center_list[5]: (1,0),
        circle_center_list[6]: (1,1),
        circle_center_list[7]: (1,2),
        circle_center_list[8]: (1,3),
        circle_center_list[9]: (1,4),
        
        circle_center_list[10]: (2,0),
        circle_center_list[11]: (2,1),
        circle_center_list[12]: (2,2),
        circle_center_list[13]: (2,3),
        circle_center_list[14]: (2,4),
        
        circle_center_list[15]: (3,0),
        circle_center_list[16]: (3,1),
        circle_center_list[17]: (3,2),
        circle_center_list[18]: (3,3),
        circle_center_list[19]: (3,4),
        
        circle_center_list[20]: (4,0),
        circle_center_list[21]: (4,1),
        circle_center_list[22]: (4,2),
        circle_center_list[23]: (4,3),
        circle_center_list[24]: (4,4),
    }

    clock = pygame.time.Clock()
    
    run = True
    while run:
        # regulate fps
        clock.tick(FPS)

        # check if the X is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #place for funtions

        mouse_x, mouse_y = pygame.mouse.get_pos()


        ############################################################################################################################## collission mouseXgrid and placement of circles
        for i in circle_center_list:
            if (collission.pointDstFlt(mouse_x, mouse_y, i[0], i[1]) <= 25) and pygame.mouse.get_pressed()[0] and button_cooldown < 0:
                button_cooldown = 15
                chosen_one = circle_positions[i]
                print(chosen_one)
                if grid[chosen_one[1]][chosen_one[0]] == 0:
                    grid[chosen_one[1]][chosen_one[0]] = current_player
                    find_squares(grid, chosen_one, current_player)
                    if current_player == 1: current_player = 2
                    else: current_player = 1

        
        button_cooldown -= 1
                

        # draw window
        draw_window(grid)

    pygame.quit()



    

if __name__ == "__main__":
    main()