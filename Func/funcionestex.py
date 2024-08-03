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
def multtrans(self,texto,tiempo=2,ref=0,inicial=-2,final=-1):
    if ((final == -1) and (inicial==-2)):
        for i in range(1,len(texto)):
            self.play(Transform(texto[0],texto[i]),run_time=tiempo)
    elif ((final== -1) and (inicial!=-2)):
        for i in range(inicial+1, len(texto)):
            self.play(Transform(texto[ref], texto[i]), run_time=tiempo)
    else:
        for i in range(inicial + 1, final+1):
            self.play(Transform(texto[ref], texto[i]), run_time=tiempo)