from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tic Tac Toe Game by Wakil")
clicked = True
count = 0

# Buttons
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = Button(root, text="", font=("Helvetica", 20 ), height=3, width=6, command=lambda row=i, col=j: click(row, col))
        button.grid(row=i, column=j, sticky="nsew")
        row.append(button)
    buttons.append(row)

def click(row, col):
    global clicked, count

    if buttons[row][col]["text"] == "" and clicked == True:
        buttons[row][col]["text"] = "X"
        computer_move()
        count += 1

        # Check for Win
        if check_win("X") == True and check_win("O") == True:
            messagebox.showinfo("Tic Tac Toe", "Draw")
            messagebox.showinfo("Tic Tac Toe", "Click reset to play again")
            disable_all_buttons()
        
        elif check_win("X"):
            messagebox.showinfo("Tic Tac Toe", "You Won!")
            messagebox.showinfo("Tic Tac Toe", "Click reset to play again")
            disable_all_buttons()

        elif check_win("O"):
            messagebox.showinfo("Tic Tac Toe", "You Lost!")
            messagebox.showinfo("Tic Tac Toe", "Click reset to play again")
            disable_all_buttons()

        elif count == 9:
            messagebox.showinfo("Tic Tac Toe", "Tie")
            messagebox.showinfo("Tic Tac Toe", "Click reset to play again")
            disable_all_buttons()
# Check for win
def check_win(player):
    # check in rows
    for i in range(3):
        if buttons[i][0]["text"] == player and buttons[i][1]["text"] == player and buttons[i][2]["text"] == player:
            buttons[i][0].config(bg="lightgreen")
            buttons[i][1].config(bg="lightgreen")
            buttons[i][2].config(bg="lightgreen")
            return True
        # Check in columns
        if buttons[0][i]["text"] == player and buttons[1][i]["text"] == player and buttons[2][i]["text"] == player:
            buttons[0][i].config(bg="lightgreen")
            buttons[1][i].config(bg="lightgreen")
            buttons[2][i].config(bg="lightgreen")
            return True
    # Check in diagonals
    if buttons[0][0]["text"] == player and buttons[1][1]["text"] == player and buttons[2][2]["text"] == player:
        buttons[0][0].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][2].config(bg="lightgreen")
        return True
    if buttons[0][2]["text"] == player and buttons[1][1]["text"] == player and buttons[2][0]["text"] == player:
        buttons[0][2].config(bg="lightgreen")
        buttons[1][1].config(bg="lightgreen")
        buttons[2][0].config(bg="lightgreen")
        return True
    return False

# Computer Move
def computer_move():
    global count
    empty_cells = []

    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                empty_cells.append((i, j))

    if not empty_cells:
        return

    row, col = random.choice(empty_cells)
    buttons[row][col]["text"] = "O"
    count += 1

    if check_win("O"):
        disable_all_buttons()

def disable_all_buttons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

messagebox.showinfo("Tic Tac Tie", "By : Wakil Ahmad Hamidi\nClick OK to start the game")
disable_all_buttons()

def reset():
    global clicked, count
    clicked = True
    count = 0
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = "" 
            buttons[i][j]["state"] = NORMAL
            buttons[i][j]["bg"] = "SystemButtonFace"

my_menu = Menu(root)
root.config(menu=my_menu)

# Create Menu Option
Option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options", menu=Option_menu)
Option_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()