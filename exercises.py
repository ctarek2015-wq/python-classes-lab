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
        while not self.winner and not self.tie:
            self.print_board()
            self.print_message()
            self.get_move()
            self.check_winner()
            if not self.winner and not self.tie:
                self.switch_turn()
                continue
            self.print_board()
            self.print_message()
            break

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

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if move == "quit":
                break
            if move not in self.board or self.board[move] is not None:
                print("Invalid move. Try again.")
                continue
            self.board[move] = self.turn
            break

    def check_winner(self):
        b = self.board
        lines = [
            [b["a1"], b["b1"], b["c1"]],
            [b["a2"], b["b2"], b["c2"]],
            [b["a3"], b["b3"], b["c3"]],
            [b["a1"], b["a2"], b["a3"]],
            [b["b1"], b["b2"], b["b3"]],
            [b["c1"], b["c2"], b["c3"]],
            [b["a1"], b["b2"], b["c3"]],
            [b["a3"], b["b2"], b["c1"]],
        ]
        for line in lines:
            if line[0] and line[0] == line[1] == line[2]:
                self.winner = line[0]
                return
        if all(value is not None for value in b.values()):
            self.tie = True

    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"


game_instance = Game()
game_instance.play_game()
