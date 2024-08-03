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

def borsim(self,texto,tiempo=1.5,inicial=-2,final=-1):
    animaciones =[]
    if ((final == -1) and (inicial==-2)):
        for i in range(0,len(texto)):
            anim = FadeOut(texto[i])
            animaciones.append(anim)
    elif ((final== -1) and (inicial!=-2)):
        for i in range(inicial, len(texto)):
            anim = FadeOut(texto[i])
            animaciones.append(anim)
    else:
        for i in range(inicial, final+1):
            anim = FadeOut(texto[i])
            animaciones.append(anim)
    self.play(AnimationGroup(*animaciones),run_time=tiempo)


def transf(self,text1,posicion=[0,0,0],escala=1):

    # Mover el texto a la nueva posición
    self.play(text1.animate.shift(posicion).scale(escala),
            run_time=1)
def multtrans(self,texto,tiempo=2,ref=0,inicial=-2,final=-1):
    if ((final == -1) and (inicial==-2)):
        for i in range(1,len(texto)):
            self.play(Transform(texto[0],texto[i]), run_time=1)
            self.wait(tiempo)
    elif ((final== -1) and (inicial!=-2)):
        for i in range(inicial, len(texto)):
            self.play(Transform(texto[ref], texto[i]), run_time=1)
            self.wait(tiempo)
    else:
        for i in range(inicial, final+1):
            self.play(Transform(texto[ref], texto[i]), run_time=1)
            self.wait(tiempo)

def proced(self,texto, tiempo=2,ref=0,inicial=-2,final=-1):
    if ((final == -1) and (inicial==-2)):
        for i in range(0,len(texto)):
            self.play(Write(texto[i]))
            self.wait(tiempo)
    elif ((final== -1) and (inicial!=-2)):
        for i in range(inicial, len(texto)):
            self.play(Write(texto[i]))
            self.wait(tiempo)
    else:
        for i in range(inicial, final+1):
            self.play(Write(texto[i]))
            self.wait(tiempo)