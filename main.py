#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_tie(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player, board):
    while True:
        try:
            move = int(input(f"{player}, enter your move (1-9): ")) - 1
            if 0 <= move < 9:
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    return row, col
                else:
                    print("Cell is already occupied. Try again.")
            else:
                print("Invalid move. Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ai_move(board, ai, human):
    # Try to win
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = ai
                if check_win(board, ai):
                    return row, col
                board[row][col] = " "  # Undo move

    # Block the opponent
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = human
                if check_win(board, human):
                    board[row][col] = ai  # Block the win
                    return row, col
                board[row][col] = " "  # Undo move

    # Pick a random empty spot
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_spots)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = input("Do you want to be X or O? ").upper()
    while human not in ["X", "O"]:
        human = input("Invalid choice. Please choose X or O: ").upper()
    ai = "O" if human == "X" else "X"

    print("Welcome to Tic Tac Toe!")
    print("Here's the board layout:")
    display_board([[str(i + 1) for i in range(j * 3, (j + 1) * 3)] for j in range(3)])

    current_player = "X"
    while True:
        display_board(board)

        if current_player == human:
            row, col = get_move(human, board)
        else:
            print(f"{ai} is thinking...")
            row, col = ai_move(board, ai, human)

        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Congratulations {current_player}! You win!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = ai if current_player == human else human  # Switch players

if __name__ == "__main__":
    main()


# In[ ]:




