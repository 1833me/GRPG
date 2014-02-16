import pygame

class Baddie():

    def __init__(self,x,y,width,height,color=(255,0,0),sword_color = (255,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sword_width = 10
        self.sword_height = 3
        self.alive = True
        self.color = color
        self.sword = False
        self.sword_color = sword_color
        return

    def move_x(self,dx):
        self.x += dx
        return

    def move_y(self,dy):
        self.y += dy
        return
    
    def draw(self, surface,value):
        if not value:
            self.sword = False
        if self.alive == True:
            rect = pygame.Rect( self.x, self.y, self.width, self.height )
            pygame.draw.rect(surface, self.color, rect)
            if self.sword:
                rect = pygame.Rect( self.x+self.width, self.y + ((self.height+self.sword_height)/2), self.sword_width, self.sword_height )
                pygame.draw.rect(surface, self.sword_color, rect)
        return

    def setAlive(self,alive):
        self.alive = alive
        return

    def hitRectangle(self, x2, y2, w2, h2):
        if( ((self.x + self.width) >= x2) and
            (self.x <= x2 + w2) ):
            if( ((self.y + self.height) >= y2) and
                (self.y <= y2 + h2)):
                return True               
        return False
