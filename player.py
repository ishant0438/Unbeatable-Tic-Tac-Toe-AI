import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # Randomly choose a square if the board is empty
            square = random.choice(game.available_moves())
        else:
            # Use minimax to find the best move
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # Your AI's letter
        other_player = 'O' if player == 'X' else 'X'

        # Base case: Check for a winner or no empty squares
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
            }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # Initialize best score for maximizer and minimizer
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximizing player
        else:
            best = {'position': None, 'score': math.inf}  # Minimizing player

        for possible_move in state.available_moves():
            # Make the move
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Simulate a game after making the move

            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # Keep track of the move

            # Update the best score based on maximizer or minimizer
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

                         
                
                            
                                 