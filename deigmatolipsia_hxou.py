import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

# Διαβάζουμε το αρχείο ήχου
fs, y1 = wav.read('sound_2.wav')

# Δημιουργία άξονα χρόνου
t = np.arange(len(y1)) / fs

# Συνάρτηση downsampling
def downsample_signal(signal, factor):
    return signal[::factor]

# Εφαρμογή downsampling για διαφορετικούς παράγοντες
downsampling_factors = [2, 3, 4, 5, 6]
downsampled_signals = [downsample_signal(y1, f) for f in downsampling_factors]

# Σχεδίαση αποτελεσμάτων
plt.figure(figsize=(10, 5))
for i, ds_signal in enumerate(downsampled_signals):
    plt.plot(ds_signal[:1000], label=f'Factor = {downsampling_factors[i]}')

plt.legend()
plt.xlabel('Δείγματα')
plt.ylabel('Πλάτος')
plt.title('Downsampled Σήματα')
plt.show()

# Αποθήκευση των downsampled σημάτων σε αρχεία .wav
for i, ds_signal in enumerate(downsampled_signals):
    wav.write(f'downsampled_{downsampling_factors[i]}x.wav', fs // downsampling_factors[i], ds_signal)

print("Τα downsampled αρχεία αποθηκεύτηκαν επιτυχώς!")
