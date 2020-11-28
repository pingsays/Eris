from pprint import pprint
import yaml
import random
import sys
from flask_socketio import SocketIO, emit, send
from eris_app.player import Player

cards = 'eris_app/cards3.yaml'


class Game():
    def __init__(self, game_level: int):
        self.door = []
        self.treasure = []
        self.players = {}
        self.game_level = game_level
    
        # load in the cards from yaml file
        with open(cards, 'r') as c:
            self.cards = yaml.load(c)

        # put all door cards into the door list variable
        for i in self.cards['door']:
            self.door.append(i)

        # put all door cards into the door list variable
        for i in self.cards['treasure']:
            self.treasure.append(i)

        # shuffled deck
        random.shuffle(self.door)
        random.shuffle(self.treasure)
        # print(f'door: {len(self.door)}')
        # print(f'treasure: {len(self.treasure)}')
    
    def get_deck(self):
        return len(self.door), len(self.treasure)

    def play(self, player):
        game_play = {
            'game_message': 'Enter new level: ',
            'game_status': self.game_status(player),
            # 'player_level_update': self.player_level_update(player, level)
        }
        return game_play
        

    def player_level_update(self, player, level):
        new_player_level = player.level + level
        new_player_level = {
            'player_level': player.level,
            'new_player_level': new_player_level
        }
        return new_player_level


    def game_status(self, player):
        # print(f"Game Level: {self.game_level}")
        # header_row = f"-- {player.name}'s turn --"
        # header_len = len(header_row)
        # print("-" * header_len)
        # print(header_row)
        # print("-" * header_len)
        # print(f"Level: {player.level}")
        # print()
        # player.display_hand()
        # print()
        game_info = {
            'game_level': self.game_level,
            'player_turn': player.name,
            'player_level': player.level,
            'player_hand': player.hand
        }
        print(game_info)
        return game_info

    
    def setup_players(self, players_list: list):
        for player in players_list:
            self.players[player] = Player(player)

        # print(self.players)

        # print(munchkin.door.pop(0))
        for i in range(4):
            # print(munchkin.door[i])
            for player in self.players.values():
                player.draw_card(self.door)
                player.draw_card(self.treasure)
                
        for player in self.players.values():
            pass
            # player.display_hand()

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        print(f'Dice Roll: {dice_roll}')
        return dice_roll

    def check_game_over(self):
        max_player_level = max([player.level for player in self.players.values()])
        print(max_player_level)
        if max_player_level != self.game_level:
            return True #if the player with the highest level is not equal to base game level continue
        else:
            return False



    

