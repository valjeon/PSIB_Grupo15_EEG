#!/usr/bin/env bash
# Descarga de ds005293 (experimento 6) desde S3 de OpenNeuro.
# Uso, desde la raiz del repo:   bash descargar_sujeto.sh sub-001 sub-002 ...
BASE=https://s3.amazonaws.com/openneuro.org/ds005293
OUT=data/ds005293

bajar() {  # bajar <ruta relativa>: salta si ya existe; usa .part para no dejar archivos a medias
  local f="$1"
  if [ -s "$OUT/$f" ]; then echo "ya existe: $f"; return; fi
  mkdir -p "$(dirname "$OUT/$f")"
  if curl -fL -o "$OUT/$f.part" "$BASE/$f"; then
    mv "$OUT/$f.part" "$OUT/$f"
  else
    rm -f "$OUT/$f.part"; echo "FALLO: $f"
  fi
}

# Archivos generales del dataset
for f in participants.tsv participants.json README dataset_description.json code/preprocessing_95.m; do
  bajar "$f"
done

# Por sujeto: 6 sesiones de EEG crudo + derivado de los autores
for sub in "$@"; do
  for n in 1 2 3 4 5 6; do
    S="$sub/ses-$n/eeg/${sub}_ses-${n}_task-95ByBP"
    for ext in _eeg.vhdr _eeg.vmrk _eeg.eeg _eeg.json _events.tsv _channels.tsv _electrodes.tsv; do
      bajar "$S$ext"
    done
  done
  bajar "derivatives/rerefer/${sub}_95ByBP.set"
  bajar "derivatives/rerefer/${sub}_95ByBP.fdt"
done
