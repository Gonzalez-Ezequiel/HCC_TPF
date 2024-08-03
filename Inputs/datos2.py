from manim import *

eq1 = MathTex("P(x)=", "a", "x^3+", "b", "x^2+", "c", "x+", "d", color="white")

for i in range(1, 9, 2):
    eq1[i].set_color("red")  # defino color rojo para los parametros
recta = [MathTex("y=f'(x)(x-x_0)+f(x_0)", color="white"), [-5, -1.2, 0], 0.7, 0]  # ec recta tangente

funcion= "x**3+1"

d = [None] * 4
t = [None] * 4

# funcion inicial
for i in range(0, 4):
    d[i] = DecimalNumber(0)
    t[i] = ValueTracker(0)
    # Capturar el valor de i en el lambda usando un argumento predeterminado
    d[i].add_updater(lambda z, t=t[i]: z.set_value(t.get_value()))
    d[i].move_to(np.array([-5.2, 2.7 - 0.5 * i, 0])).set_color("red").scale(0.7)

a = MathTex("a=", color="white").move_to(np.array([-6, 2.7, 0])).scale(0.7)
b = MathTex("b=", color="white").move_to(np.array([-6, 2.2, 0])).scale(0.7)
c = MathTex("c=", color="white").move_to(np.array([-6, 1.7, 0])).scale(0.7)
e = MathTex("d=", color="white").move_to(np.array([-6, 1.2, 0])).scale(0.7)
