import numpy as np
import matplotlib.pyplot as plt


def quantize_signal(signal, qbit):
    """
    Υλοποίηση της κβάντισης ενός σήματος με qbit bits.
    """
    min_val, max_val = np.min(signal), np.max(signal)
    signal_norm = (signal - min_val) / (max_val - min_val) * 2 - 1  # Κανονικοποίηση [-1,1]

    levels = 2 ** qbit  # Αριθμός επιπέδων κβάντισης
    signal_quantized = np.round(signal_norm * (levels // 2)) / (levels // 2)  # Κβάντιση

    return signal_quantized * (max_val - min_val) / 2 + (max_val + min_val) / 2  # Επαναφορά εύρους


# Δοκιμή με ημίτονο
t = np.linspace(0, 1, 1000)
sin_wave = np.sin(2 * np.pi * 5 * t)

plt.figure()
plt.plot(t, sin_wave, label="Αναλογικό")
for q in [5, 4, 3, 2, 1]:
    plt.plot(t, quantize_signal(sin_wave, q), label=f"{q} bits")
plt.legend()
plt.show()
