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


x = Game()
ping = Player()

for i in range(4):
    ping.draw_card('game_setup', x.door)

for i in range(4):
    ping.draw_card('game_setup', x.treasure)

for card in ping.hand:
    for i in card:
        print(i)
    print()
