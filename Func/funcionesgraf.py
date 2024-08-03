from manim import *
import numpy as np
import sympy as sp
def tangente(self,funcion,ax,punto):  #genera la recta tangente a una funcion en un punto dado.
    func = ax.plot(lambda x: eval(funcion, {"x" : x}))  # elijo esta funcion para hacer mover la recta tangente
    x = ValueTracker(punto)
    dx = ValueTracker(0.001)
    tangent = always_redraw(
        lambda: ax.get_secant_slope_group(
            x=x.get_value(),
            graph=func,
            dx=dx.get_value(),
            dx_line_color="yellow",
            dy_line_color="orange",
            secant_line_color="green",
            secant_line_length=25,
        )
    )
    dot1 = always_redraw(
        lambda: Dot()
        .scale(0.9)
        .move_to(ax.c2p(x.get_value(), func.underlying_function(x.get_value())))  # el punto 1 se mueve donde mande x.
    )
    dot2 = always_redraw(
        lambda: Dot()
        .scale(0.9)
        .move_to(
            ax.c2p((x).get_value() + dx.get_value(), func.underlying_function(x.get_value() + dx.get_value()), )
            # el punto 2 se mueve ligeramente respecto al punto 1, asi la secante se parece a la tangente.
        )

    )
    return tangent,dot1,dot2,x

def movobj(self,variable,punto,tiempo):
    self.play(variable.animate.set_value(punto), run_time=tiempo)

def varparm(self,variable,puntos,tiempo=2,nro=1):
    animaciones= [variable[i].animate.set_value(puntos[i]) for i in range(0,nro)]
    self.play(*animaciones, run_time=tiempo)