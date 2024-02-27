def is_even_bitwise(value: int):
    """
    Преимущества: Быстрее, тк манипуляции с битами
    Недостатки: Менее понятно, требует знания операций с битами
    """
    return (value & 1) == 0


def is_even_modulus(value: int):
    """
    Преимущества: Понятно и просто
    Недостатки: Медленнее из-за математической операции
    """
    return value % 2 == 0
