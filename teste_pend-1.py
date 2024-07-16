#%%
import numpy as np
from scipy.optimize import fsolve
from backward_euler_methods import backward_euler
#%%
# Backward Euler



def beuler(odefun, tspan, y, Nh):
    h = (tspan[1] - tspan[0]) / Nh # tamanho time step
    tt = np.linspace(tspan[0], tspan[1], Nh+1) # time step
    
    y = y.reshape((1, -1)) 
    # print(y)
    
    for t in tt[1:]:
        # Define o sistema de eq
        f = lambda w: w - y[-1] - h * odefun(t, w)
        
        # Resolve o sistema de eq
        w = np.linalg.solve(f, y[-1])
        # print(w)
        y = np.vstack((y, w))
    
    return tt, y

#%%
def fvinc(t, y):
    n = np.size(y)
    f = np.zeros(n)
    
    phix = 2*y[0]
    phiy = 2*y[1]
    phiz = 2*y[2]
    
    H = 2*np.eye(3)
    mass = 1
    
    F1 = 0
    F2 = 0
    F3 = -mass*9.8
    
    xp = np.array(y[3:6])
    
    
    F = np.array([F1, F2, F3])
    G = np.array([phix, phiy, phiz])
    
    lambda_val = (mass * xp.T @ H @ xp + F.T @ G) / (G.T @ G)
    
    f[0:3] = y[3:6]
    
    for k in range(3):
        f[k+3] = (F[k] - lambda_val * G[k]) / mass
    return f

#%%
y0 = np.array([0, 1, 0, .8, 0, 1.2])
tspan = [0, 25]
#%%
# Solução com o backward Euler.
t, Sol_beuler = backward_euler(fvinc, tspan, y0, 100000)

#%%
Sol_beuler
# %%
# Plota a solução com o backward Euler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot(Sol_beuler[:,0], Sol_beuler[:,1], Sol_beuler[:,2])
plt.show()
# %%
