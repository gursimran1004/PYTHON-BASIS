import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("TIC TAC TOE - GUI VERSION")

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

def is_draw():
    for row in board:
        if "" in row:
            return False
    return True

def on_click(r, c):
    global current_player

    if board[r][c] == "":
        board[r][c] = current_player
        buttons[r][c].config(text=current_player, state="disabled")

        if check_winner():
            messagebox.showinfo("Game Over", f" Player {current_player} wins!")
            root.quit()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"

for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="", font=('Arial', 20), width=6, height=3,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn
root.mainloop()
