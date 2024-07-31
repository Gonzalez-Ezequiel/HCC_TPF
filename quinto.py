from manim import *

class video(Scene):
    def construct(self):

        #defino las ecuaciones

        eq1= MathTex("d=2", color="white").move_to([0, 1.5, 0])
        eq2= MathTex("8a+4b+2c+d=0", color="white").move_to([0, 0.5, 0])
        eq3= MathTex("c=0", color="white").move_to([0, -0.5, 0])
        eq4= MathTex("12a+4b+c=0", color="white").move_to([0, -1.5, 0])

        #reduzco el problema y opero un poco

        eq11 = MathTex("d=2", color="white").move_to([6, 3.3, 0]).scale(0.75)
        eq22 = MathTex("8a+4b+2c+d=0", color="white").move_to([0, 0.5, 0])
        eq33 = MathTex("c=0", color="white").move_to([6, 2.9, 0]).scale(0.75)
        eq44 = MathTex("12a+4b+c=0", color="white").move_to([0, -0.5, 0])

        eq22b = MathTex("8a+4b+2=0", color="white").move_to([0, 0.5, 0])
        eq44b = MathTex("12a+4b=0", color="white").move_to([0, -0.5, 0])

        eq22c = MathTex("8a+4b=-2", color="white").move_to([0, 0.5, 0])

        eq111 = MathTex("d=2", color="white").move_to([5, 3.3, 0]).scale(0.6)
        eq222 = MathTex("8a+4b=-2", color="white").move_to([-5, 3.3, 0]).scale(0.6)
        eq333 = MathTex("c=0", color="white").move_to([5, 3, 0]).scale(0.6)
        eq444 = MathTex("12a+4b=0", color="white").move_to([-5, 2.9, 0]).scale(0.6)

        #nro de ecuaciones

        nro1 = Text("(1)",color="white").move_to([3,1.5,0]).scale(0.5)
        nro2 = Text("(2)",color="white").move_to([3,0.5,0]).scale(0.5)
        nro3 = Text("(3)",color="white").move_to([3,-0.5,0]).scale(0.5)
        nro4 =  Text("(4)",color="white").move_to([3,-1.5,0]).scale(0.5)

        nro11 = Text("(1)",color="white").move_to([3,0.5,0]).scale(0.5)
        nro22 = Text("(2)",color="white").move_to([3,-0.5,0]).scale(0.5)

        nro111 = Text("(1)",color="white").move_to([-3.4,3.3,0]).scale(0.3)
        nro222 = Text("(2)",color="white").move_to([-3.4,2.9,0]).scale(0.3)

        #defino las llaves que voy a usar ajustandolas a un cuadrado invisible

        s1 = Square(side_length=3.6).move_to([-3,2.2,0])
        s2 = Square(side_length=1.8).move_to([-3,1.2,0])
        s3 = Square(side_length=1.8).move_to([-2,1.2,0])
        s4 = Square(side_length=0.8).move_to([-6.05, 3.85, 0])
        llave= Brace(s1,sharpness=1.5).rotate(-3.1415/2)
        llave2 = Brace(s2, sharpness=1.5).rotate(-3.1415 / 2)
        llave3 = Brace(s3, sharpness=1.5).rotate(-3.1415 / 2)
        llave4 = Brace(s4, sharpness=1.5).rotate(-3.1415 / 2)

        #Resolución de a:

        cuenta= Text("Haciendo (2)-(1):").move_to([0,2,0]).scale(0.5)
        resta1= MathTex("12a+4b-(8a+4b)=0-(-2)").move_to([0,1,0]).scale(0.6)
        resta2 = MathTex("12a+4b-8a-4b=0+2").move_to([0, 0.5, 0]).scale(0.6)
        resta3 = MathTex("4a=2").move_to([0, 0, 0]).scale(0.6)
        resta4 = MathTex(r"a=\frac{2}{4}").move_to([0, -0.7, 0]).scale(0.6)
        resta5 = MathTex(r"a=\frac{1}{2}").move_to([0, -1.47, 0]).scale(0.6)
        resta6 = MathTex(r"a=\frac{1}{2}").move_to([0, -1.47, 0]).scale(0.6)
        resultado3 = MathTex(r"a=\frac{1}{2}").move_to([6, 2.2, 0]).scale(0.75)

        #Resolución de b:

        cuenta2 = Text("remplazando el valor de a en (2): ").move_to([0, 2.3, 0]).scale(0.6)
        remp0 = MathTex("12a+4b=0").move_to([0, 1.6, 0]).scale(0.6)
        remp1 = MathTex(r"12(\frac{1}{2})+4b=0").move_to([0, 1, 0]).scale(0.6)
        remp2 = MathTex("6+4b=0").move_to([0, 0.3, 0]).scale(0.6)
        remp3 = MathTex("4b=-6").move_to([0, -0.2, 0]).scale(0.6)
        remp4 = MathTex(r"b=-\frac{6}{4}").move_to([0, -0.9, 0]).scale(0.6)
        remp5 = MathTex(r"b=-\frac{3}{2}").move_to([0, -1.6, 0]).scale(0.6)
        remp6 = MathTex(r"b=-\frac{3}{2}").move_to([0, -1.6, 0]).scale(0.6)
        resultado4 = MathTex(r"b=-\frac{3}{2}").move_to([6, 1.3, 0]).scale(0.75)

        #Presentacion formal del valor de los parametros

        res1 = MathTex(r"a=\frac{1}{2},",r"b=-\frac{3}{2},","c=0,","d=2,")
        res1[0].move_to([-2.25,2.5,0]).scale(0.8)
        res1[1].move_to([-0.75, 2.5, 0]).scale(0.8)
        res1[2].move_to([0.75, 2.5, 0]).scale(0.8)
        res1[3].move_to([2.25, 2.5, 0]).scale(0.8)

        cub= MathTex(r"P(x)=ax^3+bx^2+cx+d").move_to([0,1,0])
        cub2= MathTex(r"P(x)=\frac{1}{2}x^3-\frac{3}{2}x^2+2").move_to([0,0,0])


        self.add(eq1,eq2,eq3,eq4,llave,nro1,nro2,nro3,nro4) #agrego las ecs
        self.wait(10)
        self.remove(nro3,nro4) #quito los nros 3 y 4 ya que reduci el problema a 2 ecs
        self.play(Transform(eq1,eq11),Transform(eq2,eq22),Transform(eq3,eq33),Transform(eq4,eq44),Transform(llave,llave2),Transform(nro1,nro11),Transform(nro2,nro22)) #muevo ecuaciones
        self.wait(10)

        #opero

        self.play(Transform(eq2,eq22b,run_time=0.2),Transform(eq4,eq44b,run_time=0.2))
        self.wait(4)
        self.play(Transform(eq2, eq22c,run_time=0.2),Transform(llave,llave3))
        self.wait(4)
        self.play(Transform(eq2, eq222),Transform(eq4,eq444), Transform(llave, llave4),Transform(nro1,nro111),Transform(nro2,nro222)) #llevo el sistema a la esquina superior izquierda
        self.wait(5)

        #resolucion de a

        self.play(FadeIn(cuenta,run_time=1.5))
        self.wait(2)
        self.play(Write(resta1))
        self.wait(4)
        self.play(Write(resta2))
        self.wait(4)
        self.play(Write(resta3))
        self.wait(4)
        self.play(Write(resta4))
        self.wait(4)
        self.play(FadeIn(resta5,run_time=0.5))
        self.wait(4)
        self.add(resta6)
        self.play(Transform(resta5,resultado3))
        self.wait(5)
        self.play(FadeOut(resta1),FadeOut(resta2),FadeOut(resta3),FadeOut(resta4),FadeOut(resta6),FadeOut(cuenta))

        # resolucion de b

        self.play(FadeIn(cuenta2,run_time=1.5))
        self.wait(3)
        self.play(Write(remp0))
        self.wait(3)
        self.play(Write(remp1))
        self.wait(3)
        self.play(Write(remp2))
        self.wait(3)
        self.play(Write(remp3))
        self.wait(3)
        self.play(Write(remp4))
        self.wait(3)
        self.play(FadeIn(remp5,run_time=0.5))
        self.wait(3)
        self.add(remp6)
        self.play(Transform(remp5,resultado4))
        self.wait(2)
        self.play(FadeOut(remp0,remp1,remp2,remp3,remp4,remp6,cuenta2,eq2,eq4,llave,nro1,nro2))

        #presento la solucion del problema

        self.play(Transform(eq1,res1[3]),Transform(eq3,res1[2]),Transform(remp5,res1[1]),Transform(resta5,res1[0]))
        self.wait(3)
        self.play(Write(cub))
        self.wait(2)
        self.play(Transform(cub,cub2))
        self.wait(10)
        self.play(FadeOut(cub,eq1,eq3,remp5,resta5)) #desaparezcotodo
        self.wait(1)