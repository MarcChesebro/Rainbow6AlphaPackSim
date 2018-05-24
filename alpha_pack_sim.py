import random

_inc_ = .023
_total_packs_ = 10000
_win_rate_ = 0.5


def game(chance):
    win_attempt = random.uniform(0, 1)
    if _win_rate_ > win_attempt:
        return roll(chance)
    return False


def roll(chance):
    roll = random.uniform(0, 1)
    if chance > roll:
        return True
    return False


if __name__ == '__main__':

    total_games = 0
    attempts_till_suc = []
    chance_at_suc = []

    for _ in range(_total_packs_):
        attempt = 1
        total_games = total_games + 1
        chance = _inc_

        while not game(chance):
            chance = chance + _inc_
            attempt = attempt + 1
            total_games = total_games + 1

        attempts_till_suc.append(attempt)
        chance_at_suc.append(chance)

    print("total games: {}".format(total_games))
    print("average games to win a pack, after {} tests. packs: {}".format(_total_packs_, sum(attempts_till_suc) / len(attempts_till_suc)))
    print("average alpha pack chance after {} tests. chance: {}".format(_total_packs_, sum(chance_at_suc) / len(chance_at_suc)))
