DIRECTIONS = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1))

    # move_x = [2, 1, -1, -2, -2, -1,  1,  2]
    # move_y = [1, 2,  2,  1, -1, -2, -2, -1]

def _find_postion(board,N,moves,postions):
    row,col = postions
    if row < 0 or col < 0 or row >= N or col >= N or board[row][col] > 0: return 0
    elif moves + 1 == N * N:
        board[row][col] = moves
        if board[0][1] == 59:
            [print(*i) for i in board]
        board[row][col] = 0
        return 1
    else:
        board[row][col] = moves
        for x,y in DIRECTIONS:
            if _find_postion(board,N,moves+1,(row+x, col+y)) == 1: return 1
        
        board[row][col] = 0



def knight_moves(board_size):
    board = [[0 for _ in range(board_size)] for __ in range(board_size)]
    _find_postion(board,board_size,0,(0,0))


if __name__ == '__main__':
    knight_moves(8)