from pprint import pprint
import yaml
import random

cards = 'cards2.yaml'


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
            for j in self.cards['treasure'][i]:
                self.treasure.append(j)

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

        if action == 'kick_open_the_door':
            if reveal_card['card_type'] == 'curse':
                print(f"Curse: {reveal_card['name']}")
                print(f"Description: {reveal_card['description']}", end='')
            elif reveal_card['card_type'] == 'monster':
                print(f"Monster Name: {reveal_card['name']}")
                print(f"Ability: {reveal_card['description']['ability']}", end='')
                print(f"Bad Stuff: {reveal_card['description']['bad_stuff']}", end='')
        else:  # this includes loot the room and monster treasures
            self.hand.append(reveal_card)

    def check_hand(self):
        for card in self.hand:
            for key, value in card.items():
                print(key, value)


x = Game()
pprint(x.door)
print()
pprint(x.treasure)
print()

ping = Player()
ping.draw_card('kick_open_the_door', x.door)
# ping.draw_card('loot_the_room', x.door)
# print(ping.field[0]['name'])
# ping.check_hand()
