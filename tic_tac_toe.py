def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board, player):
    for row in board:
        if all([spot==player for spot in row]):
            return True
    for col in range(3):
        if all(board[row][col]==player for row in range(3)):
            return True
    if all([board[i][i]==player for i in range(3)]) or all([board[i][2-i]==player for i in range(3)]):
        return True
    return False
def is_board_full(board):
    return all([spot != " " for row in board for spot in row])
def main():
    board=[[" " for _ in range(3)] for _ in range(3)]
    current_player="X"
    while True:
        print_board(board)
        row=int(input(f"Player {current_player}, enter row (0-2): "))
        col=int(input(f"Player {current_player}, enter column (0-2): "))
        if board[row][col]!=" ":
            print("Spot already taken, try again.")
            continue
        board[row][col]=current_player

        if check_winner(board,current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player="O" if current_player=="X" else "X"
if __name__=="__main__":
    main()
