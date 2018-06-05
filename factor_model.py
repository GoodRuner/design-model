#工厂模式
#设计一个计算器计算程序，运用工厂模式。
class Operation(object):  #设置基类
	def __init__(self):
		self._numberA = 0
		self._numberB = 0
	
	def GetNumberA(self):
		return self._numberA

	def GetNumberB(self):
		return self._numberB

	def SetNumberA(self, A):
		self._numberA = A

	def SetNumberB(self,B):
		self._numberB = B

	def GetResult(self): 
		pass


class OperationAdd(Operation): # 定义加法类
	def GetResult(self):  #重写基类的方法
		return self.GetNumberA() + self.GetNumberB()
	

class OperationSub(Operation):  # 定于减法类
	def GetResult(self):
		return self.GetNumberA() - self.GetNumberB()


class OperationMul(Operation):   # 定义乘法类
	def GetResult(self):
		return self.GetNumberA() * self.GetNumberB()


class OperationDiv(Operation):   # 定义除法类
	def GetResult(self):
		return self.GetNumberA() // self.GetNumberB()


class OperationFactory(object):  #定义操作符生产工厂
	def __init__(self):
		self.oper = None

	def CreateOperate(self, operate):
		if operate == '+':
			self.oper = OperationAdd()
		if operate == '-':
			self.oper = OperationSub()
		if operate == '*':
			self.oper = OperationMul()
		if operate == '/':
			self.oper = OperationDiv()
		return self.oper
		

oper = OperationFactory().CreateOperate('/')

oper.SetNumberA(4)
oper.SetNumberB(2)
result = oper.GetResult()
print(result)	
