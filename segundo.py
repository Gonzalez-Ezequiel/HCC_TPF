from manim import *
from Func.funcionesgraf import *
from Func.funcionestex import *
from Inputs.datos2 import *
class video(Scene):
    def construct(self):
        #función del ejercicio

        for i in range(1,9,2):
            eq1[i].set_color("red") #defino color rojo para los parametros
        recta= [MathTex("y=f'(x)(x-x_0)+f(x_0)",color="white"),[-5,-1.2,0],0.7,0] #ec recta tangente
        funcion = lambda x:x**3+1
        *tangent,x= tangente(self,funcion,-2) #funcion que genera recta tangente en tiempo real.
        #defino ejes

        ax=Axes(x_range=[-10,10,1],
                y_range=[-7,7,1],
                x_length=13,
                y_length=8,
                axis_config={"include_tip" : True,"include_numbers" : False}).set_color("white")

        #funcion inicial
        curva = ax.plot(lambda x: x**3+3*x**2-2*x+1)
        #OOP, la unica forma de hacer variar parametros de funciones, en este caso son 4.
        t = [None] * 4
        d = [None] * 4
        # Inicializar las listas

        # Crear los objetos ValueTracker y DecimalNumber
        for i in range(4):
            t[i] = ValueTracker(0)
            d[i] = DecimalNumber(0)

            # Capturar el valor de i en el lambda usando un argumento predeterminado
            d[i].add_updater(lambda z, t=t[i]: z.set_value(t.get_value()))

        d[0].move_to(np.array([-5.2,2.7,0])).set_color("red").scale(0.7)
        d[1].move_to(np.array([-5.2,2.2,0])).set_color("red").scale(0.7)
        d[2].move_to(np.array([-5.2,1.7,0])).set_color("red").scale(0.7)
        d[3].move_to(np.array([-5.2,1.2,0])).set_color("red").scale(0.7)
        a = MathTex("a=",color="white").move_to(np.array([-6,2.7,0])).scale(0.7)
        b = MathTex("b=",color="white").move_to(np.array([-6, 2.2, 0])).scale(0.7)
        c = MathTex("c=",color="white").move_to(np.array([-6, 1.7, 0])).scale(0.7)
        e = MathTex("d=",color="white").move_to(np.array([-6, 1.2, 0])).scale(0.7)
        curva.add_updater(lambda z: z.become(ax.plot(lambda x: t[0].get_value() * x ** 3 + t[1].get_value() * x ** 2 + t[2].get_value() * x + t[3].get_value(), color="red")))

        #escribo el polinomio, lo desplazo y creo los ejes
        esctex(self,eq1)
        self.wait(15)
        transf(self,eq1,[-5,3.2,0],0.7)
        self.play(Create(ax))

        #creo cubicas con distintos parametros

        self.play(Create(curva))
        self.add(a, b, c, e, *d)
        self.play(t[0].animate.set_value(3),t[1].animate.set_value(-3),t[2].animate.set_value(-3),t[3].animate.set_value(2), run_time=4) #cambia el valor de los parametros
        self.play(t[0].animate.set_value(-0.5), t[1].animate.set_value(-1), t[2].animate.set_value(1), t[3].animate.set_value(0),run_time=4)
        self.play(t[0].animate.set_value(1), t[1].animate.set_value(0), t[2].animate.set_value(0),t[3].animate.set_value(1),run_time=4)
        self.wait(6)
        #genero y desplazo la recta tangente
        self.play(Create(VGroup(*tangent)))
        esctex2(self,recta)
        movobj(self,x,-1.5,5)
        movobj(self,x,1,3)
        movobj(self, x, 0, 3)
        self.wait(10)
        self.play(FadeOut(curva,*d,a,b,c,e,ax,*tangent,eq1,recta[0]),FadeOut(curva),run_time=1)
        self.wait(3)