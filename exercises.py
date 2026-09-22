class Game:
    def __init__(
        self,
        turn="X",
        tie=False,
        winner=None,
    ):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        }

    def play_game(self):
        print("Shall we play a game?")
        self.print_board()

    def print_message(self):
        if self.tie == True:
            print("Tie Game")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)


game_instance = Game()
game_instance.play_game()
