from math import log

class OnlineAlgorithm:
	def __init__(self):
		self.reset()
	def reset(self):
		self.count = 0
		self.reset_record()
	def step(self,x):
		self.update_rule(x)
		self.count += 1
		if self.recording:
			self.record()
	def set_record(self,bool):
		self.recording = bool
	def reset_record(self):
		self.record_arr = []

class BaseMean(OnlineAlgorithm):
	def reset(self):
		super().reset()
		self.mean = 0
	def convex_update(self,x,p):
		self.mean = (1.-p)*self.mean + p*x
	def record(self):
		self.record_arr.append(self.mean)

class UniformMean(BaseMean):
	def __init__(self):
		super().__init__()
	def update_rule(self,x):
		p = 1./(self.count + 1)
		self.convex_update(x,p)

class ExponentialMean(BaseMean):
	def __init__(self,p):
		super().__init__()
		self.p = p
	def update_rule(self,x):
		if self.count==0:
			self.mean = x
		else:
			p = self.p
			self.convex_update(x,p)

class PowerMean(BaseMean):
	def __init__(self,p,kappa=1.):
		super().__init__()
		self.p = p
		self.kappa = kappa
	def update_rule(self,x):
		p = (self.kappa/(self.count + self.kappa))**self.p
		self.convex_update(x,p)

class LogMean(BaseMean):
	def __init__(self,gamma):
		super().__init__()
		self.gamma = gamma
	def update_rule(self,x):
		p = 1./(log(self.count+self.gamma)/log(self.gamma))
		self.convex_update(x,p)



