# Édit Iron Man « I am Iron Man » ×2 — dossier de préparation

État : **préparation terminée pour tout ce qui ne dépend ni des médias ni d'Adobe**. Le montage n'a pas commencé ; il attend le message « Je suis sur mon PC, tu peux commencer ».

## 1. Ce qui a été vérifié dans cette session

| Point | Résultat |
|---|---|
| Outils Adobe connectés (Premiere, After Effects, Audition, Media Encoder) | **Aucun.** Aucun connecteur n'est installé sur le compte. Un connecteur « Adobe » existe dans l'annuaire claude.ai mais n'est pas connecté ; ses fonctions réelles (pilotage de Premiere ou non) restent à vérifier une fois connecté. |
| Accès à ton PC | **Aucun dossier partagé** via Remote Control pour l'instant. |
| Clips A à F | **Non visionnés.** Aucun fichier vidéo n'est présent dans la session et YouTube est bloqué par le réseau de l'environnement. Le brief contient les intitulés des vidéos, pas leurs URL. |
| VO anglaise | **Non vérifiée** (pas de fichier à écouter). Le contrôle automatique est prêt : `tools/probe_sources.sh`. |
| Musiques Adobe Stock | **Non écoutées** (stock.adobe.com bloqué, pas de compte accessible). Critères de recherche en §6 ; aucune référence de morceau n'est donc arrêtée. |
| Timecodes source | **À relever** sur les fichiers réels : colonnes `src_in`/`src_out` de `sources.csv` et `src_in_s` de `cutlist.csv` laissées vides volontairement. |

Les répliques des sous-titres sont écrites de mémoire des films et leurs timings sont des repères : à recaler à l'écoute.

## 2. Ce qu'il faut de ton côté avant le montage

1. Déposer les fichiers dans `media/` avec les noms de `sources.csv` (1080p minimum, piste audio anglaise).
2. Partager le dossier de travail depuis ton PC : app Claude Desktop → Réglages → Claude Code → Remote Control.
3. Connecter le connecteur Adobe sur claude.ai si tu veux un pilotage direct des applications.
4. Premiere Pro et After Effects dans la **même version majeure** si Dynamic Link est utilisé.

Si aucun pilotage de Premiere n'est possible, le chemin de repli est prêt : `tools/build_premiere_xml.py` produit un XML Final Cut Pro 7 que Premiere importe (Fichier → Importer) en séquence 1080 × 1920 avec les clips placés. Le script est testé sur médias synthétiques (structure XML valide) mais **pas encore importé dans Premiere**.

## 3. Contenu du dossier

| Fichier | Rôle |
|---|---|
| `sources.csv` | Journal des sources : origine, contenu recherché, timecodes, statut |
| `cutlist.csv` | Découpage plan par plan (22 lignes, 0 → 35 s, continuité vérifiée) |
| `subtitles/iron_man_edit_EN.srt` | Sous-titres anglais provisoires |
| `tools/probe_sources.sh` | Contrôle cadence, définition, HDR, audio 48 kHz, langue → `reports/sources_report.csv` |
| `tools/build_premiere_xml.py` | Génère la séquence d'assemblage importable dans Premiere |
| `media/`, `project/`, `export/` | Arborescence de travail (contenu exclu de git) |

## 4. Réglages de projet

- Séquence : 1080 × 1920, pixels carrés, **23,976 i/s** (cadence attendue des sources film ; à confirmer par le rapport de sonde, sinon conformer).
- Espace de travail : Rec.709 SDR. Toute source HDR (PQ/HLG) est convertie en Rec.709 dès l'import (Interpréter le métrage / tone mapping automatique), avant étalonnage.
- Audio : 48 kHz stéréo. Pistes : A1 Dialogues · A2 Ambiances · A3 FX (mécaniques, whoosh, snap, rewind) · A4 Musique héroïque · A5 Musique triste.
- Vidéo : V1 plans · V2 calques d'effet (flash, grain VHS) · V3 calque d'étalonnage par partie · piste de légendes.
- Recadrage : source 1080p → 178 % pour remplir la hauteur ; 200-230 % sur les visages ; position clé par clé dans `cutlist.csv`.

## 5. Découpage et raccord

Le détail est dans `cutlist.csv`. Structure :

