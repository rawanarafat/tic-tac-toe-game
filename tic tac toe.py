board = [' ' for x in range(10)]
game_is_going = True
current_player = 'x'

def inseretLetter(letter, pos):
    board[pos] = letter

def spaceisfree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('     |    |')
    print(' ' + board[1] + '   | ' + board[2] + '  | ' + board[3] + "       1 | 2 | 3 ")
    print('     |    |')
    print("-----------------")
    print(' ' + board[4] + '   | ' + board[5] + '  | ' + board[6] + "       4 | 5 | 6 ")
    print('     |    |')
    print('     |    |')
    print("-----------------")
    print(' ' + board[7] + '   | ' + board[8] + '  | ' + board[9] + "       7 | 8 | 9 ")
    print('     |    |')
    

def isWinner(board,letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter) or(board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter)
    
def boardisfull(board):
    global game_is_going
    if " " not in board:
        game_is_going = False
        return True
    else:
        game_is_going = True
        return False
    
def game_running():
    global game_is_going
    game_is_going = True
    if isWinner(board, 'x'):
        print("X Is The Winner")
        game_is_going = False
        return False
        
    
    if isWinner(board, 'o'):
        print("O Is The Winner") 
        game_is_going = False
        return False
    
    if boardisfull(board):
        print("Its A Tie")
        game_is_going = False
        return False
        
def playerMove():
    # ask user for input for X 
    run = True
    while run:
      letter = current_player
      pos = input(letter + " turn, enter position 1-9: ")
      while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
           pos = input(letter + " turn, enter position 1-9: ")
      pos = int(pos)
     # check if pos is free
      if spaceisfree(pos):
          run = False
          inseretLetter(letter, pos)
      else:
          print("space is full")
          



def handle_move():
    global current_player
    if current_player == 'x':
        current_player = 'o'
    else:
        current_player = 'x'
    


def main():
   global game_is_going
   game_is_going = True
   print("Welcome TO Tic Tac Toe Game")
   while game_is_going:
      printBoard(board)
      playerMove()
      game_running()
      handle_move()
    
  
     
    
    
    
    
main()