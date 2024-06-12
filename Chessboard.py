# ChessBoard
"""
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
"""
black_square = "\u25A0"
white_square = "\u25A1"
black_king = "\u265A"
black_queen = "\u265B"
black_rook = "\u265C"
black_bishop = "\u265D"
black_knight = "\u265E"
black_pawn = "\u265F"
white_king = "\u2654"
white_queen = "\u2655"
white_rook = "\u2656"
white_bishop = "\u2657"
white_knight = "\u2658"
white_pawn = "\u2659"
for i in range(0,8):
    
    for j in range(0,8):
        if i == 0:
            # Black pieces row
            if j == 0 or j == 7:
                print(black_rook, end= " ")
            elif j == 1 or j == 6:
                print(black_knight, end=" ")    
            elif j == 2 or j == 5:
                print(black_bishop, end=" ")
            elif j == 3:
                print(black_queen, end=" ")
            elif j ==4:
                print(black_king, end=" ")
            elif j%2 == 0:
                    print(black_square, end = " ")
            else:
                    print(white_square, end = " ")
        elif i == 1:
            #Black pawns
            print(black_pawn, end= " ")
        elif i == 6:
            # white pawns 
            print(white_pawn, end=" ")
        elif i == 7:
            # White pieces row
            if j == 0 or j == 7:
                print(white_rook, end= " ")
            elif j == 1 or j == 6:
                print(white_knight, end=" ")    
            elif j == 2 or j == 5:
                print(white_bishop, end=" ")
            elif j == 3:
                print(white_queen, end=" ")
            elif j ==4:
                print(white_king, end=" ")
            elif j%2 == 0:
                    print(black_square, end = " ")
            else:
                    print(white_square, end = " ")
        else:
            if i%2 == 0:
            #print(j%2, end =" ")
                if j%2 == 0:
                    print(black_square, end = " ")
                else:
                    print(white_square, end = " ")
            else:
           # print((j+1)%2, end = " ")
                if (j+1)%2 == 0:
                    print(black_square, end = " ")
                else:
                    print(white_square, end = " ")
            
    print()

