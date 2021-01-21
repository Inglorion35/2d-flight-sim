import pygame
import pygame.freetype
import os, sys, psutil, logging #os, sys and logging are inbuilt

pygame.init()
pygame.font.init()
#font colors (rgb)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0,0,0)

def print_text(text, fontsize, textcolor, bgcolor, isbold):
    font = pygame.freetype.SysFont("Consolas", fontsize, bold=isbold)
    surface, _ = font.render(text=text, fgcolor=textcolor, bgcolor=bgcolor)
    return surface.convert_alpha()

def restart_program():
    try:
        psy = psutil.Process(os.getpid())  #gives id of memory process
        for handler in psy.open_files() + psy.connections():    #sees files open using memory id
            os.close(handler.fd)     #closes the files given by loop
    except Exception as exc:  #wildcard* exception
        logging.error(exc)    #should give a summary of what made program crash ig
    python = sys.executable   #path for executable binary python (bytecode for specific processor)
    os.execl(python, python, *sys.argv)  #execl causes running process 'python' to be replaced by program passed as arguments

def play_game(screen):
    playagainbox = print_text('PLAY AGAIN?', 56, BLACK, None, False)
    againrect = playagainbox.get_rect(center = (screen.get_width()/2, screen.get_height()/2))
    screen.blit(playagainbox, againrect)

def quit_program():
    pygame.time.wait(1000)
    pygame.quit()
    sys.exit()

def newgame(screen):
    newgame_box = print_text('FLIGHT SIMULATOR', 46, WHITE , None, True)
    presskeymsg = print_text('PRESS ANY KEY TO START', 9, RED, None, True)
    wt = screen.get_width()
    ht = screen.get_height()
    keymsg_rect = presskeymsg.get_rect(center = (wt/2, ht*2/3))
    newgame_rect = newgame_box.get_rect(center=(wt/2, ht/2))
    screen.blit(newgame_box, newgame_rect)
    screen.blit(presskeymsg, keymsg_rect)
    
# def resize_window(screen, player, w,h):
#     global SCREEN_HEIGHT
#     global SCREEN_WIDTH
#     screen = pygame.display.set_mode(( w,  h),pygame.RESIZABLE)
#     SCREEN_HEIGHT, SCREEN_WIDTH =  h,  w 

def flightscore(screen, time):
    text1 = 'SCORE: ' + str(int(time))
    score = print_text(text1, 16, WHITE, None, False)
    wt = screen.get_width()
    ht = screen.get_height()
    scorebox = score.get_rect(center = (wt*8/9, ht*7/9))
    screen.blit(score, scorebox)
    