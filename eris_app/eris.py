from game import Game

if __name__ == "__main__":
    munchkin = Game(game_level=10) # sets up deck 

    player_names = ['ping', 'james', 'abdul'] # this list could be generated however we like
    
    munchkin.setup_players(player_names) # sets up players and draws initial cards from the deck

    import itertools as it
    player = it.cycle([*munchkin.players.values()]) # cool built in module that allows for cycling through each player turn

    while munchkin.check_game_over(): # this checks if any body has won before calling on next player
        current_player = next(player) # next() is part of the iter module to call on next items in an iterable
        munchkin.play(current_player)

    print(f"Game Over: {current_player.name} has won the game!")