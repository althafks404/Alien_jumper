import pygame
from util import Loader
def menu_screen(screen,height,width,font,score,high_score,game_state):
    if game_state:
        pass
    else:    
        screen.fill((94,129,162))
        player_image = Loader.load_image('/Player/player_walk_1.png')
        player_image = pygame.transform.rotozoom(player_image,0,2)
        player_image_rect = player_image.get_rect(center = (height / 2 , width / 2))
        screen.blit(player_image,player_image_rect)
    
        menu_score = font.render(f'Score:{score}','False',(111,196,169))
        menu_score_rect = menu_score.get_rect(center = (height / 2, 95))
        screen.blit(menu_score,menu_score_rect)

        game_name = font.render('Alien Runner',False,(111,196,169))
        game_name_rect = game_name.get_rect(center = (height / 2,50))
        screen.blit(game_name,game_name_rect)

        high_score = font.render(f'High Score:{high_score}','False',(111,196,169))
        high_score_rect = high_score.get_rect(center = (height / 2 , width / 2 + 110))
        screen.blit(high_score,high_score_rect)

        hint = font.render('Press {"Space"} to Play',False,'Black')
        hint_rect = hint.get_rect(center = (height / 2, width / 2 + 150))
        screen.blit(hint,hint_rect)


