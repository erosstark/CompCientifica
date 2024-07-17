# Essa é a versão Python do programa fvinc escrito em matlab
#que foi apresentado no livro Scientific Programing with MATLAB and Octave 4th edition

# Esse programa é o sistema de equações da dinâmica de um pêndulo esférico.
# Quando eu entender melhor essa isso eu descrevo melhor.
import numpy as np

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

