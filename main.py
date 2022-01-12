from online_models import *
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1,1)
plt.ion()

def run(p,models,fig=fig,ax=ax):
	data = np.random.random(size=T)<p
	for model in models.values():
		model.set_record(True)
	N = 10
	for t,x in enumerate(data):
		for model in models.values():
			model.step(x)
		if t%N==N-1:
			ax.clear()
			ax.plot(p[:t+1],color='grey',label='Target')
			for name,model in models.items():
				ax.plot(model.record_arr,label=name)
			ax.set_ylim(-0.05,1.05)
			ax.set_xlabel('Iterations')
			plt.legend()
			plt.pause(.001)


T = 3*10**3

p = np.ones(T)*.75
models = {'Regular':UniformMean()}
run(p,models)
fig.savefig('RegularConstant.png')

p = (np.arange(T)>T/3)*.5+.25
models = {'Regular':UniformMean()}
run(p,models)
fig.savefig('RegularSwitch.png')

p = np.ones(T)*.75
models = {'Regular':UniformMean(),'Exponential':ExponentialMean(.02)}
run(p,models)
fig.savefig('ExponentialConstant.png')

p = (np.arange(T)>T/3)*.5+.25
models = {'Regular':UniformMean(),'Exponential':ExponentialMean(.02)}
run(p,models)
fig.savefig('ExponentialSwitch.png')


p = np.ones(T)*.75
models = {'Regular':UniformMean(),'Exponential':ExponentialMean(.02),'Root':PowerMean(.5,.02)}
run(p,models)
fig.savefig('RootConstant.png')

p = (np.arange(T)>T/3)*.5+.25
models = {'Regular':UniformMean(),'Exponential':ExponentialMean(.02),'Root':PowerMean(.5,.02)}
run(p,models)
fig.savefig('RootSwitch.png')


