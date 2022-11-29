import pygame,sys
import tetris.constants as const
from tetris import board, piece
WIN= pygame.display.set_mode((const.WIDTH,const.HEIGHT))
"""this version will now store the last coordinates of the shape and store them in a list. The list will be passed to the new board
and those coordinates will generate squares which will then be colored in the new board"""
"""add capacity to erase complete lines"""
pygame.display.set_caption('Tetris')
#my_board=board3.Board(const)
FPS=60
def main():
    score = 0
    blocked_squares = []
    run = True
    clock=pygame.time.Clock()
    
    
    while run:
        my_board=board.Board(const,blocked_squares)
        myPiece= piece.Piece(WIN,blocked_squares)

        while myPiece.stop == False:
            my_board.draw_cubes(WIN)
            myPiece.generate_piece()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run=False
                elif event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_RIGHT:
                        myPiece.move_piece_right()
                    elif event.key==pygame.K_LEFT:
                        myPiece.move_piece_left()
                    elif event.key==pygame.K_UP:
                        myPiece.rotate_piece_up()
                    elif event.key== pygame.K_DOWN:
                        myPiece.rotate_piece_down()
            clock.tick(1)
            pygame.display.flip()
            myPiece.move_piece_down()
            if myPiece.stop== True:
                blocked_squares.append((myPiece.get_loc_X(),myPiece.get_loc_Y()))
                blocked_squares.append((myPiece.get_first_piece_X(),myPiece.get_first_piece_Y()))
                blocked_squares.append((myPiece.get_second_piece_X(),myPiece.get_second_piece_Y()))
                blocked_squares.append((myPiece.get_third_piece_X(),myPiece.get_third_piece_Y()))
                #print(blocked_squares)
                if (myPiece.get_loc_Y()<=const.MARGIN
                    or myPiece.get_first_piece_Y()<=const.MARGIN
                    or myPiece.get_second_piece_Y()<=const.MARGIN
                    or myPiece.get_third_piece_Y()<=const.MARGIN):
                    #print("I got here!")
                    pygame.display.quit()
                    pygame.quit()
                    print(score)
                    sys.exit()
                else:
                    Rows=[]
                    for row in range(5,const.HEIGHT,55):
                        filled_spaces=[]
                        for column in range(5,const.WIDTH,55):
                            if (column,row) in blocked_squares:
                                filled_spaces.append('f')
                                """indicates square is filled"""
                            #print(filled_spaces)
                        if len(filled_spaces)==const.COLS:
                            score+=100
                            print(score)
                            for column in range(5,const.WIDTH,55):
                                blocked_squares.remove((column,row))
                                #adjusting filled squares above filled row to move down
                                for row1 in range(5,row,55):
                                    if (column,row1) in blocked_squares:
                                        blocked_squares.append((column,row1+55))
                                        blocked_squares.remove((column,row1))
                                        
    pygame.QUIT

main()