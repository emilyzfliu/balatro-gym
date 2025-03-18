import sys
sys.path.append('../')
from balatro_gym.balatro_game import BalatroGame, Card
from utils import *

def greedy(game: BalatroGame) -> list[Card]:
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
        
        print(game.highlighted_to_string())
        
        score = game.play_hand()
    print(game.state)
    return game.state

def top_k_epsilon_greedy(game: BalatroGame, k: int = 10) -> list[Card]:
    pass

if __name__ == "__main__":
    game = BalatroGame()
    greedy(game)