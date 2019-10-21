from pprint import pprint
import yaml
import random
import sys

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

        if reveal_card['card_type'] == 'curse':
            card.append(f"Curse: {reveal_card['name']}")
            card.append(f"Description: {reveal_card['description']}")
            self.hand.append(card)
        elif reveal_card['card_type'] == 'monster':
            card.append(f"Monster: {reveal_card['name']}")
            card.append(f"Level: {reveal_card['level']}")
            card.append(f"Ability: {reveal_card['description']['ability']}")
            card.append(f"Bad Stuff: {reveal_card['description']['bad_stuff']}")
            if 'treasure_reward' in reveal_card['reward']:
                card.append(f"Treasure Reward: {reveal_card['reward']['treasure_reward']}")
            if 'level_reward' in reveal_card['reward']:
                card.append(f"Level Reward: {reveal_card['reward']['level_reward']}")
                # print(f"{sys.exc_info()[0]} {sys.exc_info()[1]}, line: {sys.exc_info()[2].tb_lineno}")
            self.hand.append(card)
        elif reveal_card['card_type'] == 'spell':
            card.append(f"Spell: {reveal_card['name']}")
            if 'description' in reveal_card:
                card.append(f"Description: {reveal_card['description']}")
            self.hand.append(card)
        elif reveal_card['card_type'] == 'class':
            card.append(f"Class: {reveal_card['name']}")
            for i in reveal_card['description']:
                card.append(i)
            self.hand.append(card)
        elif reveal_card['card_type'] == 'race':
            card.append(f"Race: {reveal_card['name']}")
            for i in reveal_card['description']:
                card.append(i)
            self.hand.append(card)

    def check_hand(self):
        for card in self.hand:
            for key, value in card.items():
                print(key, value)


x = Game()
# pprint(x.door)
# print()
# pprint(x.treasure)
# print()

ping = Player()
ping.draw_card('kick_open_the_door', x.door)
ping.draw_card('kick_open_the_door', x.door)
ping.draw_card('kick_open_the_door', x.door)
ping.draw_card('kick_open_the_door', x.door)
# ping.draw_card('loot_the_room', x.treasure)
# ping.draw_card('loot_the_room', x.treasure)
# ping.draw_card('loot_the_room', x.treasure)
# ping.draw_card('loot_the_room', x.treasure)
# ping.draw_card('loot_the_room', x.door)
# print(ping.field[0]['name'])
# ping.check_hand()
for card in ping.hand:
    # print(card)
    for i in card:
        print(i)
    print()
