#%%
import numpy as np
import matplotlib.pyplot as plt

def Dif_frente(f, x, h):
    """retorna a derivada de f usando aproximação x+h """
    return (f(x + h) - f(x)) / h

def Dif_atras(f, x, h):
    """retorna a derivada de f usando aproximação x-h """
    return (f(x) - f(x - h)) / h 

def Dif_centrada(f, x, h):
    """retorna a derivada de f usando aproximação x-h e x+h

    Args:
        f (função): função a ser derivada
        x (float): ponto em que a derivada deve ser calculada 
    """
    return (f(x + h) - f(x - h)) / (2 * h)



senx = lambda x: np.sin(x)

# %%
plot1 = plt.subplot2grid((50, 1), (0, 0), rowspan = 20) 
plot2 = plt.subplot2grid((50, 1), (25, 0), rowspan = 20) 
plot3 = plt.subplot2grid((50, 1), (7, 0)) 

for n in range(5,11):
    h = (2*np.pi) / 2**n
    x = np.linspace(0, 2*np.pi, 2**n)
    y_centrada = [Dif_centrada(senx, xi, h) for xi in x]
    y_frente = [Dif_frente(senx, xi, h) for xi in x]
    y_atras = [Dif_atras(senx, xi, h) for xi in x]
    plot1.plot(x,y_centrada, label = f"{n}")
    plot2.plot(x,y_frente, label = f"{n}")
    plot3.plot(x,y_atras, label = f"{n}")

plot1.set_title("Centrada")
plot1.legend()
plot2.set_title("Frente")
plot2.legend()
plot3.set_title("Atras")
plot3.legend()
plt.savefig("derivadas.pdf")
plt.show()


# %%
