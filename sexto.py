from manim import *
from Func.funcionesgraf import *
from Inputs.datos6 import *

class video(Scene):
    def construct(self):
     #ejes
     ax=Axes(x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=13,
            y_length=8,
            axis_config={"include_tip" : True,"include_numbers" : False}).set_color("white")
     #condiciones de puntos
     solucion = ax.plot(lambda x: 0.5 * x ** 3 - 1.5 * x ** 2 + 2, color="red")

     dot1 = Dot(color="yellow").move_to(ax.c2p(0, 2))
     dot2 = Dot(color="green").move_to(ax.c2p(2, 0))
     *tangent,x= tangente(self,funcion,ax,-2)


     #Agradecimiento


     #grafico ejes y puntos
     self.play(Create(ax,run_time=1.5))
     self.play(Write(dot1,run_time=0.5))
     self.play(Write(dot2, run_time=0.5))
     self.wait(1)

     #grafico solucion
     self.play(Write(cub),Write(punto1),Write(punto2))
     self.play(Create(solucion,run_time=6))
     self.wait(4)
     #dibujo recta tangente
     self.play(Create(VGroup(*tangent)))
     self.play(x.animate.set_value(0),
               run_time=5) # cambio valores de x para que la tangente se calcule sobre distintos puntos
     self.wait(2)
     self.play(x.animate.set_value(2.5), run_time=2)
     self.play(x.animate.set_value(1.75), run_time=2)
     self.play(x.animate.set_value(2), run_time=1)
     self.wait(8)



     #quitotodo
     self.play(FadeOut(cub,ax,solucion,dot1,dot2,*tangent))

     #agradecimiento
     self.play(FadeIn(gracias))
     self.wait(8)
