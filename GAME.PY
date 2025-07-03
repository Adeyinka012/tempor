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
text=pygame.font.Font(None,36).render("Welcome to the game! ", True,(255, 200, 255))
text_rect=text.get_rect(center=[SCREEN_WIDTH//2, SCREEN_HIEGHT//2+110])
def game_loop():
    Clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            display_surface.blit(background_image,(0,0))
            display_surface.blit(player,player_rect)
            display_surface.blit(text, text_rect)
            pygame.display.flip()
            Clock.tick(60)
        pygame.quit()
if __name__ == "__main__":
    game_loop()
