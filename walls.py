import pygame

class Walls():

    def __init__(self,width,height):
        self.wall_list = []
        fin = open('walls.blrb','rb')
        
        for line in fin:
            for char in line:
                if char == '1' or char == '0':
                    self.wall_list.append(int(char))
        self.block_width = 20
        self.block_height = 20
        self.color = (0,0,255)
        self.not_color = (0,0,0)
        self.width = width/self.block_width
        self.height = height/self.block_height
        fin.close()
        return

    
    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if self.wall_list[y*self.width+x] == 1:
                    color = self.color
                else:
                    color = self.not_color
                rect = pygame.Rect( x*self.block_width, y*self.block_height, self.block_width, self.block_height )
                pygame.draw.rect(surface, color, rect)
        return     

    def hitRectangle(self, x2, y2, w2, h2):
        for y in range(self.height):
            for x in range(self.width):
                if self.wall_list[y*self.width+x] == 1:
                    if( ((x*self.block_width + self.block_width) >= x2) and
                        (x*self.block_width <= x2 + w2) ):
                        if( ((y*self.block_height + self.block_height) >= y2) and
                            (y*self.block_height <= y2 + h2)):
                            return True
                    
        return False
        
