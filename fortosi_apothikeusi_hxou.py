import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

# Διαβάζουμε το αρχείο ήχου
fs, y1 = wav.read('sound.wav')

# Δημιουργία άξονα χρόνου
t = np.arange(len(y1)) / fs

# Αποθήκευση του ίδιου αρχείου ξανά
wav.write('sound_output.wav', fs, y1)

# Σχεδίαση του σήματος
plt.plot(t[:5000], y1[:5000])  # Εμφανίζουμε τα πρώτα 5000 δείγματα
plt.xlabel('Χρόνος (s)')
plt.ylabel('Πλάτος')
plt.title('Αναπαράσταση Σήματος Ήχου')
plt.show()
