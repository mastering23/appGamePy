import random

class Character:

    def __init__(self, name, guild, power, block, specialAttack, level, attackLevel):
        self.name = name
        self.guild = guild
        self.power = power
        self.block = block
        self.specialAttack = specialAttack
        self.level = level
        self.attackLevel = attackLevel

    def Attack(self):
        print(f"Player : {self.name}")
        print(f"Attack : {self.power} {self.attackLevel}")
        print("-----------------------------------\n")

    def SpecialAttack(self):
        print(f"Player : {self.name}")
        print(f"Special Attack : {self.specialAttack}")
        print(f"Attack : {self.power} {self.attackLevel * 2}")
        print("-----------------------------------\n")

    def Block(self):
        print(f"Player : {self.name}")
        print(f"Block : {self.block}")
        print("-----------------------------------\n")


player1 = Character("Max Flame", "Red Guild", "FireBall", "Cross Block", "Fire Thunder", 100, 20)
player2 = Character("FoxShadow", "Blue Guild", "Ice Punch", "Ice Shield", "Cold Ghost", 100, 20)
print("---TeSting Game Fight---\n")


def SelectPlayer():
    title = " Game  |  Python Kai \n"
    selectPlayerMessage = "Select player : \n1. Max Flame\n2. FoxShadow"
    print(f"{title}{selectPlayerMessage}")
    op = int(input("Type: "))
    if op == 1:
        return player1
    elif op == 2:
        return player2
    else:
        print("Invalid selection!")
        return SelectPlayer()


def currentTurn():
    return random.randint(0, 1)


playerSelected = SelectPlayer()
print(f"Selected Player: {playerSelected.name}")

while player1.level > 0 and player2.level > 0:
    turn = currentTurn()
    if turn == 0:
        print(f"{player1.name}'s turn:")
        move = random.choice([player1.Attack, player1.SpecialAttack, player1.Block])
        move()
        player2.level -= player1.attackLevel
    else:
        print(f"{player2.name}'s turn:")
        move = random.choice([player2.Attack, player2.SpecialAttack, player2.Block])
        move()
        player1.level -= player2.attackLevel

    print(f"{player1.name} Level: {player1.level}")
    print(f"{player2.name} Level: {player2.level}")
    print("=====================================")

if player1.level <= 0:
    print(f"{player2.name} wins!")
elif player2.level <= 0:
    print(f"{player1.name} wins!")