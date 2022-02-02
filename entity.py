import math

# TODO
# 엔티티 클래스
#	1. 메소드
#		- giveDamage : 객체가 피해량 받는 함수
#		- giveHeal : 객체가 회복량 받는 함수
#		- giveExp : 객체가 경험치 받는 함수
# 몬스터 클래스
# 플레이어 클래스

class Entity:
	def __init__(self, name, level, exp, maxHp, hp, generalAttack, generalDefence):
		self.name = name
		self.level = level
		self.exp = exp
		self.maxHp = maxHp
		self.hp = hp
		self.generalAttack = generalAttack
		self.generalDefence = generalDefence
	
	def getEntityData(self):
		print("==================================================================")
		print("name : " + self.name + " Lv." + self.level)
		print("Hp : " + self.hp + "/" + self.maxHp)
		print("Exp : " + self.exp)
		print("ATK : " + self.generalAttack)
		print("==================================================================")

	def isFainted(self):
		(self.hp <=0) if True else False

#	def useGeneralAttack(self, victim):
#		damage = math.round( ( self.generalAttack * ( 1 - ( victim.generalDefence / ( 100 + victim.generalDefence ) ) ) ) )
#		if (victim.hp < damage):
#			victim.hp = 0
#		else:
#			victim.hp -= damage

#	def useGeneralDefence(self):
#		self.extraGeneralDefence += ( 0.5 * self.generalDefence )
#		self.extraDefenceCount = 1

#	def useAttackDamage(self):
#		return self.generalAttack

#	def getDamage(self, rawDamage):
		
	
#	def useDefence(self):
