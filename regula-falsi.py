import math

def regula_falsi(f,precision,a,b):
	iteration = 0
	while True:
		iteration += 1
		fa = f(a)
		fb = f(b)

		x = (a*fb - b*fa) / (fb-fa)
		fx = f(x)
		print(f"a: {a:.6f}, b: {b:.6f}, f(a): {fa:.6f}, f(b): {fb:.6f}\n")
		print(f"x{iteration} = ({a:.6f} x {fb:.6f}) - ({fa:.6f} x {b:.6f})\n\t------------------------------------\n\t\t{fb:.6f} - {fa:.6f}\n\n\t= {x:.6f}\n\nf(x{iteration}) = {fx:.6f}\n")

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
	return x**3 - 4*x - 9

def q2(x):
	return x*math.exp(x) - 2

def q3(x):
	return x*math.log(x,10)-2

# regula_falsi(q1, 5, 2.7,2.8) 
# regula_falsi(q2, 4, 0.8,0.9) 
regula_falsi(q3, 5, 1,10) 
