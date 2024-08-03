from manim import *
from Func.funcionesgraf import *
from Func.funcionestex import *
from Inputs.datos4 import *

class video(Scene):
    def construct(self):
        #planteo el problema y sus condiciones.

        # planteo ec1
        self.play(Write(condicion11,run_time=1),Write(ecd[3],run_time=2))
        self.play(Write(P02,run_time=2))
        self.play(Write(flecha,run_time=3))
        self.play(Write(ec1[0],run_time=3))
        self.wait(3)
        self.play(FadeOut(P02,flecha),Transform(ec1[0],ec1[1]),run_time=1)
        multtrans(self,ec1,2,0,2,3)
        self.wait(2)

        # planteo ec2
        self.play(FadeOut(condicion11,run_time=0.2),FadeIn(condicion22,run_time=1))
        self.play(Write(P20, run_time=2))
        self.play(Write(flecha, run_time=1.3))
        self.play(Write(ec2[0], run_time=3))
        self.play(FadeOut(P20, flecha),Transform(ec2[0],ec2[1]),run_time=1)
        multtrans(self, ec2,2,0,2, 4)


        self.wait(3)
        # derivo y planteo ec3
        self.play(FadeOut(condicion22,run_time=0.2), FadeIn(condicion33,run_time=1))
        self.wait(3)
        self.play(Transform(ecd[3],ecd[0], run_time=2))
        self.play(Write(flecha2, run_time=1),Write(polg1),Write(polg2))
        self.wait(5)
        self.play(Write(ecd[1], run_time=3))
        self.wait(3)
        self.remove(ecd[3], flecha2,polg1,polg2)
        self.play(Transform(ecd[1], ecd[2], run_time=2.5))

        self.wait(2)
        #ec3
        self.play(Write(PP00, run_time=2))
        self.play(Write(flecha, run_time=1.3))
        self.play(Write(ec3[0], run_time=3))
        self.wait(3)
        self.remove(PP00, flecha)
        multtrans(self,ec3,2,0,1,3)

        self.wait(5)
        # planteo ec4
        self.play(Write(PP20, run_time=2))
        self.play(Write(flecha, run_time=1.3))
        self.play(Write(ec4[0], run_time=3))
        self.wait(3)
        self.play(FadeOut(PP20, flecha),Transform(ec4[0],ec4[1],run_time=1))
        multtrans(self, ec4, 2, 0, 2, 4)
        self.remove(condicion33,ecd[1])
        #Planteo el sistema completo
        self.play(Transform(ec1[0],ec1[4]),Transform(ec2[0],ec2[5]),Transform(ec3[0],ec3[4]),Transform(ec4[0],ec4[5]),Write(llave))
        self.wait(3)


