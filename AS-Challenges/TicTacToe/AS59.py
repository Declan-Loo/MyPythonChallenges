"""
AS59	
150	
TICTACTOE	
Make a game of tictactoe using a 2 dimensional Array
"""

#Draw the board
def DrawBoard():
    print(board[0][0],'|',board[0][1],'|',board[0][2])
    print('---------')
    print(board[1][0],'|',board[1][1],'|',board[1][2])
    print('---------')
    print(board[2][0],'|',board[2][1],'|',board[2][2])

#Check whether position is occupied
def CheckPosition(i,j):
    if board[i-1][j-1] == ' ':
        return True
    else:
        return False

#Check the results of the game
def CheckResults():
    global board, FinishGame
    # Horizontal winning condition
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " ":
        FinishGame = 'Yes'
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != " ":
        FinishGame = 'Yes'
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != " ":
        FinishGame = 'Yes'
        
    # Vertical Winning Condition
    elif board[0][0]== board[1][0] and board[1][0] == board[2][0] and board[0][0] != " ":
        FinishGame = 'Yes'
    elif board[0][1]== board[1][1] and board[1][1] == board[2][1] and board[0][1] != " ":
        FinishGame = 'Yes'
    elif board[0][2]== board[1][2] and board[1][2] == board[2][2] and board[0][2] != " ":
        FinishGame = 'Yes'
        
    # Diagonal Winning Condition
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != " ":
        FinishGame = 'Yes'
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != " ":
        FinishGame = 'Yes'
        
    #Draw condition
    elif board[0][0] != ' ' and board[1][0] != ' ' and board[2][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and board[1][1] != ' ' and board[1][2]!= ' ' and board[2][1] != ' ' and board[2][2] != ' ':
        FinishGame = 'Draw' 
    else:
        FinishGame = 'No'
        
    return FinishGame

#Main function
def main():
    global board, player1, player2, FinishGame
    board = [[' ' for i in range(3)] for j in range(3)]

    player1 = 'X'
    player2 = 'O'
    FinishGame = 'No'
    
    print("Welcome to the TicTacToe game!")
    print("Player 1 will start first. Your symbol is 'X'")
    print("Player 2 will start second. Your symbol is 'O'")
    PlayerTurn = 1
    while FinishGame == 'No':
        DrawBoard()
        print("It is player " + str(PlayerTurn) + "'s turn!")
        row = int(input("Please enter row (from 1-3): "))
        column = int(input("Please enter column (from 1-3): "))
        while not CheckPosition(row, column):
            row = int(input("Please re-enter row (from 1-3): "))
            column = int(input("Please re-enter column (from 1-3): "))
        if PlayerTurn == 1:
            #Assign position to the board
            board[row-1][column-1] = player1
            #Change turn
            PlayerTurn = 2
            
            #Check whether game is over or not
            FinishGame = CheckResults()
        elif PlayerTurn == 2:
            #Assign position to the board
            board[row-1][column-1] = player2
            #Change turn
            PlayerTurn = 1
            
            #Check whether game is over or not
            FinishGame = CheckResults()
        
        
    print()
    if FinishGame == 'Yes':
        if PlayerTurn == 1:
            print("Player 2 WINS")
        else:
            print("Player 1 WINS")
        
    
    elif FinishGame == 'Draw':
        print("DRAW")
    print("FINAL BOARD:")
    DrawBoard()
    
if __name__ == "__main__":
    main()
