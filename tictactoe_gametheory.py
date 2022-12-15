"""Implementation of tic tac toe using game theory.
"""

import os


class TicTacToe:
  """Class for tic tac toe game."""

  def __init__(self, player: str = 'O') -> None:
    self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    self.player = player
    self.opponent = 'X' if player == 'O' else 'O'

  def clear(self):
    # for windows
    if os.name == 'nt':
      os.system('cls')
    # for mac and linux
    else:
      os.system('clear')

  def printboard(self):
    print(f'{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}')
    print('-+-+-')
    print(f'{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}')
    print('-+-+-')
    print(f'{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}')
    print()

  def instruct(self):
    print('Tic-Tac-Toe')
    print('Inputs')
    print('1|2|3')
    print('-+-+-')
    print('4|5|6')
    print('-+-+-')
    print('7|8|9')
    print()

  def movesleft(self):
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == ' ':
          return True
    return False

  def evaluate(self):
    for row in range(3):
      if self.board[row][0] == self.board[row][1] == self.board[row][2]:
        if self.board[row][0] == self.player:
          return +10
        elif self.board[row][0] == self.opponent:
          return -10

    for col in range(3):
      if self.board[0][col] == self.board[1][col] == self.board[2][col]:
        if self.board[0][col] == self.player:
          return +10
        elif self.board[0][col] == self.opponent:
          return -10

    if self.board[0][0] == self.board[1][1] == self.board[2][2]:
      if self.board[0][0] == self.player:
        return +10
      elif self.board[0][0] == self.opponent:
        return -10

    if self.board[0][2] == self.board[1][1] == self.board[2][0]:
      if self.board[0][2] == self.player:
        return +10
      elif self.board[0][2] == self.opponent:
        return -10

    return 0

  def minimax(self, depth, is_max):
    score = self.evaluate()
    if score == 10:
      return score
    if score == -10:
      return score
    if not self.movesleft():
      return 0
    if is_max:
      best = -1000
      for i in range(3):
        for j in range(3):
          if self.board[i][j] == ' ':
            self.board[i][j] = self.player
            best = max(best, self.minimax(depth + 1, not is_max))
            self.board[i][j] = ' '
      return best
    else:
      best = 1000
      for i in range(3):
        for j in range(3):
          if self.board[i][j] == ' ':
            self.board[i][j] = self.opponent
            best = min(best, self.minimax(depth + 1, not is_max))
            self.board[i][j] = ' '
      return best

  def best_move(self):
    best_val = -1000
    row = -1
    col = -1
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == ' ':
          self.board[i][j] = self.player
          move_val = self.minimax(0, False)
          self.board[i][j] = ' '
          if move_val > best_val:
            row = i
            col = j
            best_val = move_val
    return [row, col]

  def is_int(self, v: str) -> bool:
    try:
      int(v)
    except ValueError:
      return False
    return True

  def play(self) -> None:
    turn = self.opponent
    count = 0
    for _ in range(10):
      self.clear()
      self.instruct()
      self.printboard()
      move = ''
      r = -1
      c = -1
      if turn == self.player:
        r, c = self.best_move()
      else:
        print('It\'s your turn, ' + turn)
        move = input()

        if not self.is_int(move):
          print('Wrong choice')
          continue
        move = int(move) - 1
        if move > 8 or move < 0:
          print('Wrong choice')
          continue

        r = int(move / 3)
        c = move % 3

      if self.board[r][c] == ' ':
        self.board[r][c] = turn
        count += 1
      else:
        print('Already filled')
        continue

      win = ''
      if count >= 5:
        for row in range(3):
          if self.board[row][0] == self.board[row][1] == self.board[row][2]:
            win = self.board[row][0]
        for col in range(3):
          if self.board[0][col] == self.board[1][col] == self.board[2][col]:
            win = self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
          win = self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
          win = self.board[0][2]

      if win == 'O':
        self.printboard()
        print('O won')
        break
      elif win == 'X':
        self.printboard()
        print('X won')
        break

      if count == 9:
        self.printboard()
        print('\nGame Over')
        print('Draw!!')
        break

      if turn == self.player:
        turn = self.opponent
      else:
        turn = self.player


if __name__ == '__main__':
  game = TicTacToe()
  game.play()
