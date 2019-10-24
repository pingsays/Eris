from pprint import pprint
import yaml
import random
import sys

cards = 'cards3.yaml'


class Game():
    def __init__(self):
        self.door_draw = []
        self.treasure_draw = []
        self.door_discard = []
        self.treasure_discard = []

        # load in the cards from yaml file
        with open(cards, 'r') as c:
            self.cards = yaml.load(c)

        # put all door cards into the door list variable
        for i in self.cards['door']:
            self.door_draw.append(i)

        # put all door cards into the door list variable
        for i in self.cards['treasure']:
            self.treasure_draw.append(i)

        # shuffle the decks
        self.shuffle_deck(self.door_draw)
        self.shuffle_deck(self.treasure_draw)
        # random.shuffle(self.door_draw)
        # random.shuffle(self.treasure_draw)

    def shuffle_deck(self, deck):
        """deck: need to provide list"""
        random.shuffle(deck)
        return deck

    def reshuffle_discard_pile(self, deck_type):
        if deck_type == 'door':
            self.door_draw = self.shuffle_deck(self.door_discard)
            self.door_discard = []
        elif deck_type == 'treasure':
            self.treasure_draw = self.shuffle_deck(self.treasure_discard)
            self.treasure_discard = []

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        print(f'Dice Roll: {dice_roll}')
        return dice_roll


class Player():
    def __init__(self):
        self.hand = []
        self.playing_field = {
            'temp': [], 'equipment': [], 'monster': [], 'curse': [], 'class': [], 'race': []
        }

    def draw_card(self, action, deck):
        card_details = deck.pop(0)  # need to rename variable to something that makes more sense
        card = {}

        # for key, value in card_details.items():
        #     if key == 'description':
        #         for i in value:
        #             card.append(f"{i}")
        #     elif key == 'metadata':
        #         continue
        #     else:
        #         card.append(f"{key}: {value}")
        # self.hand.append(card)

        self.hand.append(card_details)

    def use_card(self, card_index, target):
        """this can be used for both playing or discarding"""

        card = self.hand.pop(card_index)

        # check if the target is a Player class
        if isinstance(target, Player):
            if 'monster' in card.keys():
                target['playing_field']['monster'].append(card)
        else:
            target.append(self.hand.pop(card_index))

    # def sort_card(self, card, target):
    #     """this method should be called whenever a card is used on player"""
    #     if 'monster' in card.keys():
    #         target['playing_field']['monster'].append(card)

    def check_hand(self):
        for card in self.hand:
            for key, value in card.items():
                print(key, value)


mk = Game()
player_names = ['ping', 'james', 'abdul']
players = {}

# print(mk.door_draw)
# mk.door_draw = mk.shuffle_deck(mk.door_draw)
# print(mk.door_draw)

for player_name in player_names:
    players[player_name] = Player()

# print(mk.door.pop(0))
for i in range(4):
    # print(mk.door[i])
    for player in players.values():
        player.draw_card('game_setup', mk.door_draw)

for i in range(4):
    # print(mk.treasure[i])
    for player in players.values():
        player.draw_card('game_setup', mk.treasure_draw)

#=====================#
# testing player hand #
#=====================#
for player in player_names:
    header_row = f"-- {player}'s hand --"
    header_len = len(header_row)

    print("-" * header_len)
    print(header_row)
    print("-" * header_len)

    for card in players[player].hand:
        for key, value in card.items():
            if 'metadata' in key:
                continue
            elif 'description' in key:
                print('description: ', end='')
                for i in value:
                    print(i)
            else:
                print(f"{key}: {value}")
        print()

#===========================================#
# testing discard card and reshuffling deck #
#===========================================#
print(players['ping'].hand)
# players['ping'].discard_card(0, mk.door_discard)
# players['ping'].discard_card(0, mk.door_discard)
# players['ping'].discard_card(0, mk.door_discard)
# players['ping'].discard_card(0, mk.door_discard)
# print()
# print(mk.door_discard)
# print()
# # print(players['ping'].hand)
# print()

# print('reshuffling')
# mk.reshuffle_discard_pile('door')
# print(f"discard: {mk.door_discard}")
# print()
# print(f"draw: {mk.door_draw}")

# print(type(players['ping']))

# print(isinstance(players['ping'], Player))
# if type(players['ping']) == :
#     print('true')
# else:
#     print('false')
