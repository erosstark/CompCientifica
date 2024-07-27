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

with open("dados_pendulum.txt", "w") as f:
    for t, x, y, z in zip(time_data, x_data, y_data, z_data):
        f.write(f"{t} {x} {y} {z}\n")
f.close()
        