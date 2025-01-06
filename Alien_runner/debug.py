import pygame

pygame.init()
font = pygame.font.Font(None,30)

def debug(info,y = 10, x = 10):
    dispaly_surf = pygame.display.get_surface()
    debug_surf   = font.render(str(info),True,'Black')
    debug_rect   = dispaly_surf.get_rect(topleft = (x , y))
    pygame.draw.rect(dispaly_surf,'Black',debug_rect)
    dispaly_surf.blit(debug_surf,debug_rect)
    