class Entity:
	def __init__(self, name, level, exp, maxHp, hp, generalAttack, generalDefence, skillPoint=0):
		self.name = name
		self.level = level
		self.exp = exp
		self.maxHp = maxHp
		self.hp = hp
		self.generalAttack = generalAttack
		self.generalDefence = generalDefence
		self.skillPoint = skillPoint
	
	def getEntityData(self):
		print("name : " + self.name + " Lv." + self.level)
		print("Hp : " + self.hp + "/" + self.maxHp)
		print("Exp : " + self.exp)
		print("")

	def isFainted(self):
		(self.hp <=0) if True else False

	def attack(self, victim):
		if (self.generalAttack <= victim.generalDefence):
			print(self.name + "의 공격!")