import tkinter as tk
from tkinter import ttk
from actions import *


class RPS:
    game_count = 0
    players = {}

    def __init__(self):
        while True:
            self.restart_game()
            self.action(123)

    def restart_game(self):
        player1_id = input('Введите имя 1-го игрока: ')
        player2_id = input('Введите имя 2-го игрока: ')
        self.start_game(player1_id, player2_id)

    def start_game(self, player1_id, player2_id):
        self.create_player(player1_id)
        self.create_player(player2_id)
        self.game_count += 1
        self.p1_move = ''
        self.p2_move = ''

    def create_player(self, player_id):
        if player_id in self.players.keys():
            return 'Игрок уже создан!'
        self.players[id] = {'wins': 0, 'loses': 0}
        return 'Игрок создан.'

    def action(self, player_id):
        root = tk.Tk()

        button = ttk.Button(root, text='Rock',
                            command=self.move1_r)
        button = ttk.Button(root, text='Paper',
                            command=self.move())
        button = ttk.Button(root, text='Scissors',
                            command=self.move())

        root.mainloop()

    def move(self, p_num, act):
        exec(f'self.__p{p_num}_move = {act}')

    def win(self, player_id):
        self.players[player_id]['win'] += 1

    def lose(self, player_id):
        self.players[player_id]['lose'] += 1

    def game_end(self, winner_id, loser_id):
        self.win(winner_id)
        self.lose(loser_id)
        print('Игра закончена!')


game = RPS()


