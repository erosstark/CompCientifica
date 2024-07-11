

def number_to_text(num):
    """Converts a number to its text representation.

    Args:
        num (float or int): The number to convert.

    Returns:
        str: The text representation of the number.
    """
    text_numbers = ["zero", "um", "dois", "três", "quatro", "cinco",
                    "seis", "sete", "oito", "nove"]

    text_list = [text_numbers[int(num)] if int(num) in range(10)
                 else "ponto" if num == "." else "" for num in number_strings]

    return " ".join(text_list)

pi_texto = number_to_text(3.1415926)

print(pi_texto)