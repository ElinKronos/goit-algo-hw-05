# Here begins a new world ...

import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа з тексту, які відокремлені пробілами.
    """
    # Шукаємо дійсні числа у тексті (відокремлені пробілами або межами рядка)
    for match in re.findall(r"(?<=\s)\d+\.\d+(?=\s)|^\d+\.\d+(?=\s)|(?<=\s)\d+\.\d+$", text):
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Підсумовує всі прибутки, використовуючи генератор чисел з тексту.
    """
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1254.08 як основний дохід, доповнений додатковими надходженнями 68.95 і 348.94 доларів."

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")

