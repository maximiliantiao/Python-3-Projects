#
# Returns true or false if coordinates provided by user are valid
#
# row_num    : row number to check
# col_num    : column number to check
# game_array : tic-tac-toe board (3x3 array)
#
def valid_coord(row_num, col_num, game_array):
  if game_array[row_num][col_num] == '*':
    return True
  else:
    return False

#
# Return true or false if end of game scenario is reached
# End of game scenarios
# 1. 3 matching in 1st, 2nd, or 3rd rows
# 2. 3 matching in 1st, 2nd, or 3rd columns
# 3. Matching on left->right diagonal or matching on right->left diagonal
#
def end_of_game(game_array):
  # Check 1st, 2nd, and 3rd rows
  for i in range(len(game_array)):
    num_x = 0
    num_o = 0
    for j in range(len(game_array[i])):
      if game_array[i][j] == 'X':
        num_x += 1
      elif game_array[i][j] == 'O':
        num_o += 1 
      else:
        continue

    if num_x == 3:
      print("Player 1 wins!")
      return True
    elif num_o == 3:
      print("Player 2 wins!")
      return True

  # Check 1st, 2nd, and 3rd columns
  for j in range(len(game_array)):
    num_x = 0
    num_o = 0
    for i in range(len(game_array[j])):
      if game_array[i][j] == 'X':
        num_x += 1
      elif game_array[i][j] == 'O':
        num_o += 1
      else:
        continue

    if num_x == 3:
      print("Player 1 wins!")
      return True
    elif num_o == 3:
      print("Player 2 wins!")
      return True

  # Check left->right diagonal
  num_x = 0
  num_o = 0
  for i in range(len(game_array)):
    if game_array[i][i] == 'X':
      num_x += 1
    elif game_array[i][i] == 'O':
      num_o += 1
    else:
      continue

  if num_x == 3:
    print("Player 1 wins!")
    return True
  elif num_o == 3:
    print("Player 2 wins!")
    return True

  # Check right->left diagonal
  num_x = 0
  num_o = 0
  j = 0
  for i in range(len(game_array)-1, -1, -1):
    if game_array[j][i] == 'X':
      num_x += 1
    elif game_array[j][i] == 'O':
      num_o += 1
    else:
      j += 1
      continue
    j += 1

  if num_x == 3:
    print("Player 1 wins!")
    return True
  elif num_o == 3:
    print("Player 2 wins!")
    return True

  return False

if __name__ == '__main__':
  board = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
  ]
  turns = 0
  row_coord = 0
  col_coord = 0
  valid_coordinates = False
  end_game = False

  while (turns < 9):
    print("-------------")
    for i in range(len(board)):
      print("|", end="")
      for j in range(len(board[i])):
        print(" " + str(board[i][j]) + " |", end="")

      print("")
    print("-------------")
    valid_coordinates = False
    end_game = False

    while(~valid_coordinates):
      row_coord = int(input("Row Number: ")) - 1
      col_coord = int(input("Column Number: ")) - 1
      if (row_coord > 2 or col_coord > 2):
        print("Row or Column must be less than or equal to 3!")
        continue
      if (valid_coord(row_coord, col_coord, board)):
        valid_coordinates = True
        break
      else:
        print("Not a valid row or column number. Please try again")

    board[row_coord][col_coord] = 'O' if turns % 2 != 0 else 'X'

    if (end_of_game(board)):
      end_game = True
      break
    else:
      turns += 1

  if (end_game):
    exit(0)
  else:
    print("Draw")
    exit(0)



