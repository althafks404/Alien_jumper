import pygame
from util import Loader
from assets import Assets
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1                       = Loader.load_image('/Player/player_walk_1.png')
        player_walk_2                       = Loader.load_image('/Player/player_walk_2.png')
        self.player_jump_img                = Loader.load_image('/Player/jump.png')
        self.jump_audio                     = Assets.jump_audio()
        self.jump_audio.set_volume(0.3)
        self.player_walk                    = [player_walk_1,player_walk_2]
        self.player_walk_animation_index    = 0
        self.image                          = self.player_walk[self.player_walk_animation_index]
        self.rect                           = self.image.get_rect(midbottom = (80,200))
        self.gravity                        = 0 
        self.jump_sound                     = 0 
    
    def walk_animation(self):
        if self.rect.bottom < 300:   # if the player is jump or the rect.bottom value is less than 300 then show the jump image
            self.image = self.player_jump_img
        else:
            self.player_walk_animation_index += 0.1
            if self.player_walk_animation_index >= len(self.player_walk):
                self.player_walk_animation_index = 0
            self.image = self.player_walk[int(self.player_walk_animation_index)]
    
    def jumping(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys [pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_audio.play()
            self.gravity = -20

    def update(self):
        self.walk_animation()
        self.player_input()
        self.jumping()