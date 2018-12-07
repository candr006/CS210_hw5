
from math import *

#x^3-2x-5
def f1(x):
	return (x*x*x)-(2*x)-5

#To change function, comment out above return expression, and either type in your own, or uncomment one of the below expressions
	#return math.exp(-x)-x
	#return (x*math.sin(x))-1
	#(x*x*x)-(3*(x*x))+(3*x)-1


#e^-x-x
def f2(x):
	return math.exp(-x)-x

#xsin(x)-1
def f3(x):
	return (x*math.sin(x))-1

#x^3-3x+3x-1
def f4(x):
	return (x*x*x)-(3*(x*x))+(3*x)-1

def bisection():
	a=0
	b=0
	#initialize x
	i=1
	#error
	e=0.00000000001

	#evaluate for f1: #x^3-2x-5
	while 1==1:
		if i % 2 == 0:
		    a+=1
		else:
		    b+=1

		f1_a=f1(a)
		f1_b=f1(b)
		i+=1

		if ((f1_a*f1_b)<0):
			#found bisection initial vals
			print('Bisection Initial a: '+str(a)+' b: '+str(b))
			break

	while 1==1:
		x0=float((a+b)/2)
		f1_x0=f1(x0)

		if(f1_a*f1_x0)<0:
			b=x0
		else:
			a=x0
			f1_a=f1_x0
		if(fabs(float((b-a)/b)) < e):
			print ('Root: '+str((a+b)/2))
			break



	

bisection()