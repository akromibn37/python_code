def same_row(i,j):
    return (i//9 == j//9)
def same_col(i,j):
    return (i-j) % 9 == 0
def same_block(i,j):
    return (i//27 == j//27 and i%9//3 == j%9//3)
def show(b):
    for i in range(3):
        print('+---+---+---+') 
        for j in range(3):
            k = 9*(3*i+j)
            print('|'+b[k:k+3]+'|'+b[k+3:k+6]+'|'+b[k+6:k+9]+'|')
    print('+---+---+---+') 
        
def solve(board):
    i = board.find('.')
    if i == -1: return board
    S = { board[j] for j in range(81)
            if same_row(i,j) or same_col(i,j) or same_block(i,j) }
    T = set('123456789')-S
    for e in T:
        newboard = board[:i]+e+board[i+1:]
        sol = solve(newboard)
        if sol != '' : return sol
    return ''

sol = solve(input().strip())
show(sol)
