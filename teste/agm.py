from math import sqrt

def AGM(x: float, y: float, err=1.e-16, intmax = 100):
    """Retorna a média aritmética-geométrica de dois números
    reais positivos x e y definida como o limite das sequências

    a(n+1) = 1/2*(a(n) + a(n)) 
    g(n+1) = sqrt(a(n) * g(n))
    
    Ambas as sequências convergem para o mesmo número

    Args:
        x (float): 
        y (float): 
        err (float, optional): erro relativo. Defaults to 1.e-16.
        intmax (int, optional): número máximo de interações. Defaults to 100.

    Returns:
        tuple: ai, gi, interacaoes
    """
    a = x
    g = y
    ai = 1/2 * (x + y)
    gi = sqrt(x * y)
    interacoes = 0
    while err < ( abs((ai - a) / a) and abs((gi - g) / g) ) or interacoes == intmax:
        a = ai
        g = gi
        gi = sqrt(a * g)
        ai = 1/2 * (a + g)
        interacoes += 1
    return ai, gi, interacoes

