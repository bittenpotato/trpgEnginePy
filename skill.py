# TODO
#   - 멤버 변수
#		- damage : 피해량
#		- heal : 회복량
#		- effect : 효과 (리스트)
#		- environment : 환경
#	- 메소드
#		- getDamage : 피해량 계산 함수
#		- getHeal : 회복량 계산 함수
# 		- getEffect : 효과 전달 함수
#		- getEnvironment : 환경 전달 함수

class Skill():
	def __init__(self, damage):
		self.damage = damage
	
	def getDamage(self):
		return self.damage
