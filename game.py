from pprint import pprint
import yaml
import random
import sys

cards = 'cards3.yaml'


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
        self.game_status(player)
        player_level = eval(input("Enter level gained or lost: "))
        player.level += player_level



    def game_status(self, player):
        print(f"Game Level: {self.game_level}")
        header_row = f"-- {player.name}'s turn --"
        header_len = len(header_row)
        print("-" * header_len)
        print(header_row)
        print("-" * header_len)
        print(f"Level: {player.level}")
        print()
        player.display_hand()
        print()

    
    def setup_players(self, players_list: list):
        for player in players_list:
            self.players[player] = Player(player)

        print(self.players)

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


class Player():
    def __init__(self, name: str):
        self.hand = []
        self.field = []
        self.name = name
        self.level = 0

    def draw_card(self, game_deck: list):
        drawn_card = game_deck.pop(0)  # need to rename variable to something that makes more sense
        cards = []

        for key, value in drawn_card.items():
            if key == 'description':
                for i in value:
                    cards.append(f"{i}")
            elif key == 'metadata':
                continue
            else:
                cards.append(f"{key}: {value}")
        self.hand.append(cards)

    def check_hand(self):
        for cards_dict in self.hand:
            for card in cards_dict:
                print(card)
            print()

    def display_hand(self):
        header_row = f"-- {self.name}'s hand --"
        header_len = len(header_row)
        
        print("-" * header_len)
        print(header_row)
        print("-" * header_len)

        for cards_dict in self.hand:
            for card in cards_dict:
                print(card)
            print()




if __name__ == "__main__":
    munchkin = Game(game_level=10) # sets up deck 

    player_names = ['ping', 'james', 'abdul'] # this list could be generated however we like
    
    munchkin.setup_players(player_names) # sets up players and draws initial cards from the deck

    import itertools as it
    player = it.cycle([*munchkin.players.values()]) # cool BI module that allows for cycling through each player turn

    while munchkin.check_game_over(): # this checks if any body has won before calling on next player
        current_player = next(player) # next() is part of the iter module to call on next items in an iterable
        munchkin.play(current_player)

    print(f"Game Over: {current_player.name} has won the game!")

    

