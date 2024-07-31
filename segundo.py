from manim import *

class video(Scene):
    def construct(self):
        #función del ejercicio
        eq1 = MathTex("P(x)=", "a", "x^3+", "b", "x^2+", "c", "x+", "d", color="white")
        eq2 = MathTex("P(x)=","a","x^3+","b","x^2+","c","x+","d", color="white").move_to(np.array([-5,3.2,0])).scale(0.7)
        recta= MathTex("y=f'(x)(x-x_0)+f(x_0)",color="white").move_to(np.array([-5,-1.2,0])).scale(0.7) #ec recta tangente
        #defino ejes
        ax=Axes(x_range=[-10,10,1],
                y_range=[-7,7,1],
                x_length=13,
                y_length=8,
                axis_config={"include_tip" : True,"include_numbers" : False}).set_color("white")
        for i in range(1,9,2):
            eq1[i].set_color("red") #defino color rojo para los parametros
        for i in range(1,9,2):
            eq2[i].set_color("red") #defino color rojo para los parametros

        #funcion inicial
        curva = ax.plot(lambda x: x**3+3*x**2-2*x+1)
        #OOP, la unica forma de hacer variar parametros de funciones, en este caso son 4.
        t0 = ValueTracker(0)
        d0 = DecimalNumber(0)
        t1 = ValueTracker(0)
        d1 = DecimalNumber(0)
        t2 = ValueTracker(0)
        d2 = DecimalNumber(0)
        t3 = ValueTracker(0)
        d3 = DecimalNumber(0)
        # Actualizar d[i]
        d0.add_updater(lambda z: z.set_value(t0.get_value()))
        d1.add_updater(lambda z: z.set_value(t1.get_value()))
        d2.add_updater(lambda z: z.set_value(t2.get_value()))
        d3.add_updater(lambda z: z.set_value(t3.get_value()))
        #d[i].move_to(np.array([])) Si quiero que se vea en pantalla el valor de d[i]
        d0.move_to(np.array([-5.2,2.7,0])).set_color("red").scale(0.7)
        d1.move_to(np.array([-5.2,2.2,0])).set_color("red").scale(0.7)
        d2.move_to(np.array([-5.2,1.7,0])).set_color("red").scale(0.7)
        d3.move_to(np.array([-5.2,1.2,0])).set_color("red").scale(0.7)
        a = MathTex("a=",color="white").move_to(np.array([-6,2.7,0])).scale(0.7)
        b = MathTex("b=",color="white").move_to(np.array([-6, 2.2, 0])).scale(0.7)
        c = MathTex("c=",color="white").move_to(np.array([-6, 1.7, 0])).scale(0.7)
        d = MathTex("d=",color="white").move_to(np.array([-6, 1.2, 0])).scale(0.7)
        curva.add_updater(lambda z: z.become(ax.plot(lambda x: t0.get_value()*x**3+t1.get_value()*x**2+t2.get_value()*x+t3.get_value(), color="red"))) #la cubica se va actualizando

        func= ax.plot(lambda x: x**3+1) #elijo esta funcion para hacer mover la recta tangente
        x=ValueTracker(-2)
        dx=ValueTracker(0.001)
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
        dot1= always_redraw(
            lambda: Dot()
            .scale(0.9)
            .move_to(ax.c2p(x.get_value(), func.underlying_function(x.get_value()))) #el punto 1 se mueve donde mande x.
        )
        dot2= always_redraw(
            lambda: Dot()
            .scale(0.9)
            .move_to(
                ax.c2p((x).get_value()+dx.get_value(), func.underlying_function(x.get_value()+dx.get_value()),) #el punto 2 se mueve ligeramente respecto al punto 1, asi la secante se parece a la tangente.
            )

        )
        #escribo el polinomio, lo desplazo y creo los ejes
        self.play(Write(eq1))
        self.wait(15)
        self.play(Transform(eq1,eq2))
        self.play(Create(ax))

        #creo cubicas con distintos parametros

        self.play(Create(curva))
        self.add(d0,d1,d2,d3,a,b,c,d) #agrego texto que indica el valor de los parametros en tiempo real
        #self.play()
        self.play(t0.animate.set_value(3),t1.animate.set_value(-3),t2.animate.set_value(-3),t3.animate.set_value(2), run_time=4) #cambia el valor de los parametros
        self.play(t0.animate.set_value(-0.5), t1.animate.set_value(-1), t2.animate.set_value(1), t3.animate.set_value(0),
                  run_time=4)
        self.play(t0.animate.set_value(1), t1.animate.set_value(0), t2.animate.set_value(0),
                  t3.animate.set_value(1),
                  run_time=4)
        self.wait(6)
        #genero y desplazo la recta tangente
        self.play(Create(VGroup(dot1, dot2, tangent)))
        self.add(recta)
        self.play(x.animate.set_value(1.5), run_time=5) #cambio valores de x para que la tangente se calcule sobre distintos puntos
        self.play(x.animate.set_value(-1), run_time=3)
        self.play(x.animate.set_value(0), run_time=3)
        self.wait(10)
        self.play(FadeOut(d0,d1,d2,d3,a,b,c,d,curva,ax,dot1,dot2,tangent,eq1,recta))
        self.wait(3)