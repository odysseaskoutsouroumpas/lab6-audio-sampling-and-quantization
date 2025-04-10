import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

# Διαβάζουμε το αρχείο ήχου
fs, y1 = wav.read('sound_2.wav')

# Προσθήκη λευκού θορύβου
noise = np.random.normal(0, np.std(y1) / 10, y1.shape)
y1_noisy = np.clip(y1 + noise, -32768, 32767).astype(np.int16)

# Κβάντιση
qbits = [6, 5, 4, 3, 2]
quantized_signals = []
for q in qbits:
    levels = 2 ** q
    q_signal = np.round(y1_noisy / (32767 / (levels - 1))) * (32767 / (levels - 1))
    quantized_signals.append(q_signal.astype(np.int16))

# Σχεδίαση γραφήματος
plt.figure()
for i, q_signal in enumerate(quantized_signals):
    plt.plot(q_signal[:1000], label=f'{qbits[i]} bits')
plt.legend()
plt.title('Κβάντιση με Θόρυβο')
plt.show()

# Αποθήκευση αρχείων
wav.write('white_noise.wav', fs, y1_noisy)
for i, q_signal in enumerate(quantized_signals):
    wav.write(f'quantized_{qbits[i]}bit.wav', fs, q_signal)

print("Αποθήκευση ολοκληρώθηκε!")
