
from math import *

#NOTE: This program does not take a user input for the function
def f1(x, function_num, function_type=''):
	if (function_type=="diff"):
		if(int(function_num)==1):
			return float((3*(x*x))-(2))
		if (int(function_num)==2):
			return float(-1*exp(-x)-1)
		if(int(function_num)==3):
			return float(sin(x)+ (x*cos(x)))
		if(int(function_num)==4):
			return float((3*(x*x))-(6*x)+3)
	else:
		if(int(function_num)==1):
			return float((x*x*x)-(2*x)-5)
		if (int(function_num)==2):
			return float(exp(-x)-x)
		if(int(function_num)==3):
			return float(x*sin(x)-1)
		if(int(function_num)==4):
			return float((x*x*x)-(3*(x*x))+(3*x)-1)

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
	error_list=[]

	#evaluate for f1: #x^3-2x-5
	while 1==1:
		if i % 2 == 0:
		    a+=1
		else:
		    b+=1

		f1_a=(f1(a,function_num))
		if(f1_a==0):
			print ('Bisection Root: '+str(a))
			print('\n\n\n')
			return
		f1_b=(f1(b,function_num))
		if(f1_b==0):
			print ('Bisection Root: '+str(b))
			print('\n\n\n')
			return
		i+=1
		if ((f1_a*f1_b)<0):
			#found bisection initial vals
			#print('Bisection Initial Values a: '+str(a)+' b: '+str(b))
			break

	while 1==1:
		x0=float((a+b)/2)
		f1_x0=f1(x0,function_num)

		if((f1_a*f1_x0)<0):
			b=x0
		else:
			a=x0
			f1_a=f1_x0
		error_list.insert(0,fabs(float((b-a)/b)))
		if(fabs(float((b-a)/b)) < e):
			if(len(error_list)>2):
				r=float(log(error_list[1]/error_list[2])/log(error_list[0]/error_list[1]))
				print("Bisection Rate of Convergence at end:"+str(r))
			print ('Bisection Root: '+str((a+b)/2))
			print('\n\n\n')
			break


def newtons_method(function_num):
	if (int(function_num)==1):
		a=-3.5
	elif(int(function_num)==2):
		a=18
	elif(int(function_num)==3):
		a=1
	elif(int(function_num)==4):
		a=0
	else:
		a=0
	#error
	e=0.00001
	error_list=[]
	i=0
	while 1==1:
		i+=1
		f1_a=f1(a,function_num)
		f1_diff_a=f1(a,function_num,"diff") #find the derivative at the current xi guess
		#print("Der "+str(i)+' '+str(f1_diff_a)+' a:'+str(a))
		if(float(f1_diff_a)==0):
			print ('ERROR. Cant find root when derivative is 0. Exiting')
			return
		else:
			x2= float(a)-float(f1_a/f1_diff_a)
			error_list.insert(0,fabs(float(x2-a)))

			if(fabs(float(x2-a)) <= float(e)):
				if(len(error_list)>2):
					r=float(log(error_list[1]/error_list[2])/log(error_list[0]/error_list[1]))
					print("Newtons Method Rate of Convergence at end :"+str(r))
				print("Newtons Method Root: "+str(x2))
				print('\n\n\n')
				return
			else:
				a=x2

def secant_method(function_num):
	a=0
	b=0
	#initialize i
	i=1
	#error
	e=0.00001
	error_list=[]

	if (int(function_num)==1):
		a=.82
		b=2
	elif(int(function_num)==2):
		a=18.0
		b=20.0
	elif(int(function_num)==3):
		a=-9.5
		b=-6.5
	elif(int(function_num)==4):
		a=2
		b=1


	while 1==1:
		f1_a=f1(a,function_num)
		f1_b=f1(b,function_num)
		x2=float((a*f1_b)-(b*f1_a))/float(f1_b-f1_a)
		if(float(f1(x2,function_num))==float(0)):
			print ('Secant Root: '+str(x2))
			return
		else:
			if(fabs(float((x2-b)/x2)) > e):
				error_list.insert(0,float((x2-b)/x2))
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