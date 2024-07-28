import re
from typing import Callable

data = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    pattern = r'\b\d+(\.\d+)?\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))

total_profit = sum_profit(data, generator_numbers)
print(total_profit)
