import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def player_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("해당 위치는 이미 차 있습니다. 다른 위치를 선택하세요.")
        return False

def computer_move(board, player):
    available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if available_moves:
        row, col = random.choice(available_moves)
        board[row][col] = player

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)
    print("플레이어 '{}' 가 먼저 시작합니다.".format(current_player))

    while True:
        print_board(board)

        if current_player == 'X':
            row = int(input("행을 선택하세요 (0, 1, 2): "))
            col = int(input("열을 선택하세요 (0, 1, 2): "))
            if player_move(board, row, col, current_player):
                if check_winner(board, current_player):
                    print("플레이어 '{}' 가 이겼습니다!".format(current_player))
                    break
                elif check_draw(board):
                    print("무승부입니다!")
                    break
                current_player = 'O'
        else:
            computer_move(board, current_player)
            if check_winner(board, current_player):
                print("컴퓨터가 이겼습니다!")
                break
            elif check_draw(board):
                print("무승부입니다!")
                break
            current_player = 'X'

if __name__ == "__main__":
    main()

