import sys
import random
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def setup():
    # Make the board
    print("Board")
    board = QGroupBox(mainWindow)
    board.resize(480, 480)
    
    # center the board vertically
    vertCenter = QVBoxLayout(mainWindow)
    vertCenter.addWidget(board)
    
    boardGrid = QGridLayout(board)
    
    print("End Board")
    
    # Pieces
    # Set up pieces and place them on the grid
    
    print("Pieces")
    def lightRookLeftClick(self):
        print("light rook from left clicked")
    pieceLightRookLeft = QLabel(mainWindow)
    pieceLightRookLeft.setPixmap(QPixmap("images/light-rook.png"))
    pieceLightRookLeft.mouseReleaseEvent = lightRookLeftClick
    def lightKnightLeftClick(self):
        print("light knight from left clicked")
    pieceLightKnightLeft = QLabel(mainWindow)
    pieceLightKnightLeft.setPixmap(QPixmap("images/light-knight.png"))
    pieceLightKnightLeft.mouseReleaseEvent = lightKnightLeftClick
    def lightBishopLeftClick(self):
        print("light bishop from left clicked")
    pieceLightBishopLeft = QLabel(mainWindow)
    pieceLightBishopLeft.setPixmap(QPixmap("images/light-bishop.png"))
    pieceLightBishopLeft.mouseReleaseEvent = lightBishopLeftClick
    
    def lightQueenLeftClick(self):
        print("light queen clicked")
    pieceLightQueen = QLabel(mainWindow)
    pieceLightQueen.setPixmap(QPixmap("images/light-queen.png"))
    pieceLightQueen.mouseReleaseEvent = lightQueenLeftClick
    def lightKingLeftClick(self):
        print("light king clicked")
    pieceLightKing = QLabel(mainWindow)
    pieceLightKing.setPixmap(QPixmap("images/light-king.png"))
    pieceLightKing.mouseReleaseEvent = lightKingLeftClick
    
    def lightBishopRightClick(self):
        print("light bishop from right clicked")
    pieceLightBishopRight = QLabel(mainWindow)
    pieceLightBishopRight.setPixmap(QPixmap("images/light-bishop.png"))
    pieceLightBishopRight.mouseReleaseEvent = lightBishopRightClick
    def lightRookRightClick(self):
        print("light rook from right clicked")
    pieceLightRookRight = QLabel(mainWindow)
    pieceLightRookRight.setPixmap(QPixmap("images/light-rook.png"))
    pieceLightRookRight.mouseReleaseEvent = lightRookRightClick
    def lightKnightRightClick(self):
        print("light knight from right clicked")
    pieceLightKnightRight = QLabel(mainWindow)
    pieceLightKnightRight.setPixmap(QPixmap("images/light-knight.png"))
    pieceLightKnightRight.mouseReleaseEvent = lightKnightRightClick
    
    def lightPawn1Click(self):
        print("light pawn 1 clicked")
    pieceLightPawn1 = QLabel(mainWindow)
    pieceLightPawn1.setPixmap(QPixmap("images/light-pawn.png"))
    pieceLightPawn1.mouseReleaseEvent = lightPawn1Click
    def lightPawn2Click(self):
        print("light pawn 2 clicked")
    pieceLightPawn2 = QLabel(mainWindow)
    pieceLightPawn2.setPixmap(QPixmap("images/light-pawn.png"))
    pieceLightPawn2.mouseReleaseEvent = lightPawn2Click
    def lightPawn3Click(self):
        print("light pawn 3 clicked")
    pieceLightPawn3 = QLabel(mainWindow)
    pieceLightPawn3.setPixmap(QPixmap("images/light-pawn.png"))
    pieceLightPawn3.mouseReleaseEvent = lightPawn3Click
    def lightPawn4Click(self):
        print("light pawn 4 clicked")
    pieceLightPawn4 = QLabel(mainWindow)
    pieceLightPawn4.setPixmap(QPixmap("images/light-pawn.png"))
    pieceLightPawn4.mouseReleaseEvent = lightPawn4Click
    def lightPawn5Click(self):
        print("light pawn 5 clicked")
    pieceLightPawn5 = QLabel(mainWindow)
    pieceLightPawn5.setPixmap(QPixmap("images/light-pawn.png"))
    pieceLightPawn5.mouseReleaseEvent = lightPawn5Click
    def lightPawn6Click(self):
        print("light pawn 6 clicked")
    pieceLightPawn6 = QLabel(mainWindow)
    pieceLightPawn6.setPixmap(QPixmap("images/light-pawn.png"))
    pieceLightPawn6.mouseReleaseEvent = lightPawn6Click
    def lightPawn7Click(self):
        print("light pawn 7 clicked")
    pieceLightPawn7 = QLabel(mainWindow)
    pieceLightPawn7.setPixmap(QPixmap("images/light-pawn.png"))
    pieceLightPawn7.mouseReleaseEvent = lightPawn7Click
    def lightPawn8Click(self):
        print("light pawn 8 clicked")
    pieceLightPawn8 = QLabel(mainWindow)
    pieceLightPawn8.setPixmap(QPixmap("images/light-pawn.png"))
    pieceLightPawn8.mouseReleaseEvent = lightPawn8Click
    
    # dark
    print("dark")
    def darkRookLeftClick(self):
        print("dark rook from left clicked")
    pieceDarkRookLeft = QLabel(mainWindow)
    pieceDarkRookLeft.setPixmap(QPixmap("images/dark-rook.png"))
    pieceDarkRookLeft.mouseReleaseEvent = darkRookLeftClick
    def darkKnightLeftClick(self):
        print("dark knight from left clicked")
    pieceDarkKnightLeft = QLabel(mainWindow)
    pieceDarkKnightLeft.setPixmap(QPixmap("images/dark-knight.png"))
    pieceDarkKnightLeft.mouseReleaseEvent = darkKnightLeftClick
    def darkBishopLeftClick(self):
        print("dark bishop from left clicked")
    pieceDarkBishopLeft = QLabel(mainWindow)
    pieceDarkBishopLeft.setPixmap(QPixmap("images/dark-bishop.png"))
    pieceDarkBishopLeft.mouseReleaseEvent = darkBishopLeftClick
    
    def darkQueenLeftClick(self):
        print("dark queen clicked")
    pieceDarkQueen = QLabel(mainWindow)
    pieceDarkQueen.setPixmap(QPixmap("images/dark-queen.png"))
    pieceDarkQueen.mouseReleaseEvent = darkQueenLeftClick
    def darkKingLeftClick(self):
        print("dark king clicked")
    pieceDarkKing = QLabel(mainWindow)
    pieceDarkKing.setPixmap(QPixmap("images/dark-king.png"))
    pieceDarkKing.mouseReleaseEvent = darkKingLeftClick
    
    def darkBishopRightClick(self):
        print("dark bishop from right clicked")
    pieceDarkBishopRight = QLabel(mainWindow)
    pieceDarkBishopRight.setPixmap(QPixmap("images/dark-bishop.png"))
    pieceDarkBishopRight.mouseReleaseEvent = darkBishopRightClick
    def darkRookRightClick(self):
        print("dark rook from right clicked")
    pieceDarkRookRight = QLabel(mainWindow)
    pieceDarkRookRight.setPixmap(QPixmap("images/dark-rook.png"))
    pieceDarkRookRight.mouseReleaseEvent = darkRookRightClick
    def darkKnightRightClick(self):
        print("dark knight from right clicked")
    pieceDarkKnightRight = QLabel(mainWindow)
    pieceDarkKnightRight.setPixmap(QPixmap("images/dark-knight.png"))
    pieceDarkKnightRight.mouseReleaseEvent = darkKnightRightClick
    
    def darkPawn1Click(self):
        print("dark pawn 1 clicked")
    pieceDarkPawn1 = QLabel(mainWindow)
    pieceDarkPawn1.setPixmap(QPixmap("images/dark-pawn.png"))
    pieceDarkPawn1.mouseReleaseEvent = darkPawn1Click
    def darkPawn2Click(self):
        print("dark pawn 2 clicked")
    pieceDarkPawn2 = QLabel(mainWindow)
    pieceDarkPawn2.setPixmap(QPixmap("images/dark-pawn.png"))
    pieceDarkPawn2.mouseReleaseEvent = darkPawn2Click
    def darkPawn3Click(self):
        print("dark pawn 3 clicked")
    pieceDarkPawn3 = QLabel(mainWindow)
    pieceDarkPawn3.setPixmap(QPixmap("images/dark-pawn.png"))
    pieceDarkPawn3.mouseReleaseEvent = darkPawn3Click
    def darkPawn4Click(self):
        print("dark pawn 4 clicked")
    pieceDarkPawn4 = QLabel(mainWindow)
    pieceDarkPawn4.setPixmap(QPixmap("images/dark-pawn.png"))
    pieceDarkPawn4.mouseReleaseEvent = darkPawn4Click
    def darkPawn5Click(self):
        print("dark pawn 5 clicked")
    pieceDarkPawn5 = QLabel(mainWindow)
    pieceDarkPawn5.setPixmap(QPixmap("images/dark-pawn.png"))
    pieceDarkPawn5.mouseReleaseEvent = darkPawn5Click
    def darkPawn6Click(self):
        print("dark pawn 6 clicked")
    pieceDarkPawn6 = QLabel(mainWindow)
    pieceDarkPawn6.setPixmap(QPixmap("images/dark-pawn.png"))
    pieceDarkPawn6.mouseReleaseEvent = darkPawn6Click
    def darkPawn7Click(self):
        print("dark pawn 7 clicked")
    pieceDarkPawn7 = QLabel(mainWindow)
    pieceDarkPawn7.setPixmap(QPixmap("images/dark-pawn.png"))
    pieceDarkPawn7.mouseReleaseEvent = darkPawn7Click
    
    def showAvailMoves(pieceType, gridX, gridY, side):
        if pieceType == "pawn":
            if side == "light":
                if gridY == 6:
                    availMoves = [gridY - 1, gridY - 2]
                    return availMoves
                else:
                    availMoves = [gridY - 1]
                    return availMoves
            if side == "dark":
                if gridY == 1:
                    availMoves = [gridY + 1, gridY + 2]
                    return availMoves
                else:
                    availMoves = [gridY - 1]
                    return availMoves
    
    def pieceClick(pieceType, gridX, gridY, side):
        print("piece Clicked")
        print(side + " " + pieceType + " at " + str(gridX) + " " + str(gridY))
        availMoves = showAvailMoves(pieceType, gridX, gridY, side)
        print(availMoves)
    pieceDarkPawn8 = QLabel(mainWindow)
    pieceDarkPawn8.setPixmap(QPixmap("images/dark-pawn.png"))
    pieceDarkPawn8.mouseReleaseEvent = lambda: pieceClick("pawn", 7, 1, "dark")
    pieceDarkPawn8.mouseReleaseEvent = darkPawn7Click("test")
    
    # set pieces on grid
    def positionPieces():
        boardGrid.addWidget(pieceLightRookLeft, 7, 0)
        boardGrid.addWidget(pieceLightKnightLeft, 7, 1)
        boardGrid.addWidget(pieceLightBishopLeft, 7, 2)
        
        boardGrid.addWidget(pieceLightQueen, 7, 3)
        boardGrid.addWidget(pieceLightKing, 7, 4)
        
        boardGrid.addWidget(pieceLightBishopRight, 7, 5)
        boardGrid.addWidget(pieceLightKnightRight, 7, 6)
        boardGrid.addWidget(pieceLightRookRight, 7, 7)
        
        boardGrid.addWidget(pieceLightPawn1, 6, 0)
        boardGrid.addWidget(pieceLightPawn2, 6, 1)
        boardGrid.addWidget(pieceLightPawn3, 6, 2)
        boardGrid.addWidget(pieceLightPawn4, 6, 3)
        boardGrid.addWidget(pieceLightPawn5, 6, 4)
        boardGrid.addWidget(pieceLightPawn6, 6, 5)
        boardGrid.addWidget(pieceLightPawn7, 6, 6)
        boardGrid.addWidget(pieceLightPawn8, 6, 7)
        
        #dark
        
        boardGrid.addWidget(pieceDarkRookLeft, 0, 0)
        boardGrid.addWidget(pieceDarkKnightLeft, 0, 1)
        boardGrid.addWidget(pieceDarkBishopLeft, 0, 2)
        
        boardGrid.addWidget(pieceDarkQueen, 0, 3)
        boardGrid.addWidget(pieceDarkKing, 0, 4)
        
        boardGrid.addWidget(pieceDarkBishopRight, 0, 5)
        boardGrid.addWidget(pieceDarkKnightRight, 0, 6)
        boardGrid.addWidget(pieceDarkRookRight, 0, 7)
        
        boardGrid.addWidget(pieceDarkPawn1, 1, 0)
        boardGrid.addWidget(pieceDarkPawn2, 1, 1)
        boardGrid.addWidget(pieceDarkPawn3, 1, 2)
        boardGrid.addWidget(pieceDarkPawn4, 1, 3)
        boardGrid.addWidget(pieceDarkPawn5, 1, 4)
        boardGrid.addWidget(pieceDarkPawn6, 1, 5)
        boardGrid.addWidget(pieceDarkPawn7, 1, 6)
        boardGrid.addWidget(pieceDarkPawn8, 1, 7)
    positionPieces()
    
    # set up board so that it has equal spacing and same size cells
    boardGrid.setHorizontalSpacing(0)
    boardGrid.setVerticalSpacing(0)
    
    for i in range(8):
        boardGrid.setRowMinimumHeight(i, 60)
        boardGrid.setColumnMinimumWidth(i, 60)
        
        boardGrid.setColumnStretch(i, 0)
        boardGrid.setRowStretch(i, 0)
        print("loop")
    print("out of loop")
    

def chess():
    print("Chess")
    setup()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QWidget()
    mainWindow.resize(480, 480)
    # wanted dimensions below. solution to row stretching in board required
    #mainWindow.resize(480, 680)
    mainWindow.setWindowTitle("PyChess")
    
    chess()
    
    mainWindow.show()
    sys.exit(app.exec_())