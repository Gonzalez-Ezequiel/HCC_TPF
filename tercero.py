from manim import *

class video(Scene):
    def construct(self):

    #escribo las condiciones y defino el formato de los ejes

     cond1= Text("Pasar por el punto (0,2)",color="yellow").scale(0.4).move_to([-4,3.2,0])
     cond2 = Text("Pasar por el punto (2,0)", color="green").scale(0.4).move_to([-4, 2.7, 0])
     cond3= Text("Rectas tangentes horizontales en dichos puntos",color="blue").scale(0.4).move_to([-3.7, 2.2, 0])
     ax=Axes(x_range=[-10,10,1],
            y_range=[-7,7,1],
            x_length=13,
            y_length=8,
            axis_config={"include_tip" : True,"include_numbers" : False}).set_color("white")

     dot1= Dot(color="yellow").move_to(ax.c2p(0,2)) #puntos por donde pasa el pol
     dot2 = Dot(color="green").move_to(ax.c2p(2, 0))

     recta1 = ax.plot(lambda x: 2,color="blue") #rectas horizontales
     recta2 = ax.plot(lambda x: 0,color="blue")

     self.play(Create(ax,run_time=3))
     self.play(Write(cond1, run_time=1),Write(dot1,run_time=2.5))
     self.wait(4)
     self.play(Write(cond2, run_time=1), Write(dot2, run_time=2.5))
     self.wait(4)
     self.play(Write(cond3,run_time=1),Create(recta1,run_time=1.8),Create(recta2,run_time=1.5))
     self.wait(10)
     self.play(FadeOut(recta1,recta2,ax,cond1,cond2,dot1,dot2,cond3))
     self.wait(2)