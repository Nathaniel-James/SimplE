import pygame
from utils import ui, objects


# Setup classes


class BaseScene:
    def __init__(self, screen):
        self.screen = screen

    def on_enter(self):
        raise NotImplementedError("Base scene function not implemented")
    def on_exit(self):
        raise NotImplementedError("Base scene function not implemented")
    def input(self, sm, input_stream):
        raise NotImplementedError("Base scene function not implemented")
    def update(self, sm, input_stream):
        raise NotImplementedError("Base scene function not implemented")
    def draw(self, sm, screen):
        raise NotImplementedError("Base scene function not implemented")

    def draw_pixel(self, x,y, color):
        self.screen.set_at((x,y), color)

    def draw_column(self, x, color):
        pass

    def draw_row(self, y, color):
        pass

class SceneManager:
    def __init__(self):
        self.stack = [] 
        self.events = []

    # Stack functions
    def push(self, scene):
        self.exit()
        self.stack.append(scene)
        self.enter()

    def pop(self):
        self.exit()
        self.stack.pop()
        self.enter()

    def set(self, scenes):
        while len(self.stack) > 0:      # Clearing stack
            self.pop()

        for s in scenes:                # Add new scenes
            self.push(s)

    def isEmpty(self):
        return len(self.stack) == 0


    # Calling current scene
    def enter(self):
        if len(self.stack) > 0:
            self.stack[-1].on_enter()

    def exit(self):
        if len(self.stack) > 0:
            self.stack[-1].on_exit()

    def input(self, input_stream):
        if len(self.stack) > 0:
            self.stack[-1].input(self, input_stream)

    def update(self, input_stream, event):
        self.events = pygame.event.get()
        
        if len(self.stack) > 0:
            self.stack[-1].update(self, input_stream)

    def draw(self):
        if len(self.stack) > 0:
            self.stack[-1].draw(self)

        pygame.display.flip()


class ExampleScene(BaseScene): # Will not run
    def __init__(self, parent):
        BaseScene.__init__(self, parent)

        # Widgets
        self.title = ui.Text(self.screen, "SimplE", (0,0), size=40, bg=(0,0,0), fg=(255,255,255))
        self.subtitle = ui.Text(self.screen, "The Simple Engine - Alpha 0.2", (0,40), size=15, bg=(0,0,0), fg=(225,225,225))

        self.player = objects.Hitbox(self.screen)
        self.player.set_size(50,50)
        self.player.debug = True
        self.player.framerate = 1

    def on_enter(self):
        print("ExampleScene loaded")

    def on_exit(self):
        raise NotImplementedError("Base scene function not implemented")

    def input(self, sm, input_stream):
        if input_stream.is_key_down(pygame.K_w) == True:
            self.player.y_vel = -1
        elif input_stream.is_key_down(pygame.K_s) == True:
            self.player.y_vel = 1
        else:
            self.player.y_vel = 0

        if input_stream.is_key_down(pygame.K_a) == True:
            self.player.x_vel = -1
        elif input_stream.is_key_down(pygame.K_d) == True:
            self.player.x_vel = 1
        else:
            self.player.x_vel = 0

    def update(self, sm, input_stream):
        self.player.update()

    def draw(self, sm):
        self.screen.fill((0,0,0))

        self.title.draw()
        self.subtitle.draw()
        self.player.draw()