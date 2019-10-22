from pprint import pprint
import yaml
import random
import sys

cards = 'cards3.yaml'


class Game():
    def __init__(self):
        self.door = []
        self.treasure = []

        # load in the cards from yaml file
        with open(cards, 'r') as c:
            self.cards = yaml.load(c)

        # put all door cards into the door list variable
        for i in self.cards['door']:
            self.door.append(i)

        # put all door cards into the door list variable
        for i in self.cards['treasure']:
            self.treasure.append(i)

        # shuffle the decks
        random.shuffle(self.door)
        random.shuffle(self.treasure)

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        print(f'Dice Roll: {dice_roll}')
        return dice_roll


class Player():
    def __init__(self):
        self.hand = []
        self.field = []

    def draw_card(self, action, deck):
        reveal_card = deck.pop(0)  # need to rename variable to something that makes more sense
        card = []

        for key, value in reveal_card.items():
            if key == 'description':
                for i in value:
                    card.append(f"{i}")
            elif key == 'metadata':
                continue
            else:
                card.append(f"{key}: {value}")
        self.hand.append(card)

    def check_hand(self):
        for card in self.hand:
            for key, value in card.items():
                print(key, value)


munchkin = Game()
player_names = ['ping', 'james']
players = {}

for player_name in player_names:
    players[player_name] = Player()

# print(munchkin.door.pop(0))
for i in range(4):
    # print(munchkin.door[i])
    for player in players.values():
        player.draw_card('game_setup', munchkin.door)

for i in range(4):
    # print(munchkin.treasure[i])
    for player in players.values():
        player.draw_card('game_setup', munchkin.treasure)

print("Ping's hand")
for card in players['ping'].hand:
    for i in card:
        print(i)
    print()

print("Jame's hand")
for card in players['james'].hand:
    for i in card:
        print(i)
    print()

# print("Abdul's hand")
# for card in players['abdul'].hand:
#     for i in card:
#         print(i)
#     print()
