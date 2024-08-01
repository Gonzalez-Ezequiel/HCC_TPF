from manim import *
import numpy as np
import sympy as sp
def esctex(self,texto,tiempo=1,posicion=[0,0,0],escala=1.0):
     texto2=texto.scale(escala).move_to(posicion)
     self.play(Write(texto2))
     self.wait(tiempo)


def esctex2(self, texto):
    texto2 = texto[0].scale(texto[3]).move_to(texto[2])
    self.play(Write(texto2))
    self.wait(texto[1])

def bortex(self,texto):
    self.play(FadeOut(texto[0]))