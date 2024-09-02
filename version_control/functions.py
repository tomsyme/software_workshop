import numpy as nmp

def frequency_calculation(lamdas, temp):
    pi = nmp.pi
    kt = 4.11e-21 * temp / 298
    frequencies = 1/(2*pi) * nmp.sqrt(lamdas/kt)

    return frequencies

print('Hello!')
