import time

# Parameter LCG
a = 22695477
c = 1
m = 2**31

# Inisialisasi seed dari waktu sekarang (ms)
x = int(time.time() * 1000)

def lcg():
    """Update global x dan kembalikan nilai pseudo-acak selanjutnya."""
    global x
    x = (a * x + c) % m
    return x

# Contoh penggunaan:
for i in range(5):
    print(lcg())
