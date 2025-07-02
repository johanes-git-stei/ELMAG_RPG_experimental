# This is recycled from daspro
# still thinking of way to connect this to questions/answers potions

import time

n: int = 0
a: int = 22695477
c: int = 1
m: int = 2 ** 31

def lcg(n: int) -> int:
    while n < 10:
        if n == 0:
            x: int = int(time.time()*1000)
            n += 1
        else:
            x: int = (a * x + c) % m
            n += 1

    return x

