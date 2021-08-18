
import Mario.runner_class as mario
import Hamster.game as hamster
import Snake.snake as snake

import pygame.freetype
import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
icon_hamster = pygame.image.load("C:/Users/ioa/CODe/DTS/WIT-J-5/Hamster/resources/images/dude.png")
icon_snake = pygame.image.load("C:/Users/ioa/CODe/DTS/WIT-J-5/Snake/snake.png")
icon_snake = pygame.transform.scale(icon_snake, (100, 50)) 
icon_snakeladders = pygame.image.load("C:/Users/ioa/CODe/DTS/WIT-J-5/SnakeAndLadders/icon.jpg")
icon_snakeladders = pygame.transform.scale(icon_snakeladders, (100, 100)) 
# icon_snake =  pygame.display.flip()


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()


class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
            action - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]

        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        self.action = action

        super().__init__()

    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the mouse_over variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)


def main():
    pygame.init()

    
    screen = pygame.display.set_mode((800, 650))
    # screen.blit(playerS, (100,100))
    game_state = GameState.TITLE
    

    while True:
        
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)
            # game_state = bird.main()
            # game_state = mario
            
        if game_state == GameState.QUIT:
            pygame.quit()
            return
        
        if game_state == GameState.HAMSTER:
            game_state = hamster.main()
        elif game_state == GameState.SNAKE:
            game_state = snake.main()
        
def title_screen(screen):
    start_btn = UIElement(
        center_position=(400, 250),
        font_size=60,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 475),
        font_size=60,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        
        pygame.display.flip()


def play_level(screen):
    return_btn_hamster = UIElement(
        center_position=(250, 200),
        font_size=40,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="HAMSTER",
        action=GameState.HAMSTER,
    )
    
    return_btn_snake = UIElement(
        center_position=(570, 200),
        font_size=40,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="SNAKE",
        action=GameState.SNAKE,
    )
    
    return_btn_snakeladders = UIElement(
        center_position=(400, 450),
        font_size=40,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="SNAKE & Ladders",
        action=GameState.SNAKEANDLADDERS,
    )
    
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )
    buttons = [return_btn_snakeladders, return_btn_hamster, return_btn_snake, return_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)
        # ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        # if ui_action is not None:
        #     return ui_action
        # return_btn.draw(screen)
        screen.blit(icon_hamster, (210, 125))
        screen.blit(icon_snake, (520, 125))
        screen.blit(icon_snakeladders, (350, 310))
        pygame.display.flip()


class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    HAMSTER = 1
    SNAKE   = 1
    SNAKEANDLADDERS = 1


if __name__ == "__main__":
    main()