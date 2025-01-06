import pygame
from util import Loader
from random import randint
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        ##########################
        #snail
        if type == 'fly':
            fly_frame_1                     = Loader.load_image('/Fly/Fly1.png')
            fly_frame_2                     = Loader.load_image('/Fly/Fly2.png')
            self.frame                      = [fly_frame_1,fly_frame_2]
            obstacle_y_pos                  = 210
        else:
            snail_frame_1                   = Loader.load_image('/snail/snail1.png')
            snail_frame_2                   = Loader.load_image('/snail/snail2.png')
            self.frame                      = [snail_frame_1,snail_frame_2]
            obstacle_y_pos                  = 300       
            
            
        self.frame_index            = 0
        self.image                  = self.frame[self.frame_index]
        self.rect                   = self.image.get_rect(midbottom = (randint(900,1100),obstacle_y_pos))

    def obstacle_animation(self):
         self.frame_index += 0.1
         if self.frame_index >= len(self.frame):
             self.frame_index = 0
         self.image = self.frame[int(self.frame_index)]

    def delete_obstacle(self):
        if self.rect.x <= -100:
            self.kill()
    
    def update(self):
        self.rect.x -= 6    
        self.obstacle_animation()
        self.delete_obstacle()



        

