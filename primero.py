from manim import *

class video(Scene):
    def construct(self):
        #planteo el reto
        reto= Text("¿Serías capaz de resolver el siguiente problema?").scale(0.8)
        #planteo el problema y sus condiciones.
        enunciado=Text("¿Existe alguna función cúbica, que cumpla las siguientes condiciones?").scale(0.55).move_to([0,3,0])
        condicion1= Text("1) Pasar por el punto (0,2)").scale(0.6).move_to([0,2,0])

        condicion2= Text("2) Pasar por el punto (2,0)").scale(0.6).move_to([0,1,0])

        condicion3= Text("3) Que en ambos puntos, la recta tangente sea horizontal").scale(0.6).move_to([0,0,0])

        objetivo= Text("En caso de existir, encontrar su expresion analitica.").scale(0.55).move_to([0,-1,0])

        # planteo el problema
        self.play(Write(reto))
        self.wait(4)
        self.play(FadeOut(reto))
        self.wait((0.2))
        self.play(Write(enunciado))
        self.play(Write(condicion1))
        self.wait(1)
        self.play(Write(condicion2))
        self.wait(1)
        self.play(Write(condicion3))
        self.wait(1)
        self.play(Write(objetivo))
        self.wait(4)

        self.play(FadeOut(condicion1,condicion2, condicion3, enunciado,objetivo))
        self.wait(3)