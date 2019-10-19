from pprint import pprint
import yaml
import random

cards = 'cards.yaml'


class Game():
    def __init__(self):
        self.door = []
        self.treasure = []

        # load in the cards from yaml file
        with open(cards, 'r') as c:
            self.cards = yaml.load(c)

        # put all door cards into the door list variable
        for i in self.cards['door']:
            for j in self.cards['door'][i]:
                self.door.append(j)

        # put all door cards into the door list variable
        for i in self.cards['treasure']:
            for j in self.cards['treasure'][i]:
                self.treasure.append(j)

        # shuffle the decks
        random.shuffle(self.door)
        random.shuffle(self.treasure)


class Player():
    def __init__(self):
        self.hand = []
        self.field = []


x = Game()
pprint(x.door)
print()
pprint(x.treasure)
