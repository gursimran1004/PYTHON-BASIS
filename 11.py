import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("TIC TAC TOE GAME")


board = [" " for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def winner(p):
    win = [(0,1,2),(3,4,5),(6,7,8), (0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in win:
        if board[a] == board[b] == board[c] == p:
            return True
    return False

def play_game():
    current = "X"
    for turn in range(9):
        print_board()
        move = int(input(f"Player {current}, enter position (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Invalid position! Try again.")
            continue

        if board[move] != " ":
            print("Already taken! Try again.")
            continue

        board[move] = current

        if winner(current):
            print_board()
            print(f"🎉 Player {current} is the winner!")
            return

        current = "O" if current == "X" else "X"

    print_board()
    print("It's a draw!")


play_game()
