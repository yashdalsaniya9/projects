import tkinter as tk
from tkinter import messagebox

a = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def check_winner():
    global winner
    for i in a:
        if buttons[i[0]]["text"] == buttons[i[1]]["text"] == buttons[i[2]]["text"] != "":
            buttons[i[0]].config(bg="green")
            buttons[i[1]].config(bg="green")
            buttons[i[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[i[0]]['text']} wins!")
            disable_buttons()
            return
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        disable_buttons()

def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player 
    current_player = "X" if current_player == "O" else "O"
    label.config(text = f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), height=2, width=6, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

def reset_game():
    global current_player, winner
    current_player = "X"
    winner = False
    for button in buttons:
        button.config(text="", state="normal", bg="SystemButtonFace")
    label.config(text=f"Player {current_player}'s turn")

reset_button = tk.Button(root, text="Reset", font=("normal", 16), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
