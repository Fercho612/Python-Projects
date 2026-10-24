def winner(board):
    if row_winner(board) or column_winner(board) or diagonal_winner(board):
        return True
    return False

def row_winner(board):
    for i in range(len(board)):
        win = True
        element_row = board[i][0]
        for j in range(len(board)):
            if element_row != board[i][j] or element_row == ' ':
              win = False
              break
        if win:
            return win
    return win

def column_winner(board):
    for i in range(len(board)):
        win = True
        element_column = board[0][i]
        for j in range(len(board)):
            if element_column != board[j][i] or element_column == ' ':
                win = False
                break
        if win:
            return win
    return win

def diagonal_winner(board):
    diagonal_principal = board[0][0]
    diagonal_secundaria = board[0][-1]
    win_principal = True
    win_secundaria = True
    for i in range(len(board)):
        for j in range(len(board)):
            if i == j and diagonal_principal != board[i][j]:
                win_principal = False
            if len(board)-1 == j+i and diagonal_secundaria != board[i][j]:
                win_secundaria = False
        
    if (win_principal and diagonal_principal != ' ') or (win_secundaria and diagonal_secundaria != ' '):
        return True
    return False
  
  
print(diagonal_winner(
  [
    ['X',' ','O'],
    ['X','X','X'],
    ['O','O','X']
  ]
))

print(diagonal_winner(
    [
        ['S', 'M', ' ', 'M'], 
        [' ', 'S', 'M', ' '], 
        ['S', 'M', ' ', 'S'], 
        ['M', ' ', ' ', 'M']
    ]
))

print(diagonal_winner(
    [
        ['X', ' ', ' ', ' ', 'X'], 
        [' ', 'O', ' ', 'X', ' '], 
        [' ', ' ', 'X', ' ', ' '], 
        [' ', 'X', ' ', 'O', ' '], 
        ['O', ' ', ' ', ' ', 'O']
    ]
))