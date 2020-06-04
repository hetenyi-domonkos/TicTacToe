import random
import time

class Board:
    '''The board is initialized as a nine item long list and each of it's items are spaces by default for printing reasons.
   Only this gets directly modified after each move. There are eight more three element long lists which represent the three rows,
   the three columns and the two diagonals. After each move these are updated from the original list, and a method checks whether
   any of these contain the same non-space value.'''
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.top = [self.board[i] for i in range(6, 9)]
        self.mid = [self.board[i] for i in range(3, 6)]
        self.bot = [self.board[i] for i in range(3)]
        self.r = [j for i, j in enumerate(self.board) if int(i)%3 == 0]
        self.m = [j for i, j in enumerate(self.board) if int(i)%3 == 1]
        self.l = [j for i, j in enumerate(self.board) if int(i)%3 == 2]
        self.diag1 = [j for i, j in enumerate(self.board) if i%4 == 0]
        self.diag2 = [self.board[2], self.board[4], self.board[6]]
        
    def __setitem__(self, place, to_this):
        self.board[place] = to_this
        self.update()
        
    def __getitem__(self, this):
        return self.board[this]
    
    def update(self):
        self.top = [self.board[i] for i in range(6, 9)]
        self.mid = [self.board[i] for i in range(3, 6)]
        self.bot = [self.board[i] for i in range(3)]
        self.r = [j for i, j in enumerate(self.board) if i%3 == 0]
        self.m = [j for i, j in enumerate(self.board) if i%3 == 1]
        self.l = [j for i, j in enumerate(self.board) if i%3 == 2]
        self.diag1 = [j for i, j in enumerate(self.board) if i%4 == 0]
        self.diag2 = [self.board[2], self.board[4], self.board[6]]

    def checkwin(self):
        if ' ' not in self.top and len(set(self.top)) == 1:
            return True
        elif ' ' not in self.mid and len(set(self.mid)) == 1:
            return True
        elif ' ' not in self.bot and len(set(self.bot)) == 1:
            return True
        elif ' ' not in self.r and len(set(self.r)) == 1:
            return True
        elif ' ' not in self.m and len(set(self.m)) == 1:
            return True
        elif ' ' not in self.l and len(set(self.l)) == 1:
            return True
        elif ' ' not in self.diag1 and len(set(self.diag1)) == 1:
            return True
        elif ' ' not in self.diag2 and len(set(self.diag2)) == 1:
            return True
        else:
            return False
        
    def show(self):
        print(self.top[0], self.top[1], self.top[2], sep = '|')
        print('-'*5)
        print(self.mid[0], self.mid[1], self.mid[2], sep = '|')
        print('-'*5)
        print(self.bot[0], self.bot[1], self.bot[2], sep = '|')

class Enemy:
    
    def __init__(self, board = Board()):
        self.board = board

    def pick(self):
        pickable = [i for i, j in enumerate(self.board) if j == ' ']
        self.board[pickable[random.randint(0, len(pickable)-1)]] = 'x'

def game():
    '''there is an unexpected error when you choose a tile which isnt empty and on the retry you give an invalid input'''
    board = Board()
    enemy = Enemy(board)
    hort = ["heads", "tails"]
    player_choice = input("Let's toss a coin. Heads or tails?")
    while player_choice not in hort:
        player_choice = input("Invalid input! Try again: ")
    if hort[random.randint(0,1)] == player_choice:
        print("You go first!")
        while True:
            player = input("Your turn, choose a tile! (1-9): ")
            a = None
            while a != 0:
                a = 0
                while player not in [str(i) for i in range(1,10)]:
                    print("Invalid input!")
                    player = input("Try again: ")
                while board[int(player)-1] != ' ':
                    print("Invalid input!")
                    player = input("Try again: ")
                    a += 1
            board[int(player)-1] = 'O'
            board.show()
            if board.checkwin():
                print("You have won!")
                return 1
            time.sleep(1)
            print("It's the enemy's turn!")
            time.sleep(1)
            enemy.pick()
            board.show()
            if board.checkwin():
                print("You have lost!")
                return 0
    else:
        print("The enemy goes first!")
        time.sleep(1)
        while True:
            print("It's the enemy's turn!")
            time.sleep(1)
            enemy.pick()
            board.show()
            if board.checkwin():
                print("You have lost!")
                return 0
            player = input("Your turn, choose a tile! (1-9): ")
            a = None
            while a != 0:
                a = 0
                while player not in [str(i) for i in range(1,10)]:
                    print("Invalid input!")
                    player = input("Try again: ")
                while board[int(player)-1] != ' ':
                    print("Invalid input!")
                    player = input("Try again: ")
                    a += 1
            board[int(player)-1] = 'O'
            board.show()
            if board.checkwin():
                print("You have won!")
                return 1
            time.sleep(1)

def tournament():
    player_wins = 0
    enemy_wins = 0
    while player_wins + enemy_wins < 5:
        if player_wins + enemy_wins != 0:
            if input("Do you want to continue playing? Press q to quit or press anything else to continue") == 'q':
                break
        print(f"The score is {player_wins}:{enemy_wins}")
        a = game()
        if a == 1:
            player_wins += 1
        else:
            enemy_wins += 1
    if player_wins > enemy_wins:
        print(f"Good job, you won the tournament! The final score is {player_wins}:{enemy_wins}")
    else:
        print(f"You have lost the tournament, netter luck next time! The final score is {player_wins}:{enemy_wins}")
    time.sleep(1)
	
def pvp():
    board = Board()
    marks = ['x','O']
    i = 0
    while True:
        player = input(f"Player {(i%2)+1}'s turn, choose a tile! (1-9): ")
        a = None
        while a != 0:
            a = 0
            while player not in [str(i) for i in range(1,10)]:
                print("Invalid input!")
                player = input("Try again: ")
            while board[int(player)-1] != ' ':
                print("Invalid input!")
                player = input("Try again: ")
                a += 1
        board[int(player)-1] = marks[i%2]
        board.show()
        if board.checkwin():
            print(f"Player {(i%2)+1} has won!")
            return 1
        i += 1

def main():
    first_time = True
    while True:
        if first_time:
            print("Welcome! How would you like to play?")
            first_time = False
        else:
            print("Do you still want to play?")
        print("Type 'tournament' to play a tournament against the computer",
        "Type 'game' to play a simple game against the computer",
        "Type 'pvp' to play against a friend",
        "Type 'e' to exit the game", sep="\n")    
        playmode = input("")
        while playmode not in ["tournament","game","pvp",'e']:
            playmode = input("Invalid input! Try again: ")
        if playmode == 'e':
            print("Goodbye!")
            break
        else:
            exec(f"{playmode}()")
        
main()
