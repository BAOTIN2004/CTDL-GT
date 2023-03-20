def solveKnightTour(n):
    # Khởi tạo bàn cờ
    board = [[-1 for i in range(n)] for j in range(n)]
    # Các nước đi của con mazz
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    # Đặt con mã vào ô bắt đầu
    # a,b=map(int,input('Nhập vị trí xuất phát của mã:\t').split())
    board[2][5] = 0
    # Bắt đầu tìm kiếm đường đi
    if not ma_di_chuyen(board, 0, 0, moves, 1, n):
        print("Không tìm thấy giải pháp")
    else:
        printSolution(board)

def ma_di_chuyen(board, x, y, moves, movei, n):
    # Tất cả các ô đã được đi qua
    if movei == n*n:
        return True
    # Duyệt tất cả các nước đi của con mã
    for i in range(8):
        next_x = x+ moves[i][0]
        next_y = y+moves[i][1]
        # Kiểm tra xem nước đi mới có nằm trên bàn cờ và chưa được đi qua
        if isSafe(next_x, next_y, board, n)==True:
            board[next_x][next_y] = movei
            # Tìm kiếm đường đi từ nước đi mới
            if ma_di_chuyen(board, next_x, next_y, moves, movei+1, n):
                return True
            # Quay lui nếu không tìm thấy giải pháp từ nước đi mới
            board[next_x][next_y] = -1
    return False

def isSafe(x, y, board, n):
    return x>=0 and x<n and y>=0 and y<n and board[x][y]==-1

def printSolution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end = ' ')
        print()

solveKnightTour(6)
