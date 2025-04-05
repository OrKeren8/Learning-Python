import json
from typing import Generator
import sys

weights = {"rock": 2, "paper": 1, "scissors": 0}

def results(results_filename) -> Generator[str, None, None]:
    """get all of the 1v1 rps game results from a file
    
    Args:
        results_filename: path to the results file
    
    Returns: list of a list with the results of each match in the format:
            [player1, player1-choice, player2, player2-choice]
    """
    try:
        with open(results_filename, 'r', encoding='utf-8') as results_file:
            good_header = "player1 player1-choice player2 player2-choice\n"
            if results_file.readline() != good_header:
                raise FileNotFoundError("file does not have the right header")
            for result_line in results_file:
                result = result_line.split()
                yield result
    except FileNotFoundError as e:
        print(f"file does not exist: {e}")
        sys.exit()

def game(results_filename: str) -> str:
    """checks who is the winning player in rps game
    
    Args:
        results_filename: path to the file with all of the 1v1 rps games
    
    Returns: the name of the highest percentage winning player or "tie" if there is no only one winner
    """
    print(f'starting the game with {results_filename}')
    scores = {}
    matches_count = {}
    for result in results(results_filename):
        matches_count[result[0]] = matches_count.get(result[0], 0) + 1
        matches_count[result[2]] = matches_count.get(result[2], 0) + 1
        score = weights[result[1]] - weights[result[3]]
        match score:
            case 1 | -2:
                scores[result[2]] = scores.get(result[2], 0) + 1
            case -1 | 2:
                scores[result[0]] = scores.get(result[0], 0) + 1
    for key in scores.keys():
        scores[key] = scores[key] / matches_count[key]
    sorted_winners = sorted(scores, key=scores.get, reverse=True)
    if scores[sorted_winners[0]] > scores[sorted_winners[1]]:
        winner = sorted_winners[0]
    else:
        winner = "tie"
    return winner

students = {'id1': '315155531', 'id2': '000000000'}

if __name__ == '__main__':
    with open('config-rps.json', 'r') as json_file:
        config = json.load(json_file)
    winner = game(config['results_filename'])
    print(f'the winner is: {winner}')
