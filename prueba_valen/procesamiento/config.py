"""Constantes del proyecto. Todo lo que se pueda querer cambiar vive aca, no en las funciones."""
import os
from pathlib import Path

# --- Rutas -------------------------------------------------------------------
# Absolutas a partir de la ubicacion de este archivo, asi el codigo corre igual
# desde cualquier carpeta. Estructura asumida:
#   <repo>/data/ds005293/...            (datos crudos)
#   <repo>/<carpeta>/procesamiento/config.py
# Si en alguna compu el dataset esta en otro lado: export TP_RAIZ_DATOS=/ruta/al/ds005293
RAIZ_PROYECTO = Path(__file__).resolve().parents[2]
RAIZ_DATOS = Path(os.environ.get("TP_RAIZ_DATOS", RAIZ_PROYECTO / "data" / "ds005293"))
CARPETA_SALIDA = Path(os.environ.get("TP_SALIDA", RAIZ_PROYECTO / "data" / "derived_mine"))

TAREA = "95ByBP"                    # nombre de la tarea en los archivos BIDS

# --- Canales -----------------------------------------------------------------
# Canales que los autores descartan (TP9/TP10: mastoides; HEOR: ojo horizontal)
CANALES_DESCARTADOS = ["TP9", "TP10", "HEOR"]
CANAL_EOG = "VEO"                   # ojo vertical: referencia para detectar parpadeos

# --- Eventos -----------------------------------------------------------------
# Regla de los autores (code/preprocessing_95.m): un trigger S 32..S 35 seguido
# inmediatamente por S100 es un pulso laser. Los otros codigos son otras modalidades.
CODIGOS_LASER = {32: 1, 33: 2, 34: 3, 35: 4}   # codigo del trigger -> nivel E1..E4
CODIGO_CONFIRMACION = 100
NIVELES = {"E1": 1, "E2": 2, "E3": 3, "E4": 4}

# Esperado en el dataset: 80 pulsos por sujeto, 20 por nivel
PULSOS_POR_NIVEL = 20

# --- Filtros (filtros.py) ----------------------------------------------------
PASA_ALTOS_HZ = 1.0
PASA_BAJOS_HZ = 100.0
NOTCH_HZ = 50.0                     # red electrica argentina/china: 50 Hz
NOTCH_ANCHO_HZ = 4.0                # rechaza 48-52 Hz (como filtrado.py)
ORDEN_IIR = 4                       # solo para la comparacion FIR vs IIR
PASA_BAJOS_LEP_HZ = 30.0            # para mirar y medir LEPs

# --- Segmentacion ------------------------------------------------------------
TMIN, TMAX = -1.0, 2.0              # ventana de la epoca respecto del pulso (s)
BASELINE = (-1.0, 0.0)              # linea de base: todo el pre-estimulo

# --- Control de calidad ------------------------------------------------------
CANAL_QC = "Cz"                     # vertex: donde N2 y P2 son maximos
VENTANA_N2 = (0.12, 0.30)           # s; busqueda del minimo (N2 en mano ~200-250 ms)
VENTANA_P2 = (0.25, 0.50)           # s; busqueda del maximo (P2 ~300-400 ms)
UMBRALES_PTP_UV = (100, 150)        # lineas de referencia en la figura de pico a pico