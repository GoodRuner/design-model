#策略模式，和工厂模式相似程度很大，但是耦合程度小于工厂模式。

class StrategeA(object):
	def Agri(self):
		print('完成算法A的执行过程')


class StrategeB(object):
	def Agri(self):
		print('完成算法B的执行过程')


class StrategeC(object):
	def Agri(self):
		print('完成算法C的执行过程')


class StrategeCenter(object):
	def __init__(self):
		self.obj = None
		self.stratege_list = ['A', 'B', 'C']

	def CreateStratege(self, stratege):
		if stratege in self.stratege_list:
			if stratege == 'A':
				self.obj = StrategeA()
			if stratege == 'B':
				self.obj = StrategeB()
			if stratege == 'C':
				self.obj = StrategeC()
			self.GetResult()
	def GetResult(self):
		self.obj.Agri()



obj = StrategeCenter().CreateStratege('A')	
