from typing import List, Dict

def solution(num: int) -> int:
    f = num
    if num % 2 == 0:
        while num % 2 == 0:
            num = num // 2
        f = f // 2
    i = 3
    while i * i <= num:
        if num % i == 0:
            while num % i == 0:
                num = num // i
            f = f // i
            f = f * (i - 1)
        i = i + 2
    if num > 1:
        f = f // num
        f = f * (num - 1)
    return f
