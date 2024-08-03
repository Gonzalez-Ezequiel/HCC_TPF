from manim import *
from Func.funcionesgraf import *
from Func.funcionestex import *

class video(Scene):
    def construct(self):
        #planteo el problema y sus condiciones.
        condicion11 = Text("1) Pasar por el punto (0,2)").scale(0.6).move_to([-4,3.2,0])

        condicion22 = Text("2) Pasar por el punto (2,0)").scale(0.6).move_to([-4,3.2,0])

        condicion33 = Text("3) Que en ambos puntos, la recta tangente sea horizontal").scale(0.5).move_to([-2,3.2,0])

        #estas flechas las uso para varias ecuaciones
        flecha= Arrow(start=LEFT*0.8, end=RIGHT*0.7, color="white").move_to([-1,0,0])
        flecha2 = Arrow(end=RIGHT * 0.5, color="white").move_to([0, 0, 0])

        #planteo las 4 ecuaciones una por una.
        #(1)
        ec1= []
        ec2 = []
        P02= MathTex ("P(0)=2",color="white").move_to([-3,0,0])
        ec1.append( MathTex("a\cdot 0^3+b\cdot 0^2+c\cdot 0+d=2", color="white").move_to([3, 0, 0]))
        ec1.append(MathTex("a\cdot 0^3+b\cdot 0^2+c\cdot 0+d=2", color="white").move_to([0, 0, 0]))
        ec1.append(MathTex("d=2", color="white").move_to([0, 0, 0]))
        ec1.append(MathTex("d=2", color="white").move_to([5, 3.2, 0]).scale(0.6))
        ec1.append(MathTex("d=2", color="white").move_to([0, 1.5, 0]))

        #(2)
        P20 = MathTex("P(2)=0", color="white").move_to([-3, 0, 0])
        ec2.append(MathTex("a\cdot 2^3+b\cdot 2^2+c\cdot 2+d=0", color="white").move_to([3, 0, 0]))
        ec2.append(MathTex("a\cdot 2^3+b\cdot 2^2+c\cdot 2+d=0", color="white").move_to([0, 0, 0]))
        ec2.append(MathTex("a\cdot 8+b\cdot 4+c\cdot 2+d=0", color="white").move_to([0, 0, 0]))
        ec2.append(MathTex("8a+4b+2c+d=2", color="white").move_to([0, 0, 0]))
        ec2.append(MathTex("8a+4b+2c+d=2", color="white").move_to([5, 2.8, 0]).scale(0.6))
        ec2.append(MathTex("8a+4b+2c+d=2", color="white").move_to([0, 0.5, 0]))

        #derivo el polinomio de forma generica


        polg1= MathTex( "f(x)=x^n",color="red").move_to([0,1,0]).scale(0.6)
        polg2= MathTex ("f'(x)=nx^{n-1}",color="red").move_to([0,0.5,0]).scale(0.6)
        ecd1= MathTex( "P(x)=ax^3+bx^2+cx+d").move_to([-4, 0, 0]).scale(0.9)
        ecd2= MathTex("P'(x)=3ax^2+2bx+c").move_to([3.4,0,0]).scale(0.9)
        ecd3 = MathTex("P'(x)=3ax^2+2bx+c").move_to([-3.8,2.6, 0]).scale(0.75) #muevo debajo del enunciado
        ecd4 = MathTex("P(x)=ax^3+bx^2+cx+d").move_to([-3.8, 2.6, 0]).scale(0.75) #debajo del enunciado tmbn

        #(3)

        ec3 = MathTex("P'(0)=0", color="white").move_to([-3, 0, 0])
        ec33 = MathTex("3a\cdot 0^2+2b\cdot 0+c=0", color="white").move_to([3, 0, 0])
        ec333 = MathTex("3a\cdot 0^2+2b\cdot 0+c=0", color="white").move_to([0, 0, 0])
        ec3333 = MathTex("c=0", color="white").move_to([0, 0, 0])
        ec33333 = MathTex("c=0", color="white").move_to([5, 2.4, 0]).scale(0.6)
        ec33333f = MathTex("c=0", color="white").move_to([0, -0.5, 0])

        #(4)

        ec4 = MathTex("P'(2)=0", color="white").move_to([-3, 0, 0])
        ec44 = MathTex("3a\cdot 2^2+2b\cdot 2+c=0", color="white").move_to([3, 0, 0])
        ec444 = MathTex("3a\cdot 2^2+2b\cdot 2+c=0", color="white").move_to([0, 0, 0])
        ec444b = MathTex("3a\cdot 4+2b\cdot 2+c=0", color="white").move_to([0, 0, 0])
        ec4444 = MathTex("12a+4b+c=0", color="white").move_to([0, 0, 0])
        ec44444 = MathTex("12a+4b+c=0", color="white").move_to([5, 2.1, 0]).scale(0.6)
        ec44444f = MathTex("12a+4b+c=0", color="white").move_to([0, -1.5, 0])

        #llave para el sistema de ecuaciones final
        s1 = Square(side_length=3.6).move_to([-3, 2.2, 0])
        llave = Brace(s1, sharpness=1.5).rotate(-3.1415 / 2)

        # planteo ec1
        self.play(Write(condicion11,run_time=1),Write(ecd4,run_time=2))
        self.play(Write(P02,run_time=2))
        self.play(Write(flecha,run_time=3))
        self.play(Write(ec1[0],run_time=3))
        self.wait(3)
        self.remove(P02,flecha)
        multtrans(self,ec1,2,0,0,3)
        self.wait(2)

        # planteo ec2
        self.play(FadeOut(condicion11,run_time=0.2),FadeIn(condicion22,run_time=1))
        self.play(Write(P20, run_time=2))
        self.play(Write(flecha, run_time=1.3))
        self.play(Write(ec2[0], run_time=3))
        self.remove(P20, flecha)
        self.play(Transform(ec2[0],ec2[1]),run_time=1)
        multtrans(self, ec2,2,0,1, 4)


        self.wait(3)
        # derivo y planteo ec3
        self.play(FadeOut(condicion22,run_time=0.2), FadeIn(condicion33,run_time=1))
        self.wait(3)
        self.play(Transform(ecd4,ecd1, run_time=2))
        self.play(Write(flecha2, run_time=1),Write(polg1),Write(polg2))
        self.wait(5)
        self.play(Write(ecd2, run_time=3))
        self.wait(3)
        self.remove(ecd4, flecha2,polg1,polg2)
        self.play(Transform(ecd2, ecd3, run_time=2.5))

        self.wait(2)
        #ec3
        self.play(Write(ec3, run_time=2))
        self.play(Write(flecha, run_time=1.3))
        self.play(Write(ec33, run_time=3))
        self.wait(3)
        self.remove(ec3, flecha)
        self.play(Transform(ec33, ec333, run_time=2))
        self.wait(2)
        self.play(Transform(ec33, ec3333, run_time=2))
        self.wait(2)
        self.play(Transform(ec33, ec33333, run_time=2))

        self.wait(5)
        # planteo ec4
        self.play(Write(ec4, run_time=2))
        self.play(Write(flecha, run_time=1.3))
        self.play(Write(ec44, run_time=3))
        self.wait(3)
        self.remove(ec4, flecha)
        self.play(Transform(ec44, ec444, run_time=2))
        self.wait(2)
        self.play(Transform(ec44, ec444b, run_time=1))
        self.wait(2)
        self.play(Transform(ec44, ec4444, run_time=1))
        self.wait(2)
        self.play(Transform(ec44, ec44444, run_time=1.5))
        self.wait(2)
        self.remove(condicion33,ecd2)
        #Planteo el sistema completo
        self.play(Transform(ec1[0],ec1[4]),Transform(ec2[0],ec2[5]),Transform(ec33,ec33333f),Transform(ec44,ec44444f),Write(llave))
        self.wait(3)


