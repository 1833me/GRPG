import pygame
import random
import Player
import walls
import baddie

class RPGData:

    def __init__(self,width,height,frame_rate):
        self.width  = width
        self.height = height
        self.background_color = (0,0,0)
        self.speed = 3
        self.player = Player.Player(self.width/2,self.height/2,10,10)
        self.walls = walls.Walls(self.width,self.height)
        self.baddies = []
        self.baddies.append(baddie.Baddie(self.width-100,100,20,20))
        return

    def evolve(self, keys, newkeys, buttons, newbuttons, mouse_position):

        if self.player.alive:
            s_x = self.player.x + self.player.width
            s_y = self.player.y + ((self.player.height + self.player.sword_height)/2)
            s_w = self.player.sword_width
            s_h = self.player.sword_height
            if pygame.K_UP in keys and self.player.y >= 0:
                self.player.move_y(-1 * self.speed)
                if self.walls.hitRectangle(self.player.x,self.player.y,self.player.width,self.player.height):
                    self.player.move_y(1 * self.speed)
            if pygame.K_DOWN in keys and self.player.y <= self.height-self.player.height:
                self.player.move_y(self.speed)
                if self.walls.hitRectangle(self.player.x,self.player.y,self.player.width,self.player.height):
                    self.player.move_y(-1 * self.speed)
            if pygame.K_LEFT in keys and self.player.x >= 0:
                self.player.move_x(-1 * self.speed)
                if self.walls.hitRectangle(self.player.x,self.player.y,self.player.width,self.player.height):
                    self.player.move_x(self.speed)
            if pygame.K_RIGHT in keys and self.player.x <= self.width-self.player.width:
                self.player.move_x(self.speed)
                if self.walls.hitRectangle(self.player.x,self.player.y,self.player.width,self.player.height):
                    self.player.move_x(-1 * self.speed)
            if pygame.K_SPACE in keys:
                
                if not self.walls.hitRectangle(s_x,s_y,s_w,s_h):
                    self.player.sword = True
            if pygame.K_SPACE not in keys:
                self.player.sword = False
                
            if self.player.sword:
                for b in self.baddies:
                    if b.hitRectangle(s_x,s_y,s_w,s_h):
                        b.setAlive(False)
        return

    def draw(self,surface):
        player_value = False
        rect = pygame.Rect(0,0,self.width,self.height)
        surface.fill(self.background_color,rect )
        self.walls.draw(surface)
        s_x = self.player.x + self.player.width
        s_y = self.player.y + ((self.player.height + self.player.sword_height)/2)
        s_w = self.player.sword_width
        s_h = self.player.sword_height
        if not self.walls.hitRectangle(s_x,s_y,s_w,s_h):
            value = True
        self.player.draw(surface,value)
        for b in self.baddies:
            b.draw(surface,False)
        return
    
    def drawTextLeft(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return

    def drawTextRight(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomright = (x, y)
        surface.blit(textobj, textrect)
        return
