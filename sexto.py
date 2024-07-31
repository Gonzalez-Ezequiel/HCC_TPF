from manim import *

class video(Scene):
    def construct(self):
     #ejes
     ax=Axes(x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=13,
            y_length=8,
            axis_config={"include_tip" : True,"include_numbers" : False}).set_color("white")
     #condiciones de puntos
     dot1= Dot(color="yellow").move_to(ax.c2p(0,2))
     dot2 = Dot(color="green").move_to(ax.c2p(2, 0))

     #solucion

     #escrita
     cub= MathTex(r"P(x)=\frac{1}{2}x^3-\frac{3}{2}x^2+2").move_to([-4,3,0]).scale(0.8)
     #grafica
     solucion= ax.plot( lambda x: 0.5*x**3-1.5*x**2+2,color="red")

     #recta tangente
     x = ValueTracker(-2)
     dx = ValueTracker(0.001)
     tangent = always_redraw(
      lambda: ax.get_secant_slope_group(
       x=x.get_value(),
       graph=solucion,
       dx=dx.get_value(),
       dx_line_color="yellow",
       dy_line_color="orange",
       secant_line_color="green",
       secant_line_length=25,
      )
     )
     dot11 = always_redraw(
      lambda: Dot()
      .scale(0.9)
      .move_to(ax.c2p(x.get_value(), solucion.underlying_function(x.get_value())))  # el punto 1 se mueve donde mande x.
     )
     dot22 = always_redraw(
      lambda: Dot()
      .scale(0.9)
      .move_to(
       ax.c2p((x).get_value() + dx.get_value(), solucion.underlying_function(x.get_value() + dx.get_value()), )
       # el punto 2 se mueve ligeramente respecto al punto 1, asi la secante se parece a la tangente.
      )

     )



     #Agradecimiento

     gracias= Text("¡Muchas gracias por ver! :)")


     #grafico ejes y puntos
     self.play(Create(ax,run_time=1.5))
     self.play(Write(dot1,run_time=0.5))
     self.play(Write(dot2, run_time=0.5))
     self.wait(1)

     #grafico solucion
     self.play(Write(cub))
     self.play(Create(solucion,run_time=6))
     self.wait(4)
     #dibujo recta tangente
     self.play(Create(VGroup(dot11, dot22, tangent)))
     self.play(x.animate.set_value(0),
               run_time=5) # cambio valores de x para que la tangente se calcule sobre distintos puntos
     self.wait(2)
     self.play(x.animate.set_value(2.5), run_time=2)
     self.play(x.animate.set_value(1.75), run_time=2)
     self.play(x.animate.set_value(2), run_time=1)
     self.wait(8)



     #quitotodo
     self.play(FadeOut(cub,ax,solucion,dot11,dot22,tangent,dot1,dot2))

     #agradecimiento
     self.play(FadeIn(gracias))
     self.wait(8)
