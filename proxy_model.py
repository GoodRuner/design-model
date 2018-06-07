#代理模式

class Girl(object):
	def __init__(self, name):
		self.name = name

	def GetName(self):
		return self.name

	def SetName(self, newname):
		self.name = newname


class Pursuit(object):
	def __init__(self, name):
		self.girl = Girl(name)
	
	def GiveDolls(self):
		print(self.girl.GetName() + "送你洋娃娃")

	def GiveFlower(self):
		print(self.girl.GetName() + "送你鲜花")

	def GiveChocolate(self):
		print(self.girl.GetName() + "送你巧克力")


class Proxy(object):
	def __init__(self, grilname):
		self.pursuit = Pursuit(grilname)
	
	def GiveDolls(self):
		self.pursuit.GiveDolls()
	
	def GiveFlower(self):
		self.pursuit.GiveFlower()

	def GiveChocolate(self):
		self.pursuit.GiveChocolate()



	
obj = Proxy("jiaojiao")
obj.GiveDolls()		

obj.GiveFlower()
obj.GiveChocolate()
