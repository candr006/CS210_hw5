
from math import *

#NOTE: This program does not take a user input for the function
def f1(x, function_num, function_type=''):
	if (function_type=="diff"):
		if(int(function_num)==1):
			return ((3*(x*x))-(2))
		if (int(function_num)==2):
			return (-1*exp(-x)-1)
		if(int(function_num)==3):
			return (sin(x)+ (x*cos(x)))
		if(int(function_num)==4):
			return (3*(x*x)-(6*x)+3)
	else:
		if(int(function_num)==1):
			return ((x*x*x)-(2*x)-5)
		if (int(function_num)==2):
			return (exp(-x)-x)
		if(int(function_num)==3):
			return (x*sin(x)-1)
		if(int(function_num)==4):
			return ((x*x*x)-(3*(x*x))+(3*x)-1)

	print('Invalid Choice. Exiting\n')
	exit(0)
	return 


def bisection_method(function_num):
	a=0
	b=0
	#initialize x
	i=1
	#error
	e=0.000001

	#evaluate for f1: #x^3-2x-5
	while 1==1:
		if i % 2 == 0:
		    a+=1
		else:
		    b+=1

		f1_a=(f1(a,function_num))
		if(f1_a==0):
			print ('Bisection Root: '+str(a))
			return
		f1_b=(f1(b,function_num))
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
		f1_x0=f1(x0,function_num)

		if((f1_a*f1_x0)<0):
			b=x0
		else:
			a=x0
			f1_a=f1_x0
		if(fabs(float((b-a)/b)) < e):
			print ('Bisection Root: '+str((a+b)/2))
			break


def newtons_method(function_num):
	if (function_num==1):
		a=-3.5
	if(function_num==2):
		a=18
	if(function_num==3):
		a=1
	if(function_num==4):
		a=0
	else:
		a=0
	#error
	e=float(0)

	while 1==1:
		f1_a=f1(a,function_num)
		f1_diff_a=f1(a,function_num,"diff") #find the derivative at the current xi guess
		if(float(f1_diff_a)==0):
			print ('ERROR. Cant find root when derivative is 0. Exiting')
			return

		else:
			x2= a-float(f1_a/f1_diff_a)
			if(fabs(float(x2-a)) <= e):
				print("Newtons Method Root: "+str(x2))
				return
			else:
				a=x2

def secant_method(function_num):
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

		f1_a=f1(a,function_num)
		if(f1_a==0):
			print ('Secant Root: '+str(a))
			return
		f1_b=f1(b,function_num)
		if(f1_b==0):
			print ('Secant Root: '+str(b))
			return
		i+=1

		if (float(f1_a*f1_b)<0):
			#found secant initial vals
			print('Secant Initial Values a: '+str(a)+' b: '+str(b))
			break

	while 1==1:
		x2=float((a*f1_b)-(b*f1_a))/float(f1_b-f1_a)
		if(f1(x2,function_num,'')==0):
			print ('Secant Root: '+str(x2))
			return
		else:
			if(float((x2-b)/x2) > e):
				a=b
				b=x2
			else:
				print ('Secant Root: '+str(x2))
				return


	#return (x*x*x)-(2*x)-5
	#return exp(-x)-x
	#return (x*sin(x))-1
	#(x*x*x)-(3*(x*x))+(3*x)-1
function_num=raw_input("Enter one of the numbers below: \n1. x^3-2x-5\n2. exp^-x = x\n3. xsin(x)-1 \n4. x^3 - 3x^2 +3x -1\n\n")

#run all 3 of the methods
bisection_method(function_num)
newtons_method(function_num)
secant_method(function_num)