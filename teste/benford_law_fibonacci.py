

""" 
o condigo de benford-law foi escrito aprimorado pela IA, o meu original se encontra no texte 1 de computação cientifica.
"""

def fibonacci(N:int) -> list:
    """ Calcula os N primeiros números 
    da série de Fibonacci

    Args:
        N (int): quantidade de números da série

    Returns:
        list: N's números da série 
    """
    fibonacci = [0,1]
    for k in range(0,N-2):
        i = fibonacci[0+k]
        j = fibonacci[1+k]
        fibonacci.append(j+i)
    return fibonacci

def benford_law(numbers: list) -> list:
    """ Calculates the Benford's Law for a list of numbers.
    """
    frequencies = {str(digit): 0 for digit in range(1, 10)}
    print(frequencies)
    for num in numbers:
        digit = str(num)[0]
        if digit == '0':
            pass
        else:
            frequencies[digit] += 1
    normalized_frequencies = [frequencies[str(i)] / len(numbers) for i in range(1, 10)]
    return normalized_frequencies
print(benford_law(fibonacci(10000)))