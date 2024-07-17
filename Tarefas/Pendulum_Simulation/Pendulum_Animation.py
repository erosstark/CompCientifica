#%%
import numpy as np
from scipy.integrate import solve_ivp
from fvinc import fvinc

# Condições iniciais
y0 = np.array([0, 1, 0, .8, 0, 1.2])
tspan = [0, 25]
t = np.linspace(tspan[0], tspan[-1], 1500)


# Solução com RK23
sol_RK23 = solve_ivp(fvinc, [tspan[0], tspan[-1]], y0, method="RK23", rtol = 1e-4, t_eval=t)
#%%
time_data = sol_RK23.t
x_data = sol_RK23.y[0]
y_data = sol_RK23.y[1]
z_data = sol_RK23.y[2]
#%%
from manim import *
class PendulumAnimation(Scene):
    def construct(self):
        # Create a pendulum line
        pendulum_line = Line(ORIGIN, y0)
        pendulum_bob = Dot(pendulum_line.get_end(), color=RED)
        pendulum = VGroup(pendulum_line, pendulum_bob)

        self.add(pendulum)
        trajectory = Line(y0, pendulum_bob.get_center())
        self.add(trajectory)
        self.wait()

        # Animate the pendulum based on the data
        self.play(
            UpdateFromFunc(pendulum, lambda mob: self.update_pendulum(mob)),
            run_time=sol_RK23.t[-1],
            rate_func=linear
        )

    def update_pendulum(self, pendulum, trajectory):
        # Assuming data contains time_data, x_data, y_data, z_data
        time = self.renderer.time  # Get the current time
        x = np.interp(time, time_data, x_data)
        y = np.interp(time, time_data, y_data)
        z = np.interp(time, time_data, z_data)

        # Update the pendulum position
        pendulum[0].put_start_and_end_on(ORIGIN, [x, y, z])
        pendulum[1].move_to([x, y, z])
        trajectory.put_start_and_end_on(ORIGIN, [x, y, z])
        
        
if __name__ == "__main__":
    scene = PendulumAnimation()
    scene.render()

# %%
# %%
