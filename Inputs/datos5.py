from manim import *

eq1 = [
	MathTex("d=2", color="white").move_to([0, 1.5, 0]),
	MathTex("d=2", color="white").move_to([6, 3.3, 0]).scale(0.75),
	MathTex("d=2", color="white").move_to([5, 3.3, 0]).scale(0.6)
]

eq2 = [
	MathTex("8a+4b+2c+d=0", color="white").move_to([0, 0.5, 0]),
	MathTex("8a+4b+2c+d=0", color="white").move_to([0, 0.5, 0]),
	MathTex("8a+4b+2=0", color="white").move_to([0, 0.5, 0]),
	MathTex("8a+4b=-2", color="white").move_to([0, 0.5, 0]),
	MathTex("8a+4b=-2", color="white").move_to([-5, 3.3, 0]).scale(0.6)
]

eq3 = [
	MathTex("c=0", color="white").move_to([0, -0.5, 0]),
	MathTex("c=0", color="white").move_to([6, 2.9, 0]).scale(0.75),
	MathTex("c=0", color="white").move_to([5, 3, 0]).scale(0.6)
]

eq4 = [
	MathTex("12a+4b+c=0", color="white").move_to([0, -1.5, 0]),
	MathTex("12a+4b+c=0", color="white").move_to([0, -0.5, 0]),
	MathTex("12a+4b=0", color="white").move_to([0, -0.5, 0]),
	MathTex("12a+4b=0", color="white").move_to([-5, 2.9, 0]).scale(0.6)
]

nro1 = [
	Text("(1)",color="white").move_to([3,1.5,0]).scale(0.5),
	Text("(1)",color="white").move_to([3,0.5,0]).scale(0.5),
	Text("(1)",color="white").move_to([-3.4,3.3,0]).scale(0.3)
]

nro2 = [
	Text("(2)",color="white").move_to([3,0.5,0]).scale(0.5),
	Text("(2)",color="white").move_to([3,-0.5,0]).scale(0.5),
	Text("(2)",color="white").move_to([-3.4,2.9,0]).scale(0.3)
]


nro3 = [
	Text("(3)",color="white").move_to([3,-0.5,0]).scale(0.5)
]

nro4= [
	Text("(4)",color="white").move_to([3,-1.5,0]).scale(0.5)
]

s = [
	Square(side_length=3.6).move_to([-3,2.2,0]),
	Square(side_length=1.8).move_to([-3,1.2,0]),
	Square(side_length=1.8).move_to([-2,1.2,0]),
	Square(side_length=0.8).move_to([-6.05, 3.85, 0])
]

llave = [
	Brace(s[0],sharpness=1.5).rotate(-3.1415/2),
	Brace(s[1], sharpness=1.5).rotate(-3.1415 / 2),
	Brace(s[2], sharpness=1.5).rotate(-3.1415 / 2),
	Brace(s[3], sharpness=1.5).rotate(-3.1415 / 2)
]

cuenta = Text("Haciendo (2)-(1):").move_to([0,2,0]).scale(0.5)

resta = [
	MathTex("12a+4b-(8a+4b)=0-(-2)").move_to([0,1,0]).scale(0.6),
	MathTex("12a+4b-8a-4b=0+2").move_to([0, 0.5, 0]).scale(0.6),
	MathTex("4a=2").move_to([0, 0, 0]).scale(0.6),
	MathTex(r"a=\frac{2}{4}").move_to([0, -0.7, 0]).scale(0.6),
	MathTex(r"a=\frac{1}{2}").move_to([0, -1.47, 0]).scale(0.6),
	Text("Haciendo (2)-(1):").move_to([0, 2, 0]).scale(0.5),
	MathTex(r"a=\frac{1}{2}").move_to([0, -1.47, 0]).scale(0.6),
	MathTex(r"a=\frac{1}{2}").move_to([6, 2.2, 0]).scale(0.75)
]

cuenta2 = Text("remplazando el valor de a en (2): ").move_to([0, 2.3, 0]).scale(0.6)

remp = [
	MathTex("12a+4b=0").move_to([0, 1.6, 0]).scale(0.6),
	MathTex(r"12(\frac{1}{2})+4b=0").move_to([0, 1, 0]).scale(0.6),
	MathTex("6+4b=0").move_to([0, 0.3, 0]).scale(0.6),
	MathTex("4b=-6").move_to([0, -0.2, 0]).scale(0.6),
	MathTex(r"b=-\frac{6}{4}").move_to([0, -0.9, 0]).scale(0.6),
	MathTex(r"b=-\frac{3}{2}").move_to([0, -1.7, 0]).scale(0.6),
	MathTex(r"b=-\frac{3}{2}").move_to([0, -1.7, 0]).scale(0.6),
	MathTex(r"b=-\frac{3}{2}").move_to([6, 1.3, 0]).scale(0.75)
]

res1 = [
	MathTex(r"a=\frac{1}{2},").move_to([-2.25,2.5,0]).scale(0.8),
	MathTex(r"b=-\frac{3}{2}").move_to([-0.75, 2.5, 0]).scale(0.8),
	MathTex("c=0,").move_to([0.75, 2.5, 0]).scale(0.8),
	MathTex("d=2,").move_to([2.25, 2.5, 0]).scale(0.8)
]

cub = [
	MathTex("P(x)=", "a", "x^3+", "b", "x^2+", "c", "x+", "d", color="white").move_to([0,1,0]),
	MathTex(r"P(x)=\frac{1}{2}x^3-\frac{3}{2}x^2+2").move_to([0,0,0])
]
for i in range(1, 9, 2):
	cub[0][i].set_color("red")  # defino color rojo para los parametros,




