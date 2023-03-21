import pygame

class Text(pygame.font.Font):
    def __init__(self, parent, text, pos, bold=False, italic=False, underline=False,
                strikethrough=False, size=20, bg=(255,255,255), fg=(0,0,0),
                aa=True, font=pygame.font.get_default_font()):

        self.parent = parent

        # Initialize pygame fonts
        pygame.font.init()
        pygame.font.Font.__init__(self, font, size)

        # Setting font parameters
        self.set_bold(bold)
        self.set_italic(italic)
        self.set_underline(underline)
        self.set_strikethrough(strikethrough)

        # Setting font content
        self.text = text
        self.bg = bg
        self.fg = fg
        self.aa = aa    # Antialias
        self.x = pos[0]
        self.y = pos[1]

    def draw(self):
        widget = self.render(self.text, self.aa, self.fg, self.bg)
        self.parent.blit(widget,(self.x,self.y))
        

class Button:
    def __init__(self, parent, text=None, img=None):
        self.parent = parent
        
        if text != None:
            pass

        if img != None:
            pass

    def update(self, sm):
        pass

    def draw():
        pass


class RadioButton:
    pass


class CheckBox:
    pass


class ProgressBar:
    pass


class TextInput:
    pass


