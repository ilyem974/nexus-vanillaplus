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
| `cutlist.csv` | Découpage plan par plan (24 lignes, 0 → 38,5 s, continuité vérifiée) |
| `subtitles/iron_man_edit_EN.srt` | Sous-titres anglais provisoires |
| `MUSIQUE.md` | Morceaux retenus, publication TikTok, plan B |
| `RESSOURCES.md` | Logiciels, liens des clips, banques de sons |
| `OUTILS_PILOTAGE_ADOBE.md` | Outils pour piloter Adobe depuis Claude |
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
| 3–9 s | 10 plans héroïques de 0,5 à 0,8 s (B, C) |
| 9–9,5 s | Gel sur le plan le plus fort, coupe sèche de la musique |
| 9,5–11 s | Séquence imbriquée `HERO_NEST` (0–9 s) inversée et accélérée |
| 11–12,2 s | A à l'identique (même in, mêmes attributs, même sous-titre) |
| 12,2–17,7 s | D : « And I… am… Iron Man » |
| 17,7–19,2 s | Claquement, flash, désintégration |
| 19,2–21,7 s | E : Tony titube et s'écroule |
| 21,7–29,7 s | E : Peter, Pepper, le réacteur qui s'éteint |
| 29,7–35,2 s | F : Pepper et Morgan au ponton, puis tous les proches réunis |
| 35,2–38,5 s | F : le réacteur sur le lac, plan tenu, fondu au noir |

Durée totale : **38,5 s** (version du 11 novembre 2026 ; la première version faisait 35 s et finissait sur Tony). La partie triste commence à 19,2 s et occupe la moitié de l'édit.

Raccord A → D (plan 14 → 15) :
1. Dupliquer le clip 01 pour le plan 14 (Coller les attributs) afin de garantir un cadrage identique.
2. Sur D, superposer à 50 % d'opacité et régler échelle/position jusqu'à faire coïncider les deux pupilles avec celles de A.
3. Coupe franche. Tester l'audio de D en avance de 2, 3 puis 4 images ; garder la version où la respiration de Tony précède l'image sans mordre sur l'ambiance de la salle.
4. Option discrète : fondu luma de 2 images ou baisse de saturation qui démarre sur la coupe. Rien de plus visible.

Rembobinage : imbriquer 0–9 s, Vitesse/Durée −600 % (9 s → 1,5 s), interpolation « Échantillonnage d'images ». Si le résultat manque de lisibilité, passer la précomposition dans After Effects (remappage temporel avec paliers sur les plans 09, 07, 05, 04).

## 6. Musique, mixage, couleur

**Choix du 12 novembre 2026 : AC/DC « Back in Black » puis Alan Silvestri « The Real Hero », avec un plan B généré dans Adobe Firefly. Détail, risques TikTok et méthode dans `MUSIQUE.md`.** Les critères ci-dessous restent valables pour le plan B.

Recherche Adobe Stock Audio (à faire à l'écoute, avec la timeline) :
- **M1 héroïque** : *cinematic rock*, *hybrid trailer*, *electronic drums* ; 120-140 BPM ; attaque franche utilisable dès la première mesure ; 6 s utiles.
- **M2 triste** : *emotional piano*, *minimal strings*, *ambient orchestral* ; 60-75 BPM ; pas de mélodie dans 1-4 kHz pendant les répliques ; 20 s utiles avec une montée vers 30 s (funérailles) et une fin naturelle.
- Tonalités compatibles (même tonalité ou relative) pour que la reprise à 19 s ne heurte pas.

Niveaux cibles : dialogues −12 à −6 dBFS crête ; M1 −14 dB sous les voix, pleine en 3–10 s ; M2 −24 dB à l'entrée, ducking −8 dB sous les voix (Essential Sound → Atténuation automatique) ; intégré ≈ −14 LUFS, crête vraie −1 dBTP. Voix : passe-haut 80 Hz, réduction de bruit ≤ 20 %, pas de de-reverb agressif.

Quatre événements sonores : (1) fin de « Iron Man » → entrée de M1 sur la syllabe ; (2) 9,00 s → coupe sèche, traîne de reverb 0,3 s ; (3) 9,5–11 s → rewind + fragments inversés du mix ; (4) 17,7 s → snap +3 dB, sub-drop, 0,5 s de quasi-silence.

Couleur (Lumetri sur calques d'effet) : partie 1 contraste +15, saturation 110, teinte renforcée sur rouges et ors (HSL secondaire), netteté +20. Partie 2 contraste −10, saturation 85, hautes lumières adoucies, carnations protégées par masque HSL.

## 7. Sous-titres et export

- Police sans empattement (Montserrat SemiBold ou équivalent), 58-64 px, blanc, ombre portée 40 %, 2 lignes max.
- Zone : centre horizontal, bas du texte vers y ≈ 1400 (hors des 350 px du bas et de la colonne de droite occupés par les interfaces).
- Export : H.264 High, 1080 × 1920, 23,976 i/s, VBR 2 passes cible 20 Mb/s (max 25), Rec.709, AAC 320 kb/s stéréo 48 kHz → `export/iron_man_edit_v1.mp4`.
- Contrôle final : visionnage intégral, synchro, sous-titres, recadrages, raccord 14 → 15.

## 8. Remarque sur les sources

Les extraits appartiennent à Marvel/Disney. Je ne les ai pas téléchargés depuis YouTube : c'est à toi de fournir des fichiers que tu as le droit d'utiliser. Une publication de l'édit peut déclencher une revendication de droits sur les plateformes.
