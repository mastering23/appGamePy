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
    print(f"Attack : {self.specialAttack}")
    print(f"Attack : {self.power} {self.attackLevel * 2}")
    print("-----------------------------------\n")

  def Block(self):
    print(f"Player : {self.name}")
    print(f"Block  : {self.block}")
    print("-----------------------------------\n")


player1 = Character("Max Flame", "Red Guild", "FireBall", "Cross Block", "Fire Thunder", 100, 20)
player2 = Character("FoxShadow", "Blue Guild", "Ice punch ", "Ice Shield", "Cold Ghost", 100, 20)
print("---TeSting Game Fight---\n")


# select player
def SelectPlayer():
  title = " Game  |  Python Kai \n"
  selectPlayerMessage = "Select player : "
  print(f"{title} {selectPlayerMessage}")
  op = int(input("type:"))
  if op == 1:
    return player1.name
  elif op == 2:
    return player2.name

def currentTurn(playerSelected):
  # select who go first
  currentTurnSelected  = random.randint(0,1)
  print(currentTurnSelected)

playerSelected = SelectPlayer()
print(playerSelected)
currentTurn(playerSelected)


# player1.Attack()
# player2.Block()
# player1.Attack()
# player2.Block()
# player2.Attack()
# player1.Block()
# player2.SpecialAttack()
# player1.Block()
