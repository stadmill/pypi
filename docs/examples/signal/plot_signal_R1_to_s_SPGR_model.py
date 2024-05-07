"""
==============
Linear model for relationship between R1 and magnitude signal
==============

Demonstrating the linear model for relationship between R1 and magnitude signal, s = k.R1
"""

# %%
# Import necessary packages
import numpy as np
import matplotlib.pyplot as plt
import osipi

# %%
# Convert a series of R1 values to the corresponding signal intensities using the SPGR model.

R1 = np.linspace(0.1, 10, 50)  # R1 in units of /s.
s0 = np.float64(100)  # fully T1-relaxed signal in units of arb. unit.
tr = np.float64(5e-3)  # repetition time in units of s.
a = np.float64(15)  # prescribed flip angle in units of deg.
signal = osipi.R1_to_s_SPGR_model(R1, s0, tr, a)  # signal in arb. unit
print(f'Signal: {signal}')

# Plot signal vs. R1
plt.plot(R1, signal, 'r-')
plt.xlabel('R1 (/sec)')
plt.ylabel('signal (arb. unit)')
plt.show()
