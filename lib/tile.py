import pygame as pg

pg.init()

class tile:
    def __init__(self, x, y, w, h, sprite, tag, static=True, momentum=[0,0], script=None):
        self.rect = pg.Rect(x, y, w, h)
        self.momentum = momentum
        self.collisions = []
        self.sprite = sprite
        self.tag = tag
        self.static = static
        self.script = script
    def update(self, tiles, dt):
        if not self.script == None: self.script()
        collision_types = { 'top': False, 'bottom': False, 'right': False, 'left': False }
        self.rect.x += (self.momentum[0] * dt)
        for tile in tiles:
            if tile == self: continue
            if tile.rect.colliderect(self.rect):
                if self.momentum[0] > 0:
                    self.rect.x = tile.rect.x - tile.rect.width
                    collision_types['right'] = True
                elif self.momentum[0] < 0:
                    self.rect.x = tile.rect.x + tile.rect.width
                    collision_types['left'] = True
        self.rect.y += (self.momentum[1] * dt)
        for tile in tiles:
            if tile == self: continue
            if tile.rect.colliderect(self.rect):
                if self.momentum[1] > 0:
                    self.rect.y = tile.rect.y - tile.rect.height
                    collision_types['bottom'] = True
                elif self.momentum[1] < 0:
                    self.rect.y = tile.rect.y + tile.rect.height
                    collision_types['top'] = True
        if not self.static:
            if collision_types['bottom']:
                self.momentum[1] = 0
                self.isFalling = False
            else:
                self.isFalling = True
                if self.momentum[1] < 10:
                    self.momentum[1] += 1
    def render(self, display):
        display.blit(self.sprite, (self.rect.x, self.rect.y))