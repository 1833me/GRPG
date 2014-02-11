import pygame
import game_mouse
import GRPGData

class RPG(game_mouse.Game):

    def __init__(self, width, height, frame_rate):
        self.newGame(width,height,frame_rate)
        return
    
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        self.data.evolve(keys, newkeys, buttons, newbuttons, mouse_position)
        return

    def paint(self, surface):
        self.data.draw(surface)
        return

    
    def newGame(self,width, height, frame_rate):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate
        game_mouse.Game.__init__(self, "Generic RPG", width, height, frame_rate)   
        self.data = GRPGData.RPGData(width,height,frame_rate)
        
        return

def main():
    pygame.font.init()
    c = RPG(600, 400, 30)
    c.main_loop()
    return
    
if __name__ == "__main__":
    main()

     
