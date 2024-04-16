import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Test Pygame Example")
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (255,0,0), (100,100), 30,0)
    pygame.display.flip()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()