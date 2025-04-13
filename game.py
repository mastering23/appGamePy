class Character:

  def __init__(self,name,guild,power,block,specialAttack,level, attackLevel):
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




player1 = Character("Max Flame","Red Guild","FireBall","Cross Block","Fire Thunder",100,20)
player2 = Character("FoxShadow","Blue Guild","Ice punch ","Ice Shield","Cold Ghost",100,20)
print("---TeSting Game Fight---\n")
player1.Attack()
player2.Block()
player1.Attack()
player2.Block()
player2.Attack()
player1.Block()
player2.SpecialAttack()
player1.Block()