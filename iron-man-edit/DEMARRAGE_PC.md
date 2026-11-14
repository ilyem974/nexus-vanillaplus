# Démarrage du montage sur le PC

Ce fichier sert de passation à une session Claude **lancée sur le PC** (Claude Desktop ou Claude Code en local). La session cloud qui a préparé ce dossier n'a jamais eu accès au PC, aux médias ni à Adobe : rien de ce qui suit n'a été exécuté.

## Consigne à donner à la session locale

> Lis `iron-man-edit/DEMARRAGE_PC.md`, puis `PREP.md`, `cutlist.csv`, `MUSIQUE.md` et `sources.csv`. Vérifie les outils Adobe disponibles, puis réalise le montage jusqu'à l'export final.

## État au 13 novembre 2026

| Élément | État |
|---|---|
| Découpage (`cutlist.csv`) | Prêt : 24 plans, 38,5 s. Colonne `src_in_s` vide, à remplir en visionnant les fichiers |
| Sous-titres (`subtitles/iron_man_edit_EN.srt`) | Brouillon : répliques de mémoire, timings à recaler à l'écoute |
| Clips A à F | **Absents** de `media/` |
| Musiques M1, M2 | **Absentes** de `media/music/` |
| Outils Adobe pilotables | **Aucun vérifié** |

## Ordre de travail

1. **Inventaire** : lister `media/`. Signaler précisément chaque fichier manquant par rapport à `sources.csv`, et continuer avec ce qui est présent.
2. **Contrôle des sources** : `bash tools/probe_sources.sh` (demande ffmpeg et un shell bash, par exemple Git Bash). Corriger les alertes : cadence, HDR, audio 48 kHz, langue.
3. **VO anglaise** : écouter chaque réplique, corriger le `.srt`.
4. **Timecodes** : relever les points d'entrée et de sortie de chaque plan, remplir `src_in_s` dans `cutlist.csv` et `src_in`/`src_out` dans `sources.csv`.
5. **Tempo** : mesurer le tempo réel de `M1_hero.wav`, recaler les coupes héroïques sur les temps (voir `MUSIQUE.md`).
6. **Outils Adobe** : vérifier dans cet ordre ce qui marche réellement sur cette machine.
   - Versions installées de Premiere, After Effects, Audition, Media Encoder. Premiere et After Effects doivent avoir la même version majeure.
   - Un serveur MCP Premiere ou After Effects est-il installé ? (voir `OUTILS_PILOTAGE_ADOBE.md`)
   - After Effects en ligne de commande : `AfterFX.exe -r chemin\script.jsx` pour exécuter un script, `aerender.exe` pour rendre une composition. À vérifier sur la version installée avant de s'appuyer dessus.
   - Premiere : import de la séquence produite par `python tools/build_premiere_xml.py` (Fichier → Importer). Jamais testé dans Premiere.
7. **Montage** selon `PREP.md` : timeline, recadrages, raccord A → D, rembobinage par séquence imbriquée inversée, étalonnage, sous-titres.
8. **Son** : isoler les voix de Peter et Pepper (Adobe Podcast « Remove Music »), poser les musiques, mixage et niveaux de `PREP.md` §6.
9. **Exports** : `export/iron_man_edit_v1_film.mp4` (AC/DC et Silvestri) et `export/iron_man_edit_v1_safe.mp4` (musiques Firefly). H.264, 1080 × 1920, 23,976 i/s, ≈ 20 Mb/s, AAC 48 kHz.
10. **Contrôle** : visionner chaque export en entier. Synchro, voix, sous-titres, recadrages, raccord entre les deux films.
11. **Livraison** : MP4, projet Adobe dans `project/` avec la liste de ses dépendances, liste des extraits et musiques avec leurs timecodes.

## Règles

- Ne pas commiter de média : `media/`, `project/` et `export/` sont exclus de git.
- Ne pas inventer de timecode ni de référence de morceau : tout se relève sur les fichiers réels.
- Signaler tout blocage matériel avec le nom exact du fichier ou de l'outil concerné.
