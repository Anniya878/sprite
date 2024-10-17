import pygame
pygame.init()
screen = pygame.display.set_mode((700, 700))
class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("rocket.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
rocket = Player(350,350)
rocket_group = pygame.sprite.Group()
rocket_group.add(rocket)                 
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("light pink")
    rocket_group.draw(screenA)

    pygame.display.update()
   