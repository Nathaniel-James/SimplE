import pygame
import scenes
from utils.input_manager import InputManager

# Constants
WIDTH = 800
HEIGHT = 600
BG_COLOR = (0, 0, 0)
SCENES = {
    "main_menu": scenes.ExampleScene
}

# Pygame setup
pygame.init()
pygame.display.set_caption("SimplE - a0.2")

clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))

scene_manager = scenes.SceneManager()
scene_manager.push(SCENES["main_menu"](window))

input_manager = InputManager()




# Mainloop
running = True
while running:
    events = pygame.event.get()

    for event in events:            # Quit
        if event.type == pygame.QUIT:
            running = False

    input_manager.process_input()
    # globals.soundManager.update()

    if scene_manager.isEmpty():
        running = False
    scene_manager.input(input_manager)
    scene_manager.update(input_manager, events)
    scene_manager.draw() 

    clock.tick(120)

# Breaking out of loop
pygame.quit()
quit()