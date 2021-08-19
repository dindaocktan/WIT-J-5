import pygame
from pygame import surface
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

BLUE    = (106, 159, 181)
WHITE   = (255, 255, 255)

def canvas(text, font_size, text_rgb, bg_rgb):
    font        = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _  = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb) 
    return surface.convert_aplha()