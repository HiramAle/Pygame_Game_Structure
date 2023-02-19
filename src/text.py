import pygame
from src.commons import *


def load_font_image(path: str, color: str | tuple):
    foreground_color = (255, 255, 255)
    background_color = (0, 0, 0)
    font_image = pygame.image.load(path).convert()
    font_image = swap_color(font_image, foreground_color, color)
    last_x = 0
    letters = []
    letter_spacing = []
    for x in range(font_image.get_width()):
        if font_image.get_at((x, 0))[0] == 127:
            letters.append(clip_surface(font_image, last_x, 0, x - last_x, font_image.get_height()))
            letter_spacing.append(x - last_x)
            last_x = x + 1
        x += 1
    for letter in letters:
        letter.set_colorkey(background_color)
    return letters, letter_spacing, font_image.get_height()


class Font:
    def __init__(self, font_path: str, font_color: str | tuple):
        self.characters, self.letterSpacing, self.lineHeight = load_font_image(font_path, font_color)
        self.fontOrder = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
                          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                          'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3',
                          '4', '5', '6', '7', '8', '9', '0', '.', ',', '-', ':', '+', '\\', '!', '¡', '¿', '?', '(',
                          ')', '/', '_', '=', '[', ']', '*', '"', '<', '>', ':', '%', '$', '@', 'á', 'é', 'í', 'ó', 'ú']
        self.spaceWidth = self.letterSpacing[0]
        self.baseSpacing = 1
        self.lineSpacing = 2

    def width(self, text: str):
        text_width = 0
        for char in text:
            if char == ' ':
                text_width += self.spaceWidth + self.baseSpacing
            else:
                text_width += self.letterSpacing[self.fontOrder.index(char)] + self.baseSpacing
        return text_width

    def render(self, text, surf, loc, line_width=0):
        x_offset = 0
        y_offset = 0
        if line_width != 0:
            spaces = []
            x = 0
            for i, char in enumerate(text):
                if char == '\n':
                    continue
                if char == ' ':
                    spaces.append((x, i))
                    x += self.spaceWidth + self.baseSpacing
                else:
                    x += self.letterSpacing[self.fontOrder.index(char)] + self.baseSpacing
            line_offset = 0
            for i, space in enumerate(spaces):
                if (space[0] - line_offset) > line_width:
                    line_offset += spaces[i - 1][0] - line_offset
                    if i != 0:
                        text = text[:spaces[i - 1][1]] + '\n' + text[spaces[i - 1][1] + 1:]
        for char in text:
            if char not in ['\n', ' ']:
                surf.blit(self.characters[self.fontOrder.index(char)], (loc[0] + x_offset, loc[1] + y_offset))
                x_offset += self.letterSpacing[self.fontOrder.index(char)] + self.baseSpacing
            elif char == ' ':
                x_offset += self.spaceWidth + self.baseSpacing
            else:
                y_offset += self.lineSpacing + self.lineHeight
                x_offset = 0
