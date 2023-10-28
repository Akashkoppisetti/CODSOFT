from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock', 0), ('paper', 1), ('scissors', 2)]

def player_choice(player_option):
    global player_score, computer_score
    computer_option = random.choice(options)
    player_choice_label.config(text=f'Your Selected: {player_option[0]}')
    computer_choice_label.config(text=f'Computer Selected: {computer_option[0]}')
    winner = determine_winner(player_option, computer_option)
    if winner == "Player":
        player_score += 1
    elif winner == "Computer":
        computer_score += 1
    update_score_labels()

def determine_winner(player_option, computer_option):
    if player_option[1] == computer_option[1]:
        return "Tie"
    elif (player_option[1] - computer_option[1]) % 3 == 1:
        return "Player"
    else:
        return "Computer"

def update_score_labels():
    player_score_label.config(text=f'Your Score: {player_score}')
    computer_score_label.config(text=f'Computer Score: {computer_score}')
    winner_label.config(text="Winner: " + determine_overall_winner())

def determine_overall_winner():
    if player_score > computer_score:
        return "Player"
    elif computer_score > player_score:
        return "Computer"
    else:
        return "Tie"

game_window = Tk()
game_window.title("Rock Paper Scissors Game")

app_font = font.Font(size=12)

game_title = Label(text='Rock Paper Scissors', font=font.Font(size=20), fg='grey')
game_title.pack()

winner_label = Label(text="Let's Start the Game...", fg='green', font=font.Font(size=13), pady=8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

player_options = Label(input_frame, text="Your Options: ", font=app_font, fg='grey')
player_options.grid(row=0, column=0, pady=8)

rock_btn = Button(input_frame, text='Rock', width=15, bd=0, bg='pink', pady=5, command=lambda: player_choice(options[0]))
rock_btn.grid(row=1, column=1, padx=8, pady=5)

paper_btn = Button(input_frame, text='Paper', width=15, bd=0, bg='silver', pady=5, command=lambda: player_choice(options[1]))
paper_btn.grid(row=1, column=2, padx=8, pady=5)

scissors_btn = Button(input_frame, text='Scissors', width=15, bd=0, bg='light blue', pady=5, command=lambda: player_choice(options[2]))
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

score_label = Label(input_frame, text='Score: ', font=app_font, fg='grey')
score_label.grid(row=2, column=0)

player_choice_label = Label(input_frame, text='Your Selected: ---', font=app_font)
player_choice_label.grid(row=3, column=1, pady=5)

player_score_label = Label(input_frame, text='Your Score: -', font=app_font)
player_score_label.grid(row=3, column=2, pady=5)

computer_choice_label = Label(input_frame, text='Computer Selected: ---', font=app_font, fg='black')
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input_frame, text='Computer Score: -', font=app_font, fg='black')
computer_score_label.grid(row=4, column=2, padx=(10, 0), pady=5)

game_window.geometry('700x300')
game_window.mainloop()
