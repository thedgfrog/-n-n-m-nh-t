from setting import *
class AllSprites(pygame.sprite.Group):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.display_surface=pygame.display.get_surface()
        self.offset=pygame.Vector2()# set up camera through vector2

    def draw(self,target_pos):
        self.offset.x=-(target_pos[0]-W_WIDTH /2)
        self.offset.y=-(target_pos[1]-W_HEIGHT/2)
        ground_sprites=[sprite for sprite in self if hasattr(sprite,'ground')]
        object_sprites=[sprite for sprite in self if not hasattr(sprite,'ground')]

        for layer in [ground_sprites,object_sprites]:
            for sprite in sorted(layer,key=lambda sprite:sprite.rect.centery):
                self.display_surface.blit(sprite.image,sprite.rect.topleft+self.offset)