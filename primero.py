from manim import *
from SYD.subrutinas import *
from SYD.entradas import *

class video(Scene):

    def construct(self):


        # planteo el reto

        esctex2(self,reto) #escribo reto
        bortex(self,reto) #borro reto
        self.wait(0.2)

        #presento el problema

        esctex2(self, enunciado)
        esctex2(self, condicion1)
        esctex2(self, condicion2)
        esctex2(self, condicion3)
        esctex2(self, objetivo)
        self.wait(4)

        #borro

        self.play(FadeOut(condicion1[0], condicion2[0], condicion3[0], enunciado[0], objetivo[0]))
