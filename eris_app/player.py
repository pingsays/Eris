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