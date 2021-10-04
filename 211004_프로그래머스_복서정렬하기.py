from pprint import pprint
from functools import reduce


class Score:
    def __init__(self, number, weight):
        self.number = number
        self.weight = weight
        self.wins = 0
        self.total_weight_win = 0


def solution(weights, head2head):

    scores = [Score(i + 1, weights[i]) for i in range(len(weights))]

    for person1, (score, results) in enumerate(zip(scores, head2head)):
        total_round = 0
        wins = 0
        for person2, (result, weight) in enumerate(zip(results, weights)):

            if person1 == person2:
                continue

            if result == "N":
                continue

            total_round += 1

            if result == "W":
                wins += 1
                if score.weight < weight:
                    score.total_weight_win += 1

        if total_round == 0:
            continue
        score.wins = wins / total_round

    # for score in scores:
    #     print(score.number, score.weight, score.wins, score.total_weight_win)

    sorted_scores = sorted(
        scores,
        key=lambda x: (x.wins, x.total_weight_win, x.weight, -x.number),
        reverse=True,
    )
    answer = [score.number for score in sorted_scores]
    return answer


if __name__ == "__main__":
    weights = [50, 82, 75, 120]
    head2head = ["NLWL", "WNLL", "LWNW", "WWLN"]
    print(solution(weights, head2head))