import numpy as np
import matplotlib.pyplot as plt

mej = [8.43e-2, 1.95e-1, 3.72e-1, 4.78e-1, 8.59e-1, 1.21e0, 1.23e0, 1.31e0, 1.31e0, 1.40e0, 1.40e0, 1.40e0, 1.40e0, 1.40e0]

mbound = [1.32e0, 1.21e0, 1.03e0, 9.26e-1, 5.45e-1, 1.90e-1, 1.33e-1, 9.0e-2, 1.02e-1]

# Ejecta yields

ni56 = [3.45e-2, 7.30e-2, 1.58e-1, 1.83e-1, 2.64e-1, 3.35e-1, 3.26e-1, 3.55e-1, 3.29e-1, 3.78e-1, 3.71e-1, 3.34e-1, 3.40e-1, 3.15e-1]

co55 = [6.16e-4, 1.49e-3, 3.22e-3, 3.93e-3, 5.87e-3, 7.96e-3, 5.81e-3, 8.45e-3, 7.72e-3, 8.96e-3, 9.57e-3, 7.88e-3, 9.07e-3, 7.66e-3]

fe55 = [7.21e-5, 2.63e-4, 4.43e-4, 6.67e-4, 1.15e-3, 1.50e-3, 1.28e-4, 1.74e-3, 2.87e-3, 1.90e-3, 2.20e-3, 1.97e-3, 2.87e-3, 3.09e-3]

ni57 = [1.26e-3, 2.68e-3, 5.54e-3, 6.54e-3, 9.25e-3, 1.19e-2, 1.03e-2, 1.25e-2, 1.15e-2, 1.34e-2, 1.33e-2, 1.16e-2, 1.24e-2, 1.08e-2]

co57 = [3.63e-5, 1.32e-4, 2.22e-4, 3.34e-4, 5.64e-4, 7.34e-4, 4.95e-5, 8.49e-4, 1.35e-3, 9.31e-4, 1.08e-3, 9.63e-4, 1.38e-3, 1.45e-3] 

meja = np.asarray (mej)
ni56a = np.asarray (ni56)
co55a = np.asarray (co55)
fe55a = np.asarray (fe55)
ni57a = np.asarray (ni57)
co57a = np.asarray (co57)

chain55 = co55a + fe55a
chain56 = ni56a 
chain57 = ni57a + co57a
fftofiftyseven = chain55 / chain57
fftofiftysix = chain55 / chain56

plt.plot (ni56a, fftofiftysix, 'bo')

plt.xlabel ('$M$ ($^{56}$Ni + $^{56}$Co) / $M_{\odot}$', fontsize = 18)
plt.ylabel ('X ($^{55}$Ni + $^{55}$Co + $^{55}$Fe) / X ($^{56}$Ni + $^{56}$Co) ')
plt.title ('Fink et al (2014) Failed Detonation Yields')

plt.show ()
