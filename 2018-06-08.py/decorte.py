#装饰起模式
#层层装饰，一层套一层
class Person(object):
	def __init__(self, name):
		self.name = name
	
	def show(self):
		print("装饰的是" + self.name)

class Finery(Person):
	def __init__(self):
		self.obj = None

	def Decorate(self, obj):
		self.obj = obj
		
	def show(self):
		if self.obj != None:
			self.obj.show()	

class Tshrits(Finery):
	def show(self):
		print("衬衫")
		super().show()


class BigTrouser(Finery):
	def show(self):
		print("垮裤")
		super().show()

class WearTie(Finery):
	def show(self):
		print("领带")
		super().show()

class WearLeathershoes(Finery):
	def show(self):
		print("皮鞋")
		super().show()
print("0.111")

pe = Person("caicai")

print("1111")
dtx = BigTrouser()
kk = WearTie()
pqx = WearLeathershoes()

print("2222")
dtx.Decorate(pe)
kk.Decorate(dtx)
pqx.Decorate(kk)

pqx.show()


