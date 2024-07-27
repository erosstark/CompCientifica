import numpy as np
from scipy.integrate import solve_ivp
from fvinc import fvinc

# Condições iniciais
y0 = np.array([0, 1, 0, .8, 0, 1.2])
tspan = [0, 25]
t = np.linspace(tspan[0], tspan[-1], 1500)


# Solução com RK23
sol_RK23 = solve_ivp(fvinc, [tspan[0], tspan[-1]], y0, method="RK23", rtol = 1e-4, t_eval=t)

time_data = sol_RK23.t
x_data = sol_RK23.y[0]
y_data = sol_RK23.y[1]
z_data = sol_RK23.y[2]

from manim import *

class PendulumAnimation(ThreeDScene):
    def construct(self):
        
        ######################
        #  -----Intro------  #
        ######################
        
        # Titulo da Animação
        Titulo = Text("Pendulum Simulation").scale(1.5)
        self.play(Write(Titulo))
        
        self.wait(0.5)

        # texto: Nome do autor
        Autor = Text("Eros Moreira").to_edge(DOWN).scale(1)
        self.play(FadeIn(Autor))

        self.wait()
        
        self.play(FadeOut(Autor), FadeOut(Titulo))
        
        self.wait()
        
        #################################
        #  -----Pêndulo Animação------  #
        #################################
        
        # Define a posião da câmera.
        self.set_camera_orientation(phi= 65 * DEGREES, theta=10*DEGREES, zoom = 3)
        
        # Eixo 3D
        axes = ThreeDAxes(x_range = [-1, 1, 0.2],
                          y_range = [-1, 1, 0.2],
                          z_range = [-1, 1, 0.2],
                          x_length=5,
                          y_length=5,
                          z_length=5,
                          num_axis_pieces=4)
        axes.set_color = (WHITE)
        self.play(Create(axes))
        
        # Cria a linha do pêndulo.
        pendulum_line = Line(start = ORIGIN, end = y0[0:3], color = BLUE)
        self.play(Create(pendulum_line))
        
        # Cria o bola do pêndulo.
        pendulum_bob = Dot3D(pendulum_line.get_end(), color=RED, radius=0.05)
        self.play(Create(pendulum_bob))
        
        # Cria o grupo do pêndulo.
        pendulum = VGroup(pendulum_line, pendulum_bob)
        
        self.wait(2)
        
        self.timeStart = self.renderer.time
        # Animate the pendulum based on the data
        self.play(UpdateFromFunc(pendulum, lambda mob: self.update_pendulum(mob)),
            run_time=sol_RK23.t[-1],
            rate_func=linear
        )
        

    def update_pendulum(self, pendulum):
        
        time = self.renderer.time - self.timeStart
        x = np.interp(time, time_data, x_data)
        y = np.interp(time, time_data, y_data)
        z = np.interp(time, time_data, z_data)

        # Atualiza a posição do pêndulo.
        pendulum[0].put_start_and_end_on(ORIGIN, [x, y, z])
        pendulum[1].move_to([x, y, z])
        d = Dot3D([x, y, z], color=BLACK, radius=0.005)
        self.add(d)
        
        # Anima a câmera
        self.begin_3dillusion_camera_rotation(rate=0.1)

if __name__ == "__main__":
    config.background_color = ManimColor.from_rgb((210, 201, 182))
    config.quality = 'high_quality'
    
    scene = PendulumAnimation()
    scene.render()
