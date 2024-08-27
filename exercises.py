class Game():
    board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None,
    }
    
    def __init__(self, turn="X", tie=False, winner=None):
        self.turn = turn
        self.counter=0
        self.tie = tie
        self.winner = winner
        self.board = Game.board
    print("Welcome to Tic Tac Toe!")

    def Check_winner(self):
        if self.counter==8 and self.winner==None:
              self.tie=True
              print("Its TIE")
              exit()
        if (
            (self.board["a1"] is not None and self.board["a1"] == self.board["a2"] and self.board["a1"] == self.board["a3"]) or
            (self.board["b1"] is not None and self.board["b1"] == self.board["b2"] and self.board["b1"] == self.board["b3"]) or
            (self.board["c1"] is not None and self.board["c1"] == self.board["c2"] and self.board["c1"] == self.board["c3"]) or
            (self.board["a1"] is not None and self.board["a1"] == self.board["b1"] and self.board["a1"] == self.board["c1"]) or
            (self.board["a2"] is not None and self.board["a2"] == self.board["b2"] and self.board["a2"] == self.board["c2"]) or
            (self.board["a3"] is not None and self.board["a3"] == self.board["b3"] and self.board["a3"] == self.board["c3"]) or
            (self.board["a1"] is not None and self.board["a1"] == self.board["b2"] and self.board["a1"] == self.board["c3"]) or
            (self.board["c1"] is not None and self.board["c1"] == self.board["b2"] and self.board["c1"] == self.board["a3"])
        ):
            if self.turn == "X":
                self.winner = "X is the winner"
                print(self.winner)
            else:
                self.winner = "O is the winner"
                print(self.winner)
        
    def play_game(self):
        
        b = self.board
        print(f"""
          A   B   C
      1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
          ----------
      2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
          ----------
      3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

        move = input(f"Enter a valid move (example: A1): ").lower()

        if move not in self.board or self.board[move] is not None:
            print("Invalid move. Please enter a valid move.")
            self.play_game()
        else:
            self.board[move] = self.turn
            print(f"""
          A   B   C
      1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
          ----------
      2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
          ----------
      3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
            """)

           
            Game.Check_winner(self)
            if self.winner is not None:
                return
            else:
              self.turn=="O"
              if self.turn=="O" :
                self.turn="X"
                self.counter+=1
                print(self.counter)

              else: 
               self.turn="O" 
               self.counter+=1
               print(self.counter)

              self.play_game()



game_instance = Game()
game_instance.play_game()
