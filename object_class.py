import pygame

class Basic_object(pygame.sprite.Sprite):
    """
    """
    def __init__(self, sprite, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.center = center


        