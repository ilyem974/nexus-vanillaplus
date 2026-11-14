#!/usr/bin/env bash
# Vérifie les médias déposés dans media/ : cadence, définition, HDR/SDR, pistes audio et langue.
# Usage : tools/probe_sources.sh [dossier_media]   -> écrit reports/sources_report.csv
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
media="${1:-$root/media}"
mkdir -p "$root/reports"
out="$root/reports/sources_report.csv"
echo "fichier,duree_s,largeur,hauteur,fps,codec_video,transfert,primaires,plage,codec_audio,hz,canaux,langues_audio,alertes" > "$out"
find "$media" -type f \( -iname '*.mp4' -o -iname '*.mov' -o -iname '*.mkv' -o -iname '*.webm' -o -iname '*.wav' -o -iname '*.mp3' -o -iname '*.m4a' \) -print0 | sort -z |
while IFS= read -r -d '' f; do
  v() { ffprobe -v error -select_streams v:0 -show_entries "stream=$1" -of csv=p=0 -- "$f" 2>/dev/null | head -1; }
  a() { ffprobe -v error -select_streams a:0 -show_entries "stream=$1" -of csv=p=0 -- "$f" 2>/dev/null | head -1; }
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 -- "$f" | cut -c1-8)
  w=$(v width); h=$(v height); fr=$(v r_frame_rate); vc=$(v codec_name)
  trc=$(v color_transfer); pri=$(v color_primaries); rng=$(v color_range)
  ac=$(a codec_name); hz=$(a sample_rate); ch=$(a channels)
  langs=$(ffprobe -v error -select_streams a -show_entries stream_tags=language -of csv=p=0 -- "$f" | paste -sd'|' -)
  fps=""; [ -n "$fr" ] && fps=$(awk -F/ '{printf "%.3f", $1/($2?$2:1)}' <<<"$fr")
  al=""
  case "$trc" in smpte2084|arib-std-b67) al+="HDR: convertir en Rec.709; ";; esac
  [ -n "$h" ] && [ "$h" -lt 1080 ] && al+="definition < 1080p (upscale visible en 9:16); "
  [ -n "$fps" ] && case "$fps" in 23.976|24.000) ;; *) al+="cadence $fps a conformer en 23.976; ";; esac
  [ -n "$hz" ] && [ "$hz" != "48000" ] && al+="audio $hz Hz a reechantillonner en 48 kHz; "
  [ -z "$ac" ] && [ -n "$vc" ] && al+="pas de piste audio; "
  [ -n "$langs" ] && ! grep -qiE 'eng|und' <<<"$langs" && al+="langue audio non anglaise ($langs): verifier la VO; "
  echo "\"${f#$root/}\",$dur,$w,$h,$fps,$vc,$trc,$pri,$rng,$ac,$hz,$ch,$langs,\"$al\"" >> "$out"
done
column -s, -t "$out" 2>/dev/null || cat "$out"
echo "Rapport : $out  (la langue réelle se confirme à l'écoute : les fichiers YouTube n'ont souvent pas d'étiquette)"
