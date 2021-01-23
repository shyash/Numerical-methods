import math

def bisection(f,precision,a,b):
	iteration = 0
	while True:

		iteration += 1
		x = (a+b) / 2
		fx = f(x)

		print(f"x{iteration} = {a:.6f} + {b:.6f} / 2\n\t= {x:.6f}\nf(x{iteration}) = {fx:.6f}\n")

		if areNear(x,a,precision) or areNear(x,b,precision) or isPrecise(fx,precision): 
			print(f"The root of the equation is {x :.6f}\n")
			break


		if fx < 0: 
			a = x
		elif fx > 0:
			b = x

def areNear(a,b,precision):
	return math.floor(a * 10 ** precision) == math.floor(b * 10 ** precision)

def isPrecise(n,precision):
	return abs(n) * 10 ** precision < 1


def q1(x):
	return x**3 - x - 1

def q2(x):
	return x**4-4*x-9

# bisection(q1, 4, 1.3, 1.4)
bisection(q2, 4, 2.03,2.04)
