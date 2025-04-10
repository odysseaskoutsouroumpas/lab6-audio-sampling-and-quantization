import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

# Διαβάζουμε το αρχείο ήχου
fs, y1 = wav.read('sound_2.wav')

# Δημιουργία άξονα χρόνου
t = np.arange(len(y1)) / fs

# Συνάρτηση κβάντισης

def quantize_signal(signal, qbit):
    levels = 2 ** qbit
    quantized_signal = np.round(signal / (32767 / (levels - 1))) * (32767 / (levels - 1))
    return quantized_signal.astype(np.int16)

# Εφαρμογή κβάντισης για διαφορετικά επίπεδα bit
qbits = [6, 5, 4, 3, 2]
quantized_signals = [quantize_signal(y1, q) for q in qbits]

# Σχεδίαση του αρχικού και των κβαντισμένων σημάτων
plt.figure(figsize=(10, 5))
for i, q_signal in enumerate(quantized_signals):
    plt.plot(t[:1000], q_signal[:1000], label=f'qbit = {qbits[i]}')

plt.legend()
plt.xlabel('Χρόνος (s)')
plt.ylabel('Πλάτος')
plt.title('Κβαντισμένα Σήματα')
plt.show()

# Αποθήκευση των κβαντισμένων σημάτων σε αρχεία .wav
for i, q_signal in enumerate(quantized_signals):
    wav.write(f'quantized_{qbits[i]}bit.wav', fs, q_signal)

print("Τα κβαντισμένα αρχεία αποθηκεύτηκαν επιτυχώς!")
