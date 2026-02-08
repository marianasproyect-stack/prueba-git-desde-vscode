
import sympy as sp

# Definimos la variable simbólica
x = sp.Symbol('x')



#Integral indefinida
f = x**2
integral_indef = sp.integrate(f, x)
print(integral_indef)

#Integral definida
f = x**2
integral_def = sp.integrate(f, (x, 0, 2))
print(integral_def)

#Integrales más complejas
f = sp.exp(x) * sp.sin(x)
integral = sp.integrate(f, x)
print(integral)



import sympy as sp
from sympy.integrals.manualintegrate import integral_steps, manualintegrate

print("")
print("¡ INTEGRAL INDEFINIDA !")
print("")

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir la función a integrar
f = x - 2   # <-- aquí va la función

# Mostrar la función original
print("Función a integrar:")
sp.pretty_print(f)
print("")

# Mostrar los pasos del proceso de integración
print("Pasos del proceso:")
steps = integral_steps(f, x)
sp.pprint(steps, use_unicode=True)
print("")

# Calcular el resultado final de la integral
resultado = sp.integrate(f, x)

# Mostrar el resultado de manera legible
print("Resultado final:")
sp.pretty_print(resultado)

# Mostrar resultado en formato LaTeX
latex_resultado = sp.latex(resultado)
print("\nResultado en formato LaTeX:")
print(latex_resultado)
print("")
