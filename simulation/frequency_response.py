import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Wirebond parameters
Lw = 1.5e-9
Cw = 0.2e-12
Rw = 0.05

num_w = [1]
den_w = [Lw*Cw, Rw*Cw, 1]

system_w = signal.TransferFunction(num_w, den_w)

# Flip-chip parameters
Lf = 0.1e-9
Cf = 0.05e-12
Rf = 0.02

num_f = [1]
den_f = [Lf*Cf, Rf*Cf, 1]

system_f = signal.TransferFunction(num_f, den_f)

f = np.logspace(6, 10.78, 2000)
w = 2*np.pi*f

w_w, mag_w, phase_w = signal.bode(system_w, w)
w_f, mag_f, phase_f = signal.bode(system_f, w)

plt.figure(figsize=(10,6))

plt.semilogx(f, mag_w, label="Wirebond")
plt.semilogx(f, mag_f, label="Flip-Chip")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Frequency Response")

plt.legend()
plt.grid()

plt.show()
