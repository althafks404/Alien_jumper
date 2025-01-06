import pygame

class Loader:
    def load_image(path):
        BASE_IMAGE_PATH = 'Alien_runner/graphics'
        image = pygame.image.load(BASE_IMAGE_PATH + path).convert_alpha()
        return image
    
    def load_font(path):
        BASE_FONT_PATH = 'Alien_runner/font/'
        font = pygame.font.Font(BASE_FONT_PATH + path,50)
        return font
    def load_sound(path):
        BASE_MUSIC_PATH = 'Alien_runner/audio/'
        audio = pygame.mixer.Sound(BASE_MUSIC_PATH + path)
        return audio