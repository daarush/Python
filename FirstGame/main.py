import pygame

pygame.init()


# Classes
class Player(object):
    def __int__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.grounded = False
        self.left = False
        self.right = False
        self.vel = 5


# Varibles
application = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()

# Player Vars.
playerWidth = 25
playerHeight = 25
playerSpeed = 10
playerX = 1200 / 2 - playerWidth
playerY = 600 / 2 - playerHeight

player = Player(playerX, playerY, playerHeight, playerWidth)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= playerSpeed

    # if keys[pygame.K_a]:
    # playerX -= playerSpeed

    # pygame.draw.rect(application, "white", (playerX, playerY, playerWidth, playerHeight))
    pygame.display.update()
    clock.tick(60)
