import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Type Trainer")

WHITE = (255, 255, 255)
BLACK = (0 , 0, 0)
FPS = 60

def draw_text():
    font = pygame.font.Font(None, 32)
    text = font.render("Test",True, BLACK)
    text_rect = text.get_rect()
    
    WIN.blit(text, text_rect)
    pygame.display.update()
    
    
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        WIN.fill(WHITE)
        
        draw_text()
        pygame.display.update()
        
    pygame.quit()

if __name__ == "__main__":
    main()