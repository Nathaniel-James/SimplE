import pygame

class InputManager:
    def __init__(self):
        self.current_state = None
        self.previous_state = None

    def process_input(self):
        self.previous_state = self.current_state
        self.current_state = pygame.key.get_pressed()

    def is_key_down(self, code):
        if self.current_state is None or self.previous_state is None:
            return False
        return self.current_state[code] == True

    def is_key_pressed(self, code):
        if self.current_state is None or self.previous_state is None:
            return False
        return self.current_state[code] == True and self.previous_state[code] == False

    def is_key_released(self, code):
        if self.current_state is None or self.previous_state is None:
            return False
        return self.current_state[code] == False and self.previous_state[code] == True