import sys
sys.path.append('.')
from balatro_gym.balatro_game import BalatroGame, Card
from utils import *

# Because discarding adds zero reward, the greedy approach is to play the best hand possible
def greedy(game: BalatroGame, verbose: bool = True) -> list[Card]:
    # A pure greedy approach has a 5% win rate in the first round.
    while game.state == BalatroGame.State.IN_PROGRESS:
        all_hand_indices = enumerate_possible_hand_indices(game.hand_size)
        best_score = 0
        best_hand = []
        for hand_indices in all_hand_indices:
            score = game._evaluate_hand([game.deck[game.hand_indexes[card_index]] for card_index in hand_indices])
            if score > best_score:
                best_score = score
                best_hand = hand_indices

        for card_index in best_hand:
            game.highlight_card(card_index)
        
        if verbose:
            print('Current hand:', game.hand_to_string())
            print('Best hand:', game.highlighted_to_string())
        
        score = game.play_hand()
        if verbose:
            print('Score:', score)
    # print(game.state)
    return game.state

def top_k_epsilon_greedy(game: BalatroGame, k: int = 10) -> list[Card]:
    pass

if __name__ == "__main__":
    n_trials = 100
    wins = 0
    losses = 0
    for _ in range(n_trials):
        game = BalatroGame()
        greedy(game, verbose=False)
        if game.state == BalatroGame.State.WIN:
            wins += 1
        else:
            losses += 1
    print('Wins:', wins, 'Losses:', losses)
