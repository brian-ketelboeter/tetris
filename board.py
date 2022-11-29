import pygame
pygame.init()
#from tetris import constants as foo
#import constants
"""the grid system: '0' means unfilled, '1' means filled. each square on the board will either be a 0 or 1 depending on where it is filled or not"""
class Board:
    def __init__(self,constants,blocked_squares):
        #self.grid=[[0 for x in range(width)] for y in range(height)]
        self.constants= constants
        self.blocked_squares=blocked_squares
    
    def draw_cubes(self,win):
        win.fill(self.constants.BLACK)
        row=0
        value = self.constants.MARGIN
        while row in range(16):
            column = 0
            square_top =self.constants.MARGIN+row*(self.constants.SQUARESIZE+ value)
        
            while column in range(10):
                square_left=self.constants.MARGIN +column*(self.constants.SQUARESIZE +value)
                
                mySquare=pygame.Rect(square_left,square_top,self.constants.SQUARESIZE,self.constants.SQUARESIZE)
                color=self.constants.WHITE
                if (square_left,square_top) in self.blocked_squares:
                    color= self.constants.BLUE
        
                pygame.draw.rect(win,color,mySquare)
                #value= column*constants.MARGIN
                column+=1
            row+=1
        #i=0
        #while i <= WIDTH:
        #    pygame.draw.line(win,WHITE,(i,0),(i,HEIGHT-10))
        #    i+=50
    
    def create_piece(self):
        pass
    
    def get_position(self,location):
        """transforms board coordinates to grid number"""
        pass

    def get_polarity(self,location):
        """checks polarity of location"""
        pass

    def update_polarity(self,location):
        """updates polarity of location"""
        pass
"""
size=(constants.WIDTH,constants.HEIGHT)
screen=pygame.display.set_mode(size)
done=False
clock=pygame.time.Clock()
board=Board()
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
    board.draw_cubes(screen)
    pygame.display.flip()
"""



