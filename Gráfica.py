import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ Definir la variable y la función
x = sp.Symbol('x')
f = x**2

# 2️⃣ Calcular la integral definida
resultado = sp.integrate(f, (x, 0, 2))
print("Resultado simbólico:")
sp.pretty_print(resultado)
print("Resultado numérico:", float(resultado))

# 3️⃣ Crear los datos para la gráfica
# Usamos numpy para generar puntos en el eje x
x_vals = np.linspace(0, 2, 200)
# Convertimos la función simbólica de sympy a función numérica para graficarla
f_lambd = sp.lambdify(x, f, 'numpy')
y_vals = f_lambd(x_vals)

# 4️⃣ Graficar
plt.figure(figsize=(7,5))
plt.plot(x_vals, y_vals, label='f(x) = x²', color='blue')
plt.fill_between(x_vals, y_vals, 0, where=(x_vals >= 0) & (x_vals <= 2),
                 color='skyblue', alpha=0.4, label='Área bajo la curva (∫₀² x² dx)')
plt.title('Integral definida de f(x) = x² entre 0 y 2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

#Soy una linea creada desde main