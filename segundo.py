from manim import *
from Func.funcionesgraf import *
from Func.funcionestex import *
from Inputs.datos2 import *
class video(Scene):
    def construct(self):
        #función del ejercicio
        ax=Axes(x_range=[-10,10,1],
                y_range=[-7,7,1],
                x_length=13,
                y_length=8,
                axis_config={"include_tip" : True,"include_numbers" : False}).set_color("white")


        *tangent,x= tangente(self,funcion,ax,-2) #funcion que genera recta tangente en tiempo real.
        #defino ejes
        curva = ax.plot(lambda x: x ** 3 + 3 * x ** 2 - 2 * x + 1)
        curva.add_updater(lambda z: z.become(ax.plot(lambda x: t[0].get_value() * x ** 3 + t[1].get_value() * x ** 2 + t[2].get_value() * x + t[3].get_value(),color="red")))

        #escribo el polinomio, lo desplazo y creo los ejes

        esctex(self,eq1)
        self.wait(15)
        transf(self,eq1,[-5,3.2,0],0.7)
        self.play(Create(ax))

        #creo cubicas con distintos parametros

        self.play(Create(curva))
        self.add(a, b, c, e, *d)
        varparm(self,t,[3,-3,-3,2],4,4)
        varparm(self,t,[-0.5,-1,1,0],4,4)
        varparm(self,t,[1,0,0,1],4,4)
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
