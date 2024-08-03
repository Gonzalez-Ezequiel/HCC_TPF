from manim import *
def esctex(self, texto, posicion=[0, 0, 0], escala=1.0, tiempo=0):
    texto2 = texto.scale(escala).move_to(posicion)
    self.play(Write(texto2))
    self.wait(tiempo)


def esctex2(self, texto):
    texto2 = texto[0].scale(texto[2]).move_to(texto[1])
    self.play(Write(texto2))
    self.wait(texto[3])


def bortex(self, texto):
    self.play(FadeOut(texto[0]))

def transf(self,text1,posicion=[0,0,0],escala=1):

    # Mover el texto a la nueva posición
    self.play(text1.animate.shift(posicion).scale(escala),
            run_time=1)