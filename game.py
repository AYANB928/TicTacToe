import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.player = "X"
        self.computer = "O"
        self.buttons = [tk.Button(self.root, width=5, height=2, command=lambda x=i: self.play(x)) for i in range(9)]
        self.winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        self.setup_gui()

    def setup_gui(self):
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)

        self.play_again_button = tk.Button(self.root, text="Play Again", state=tk.DISABLED, command=self.play_again)
        self.play_again_button.grid(row=3, column=0, columnspan=3, pady=10)
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.grid(row=4, column=0, columnspan=3)

    def play(self, button_id):
        button = self.buttons[button_id]
        if button["text"] == "":
            button.config(text=self.player)
            if self.check_win(self.player):
                return
            self.computer_play()

    def computer_play(self):
        empty_buttons = [i for i in range(9) if self.buttons[i]["text"] == ""]
        if empty_buttons:
            move = random.choice(empty_buttons)
            self.buttons[move].config(text=self.computer)
            self.check_win(self.computer)

    def check_win(self, player):
        for combo in self.winning_combinations:
            if all(self.buttons[i]["text"] == player for i in combo):
                self.game_over(player, combo)
                return True
        if "" not in [button["text"] for button in self.buttons]:
            self.game_over("tie", ())
            return True
        return False

    def game_over(self, winner, win_combo):
        if winner == "tie":
            messagebox.showinfo("Tie", "It's a tie!")
        elif winner == self.player:
            messagebox.showinfo("Winner", "You win!")
        else:
            messagebox.showinfo("Winner", "Computer wins!")

        if win_combo:
            for i in win_combo:
                self.buttons[i].config(bg="red")

                self.play_again_button.config(state=tk.NORMAL)
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def play_again(self):
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL, bg="SystemButtonFace")
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    TicTacToe()
    tk.mainloop()



