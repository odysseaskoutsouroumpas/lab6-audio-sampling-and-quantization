import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

# Διαβάζουμε τα δύο αρχεία ήχου
fs1, y1 = wav.read('sound_2.wav')
fs2, y2 = wav.read('sound_3.wav')

# Αν είναι stereo, τα μετατρέπουμε σε mono
if y1.ndim > 1:
    y1 = y1.mean(axis=1).astype(np.int16)
if y2.ndim > 1:
    y2 = y2.mean(axis=1).astype(np.int16)

# Αν έχουν διαφορετικές συχνότητες δειγματοληψίας, σταματάμε
if fs1 != fs2:
    raise ValueError("Τα δύο αρχεία πρέπει να έχουν την ίδια συχνότητα δειγματοληψίας")
fs = fs1  # Χρησιμοποιούμε μία κοινή συχνότητα

# Κόβουμε τα σήματα ώστε να έχουν το ίδιο μήκος
min_length = min(len(y1), len(y2))
y1, y2 = y1[:min_length], y2[:min_length]

# Δημιουργούμε τους συντελεστές fade-in και fade-out
fade_in = np.linspace(0, 1, min_length)
fade_out = np.linspace(1, 0, min_length)

# Εφαρμόζουμε το fade-in και fade-out στα δύο σήματα
y1_fade = (y1 * fade_in).astype(np.int16)
y2_fade = (y2 * fade_out).astype(np.int16)

# Μίξη των σημάτων
y_mixed = np.clip(y1_fade + y2_fade, -32768, 32767).astype(np.int16)

# Αποθήκευση των αρχείων
wav.write('mixed_audio.wav', fs, y_mixed)
wav.write('fadein_audio.wav', fs, y1_fade)
wav.write('fadeout_audio.wav', fs, y2_fade)

# Σχεδίαση των σημάτων
plt.figure(figsize=(10, 5))
plt.plot(y1[:5000], label="Original Sound 1", alpha=0.5)
plt.plot(y2[:5000], label="Original Sound 2", alpha=0.5)
plt.plot(y_mixed[:5000], label="Mixed Audio", linestyle="dashed")
plt.legend()
plt.xlabel('Δείγματα')
plt.ylabel('Πλάτος')
plt.title('Μίξη Ήχου και Fade Effects')
plt.show()

print("Τα αρχεία αποθηκεύτηκαν επιτυχώς!")
