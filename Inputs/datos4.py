from manim import *

# planteo el problema y sus condiciones.
condicion11 = Text("1) Pasar por el punto (0,2)").scale(0.6).move_to([-4, 3.2, 0])

condicion22 = Text("2) Pasar por el punto (2,0)").scale(0.6).move_to([-4, 3.2, 0])

condicion33 = Text("3) Que en ambos puntos, la recta tangente sea horizontal").scale(0.5).move_to([-2, 3.2, 0])

# estas flechas las uso para varias ecuaciones
flecha = Arrow(start=LEFT * 0.8, end=RIGHT * 0.7, color="white").move_to([-1, 0, 0])
flecha2 = Arrow(end=RIGHT * 0.5, color="white").move_to([0, 0, 0])

P02 = MathTex("P(0) = 2", color="white").move_to([-3, 0, 0])

ec1 = [
	MathTex("a \cdot 0^3 + b \cdot 0^2 + c \cdot 0 + d = 2", color="white").move_to([3, 0, 0]),
	MathTex("a \cdot 0^3 + b \cdot 0^2 + c \cdot 0 + d = 2", color="white").move_to([0, 0, 0]),
	MathTex("d = 2", color="white").move_to([0, 0, 0]),
	MathTex("d = 2", color="white").move_to([5, 3.2, 0]).scale(0.6),
	MathTex("d = 2", color="white").move_to([0, 1.5, 0])
        ]

P20 = MathTex("P(2) = 0", color="white").move_to([-3, 0, 0])


ec2 = [
	MathTex("a \cdot 2^3 + b \cdot 2^2 + c \cdot 2 + d = 0", color="white").move_to([3, 0, 0]),
	MathTex("a \cdot 2^3 + b \cdot 2^2 + c \cdot 2 + d = 0", color="white").move_to([0, 0, 0]),
	MathTex("a \cdot 8 + b \cdot 4 + c \cdot 2 + d = 0", color="white").move_to([0, 0, 0]),
	MathTex("8a + 4b + 2c + d = 0", color="white").move_to([0, 0, 0]),
	MathTex("8a + 4b + 2c + d = 0", color="white").move_to([5, 2.8, 0]).scale(0.6),
	MathTex("8a + 4b + 2c + d = 0", color="white").move_to([0, 0.5, 0])
        ]



PP00= MathTex("P'(0)=0", color="white").move_to([-3, 0, 0])

polg1 = MathTex("f(x)=x^n", color="red").move_to([0, 1, 0]).scale(0.6)
polg2 = MathTex("f'(x)=nx^{n-1}", color="red").move_to([0, 0.5, 0]).scale(0.6)

ecd = [
	MathTex("P(x) = ax^3 + bx^2 + cx + d").move_to([-4, 0, 0]).scale(0.9),
	MathTex("P'(x) = 3ax^2 + 2bx + c").move_to([3.4, 0, 0]).scale(0.9),
	MathTex("P'(x) = 3ax^2 + 2bx + c").move_to([-3.8, 2.6, 0]).scale(0.75),
	MathTex("P(x) = ax^3 + bx^2 + cx + d").move_to([-3.8, 2.6, 0]).scale(0.75)
        ]


ec3=[

	MathTex("3a\cdot 0^2+2b\cdot 0+c=0", color="white").move_to([3, 0, 0]),
	MathTex("3a\cdot 0^2+2b\cdot 0+c=0", color="white").move_to([0, 0, 0]),
	MathTex("c=0", color="white").move_to([0, 0, 0]),
    MathTex("c=0", color="white").move_to([5, 2.4, 0]).scale(0.6),
	MathTex("c=0", color="white").move_to([0, -0.5, 0])

]

PP20= 	MathTex("P'(2)=0", color="white").move_to([-3, 0, 0])

ec4=[

	MathTex("3a\cdot 2^2+2b\cdot 2+c=0", color="white").move_to([3, 0, 0]),
	MathTex("3a\cdot 2^2+2b\cdot 2+c=0", color="white").move_to([0, 0, 0]),
	MathTex("3a\cdot 4+2b\cdot 2+c=0", color="white").move_to([0, 0, 0]),
	MathTex("12a+4b+c=0", color="white").move_to([0, 0, 0]),
	MathTex("12a+4b+c=0", color="white").move_to([5, 2.1, 0]).scale(0.6),
	MathTex("12a+4b+c=0", color="white").move_to([0, -1.5, 0])

]

#llave para el sistema de ecuaciones final
s1 = Square(side_length=3.6).move_to([-3, 2.2, 0])
llave = Brace(s1, sharpness=1.5).rotate(-3.1415 / 2)