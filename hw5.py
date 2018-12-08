
from math import *
from sympy import *

#NOTE: This program does not take a user input for the function
#To change function, comment out below return expressions for f1(x), and either type in your own, 
#or replace it with one of the below return expressions
	#return (x*x*x)-(2*x)-5
	#return exp(-x)-x
	#return (x*sin(x))-1
	#(x*x*x)-(3*(x*x))+(3*x)-1
def f1(x, function_type=''):
	if (function_type!='diff'):
		return (x*x*x)-(2*x)-5
	else:
		return diff((x*x*x)-(2*x)-5,x)


def bisection_method():
	a=0
	b=0
	#initialize x
	i=1
	#error
	e=0.001

	#evaluate for f1: #x^3-2x-5
	while 1==1:
		if i % 2 == 0:
		    a+=1
		else:
		    b+=1

		f1_a=f1(a)
		if(f1_a==0):
			print ('Bisection Root: '+str(a))
			return
		f1_b=f1(b)
		if(f1_b==0):
			print ('Bisection Root: '+str(b))
			return
		i+=1

		if ((f1_a*f1_b)<0):
			#found bisection initial vals
			print('Bisection Initial Values a: '+str(a)+' b: '+str(b))
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
			print ('Bisection Root: '+str((a+b)/2))
			break


def newtons_method():
	a=0
	b=0
	#initialize i
	i=1
	#error
	e=0.001

	#evaluate for f1: #x^3-2x-5
	while 1==1:
		if i % 2 == 0:
		    a+=1
		else:
		    b+=1

		f1_a=f1(a)
		if(f1_a==0):
			print ('Newtons Method Root: '+str(a))
			return
		f1_b=f1(b)
		if(f1_b==0):
			print ('Newtons Method Root: '+str(b))
			return
		i+=1

		if ((f1_a*f1_b)<0):
			#found newton initial vals
			print('Newton Initial Values a: '+str(a)+' b: '+str(b))
			break

	while 1==1:
		f1_diff_a=f1(a,"diff") #find the derivative at the current xi guess
		if(f1_diff_a==0):
			print ('ERROR. Cant find root when derivative is 0. Exiting')
			return

		else:
			x2= a-float(f1_a/f1_diff_a)
			if(fabs(float(x2-a)) < e):
				print("Newtons Method Root: "+str(x2))
				return
			else:
				print ('Newtons Method Root: '+str(x2))
				return
			a=x2

def secant_method():
	a=0
	b=0
	#initialize i
	i=1
	#error
	e=0.001

	#evaluate for f1: #x^3-2x-5
	while 1==1:
		if i % 2 == 0:
		    a+=1
		else:
		    b+=1

		f1_a=f1(a)
		if(f1_a==0):
			print ('Secant Root: '+str(a))
			return
		f1_b=f1(b)
		if(f1_b==0):
			print ('Secant Root: '+str(b))
			return
		i+=1

		if ((f1_a*f1_b)<0):
			#found secant initial vals
			print('Secant Initial Values a: '+str(a)+' b: '+str(b))
			break

	while 1==1:
		x2=float((a*f1_b)-(b*f1_a))/float(f1_b-f1_a)
		if(f1(x2,'')==0):
			print ('Secant Root: '+str(x2))
			return
		else:
			if(float((x2-b)/x2) > e):
				a=b
				b=x2
			else:
				print ('Secant Root: '+str(x2))
				return


#run all 3 of the methods
bisection_method()
newtons_method()
secant_method()