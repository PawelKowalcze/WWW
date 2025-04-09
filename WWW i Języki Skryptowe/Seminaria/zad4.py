import random
import math

#a)
yes = 0

for i in range(10^8):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    if math.gcd(a, b) == 1:
       yes += 1

probability = yes / (10^8)

#Tw Cesaro: 6/pi^2 = 0,608

myPI = math.sqrt(6/probability)
print(myPI)



# --------------------------
#b)
def blum_blum_shub(p, q, seed, bits_count):
    # Sprawdzenie warunków wstępnych
    if p % 4 != 3 or q % 4 != 3:
        raise ValueError("Zarówno p, jak i q muszą być ≡ 3 (mod 4)")

    n = p * q
    x = seed % n
    bits = []

    for _ in range(bits_count):
        x = pow(x, 2, n)         # x = x^2 mod n
        bit = x % 2              # najmłodszy bit
        bits.append(bit)

    return bits

# Przykład użycia:
p = 383
q = 503
seed = 211       # Musi być względnie pierwsze z n
bits_count = 20  # Liczba generowanych bitów

generated_bits = blum_blum_shub(p, q, seed, bits_count)
print("Wygenerowane bity:", ''.join(map(str, generated_bits)))
