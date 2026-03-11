import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0,5e-9,2000)

# Wirebond
Lw = 1.5e-9
Cw = 0.2e-12
Rw = 0.05

num_w = [1]
den_w = [Lw*Cw, Rw*Cw, 1]

system_w = signal.TransferFunction(num_w, den_w)
tw, yw = signal.step(system_w, T=t)

# Flipchip
Lf = 0.1e-9
Cf = 0.05e-12
Rf = 0.02

num_f = [1]
den_f = [Lf*Cf, Rf*Cf, 1]

system_f = signal.TransferFunction(num_f, den_f)
tf, yf = signal.step(system_f, T=t)

plt.figure(figsize=(10,6))

plt.plot(tw*1e9, yw, label="Wirebond")
plt.plot(tf*1e9, yf, label="Flip-Chip")

plt.xlabel("Time (ns)")
plt.ylabel("Voltage")
plt.title("Ringing Comparison")

plt.legend()
plt.grid()

plt.show()
