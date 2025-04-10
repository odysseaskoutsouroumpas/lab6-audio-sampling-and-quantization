import numpy as np
import scipy.io.wavfile as wav

# Ορισμός παραμέτρων
fs = 44100  # Συχνότητα δειγματοληψίας (Hz)
duration = 2  # Διάρκεια σε δευτερόλεπτα
frequency = 440  # Συχνότητα ημιτόνου (Hz)

# Δημιουργία ημιτονοειδούς σήματος 440Hz
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
y = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)  # Μετατροπή σε 16-bit PCM

# Αποθήκευση σε WAV
wav.write("test_sound.wav", fs, y)

print("Το αρχείο 'test_sound.wav' δημιουργήθηκε επιτυχώς!")
