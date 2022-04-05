import random

from exceptions import AgentException


class MinMax:
    def __init__(self, my_token='o'):
        self.my_token = my_token
        self.max_depth = 5

    def decide(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException('not my round')
        _, best_move = self.get_best_score_and_move(connect4, 0)
        return best_move

    def get_best_score_and_move(self, connect4, depth):
        if (depth == self.max_depth) | (connect4.check_game_over()):
            return connect4.get_score(), None
        if connect4.who_moves == self.my_token:
            best_score = -10000
        else:
            best_score = 10000
        best_move = None
        for drop in connect4.possible_drops():
            next_state = connect4.get_next_state(drop)
            state_score, _ = self.get_best_score_and_move(next_state, depth + 1)
            if (connect4.who_moves == self.my_token) & (state_score > best_score):
                best_score = state_score
                best_move = drop
            elif (connect4.who_moves != self.my_token) & (state_score < best_score):
                best_score = state_score
                best_move = drop
        return best_score, best_move