| Temps | Contenu |
|---|---|
| 0–3 s | A : regard puis « I am Iron Man », musique sur la dernière syllabe |
| 3–10 s | 10 plans héroïques de 0,5 à 1 s (B, C) |
| 10–10,5 s | Gel sur le plan le plus fort, coupe sèche de la musique |
| 10,5–12 s | Séquence imbriquée `HERO_NEST` (0–10 s) inversée et accélérée |
| 12–13,2 s | A à l'identique (même in, mêmes attributs, même sous-titre) |
| 13,2–19 s | D : « And I… am… Iron Man » |
| 19–21 s | Claquement, flash, désintégration |
| 21–31 s | E : Tony blessé, Peter, Pepper |
| 31–35 s | Dernier plan tenu, fondu au noir |

Raccord A → D (plan 14 → 15) :
1. Dupliquer le clip 01 pour le plan 14 (Coller les attributs) afin de garantir un cadrage identique.
2. Sur D, superposer à 50 % d'opacité et régler échelle/position jusqu'à faire coïncider les deux pupilles avec celles de A.
3. Coupe franche. Tester l'audio de D en avance de 2, 3 puis 4 images ; garder la version où la respiration de Tony précède l'image sans mordre sur l'ambiance de la salle.
4. Option discrète : fondu luma de 2 images ou baisse de saturation qui démarre sur la coupe. Rien de plus visible.

Rembobinage : imbriquer 0–10 s, Vitesse/Durée −667 % (10 s → 1,5 s), interpolation « Échantillonnage d'images ». Si le résultat manque de lisibilité, passer la précomposition dans After Effects (remappage temporel avec paliers sur les plans 09, 07, 05, 04).

## 6. Musique, mixage, couleur

Recherche Adobe Stock Audio (à faire à l'écoute, avec la timeline) :
- **M1 héroïque** : *cinematic rock*, *hybrid trailer*, *electronic drums* ; 120-140 BPM ; attaque franche utilisable dès la première mesure ; 7 s utiles.
- **M2 triste** : *emotional piano*, *minimal strings*, *ambient orchestral* ; 60-75 BPM ; pas de mélodie dans 1-4 kHz pendant les répliques ; 15 s utiles avec une fin naturelle.
- Tonalités compatibles (même tonalité ou relative) pour que la reprise à 20,5 s ne heurte pas.

Niveaux cibles : dialogues −12 à −6 dBFS crête ; M1 −14 dB sous les voix, pleine en 3–10 s ; M2 −24 dB à l'entrée, ducking −8 dB sous les voix (Essential Sound → Atténuation automatique) ; intégré ≈ −14 LUFS, crête vraie −1 dBTP. Voix : passe-haut 80 Hz, réduction de bruit ≤ 20 %, pas de de-reverb agressif.

Quatre événements sonores : (1) fin de « Iron Man » → entrée de M1 sur la syllabe ; (2) 10,00 s → coupe sèche, traîne de reverb 0,3 s ; (3) 10,5–12 s → rewind + fragments inversés du mix ; (4) 19 s → snap +3 dB, sub-drop, 0,5 s de quasi-silence.

Couleur (Lumetri sur calques d'effet) : partie 1 contraste +15, saturation 110, teinte renforcée sur rouges et ors (HSL secondaire), netteté +20. Partie 2 contraste −10, saturation 85, hautes lumières adoucies, carnations protégées par masque HSL.

## 7. Sous-titres et export

- Police sans empattement (Montserrat SemiBold ou équivalent), 58-64 px, blanc, ombre portée 40 %, 2 lignes max.
- Zone : centre horizontal, bas du texte vers y ≈ 1400 (hors des 350 px du bas et de la colonne de droite occupés par les interfaces).
- Export : H.264 High, 1080 × 1920, 23,976 i/s, VBR 2 passes cible 20 Mb/s (max 25), Rec.709, AAC 320 kb/s stéréo 48 kHz → `export/iron_man_edit_v1.mp4`.
- Contrôle final : visionnage intégral, synchro, sous-titres, recadrages, raccord 14 → 15.

## 8. Remarque sur les sources

Les extraits appartiennent à Marvel/Disney. Je ne les ai pas téléchargés depuis YouTube : c'est à toi de fournir des fichiers que tu as le droit d'utiliser. Une publication de l'édit peut déclencher une revendication de droits sur les plateformes.
