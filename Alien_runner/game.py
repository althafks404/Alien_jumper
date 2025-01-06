import pygame
from sys import exit
from assets import Assets
from util import Loader
import menu
from player import Player
from obstacle import Obstacle
from random import randint,choice
from debug import debug

def sprite_collition():    #check if the player rect and obstacle rect sprite class has been collided 
    if pygame.sprite.spritecollide(player.sprite,obstacle,False):
        obstacle.empty()
        return False    # if true the game active become false and show menu screen
    else:return True

def display_score():    # display high score
    current_score = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'Score:{current_score}',False,'Black')
    score_rect    = score_surface.get_rect(center = (height / 2, 50))
    screen.blit(score_surface,score_rect)
    return current_score

def high_score(high_score,current_score): #display high score
    if current_score > high_score:
        high_score = current_score
        return high_score

class HighScore():
    def __init__(self,current_socre,high_score):
        self.current_score = current_score
        self.high_score    = high_score
        def highscore(self):
            if self.current_score > self.high_score:
                high_score = current_score
        pass
##################################
#game initialization
pygame.init()  #initialzing the pygame
height , width             = 800,400 # screen height width
screen                     = pygame.display.set_mode((height,width)) # initializing the screen window
game_active                = False
current_score              = 0
clock                      = pygame.time.Clock()     #initialzation of clock object
current_score              = 0
start_time                 = 0  
highscore                  = 0
current_high_score         = 0
player_gravity             = 0 # player gravity when the player jump 
player                     = pygame.sprite.GroupSingle()   # assining the sprite player class to the player variablt . it is GroupSingle only has one Sprite
obstacle                   = pygame.sprite.Group()         # assining the sprite obstacle class to the obstacle variable . It is Group because it has more than one Sprite
bg_music                   = Assets.background_audio()
bg_music.set_volume(0.7)
bg_music.play(loops = -1)
###################################
#loading the assets
ground_image               = Assets.background_image()
sky_image                  = Assets.background_sky()
font                       = Assets.score_font()
###################################
#initalizing the sprite class 
player.add(Player())
###################################
#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)
obastacle_speed_timer = pygame.USEREVENT + 2
pygame.time.set_timer(obastacle_speed_timer,9000)
####################################
while True:
    # getting the user input using the event 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.exit()
            exit()

        if game_active:
            #triggering the timer event to choose from the choice
            if event.type == obstacle_timer:
                obstacle.add(Obstacle(choice(['fly','snail','snail','snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start_time = int(pygame.time.get_ticks() / 1000)   #clearing the score after game over
                game_active = True      
    
    #check wether game_active is true
    if game_active:
        #rendering the images to the screen
        screen.blit(ground_image,(0,300))
        screen.blit(sky_image,(0,0))
        current_score                    = display_score()
        current_high_score               = high_score(highscore,current_score)
        player.draw(screen)
        obstacle.draw(screen)
        player.update()
        obstacle.update()
        game_active                     = sprite_collition()
    else:
        #displaying the menu screen when the game is over or starting
        menu.menu_screen(screen,height,width,font,current_score,current_high_score,game_active)
    pygame.display.update()
    clock.tick(60)    # updating the frame , telling the main while loop to no go further than 60
