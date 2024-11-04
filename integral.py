from sympy import symbols, integrate, Abs
x = symbols('x')
function = 3**x - x**3 - 1
A1 = integrate(Abs(function), (x, 0, 2))
A2 = integrate(Abs(function), (x, 2, 3))
print(f"A1 = {float(A1)}\nA2 = {float(A2)}\nAT = {float(A1 + A2)}")