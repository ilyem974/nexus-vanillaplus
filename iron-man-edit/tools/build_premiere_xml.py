#!/usr/bin/env python3
"""Génère un XML Final Cut Pro 7 (importable dans Premiere : Fichier > Importer) à partir de
cutlist.csv et sources.csv : séquence 1080x1920 à 23,976 i/s, un clip par ligne du découpage.

Ne traite que les lignes dont la source a un fichier présent et un src_in renseigné dans
cutlist (colonne facultative `src_in_s`) ; les autres deviennent des trous à combler.
Vitesses, inversion, recadrages et effets restent à poser dans Premiere / After Effects.
Usage : python3 tools/build_premiere_xml.py [--out project/iron_man_edit_assembly.xml]
"""
import argparse, csv, pathlib, sys
from xml.sax.saxutils import escape

ROOT = pathlib.Path(__file__).resolve().parent.parent
TB = 24  # base de temps 24 + NTSC = 23,976 i/s

def frames(sec):
    return round(float(sec) * 24000 / 1001)

def rate():
    return f"<rate><timebase>{TB}</timebase><ntsc>TRUE</ntsc></rate>"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "project" / "iron_man_edit_assembly.xml"))
    args = ap.parse_args()
    src = {r["repere"]: r for r in csv.DictReader(open(ROOT / "sources.csv", encoding="utf-8"))}
    items, skipped, seen = [], [], set()
    for r in csv.DictReader(open(ROOT / "cutlist.csv", encoding="utf-8")):
        key = r["source"].split()[0]
        s = src.get(key)
        path = ROOT / s["dossier"] / s["fichier_attendu"] if s else None
        src_in = (r.get("src_in_s") or "").strip()
        if not s or not path.exists() or not src_in:
            skipped.append((r["id"], r["source"], "fichier absent" if not (path and path.exists()) else "src_in_s vide"))
            continue
        a, b = frames(r["tl_in_s"]), frames(r["tl_out_s"])
        i = frames(src_in)
        fid = f"file-{key}"
        if fid in seen:
            f = f'<file id="{fid}"/>'
        else:
            seen.add(fid)
            f = (f'<file id="{fid}"><name>{escape(path.name)}</name>'
                 f'<pathurl>{escape(path.as_uri())}</pathurl>{rate()}'
                 f'<media><video/><audio/></media></file>')
        items.append(f'<clipitem id="clip-{r["id"]}"><name>{escape(r["id"] + " " + r["plan_recherche"][:60])}</name>'
                     f'{rate()}<start>{a}</start><end>{b}</end><in>{i}</in><out>{i + b - a}</out>{f}</clipitem>')
    total = frames(35)
    xml = (f'<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n<xmeml version="4"><sequence id="IRON_MAN_EDIT">'
           f'<name>IRON_MAN_EDIT_assembly</name><duration>{total}</duration>{rate()}<media><video><format>'
           f'<samplecharacteristics>{rate()}<width>1080</width><height>1920</height>'
           f'<pixelaspectratio>square</pixelaspectratio></samplecharacteristics></format>'
           f'<track>{"".join(items)}</track></video><audio><track/></audio></media></sequence></xmeml>\n')
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(xml, encoding="utf-8")
    print(f"{len(items)} clip(s) écrits dans {out}")
    for s_ in skipped:
        print("  ignoré :", *s_, file=sys.stderr)

if __name__ == "__main__":
    main()
