from os import system
from time import sleep

board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

player="O"
opponent="X"

def printboard():
  print(' '+board[0][0] + '|' + board[0][1] + '|' + board[0][2])
  print(' -+-+-')
  print(' '+board[1][0] + '|' + board[1][1] + '|' + board[1][2])
  print(' -+-+-')
  print(' '+board[2][0] + '|' + board[2][1] + '|' + board[2][2])
  print()

def instruct():
  print('Tic-Tac-Toe')
  print('Inputs')
  print(' 1|2|3')
  print(' -+-+-')
  print(' 4|5|6')
  print(' -+-+-')
  print(' 7|8|9')
  print()

def movesleft(board):
  for i in range(3): 
    for j in range(3):
      if(board[i][j]==' '):
        return True
  return False

def evaluate(b):
    for row in range(3): 
        if (b[row][0]==b[row][1]==b[row][2]):
          if (b[row][0]==player):
            return +10
          elif (b[row][0]==opponent):
            return -10
  
    for col in range(3):
        if (b[0][col]==b[1][col]==b[2][col]): 
          if (b[0][col]==player):
            return +10 
          elif (b[0][col]==opponent): 
            return -10;

    if (b[0][0]==b[1][1]==b[2][2]):
      if (b[0][0]==player): 
        return +10
      elif (b[0][0]==opponent): 
        return -10 
  
    if (b[0][2] == b[1][1]==b[2][0]): 
      if (b[0][2]==player): 
        return +10
      elif (b[0][2]==opponent): 
            return -10 

    return 0


def minimax(board,depth,isMax):
  score=evaluate(board);
  if (score==10):
    return score 
  if (score==-10): 
    return score
  if (movesleft(board)==False):
    return 0
  if (isMax==True): 
    best = -1000
    for i in range(3):
      for j in range(3):
        if (board[i][j]==' '): 
         board[i][j] = player
         best=max(best, minimax(board,depth + 1, not isMax))
         board[i][j] = ' '
    return best
  else:
    best = 1000;
    for i in range(3):
      for j in range(3): 
        if (board[i][j]==' '):
          board[i][j]=opponent 
          best =min(best, minimax(board,depth + 1, not isMax))
          board[i][j]=' ' 
    return best


def bestMove(board): 
  bestVal = -1000; 
  row = -1; 
  col = -1; 
  for i in range(3):
    for j in range(3):
      if (board[i][j]==' '):
        board[i][j] = player
        moveVal=minimax(board, 0, False)
        board[i][j]=' ' 
        if (moveVal > bestVal): 
          row=i
          col=j
          bestVal = moveVal; 
  return [row,col]

def isInt(v):
    try:
    	i = int(v)
    except:
    	return False
    return True

def game():
    turn = 'X'
    count = 0
    for i in range(10): 
        system('cls')
        instruct()
        printboard()
        move=''
        r=-1
        c=-1
        if(turn=='O'):
          move=bestMove(board)
          r=move[0]
          c=move[1]
        else:
          print("It's your turn," + turn)
          move = input()

          if (not isInt(move)):
          	print("Wrong choice")
          	sleep(1)
          	continue
          move=int(move)-1
          if(move>8 or move<0):
          	print("Wrong choice")
          	sleep(1)
          	continue

          r=int(move/3)
          c=move%3
        
        if board[r][c] == ' ':
            board[r][c] = turn
            count += 1
        else:
            print("Already filled")
            sleep(1)
            continue

        win=''
        if count >= 5:
          for row in range(3): 
            if (board[row][0]==board[row][1]==board[row][2]):
              if (board[row][0]==player):
                win='O'
              elif (board[row][0]==opponent):
                win='X'
          for col in range(3):
            if (board[0][col]==board[1][col]==board[2][col]): 
              if (board[0][col]==player):
                win='O' 
              elif (board[0][col]==opponent): 
                win='X'
          if (board[0][0]==board[1][1]==board[2][2]):
            if (board[0][0]==player): 
              win='O'
            elif (board[0][0]==opponent): 
              win='X' 
         
          if (board[0][2] == board[1][1]==board[2][0]): 
            if (board[0][2]==player): 
              win='O'
            elif (board[0][2]==opponent): 
              win='X'
        
        if (win=='O'):
          printboard()
          print("O won")
          break
        elif win=='X':
          printboard() 
          print("X won")
          break

        if count == 9:
          printboard()
          print("\nGame Over")                
          print("Draw!!")
          break

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'

game()