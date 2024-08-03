from manim import *
from Func.funcionestex import *
from Inputs.datos5 import *
class video(Scene):
    def construct(self):

        #defino las ecuaciones
        self.add(eq1[0],eq2[0],eq3[0],eq4[0],llave[0],nro1[0],nro2[0],nro3[0],nro4[0]) #agrego las ecs
        self.wait(10)
        self.remove(nro3[0],nro4[0]) #quito los nros 3 y 4 ya que reduci el problema a 2 ecs
        self.play(Transform(eq1[0],eq1[1]),Transform(eq2[0],eq2[1]),Transform(eq3[0],eq3[1]),Transform(eq4[0],eq4[1]),Transform(llave[0],llave[1]),Transform(nro1[0],nro1[1]),Transform(nro2[0],nro2[1])) #muevo ecuaciones
        self.wait(10)

        #opero


        multtrans(self,eq2,4,0,2,3)
        self.play(Transform(eq2[0], eq2[4]),Transform(eq4[0],eq4[3]), Transform(llave[0], llave[3]),Transform(nro1[0],nro1[2]),Transform(nro2[0],nro2[2])) #llevo el sistema a la esquina superior izquierda
        self.wait(5)

        #resolucion de a

        self.play(FadeIn(resta[5],run_time=1.5))
        self.wait(2)
        proced(self,resta,4,0,1,3)
        self.play(FadeIn(resta[4],run_time=0.5))
        self.wait(4)
        self.add(resta[6])
        self.play(Transform(resta[6],resta[7]))
        self.wait(5)
        borsim(self,resta,1.5,1,5)
        # resolucion de b

        self.play(FadeIn(cuenta2,run_time=1.5))
        proced(self,remp,3,0,1,4)
        self.play(FadeIn(remp[5],run_time=0.5))
        self.wait(3)
        self.add(remp[6])
        self.play(Transform(remp[5],remp[7]))
        self.wait(2)
        self.play(FadeOut(remp[0],remp[1],remp[2],remp[3],remp[4],remp[6],cuenta2,eq2[0],eq4[0],llave[0],nro1[0],nro2[0]))

        #presento la solucion del problema

        self.play(Transform(eq1[0],res1[3]),Transform(eq3[0],res1[2]),Transform(remp[5],res1[1]),Transform(resta[6],res1[0]))
        self.wait(3)
        self.play(Write(cub[0]))
        self.wait(5)
        self.play(Transform(cub[0],cub[1]))
        self.wait(10)
        self.play(FadeOut(cub[0],eq1[0],eq3[0],remp[5],resta[4])) #desaparezcotodo
        self.wait(1)