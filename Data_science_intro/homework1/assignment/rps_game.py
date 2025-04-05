import json
from typing import Dict

weights = {"rock": 2, "paper": 1, "scissors": 0}

def results(results_filename):
    with open(results_filename, 'r', encoding='utf-8') as results_file:
        good_header = "player1 player1-choice player2 player2-choice\n"
        if results_file.readline() != good_header:
            raise FileExistsError("file does not have the right header")
        for result_line in results_file:
            result = result_line.split()
            yield result

def game(results_filename):
    scores: Dict[str, int] = {}
    print(f'starting the game with {results_filename}')
    for result in results(results_filename):
        score = weights[result[1]] - weights[result[3]]
        match score:
            case 1 | -2:
                scores[result[2]] = scores.get(result[2], 0) + 1
            case -1 | 2:
                scores[result[0]] = scores.get(result[0], 0) + 1
            case 0:
                scores["tie"] = scores.get("tie", 0) + 1
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
