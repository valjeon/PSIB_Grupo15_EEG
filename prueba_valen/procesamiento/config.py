"""Constantes del proyecto. Todo lo que se pueda querer cambiar vive aca, no en las funciones."""

RAIZ_DATOS = "data/ds005293"        # donde descargar_sujeto.sh deja el dataset
CARPETA_SALIDA = "data/derived_mine"  # resultados intermedios (epocas, figuras)

TAREA = "95ByBP"                    # nombre de la tarea en los archivos BIDS

# Canales que los autores descartan (TP9/TP10: mastoides; HEOR: ojo horizontal)
CANALES_DESCARTADOS = ["TP9", "TP10", "HEOR"]
CANAL_EOG = "VEO"                   # ojo vertical: referencia para detectar parpadeos

# Regla de los autores (code/preprocessing_95.m): un trigger S 32..S 35 seguido
# inmediatamente por S100 es un pulso laser. Los otros codigos son otras modalidades.
CODIGOS_LASER = {32: 1, 33: 2, 34: 3, 35: 4}   # codigo del trigger -> nivel E1..E4
CODIGO_CONFIRMACION = 100
NIVELES = {"E1": 1, "E2": 2, "E3": 3, "E4": 4}

# Esperado en el dataset: 80 pulsos por sujeto, 20 por nivel
PULSOS_POR_NIVEL = 20
