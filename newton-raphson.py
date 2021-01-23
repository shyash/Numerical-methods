import math

def newton_raphson(f,fd,precision,x0):
	iteration = 0
	print(f"x0 = {x0}\n")
	while True:
		iteration += 1
		fx0 = f(x0)
		fdx0 = fd(x0)  
		x = x0 - (fx0/fdx0) 
		fx = f(x) 
		print(f"f(x{iteration-1}) = {fx0:.6f}, f'(x{iteration-1}) = {fdx0:.6f}\n")
		print(f"x{iteration} = x{iteration-1} - {fx0:.6f}\n\t  ---------\n\t  {fdx0:.6f}")
		print(f"\n\t = {x:.6f}\n")
		if areNear(x,x0,precision) or isPrecise(fx,precision): 
			print(f"The root of the equation is {x :.6f}\n")
			break
		
		x0 = x

		
def areNear(a,b,precision):
	return math.floor(a * 10 ** precision) == math.floor(b * 10 ** precision)

def isPrecise(n,precision):
	return abs(n) * 10 ** precision < 1


def q1(x):
	return x**4 - x - 10

def q1d(x):
	return 4*x**3 - 1
	
def q2(x):
	return (x-1)*math.sin(x) - x - 1
def q2d(x):
	return math.sin(x) + x * math.cos(x) -  math.cos(x) - 1

def q3(x):
	return math.exp(-x) - math.sin(x)

def q3d(x):
	return -math.exp(-x) - math.cos(x)

def q4(x):
	return math.tan(x) - x

def q4d(x):
	return math.tan(x)**2

def q5(x):
	return x**2 - 12

def q5d(x):
	return 2*x

# newton_raphson(q1, q1d, 6, 1.85) 
# newton_raphson(q2, q2d, 4, 0)  
# newton_raphson(q3, q3d, 4, 0)
# newton_raphson(q4, q4d, 5, 4.5)
newton_raphson(q5, q5d, 4, 3.5)