#%%
import numpy as np
from scipy.integrate import solve_ivp
from fvinc import fvinc

# Condições iniciais
y0 = np.array([0, 1, 0, .8, 0, 1.2])
tspan = [0, 25]


# Solução com RK23
sol_RK23 = solve_ivp(fvinc, [tspan[0], tspan[-1]], y0, method="RK23", rtol = 1e-4)

#%%


# %%

