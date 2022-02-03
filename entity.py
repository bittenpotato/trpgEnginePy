import math

# TODO
# 몬스터 클래스
# 플레이어 클래스

class Entity:
	def __init__(self, name, level, maxHp, hp, generalAttack, generalDefence, magicalAttack, magicalDefence, skillPoint):
		self.name = name
		self.level = level
		self.exp = exp
		self.maxHp = maxHp
		self.hp = hp
		self.generalAttack = generalAttack
		self.generalDefence = generalDefence
		self.magicalAttack = magicalAttack
		self.magicalDefence = magicalDefence
		self.skillPoint = skillPoint
	
	def getEntityData(self):
		print("==================================================================")
		print("name : " + self.name + " Lv." + self.level)
		print("Hp : " + self.hp + "/" + self.maxHp)
		print("Exp : " + self.exp)
		print("ATK : " + self.generalAttack)
		print("DEF : " + self.generalDefence)
		print("MTK : " + self.magicalAttack)
		print("MEF : " + self.magicalDefence)
		print("SP : " + self.skillPoint)
		print("==================================================================")

	def isFainted(self):
		(self.hp <=0) if True else False
		
	def giveGeneralDamage(self, rawDamage):
		damage = math.round( ( rawDamage * ( 1 - ( self.generalDefence / ( 100 + self.generalDefence ) ) ) ) )
		if (self.hp < damage):
			self.hp = 0
		else:
			self.hp -= damage

	def giveMagicalDamage(self, rawDamage):
		damage = math.round( ( rawDamage * ( 1 - ( self.magicalDefence / ( 100 + self.magicalDefence ) ) ) ) )
		if (self.hp < damage):
			self.hp = 0
		else:
			self.hp -= damage

	def giveHeal(self, healRate):
		if (self.maxHp < ( self.hp + healRate ) ):
			self.hp = self.maxHp
		else:
			self.hp += healRate
