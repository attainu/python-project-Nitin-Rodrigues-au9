import random
import time
import sys


class welcome:

    def welcome_msg(self):
        msg = """
    Welcome to Snake and Ladder Game.

    Rules:
      1. Initally  the players are at starting position i.e. 0. 
                Take it in turns to roll the dice. 
                Move forward when dice is rolled.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. If Player gets 6 will get one more chance to roll the dice.
      5. The first player to get to the FINAL position i.e 100 is the winner.
      6. Hit enter to roll the dice. if You Are choosing manual mode.

    """
        print(msg)


class Player:

    FLAG = True
    snake = {88: 24, 36: 6, 62: 18, 97: 78, 95: 56, 48: 26, 32: 10}
    ladder = {8: 10, 4: 14, 28: 74, 21: 42, 88: 96, 71: 92, 50: 67}
    Players_names = []  # here players names will be appended

    def __init__(self, nums):    # constructor for number of players
        self.nums = nums
        self.Player_position = [0]*self.nums

    # initialising the player names in a list
    def playerlist(self):
        if self.nums in range(2, 5):
            for i in range(self.nums):
                Player.Players_names.append(input("Pls Enter the  Names:"))

            for i in range(self.nums):
                print(Player.Players_names[i], end=",")
            sys.stdout
            print("are the players")
            print()
            print("lets start the Game......")
        else:
            print("Pls enter the valid number of player between 2 to 5")
            sys.exit(1)

    # Displaying the player Names for each turn
    def disp_p(self, i):

        time.sleep(1)
        print()
        print(self.Players_names[i]+"'s turn")
        return

    # updating the position of each player in a list
    def position_Update(self, i, pos):
        self.Player_position[i] = self.Player_position[i]+pos

        # here code will decrement the postion if it crosses 100.
        if self.Player_position[i] > 100:
            self.Player_position[i] = self.Player_position[i] - pos
            print("Lets win game,u need", 100-self.Player_position[i], "more")
            Npos = self.Player_position[i]
            return Npos

        # This code for snake bite.
        elif self.Player_position[i] in self.snake:
            self.FLAG = False
            msg1 = ["Oh!got snake",
                    "snake bite back to pavillion",
                    "Oh!snake bitten me",
                    "Oh!no its snake bite",
                    "OMG Snake bite"]
            snake = self.Player_position[i]
            print(random.choice(msg1))
            self.Player_position[i] = self.snake[self.Player_position[i]]
            Npos1 = self.Player_position[i]
            print()
            print(self.Players_names[i], "moved down from", snake, "to", self.Player_position[i])
            return Npos1

        # This code is for ladder.
        elif self.Player_position[i] in self.ladder:
            self.FLAG = False
            msg2 = ["i am on ladder and flying ",
                    "yeyy i got the jump",
                    "Woooooo, i am climbing ladder",
                    "lets rock ladder for rescue",
                    "oooo i got ladder"]
            print(random.choice(msg2))
            ladder = self.Player_position[i]
            self.Player_position[i] = self.ladder[self.Player_position[i]]
            Npos1 = self.Player_position[i]
            print()
            print("and", self.Player_position[i], "moved up from", ladder, "to", self.Player_position[i])
            return Npos1

        # This will return the same position.
        else:
            Npos = self.Player_position[i]
            return Npos

    # Dice will be rolled here
    def diceval(self):
        print()
        print("Dice is rolling.......")
        time.sleep(1)
        dicevalue = random.randint(1, 6)
        return dicevalue

    # Position of each player acces to update in the list.
    def poss(self, i, dicevalue):
        time.sleep(1)
        Npos = self.position_Update(i, dicevalue)

        # This code is for dice value 6,if player gets dice 6 then player will given one more chance to roll the dice.
        while dicevalue == 6:
            print()
            print("dice value is", 6, "and", self.Players_names[i], "got one more chance to roll the dice")
            dicevalue = self.diceval()
            Npos = self.position_Update(i, dicevalue)
        return Npos

    # Check if the player has won or not
    def check(self, pos, i):
        if pos in self.Player_position:
            print()
            print(self.Players_names[i], "has won")
            sys.exit(1)

        else:
            return

    def manual(self, c):
        if c == 1:
            print(input("pls press enter the button to roll out the dice :"))
        else:
            return


welcome.welcome_msg(1)
P = Player(int(input("pls enter number of player to be played:")))
P.playerlist()
print()
Control = int(input("pls enter 1 for User Mode or 2 for Computer Mode=:"))
Npos = 0
run = True

while run:
    for i in range(P.nums):
        P.disp_p(i)
        P.manual(Control)
        dicevalue = P.diceval()
        time.sleep(1)
        print("its", dicevalue)
        oldpos = P.Player_position[i]
        Npos = P.poss(i, dicevalue)
        print()

        if P.FLAG == True:

            print(P.Players_names[i], "is Moved from", oldpos, "to", P.Player_position[i])
            print()
            time.sleep(1)
            print("Players ",P.Players_names,"'s position accordingly in the list are" , P.Player_position)

        else:

            time.sleep(1)
            print("Players ", P.Players_names, "'s position accordingly in the list are", P.Player_position)
            P.check(100, i)
            FLAG = True
