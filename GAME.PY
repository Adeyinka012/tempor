import pygame
pygame.init()
SCREEN_WIDTH=500
SCREEN_HIEGHT=500
display_surface=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption("Adding image and background image")

background_image=pygame.transform.scale(
    pygame.image.load("car.jpeg").convert(),
    (SCREEN_WIDTH, SCREEN_HIEGHT)
)
player=pygame.transform.scale(
    pygame.image.load("car.jpeg").convert_alpha(),(200,200)
)
player_rect=player.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HIEGHT//2-30))
text=pygame.font.Font(None,36).render("Welcome to the game! ", True,(254, 294, 255))