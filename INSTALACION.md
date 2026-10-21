# Instalación

## Qué hay que tener
- **Python 3.11 o más nuevo** (`python --version`; en Mac puede ser `python3`).
- **Git**, para clonar y subir cambios.
- **curl**, para bajar los datos. Ya viene en macOS y en Windows 10/11.
- **Espacio en disco:** ~1,4 GB por sujeto descargado (crudo + derivado), más lo que ocupen los resultados.
- Internet para la descarga (los datos vienen de OpenNeuro, vía S3).

## Pasos (una sola vez)

macOS / Linux:
```bash
git clone https://github.com/valjeon/PSIB_Grupo15_EEG.git
cd PSIB_Grupo15_EEG
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Windows (PowerShell):
```powershell
git clone https://github.com/valjeon/PSIB_Grupo15_EEG.git
cd PSIB_Grupo15_EEG
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
```

`pip install -e .` deja el paquete `procesamiento` importable desde cualquier carpeta, y además instala las dependencias (incluye `pytest` y `pybv` por el `[dev]`). Hay que correrlo parado en la carpeta que contiene `pyproject.toml`.

Cada vez que abras una terminal nueva hay que volver a activar el entorno (`source .venv/bin/activate` o `.venv\Scripts\activate`). Se sabe que está activo porque aparece `(.venv)` al principio de la línea.

## Datos
Bajar los sujetos que te tocan (ver `descargar_sujeto.sh`, o `descargar_sujeto.ps1` en Windows):
```bash
bash descargar_sujeto.sh sub-001
```
Quedan en `data/ds005293/`. Esa carpeta no se sube a git.

## Verificar que todo funciona
```bash
python -m pytest -q
```
Deben pasar todos los tests (usan datos sintéticos, no hace falta haber descargado nada).
Con un sujeto descargado:
```bash
python -m procesamiento.verificar sub-001
```
Debe dar 6 sesiones y, en el TOTAL, 20 pulsos por nivel (E1 a E4) y `OK`. Sin argumentos verifica todos los sujetos que haya descargados. Si los datos no están en `data/ds005293` junto al repo, indicá la carpeta con la variable `PSIB_DATOS`.

Los módulos (`datos.py`, `eventos.py`) no se ejecutan directamente: se importan (`from procesamiento import datos`) o se corren con `python -m procesamiento.verificar`.

## Problemas frecuentes
- `ModuleNotFoundError: No module named 'mne'` o `'procesamiento'`: el entorno no está activo o falta `pip install -e ".[dev]"`.
- `cannot import name 'config' from 'procesamiento'`: hay otra carpeta `procesamiento/` sin `__init__.py` que tapa al paquete; moverla (por ejemplo a `exploracion/`).
- `FileNotFoundError ... descargar_sujeto`: ese sujeto no está descargado en esta computadora.
- En Windows, si PowerShell bloquea la activación del entorno: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
