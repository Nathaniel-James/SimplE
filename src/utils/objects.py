import pygame

# Base 

class BaseObject:
    x = 0
    y = 0

    x_vel = 0
    y_vel = 0

    width = 0
    height = 0

    rect = pygame.Rect(x, y, width, height)

    def _update_hb(self):
        self.rect.update(self.x, self.y, self.width, self.height)

    def __init__(self, screen):
        self.screen = screen

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def place(self, x, y):
        self.x = x
        self.y = y
    
    def set_size(self, width, height):
        self.width = width
        self.height = height

        self._update_hb()

    def set_vel(self, x_velocity, y_velocity):
        self.x_vel = x_velocity
        self.y_vel = y_velocity

    def update(self):
        raise NotImplementedError("Object update method hasn't been implemented")

    def draw(self):
        raise NotImplementedError("Object draw method hasn't been implemented")



# Group and group management

class ObjectGroup(BaseObject):
    def __init__(self, parent):
        BaseObject.__init__(self, parent)
        
        self.group = []

    def add(self, obj):
        self.group.append(obj)
        return len(self.group)

    def remove(self, id):
        self.group.pop(id)

    def move(self, delta_x, delta_y):
        for obj in self.group:
            obj.move(delta_x, delta_y)

    def place(self, x, y):
        for obj in self.group:
            obj.place(x, y)
    
    def set_size(self, width, height):
        for obj in self.group:
            obj.set_size(width, height)

    def update(self):
        for obj in self.group:
            obj.update()

    def draw(self):
        for obj in self.group:
            obj.draw()



# Object types

class Image(BaseObject):
    def __init__(self, parent, img_path):
        BaseObject.__init__(self, parent)
        self.surface = pygame.image.load(img_path)
        self.width, self.height = self.surface.get_size()

    def update(self):
        self.x += self.x_vel
        self.y += self.y_vel

        self._update_hb()

    def draw(self):
        self.screen.blit(self.surface,(self.x,self.y))


class Animation(BaseObject):
    def __init__(self, parent, img_paths):
        BaseObject.__init__(self, parent)
        self.frames = [pygame.image.load(img) for img in img_paths]
        self.framerate = 1          # Controls "playback speed"

        self.frame_delta = 0      # Keeps track of time between last update frame
        self.current_image = 0

    def set_frame(self, frame):
        self.current_image = frame

    def update(self):
        self.x += self.x_vel        # Updating position
        self.y += self.y_vel

        self._update_hb()
    
        if self.frame_delta >= self.framerate:
            self.frame_delta = 0                                              # Resetting frame count
            self.current_image = (self.current_image+1) % len(self.frames)      # Changing image and limiting it by the length of frames
        self.frame_delta += 1

    def draw(self):
        img = self.frames[self.current_image]

        self.screen.blit(img, (self.x, self.y))


class Hitbox(BaseObject):
    def __init__(self, parent):
        BaseObject.__init__(self, parent)
        self.debug = False
        self.debug_col = (255,0,0,0.5)
        self.debug_style = 2

    def update(self):
        self.x += self.x_vel        # Updating position
        self.y += self.y_vel

        self._update_hb()

    def draw(self):
        if self.debug:
            pygame.draw.rect(self.screen, self.debug_col, self.rect, self.debug_style)

# Object method
def hb_collision(obj_1, obj_2):
    return obj_1.colliderect(obj_2)

def point_collision(obj, x, y):
    return obj.rect.collidepoint(x, y)

# Mouse methods
def get_mouse_pos():
    if pygame.mouse.get_focused():
        return pygame.mouse.get_pos()
    return (-1, -1)