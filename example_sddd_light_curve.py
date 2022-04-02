import numpy as np
import math
import sys

import matplotlib.pyplot as plt

# Program to calculate synthetic light curves from the radioactive decay of isotopes includes 56Co, 57Co, 55Fe.
# References:
#   Seitenzahl et al (2009). http://dx.doi.org/10.1111/j.1365-2966.2009.15478.x
#   Seitenzahl et al (2014). http://dx.doi.org/10.1088/0004-637X/792/1/10
#   Graur et al (2016). https://arxiv.org/pdf/1505.00777v3.pdf

# Define constants

pi = math.pi

au = 1.49597871e13 # cm
pc = 3.08567758e18 # cm
year = 3.e7 # s
t_hubble = 13.8e9 * year # s
mean_stellar_mass = 0.4 # solar masses
mean_bulge_mass = 0.27 # solar masses
msun = 1.987e33 # gm
lsun = 3.8270e33 # erg s^(-1)

def luminosity (A, mass_A, time):

# Return luminosity according to Bateman equation; see Seitenzahl et al (2014)
# Time is in units of days, A atomic number, and mass_A mass in solar masses 

   B = 0.235   # scaling factor - see eqn. 1, Graur et al, 2016

   if (A == 55):

     lambda_A = 6.916e-4  # inverse of half-life (days^-1) of isotope A
     q_A = 3.973 + 0.000 + 0.000 + 1.635  # average energy per decay (keV)
           # Auger e- + IC e- + e+ + Xray
  
   elif (A == 56):

     lambda_A = 8.975e-3  # inverse of half-life (days^-1) of isotope A
     q_A = 3.355 + 0.374 + 115.7 + 1.588  # average energy per decay (keV)

   elif (A == 57): # Co57 decay

     lambda_A = 2.551e-3  # inverse of half-life (days^-1) of isotope A
     q_A = 7.594 + 10.22 + 0.000 + 3.598  # average energy per decay (keV)

   else:
     print ('ERROR : isotope not defined.')
     sys.exit ()

   return 2.221 * (B / A) * lambda_A * mass_A * q_A * \
           math.exp (-lambda_A * time) * 1.e43   # erg/s



def magtolum (mag):

# return luminosity in erg/s given absolute magnitude

  abs = mag - 5. * (math.log (15.2e6, 10.) - 1.)
  fac = (100.)**(1./5.)
  return fac**(4.83 - abs) * lsun



# Graur et al, 2016 data
mass_co56 = 0.7
#mass_co57 = .043 * mass_co56
#mass_fe55 = 1.2 * mass_co57

# Dave et al DDT model
#mass_co57 = .033 * mass_co56
#mass_fe55 = 2.2373 * mass_co57

# Graur et al, 2016 
mass_co57_low = mass_co56 * (.043 - .011)
mass_co57_high = mass_co56 * (.043 + .012)
mass_fe55_low = 1.2 * mass_co57_low
mass_fe55_high = 1.2 * mass_co57_high

# Dave et al DDT
mass_co57_low = mass_co56 * (.03 - .011)
mass_co57_high = mass_co56 * (.03 + .012)
mass_fe55_low = 2.2373 * mass_co57_low
mass_fe55_high = 2.2373 * mass_co57_high

# Dave et al GCD model
#mass_co57 = .034 * mass_co56
#mass_fe55 = 2.06 * mass_co57
mass_co57_low = 1.49e-2
mass_co57_high = 1.88e-2
mass_fe55_low = 3.73e-3
mass_fe55_high = 1.33e-2


times = np.linspace (0., 2000., 100) # create array of equally-space times
lum56   = np.zeros (100) # and array of luminosities
lum57   = np.zeros (100) 
lum57high = np.zeros (100)
lum57low = np.zeros (100)
lum55   = np.zeros (100)
lum55high = np.zeros (100)
lum55low = np.zeros (100)
totlum  = np.zeros (100)
totlumhigh = np.zeros (100)
totlumlow = np.zeros (100)

index = 0

for time in np.nditer (times):

  lum56 [index] = luminosity (56, mass_co56, time)
  lum57high [index] = luminosity (57, mass_co57_high, time)
  lum57low  [index] = luminosity (57, mass_co57_low, time)
  lum55high [index] = luminosity (55, mass_fe55_high, time)
  lum55low  [index] = luminosity (55, mass_fe55_low, time)
  index = index + 1

totlumhigh = lum55high + lum56 + lum57high
totlumlow = lum55low + lum56 + lum57low

# data points from Graur et al, 2016

d = [924.5, 976.9, 1055.6]
lum = [magtolum (25.76), magtolum (25.94), magtolum (26.29) ]

# F350LP extinction according to Graur et al, 2015
extinction = .054 + .515  # Milky-Way + Host galaxy
dayarr = np.asarray (d)
lumarr = np.asarray (lum) - extinction

# Construct plot

fig, ax = plt.subplots (1)


ax.plot (times, np.log10 (totlumhigh), color = 'blue', linestyle = 'solid', label = 'Total Single-Degenerate')
ax.plot (times, np.log10 (totlumlow), color = 'red', linestyle = 'solid', label = 'Total Double-Degenerate')

#ax.fill_between (times, np.log10 (totlumlow), np.log10 (totlumhigh), facecolor = 'grey', alpha = 0.25, label = 'Total')
ax.plot (times, np.log10 (lum56), label = '$^{56}$Co', linewidth = 2, color ='black', linestyle = 'dashed')

ax.plot (times, np.log10 (lum57high), linestyle = 'dotted', label = '$^{57}$Co', color = 'blue')
ax.plot (times, np.log10 (lum57low), linestyle = 'dotted', color = 'red')

ax.plot (times, np.log10 (lum55high), linestyle = 'dashdot', label = '$^{55}$Fe', color = 'blue')
ax.plot (times, np.log10 (lum55low), linestyle = 'dashdot', color = 'red')

#ax.fill_between (times, np.log10 (lum57low), np.log10 (lum57high), facecolor = 'red', alpha=0.25, label = '$^{57}$Co')
#ax.fill_between (times, np.log10 (lum55low), np.log10 (lum55high), facecolor = 'green', alpha=0.25, label = '$^{55}$Fe')

plt.xlim( [500., 2000.] )
plt.ylim( [35.0, 39.] )
plt.xlabel ('Time (d)')
plt.ylabel ('Luminonsity (erg s$^{-1}$)')
plt.title ('Late-Time SNe Ia Luminosity vs. time')
plt.rcParams.update ( {'font.size' : 13})
plt.legend()
plt.show()
