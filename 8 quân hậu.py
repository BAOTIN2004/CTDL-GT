def solve(board, col):
    # Nếu đã đặt được quân hậu vào cột cuối cùng thì kết thúc
    if col == len(board):
        return True
    
    # Thử đặt quân hậu vào các ô trong cột
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            # Đệ quy đến cột tiếp the
            if solve(board, col+1):
                return True
            # Nếu không tìm thấy giải pháp thì quay lui
            board[row][col] = 0
    
    # Nếu không tìm thấy giải pháp thì trả về False
    return False

def is_safe(board, row, col):
    # Kiểm tra hàng ngang
    for i in range(col):
        if board[row][i] == 1:  
            return False
    # Kiểm tra đường chéo trên bên trái
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Kiểm tra đường chéo dưới bên trái
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    # Nếu không bị tấn công thì trả về True
    return True

# Khởi tạo bàn cờ nxn
n=int(input('Nhập kích cỡ bàn cờ: '))
board = [[0 for x in range(n)] for y in range(n)]

# Giải quyết bài toán
if solve(board, 0)== True:
    # In ra bàn cờ đã giải quyết
    for row in board:
        print(row)
else:
    print("Không tìm thấy giải pháp")
