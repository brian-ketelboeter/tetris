#module generating pieces
"""introducing the rotation of pieces"""
import pygame
import random
class Piece:
    
    #pygame.__init__(self)
    def __init__(self, screen,blocked_squares):
        self.stop= False
        self.symmetry=0
        self.shape=random.randint(0,3)
        self.loc_X=225
        self.loc_Y=5
        self.first_X=self.first_piece_position_X()
        self.first_Y=self.first_piece_position_Y()

        self.second_X=self.second_piece_position_X()
        self.second_Y=self.second_piece_position_Y()

        self.third_X=self.third_piece_position_X()
        self.third_Y=self.third_piece_position_Y()

        #self.second_X=self.loc_X+(0,50)
        #self.third=self.loc+(50,50)
        self.screen=screen
        ###for the creation of the tetronimo
        self.object0= pygame.Rect(self.loc_X,self.loc_Y,50,50)
        self.object1=pygame.Rect(self.first_X,self.first_Y,50,50)
        self.object2=pygame.Rect(self.second_X,self.second_Y,50,50)
        self.object3=pygame.Rect(self.third_X,self.third_Y,50,50)
        self.blocked_squares=blocked_squares

    def first_piece_position_X(self):
        #if self.shape == 0:
        #    return self.loc_X+55
        
        #else:
        return self.loc_X
        
    def first_piece_position_Y(self):
        #if self.shape ==0:
        #    return self.loc_Y
        #else:
        return self.loc_Y +55
    
    def second_piece_position_X(self):
        """set initial X position for second piece"""
        if self.shape== 0:
            return self.loc_X +55
        elif self.shape==1:
            return self.loc_X
        elif self.shape ==2:
            return self.loc_X+110
        else:
            return self.loc_X-55
    
    def second_piece_position_Y(self):
        """sets initial Y position for second piece"""
        if self.shape==0:
            return self.loc_Y
        elif self.shape==1:
            return  self.loc_Y+110
        else:
            return self.loc_Y+55
    
    def third_piece_position_X(self):
        """sets initial X position for third piece"""
        if self.shape==1:
            return self.loc_X
        else:
            return self.loc_X+55
    
    def third_piece_position_Y(self):
        """sets initial Y position for third piece"""
        if self.shape ==1:
            return self.loc_Y+165
        else:
            return self.loc_Y+55
        
    
        
    def generate_piece(self):
        """creates the piece"""
        pygame.draw.rect(self.screen,(100,0,0),self.object0)
        pygame.draw.rect(self.screen,(0,100,0),self.object1)
        pygame.draw.rect(self.screen,(0,0,100),self.object2)
        pygame.draw.rect(self.screen,(100,100,100),self.object3)
    """get functions for X and Y coordinates of positions of each piece"""
    def get_loc_X(self):
        """get piece current location"""
        return self.object0.left
    def get_loc_Y(self):
        return self.object0.top
    def get_first_piece_X(self):
        return self.object1.left
    def get_first_piece_Y(self):
        return self.object1.top
    def get_second_piece_X(self):
        return self.object2.left
    def get_second_piece_Y(self):
        return self.object2.top
    def get_third_piece_X(self):
        return self.object3.left
    def get_third_piece_Y(self):
        return self.object3.top

    def move_piece_down(self):
        #if (self.object3.bottom>= 825) or (self.object2.bottom>= 825) or (self.object1.bottom>= 825) or (self.object0.bottom>= 825):
        #    self.stop = True
        #    pass
        for position in self.blocked_squares:
            if ((self.object3.left,self.object3.top+55)==position  
                or (self.object2.left,self.object2.top+55) ==position 
                or (self.object1.left,self.object1.top+55) == position 
                or (self.object0.left,self.object0.top+55) ==position):
                self.stop = True
        if self.stop== True:
            pass
        elif (self.object3.bottom>= 825) or (self.object2.bottom>= 825) or (self.object1.bottom>= 825) or (self.object0.bottom>= 825):
            self.stop = True
            pass

        else:  
            self.object0.y+=55
            self.object1.y+=55
            self.object2.y+=55
            self.object3.y+=55
        

    def move_piece_right(self):
        for position in self.blocked_squares:
            if (self.object0.x+55,self.object0.y)==position or (self.object1.x+55,self.object1.y)==position or (self.object2.x+55,self.object2.y)==position or (self.object3.x+55,self.object3.y)==position:
                return
        if (self.object3.right== 550) or (self.object2.right== 550) or (self.object1.right== 550) or (self.object0.right== 550):
            return
        else:
            self.object0.x=self.object0.x +55
            self.object1.x=self.object1.x +55
            self.object2.x=self.object2.x +55
            self.object3.x=self.object3.x +55

    def move_piece_left(self):
        if (self.object3.left== 5) or (self.object2.left== 5) or (self.object1.left== 5) or (self.object0.left== 5):
            return
        else:
            self.object0.x=self.object0.x -55
            self.object1.x=self.object1.x -55
            self.object2.x=self.object2.x -55
            self.object3.x=self.object3.x -55
    
    def change_symmetry(self):
        if self.shape==1:
            self.symmetry=(self.symmetry+1)%2
        else:
            self.symmetry=(self.symmetry+1)%4


    def rotate_piece_up(self):
        """up arrow rotation"""
        #self.change_symmetry()
        #print(self.symmetry)
        if self.shape==1:
            if self.symmetry==1:
                position_x,position_y=self.object0.x,self.object0.y
                self.object0.x,self.object0.y=position_x-55,position_y
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x+55,position_y
                self.object3.x,self.object3.y=position_x+110,position_y
                self.change_symmetry()
            else:
                position_x,position_y=self.object1.x,self.object1.y
                self.object0.x,self.object0.y=position_x,position_y
                self.object1.x,self.object1.y=position_x,position_y+55
                self.object2.x,self.object2.y=position_x,position_y+110
                self.object3.x,self.object3.y=position_x,position_y+165
                self.change_symmetry()
        elif self.shape==2:
            position_x,position_y= self.object0.x,self.object0.y
            if self.symmetry==0:
                #position_x,position_y= self.object0.x,self.object0.y
                self.object0.x,self.object0.y=position_x+55,position_y
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x,position_y+55
                self.object3.x,self.object3.y=position_x,position_y+110
                self.change_symmetry()
            elif self.symmetry==1:
                self.object0.x,self.object0.y=position_x,position_y+55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x-55,position_y
                self.object3.x,self.object3.y=position_x-110,position_y
                self.change_symmetry()
            elif  self.symmetry==2:
                self.object0.x,self.object0.y=position_x+55,position_y+55
                self.object1.x,self.object1.y=position_x,position_y+55
                self.object2.x,self.object2.y=position_x,position_y
                self.object3.x,self.object3.y=position_x,position_y-55
                self.change_symmetry()
            else:
                self.object0.x,self.object0.y=position_x,position_y-110
                self.object1.x,self.object1.y=position_x,position_y-55
                self.object2.x,self.object2.y=position_x+55,position_y-55
                self.object3.x,self.object3.y=position_x+110,position_y-55
                self.change_symmetry
        elif self.shape==3:
            position_x,position_y= self.object0.x,self.object0.y
            if self.symmetry==0:
                self.object0.x,self.object0.y= position_x+55,position_y+55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x,position_y+55
                self.object3.x,self.object3.y=position_x,position_y+110
                self.change_symmetry()
            elif self.symmetry==1:
                self.object0.x,self.object0.y= position_x-55,position_y+55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x-55,position_y
                self.object3.x,self.object3.y=position_x-110,position_y
                self.change_symmetry()
            elif self.symmetry==2:
                self.object0.x,self.object0.y= position_x-55,position_y-55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x,position_y-55
                self.object3.x,self.object3.y=position_x,position_y-110
                self.change_symmetry()
            else:
                self.object0.x,self.object0.y= position_x+55,position_y-55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x+55,position_y
                self.object3.x,self.object3.y=position_x+110,position_y
                self.change_symmetry()
    
    def rotate_piece_down(self):
        """down arrow rotation"""
        #self.change_symmetry()
        #print(self.symmetry)
        if self.shape==1:
            position_x,position_y=self.object0.x,self.object0.y
            if self.symmetry==1:
                self.object0.x,self.object0.y=position_x-55,position_y
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x+55,position_y
                self.object3.x,self.object3.y=position_x+110,position_y
                self.change_symmetry()
            else:
                position_x,position_y=self.object1.x,self.object1.y
                self.object0.x,self.object0.y=position_x,position_y
                self.object1.x,self.object1.y=position_x,position_y+55
                self.object2.x,self.object2.y=position_x,position_y+110
                self.object3.x,self.object3.y=position_x,position_y+165
                self.change_symmetry()
        elif self.shape==2:
            position_x,position_y= self.object0.x,self.object0.y
            if self.symmetry==0:
                #position_x,position_y= self.object0.x,self.object0.y
                self.object0.x,self.object0.y=position_x-55,position_y
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x,position_y-55
                self.object3.x,self.object3.y=position_x,position_y-110
                self.change_symmetry()
            elif self.symmetry==3:
                self.object0.x,self.object0.y=position_x+55,position_y-55
                self.object1.x,self.object1.y=position_x+55,position_y-110
                self.object2.x,self.object2.y=position_x,position_y-110
                self.object3.x,self.object3.y=position_x-55,position_y-110
                self.change_symmetry()
            elif  self.symmetry==2:
                self.object0.x,self.object0.y=position_x,position_y-55
                self.object1.x,self.object1.y=position_x-55,position_y-55
                self.object2.x,self.object2.y=position_x-55,position_y
                self.object3.x,self.object3.y=position_x-55,position_y+55
                self.change_symmetry()
            else:
                self.object0.x,self.object0.y=position_x-55,position_y
                self.object1.x,self.object1.y=position_x-55,position_y+55
                self.object2.x,self.object2.y=position_x,position_y+55
                self.object3.x,self.object3.y=position_x+55,position_y+55
                self.change_symmetry
        elif self.shape==3:
            position_x,position_y= self.object0.x,self.object0.y
            if self.symmetry==0:
                self.object0.x,self.object0.y= position_x+55,position_y+55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x,position_y+55
                self.object3.x,self.object3.y=position_x,position_y+110
                self.change_symmetry()
            elif self.symmetry==1:
                self.object0.x,self.object0.y= position_x-55,position_y+55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x-55,position_y
                self.object3.x,self.object3.y=position_x-110,position_y
                self.change_symmetry()
            elif self.symmetry==2:
                self.object0.x,self.object0.y= position_x-55,position_y-55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x,position_y-55
                self.object3.x,self.object3.y=position_x,position_y-110
                self.change_symmetry()
            else:
                self.object0.x,self.object0.y= position_x+55,position_y-55
                self.object1.x,self.object1.y=position_x,position_y
                self.object2.x,self.object2.y=position_x+55,position_y
                self.object3.x,self.object3.y=position_x+110,position_y
                self.change_symmetry()





            self.change_symmetry()
            return
        
            
            

