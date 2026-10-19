from pathlib import Path
import mne
import numpy as np
import matplotlib.pyplot as plt

ARCHIVO = (
    Path(__file__).resolve().parent.parent
    / "data" / "ds005293"
    / "sub-001" / "ses-1" / "eeg"
    / "sub-001_ses-1_task-95ByBP_eeg.vhdr"
)

raw = mne.io.read_raw_brainvision(str(ARCHIVO), preload=True, verbose="ERROR")

#  Marcar los canales de EOG
raw.set_channel_types({"VEO": "eog", "HEOR": "eog"})

# Filtrar una copia, para poder comparar con la señal original
raw_filt = raw.copy()

# Pasabanda 1-100 Hz
raw_filt.filter(l_freq=1.0, h_freq=100.0, method="fir",
                fir_design="firwin", verbose="ERROR")

# Notch centrado en 50 Hz con 4 Hz de ancho -> rechaza 48-52 Hz
raw_filt.notch_filter(freqs=50.0, notch_widths=4.0, method="fir",
                      fir_design="firwin", verbose="ERROR")

# Comparar espectros antes y después
raw.compute_psd(fmax=120).plot()
plt.suptitle("Antes del filtrado")
raw_filt.compute_psd(fmax=120).plot()
plt.suptitle("Después del filtrado")

# Comparar un tramo de señal (10 s a partir del segundo 100)
canales = ["Fz", "Cz", "Pz"]
inicio, fin = 100, 110
fig, axes = plt.subplots(len(canales), 1, figsize=(12, 7), sharex=True)
for ax, canal in zip(axes, canales):
    antes = raw.copy().crop(inicio, fin).get_data(picks=canal)[0] * 1e6
    despues = raw_filt.copy().crop(inicio, fin).get_data(picks=canal)[0] * 1e6
    t = np.linspace(inicio, fin, len(antes))
    ax.plot(t, antes, label="Sin filtrar", alpha=0.6)
    ax.plot(t, despues, label="Filtrada", linewidth=0.8)
    ax.set_ylabel(f"{canal} (µV)")
    ax.legend(loc="upper right")
axes[-1].set_xlabel("Tiempo (s)")
plt.tight_layout()
plt.show()

# Señal sin filtrar --> se ve que tiene el offset de continua, centrada alrededor de 30 microV
# se ve como una señal "gruesa" por el ruido de línea
# Señal filtrada --> se ve que esta alrededor de 0 microV (por el pasa altos de 1 Hz)