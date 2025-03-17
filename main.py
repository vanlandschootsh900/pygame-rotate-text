#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module


def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen



def draw_text(screen, text, size, color ,x,y, font_name=None, bold=False, italic=False, rotation=0,):
    pygame.font.init()
    if font_name:
        font= pygame.font.Font(font_name, size)
    else:
        font= pygame.font.Font(None, size)

    text_surface = font.render(text, True, color)

    if rotation !=0:
        text_surface = pygame.transform.rotate(text_surface, rotation)
    text_rect = text_surface.get_rect(center=(x,y))

    screen.blit(text_surface, text_rect.topleft)



def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    
    screen = init_game()
    clock = pygame.time.Clock()
    nums=0

    
        
    
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        nums+=1
        # Add code to draw stuff (for example) below this comment
        

        font_name1='DejaVuSans.ttf'
        text1 = 'Hello Shay'
        font_size1 = 67
        color1 = config.PURPLE
       


        draw_text(screen, text1, font_size1, color1, 350,300,font_name1, bold=True, rotation=nums)





        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
