# Édit Iron Man — liste de tout ce qu'il faut

Recherches web du 11 novembre 2026. Les prix viennent de sites tiers, pas des pages officielles : à confirmer au moment de payer. Les liens YouTube sortent des résultats de recherche ; **je n'ai visionné aucune vidéo** (YouTube est bloqué depuis ma session), donc qualité, cadence et langue restent à vérifier.

## 1. Logiciels de montage : trois chemins possibles

| Chemin | Logiciels | Coût relevé | Pour qui |
|---|---|---|---|
| **A. Adobe (celui du brief)** | Premiere + After Effects + Audition + Media Encoder | Creative Cloud Pro ≈ 78,65 € TTC/mois (engagement annuel). Premiere seul ≈ 26,21 €/mois. Étudiant ≈ 19,50 €/mois la 1re année puis ≈ 40,32 € | Contrôle le plus fin, projet `.prproj` modifiable |
| **B. CapCut Desktop** | CapCut seul | Gratuit (export 1080p). Pro ≈ 19,99 $/mois ou 179,99 $/an | Le plus rapide pour un édit vertical court |
| **C. DaVinci Resolve** | Resolve seul | Gratuit (export jusqu'en 4K 60 i/s). Studio ≈ 295 $ en achat unique | Gratuit, étalonnage excellent |

Notes utiles :

- **Adobe** : After Effects, Audition et Media Encoder ne sont pas dans l'abonnement « Premiere seul ». Pour le brief complet il faut Creative Cloud Pro. Media Encoder s'installe avec Premiere.
- **Dynamic Link** : Premiere et After Effects doivent avoir le **même numéro de version majeure**, sinon le lien ne fonctionne pas. Des utilisateurs signalent des liens cassés en version 26.x ; mettre les deux applications à jour ensemble.
- **CapCut gratuit** : pas de filigrane sur un export normal, mais l'utilisation d'un effet ou d'un modèle marqué « Pro » en ajoute un. Supprimer aussi le clip de fin CapCut ajouté par défaut. Courbes de vitesse, images clés et sous-titres automatiques sont présents ; la lecture inversée sur ordinateur n'est pas confirmée par mes sources, à tester avant de choisir ce chemin pour le rembobinage.
- **Resolve gratuit** : mes sources ne parlent pas du 1080 × 1920 en particulier, mais ce format est sous le plafond d'export.

## 2. Configuration du PC (Premiere 26)

| Élément | Minimum Adobe | Conseillé pour cet édit |
|---|---|---|
| Système | Windows 11 version 24H2 | idem |
| Mémoire | 8 Go | 16 Go (HD), 32 Go si sources 4K |
| Carte graphique | 4 Go de mémoire vidéo ; NVIDIA de 2014 ou plus récente | 8 Go |
| Disque | SSD | SSD avec ≈ 20 Go libres (sources, cache, exports) |

CapCut : Windows 10 ou plus (64 bits), 8 Go de mémoire conseillés.

## 3. Clips à récupérer

Les chaînes citées dans le brief (TopMovieClips, JoBlo, Entertainment Access, Filmey Box) et la compilation officielle Marvel **n'ont pas été retrouvées** par la recherche. Voici des candidats équivalents, tous des mises en ligne non officielles qui peuvent disparaître.

| Repère | Scène | Candidats |
|---|---|---|
| A | Conférence de presse, Iron Man (2008) | [1080p](https://www.youtube.com/watch?v=LUElUV51Epo) · [Full HD](https://www.youtube.com/watch?v=aNNdVZ-mVy4) · [4K](https://www.youtube.com/watch?v=W04PQ1NU36A) |
| B | Assemblages d'armures | [Tony Stark's Best Iron Man Suit Ups](https://www.youtube.com/watch?v=qaeHKoq_CLM) (peut-être officiel, à vérifier) · [All Suit Up Scenes 2008-2019, 1080p](https://www.youtube.com/watch?v=gyIC0zq1q50) |
| C | Premier vol, Mark II | [1080p](https://www.youtube.com/watch?v=PvYhZT99g1s) · [4K](https://www.youtube.com/watch?v=9KhRwuf5AEg) · [« Yeah, I can fly »](https://www.youtube.com/watch?v=PZlL5gZeGDI) |
| D | « I am Iron Man » et claquement, Endgame | [Snap Scene 4K](https://www.youtube.com/watch?v=om8rBseFo2o) · [« I am inevitable » / « And I am Iron Man »](https://www.youtube.com/watch?v=jk5X0t37HPI) · [Tony Stark Outsmarts Thanos](https://www.youtube.com/watch?v=gzwdOh7b9eg) |
| E | Mort de Tony | [Tony Stark death and final goodbye](https://www.youtube.com/watch?v=3qqLhM-7uW4) · [Pepper: « You can rest now »](https://www.youtube.com/watch?v=jb2WuQ6pYjQ) |
| F | Funérailles (optionnel) | [Funeral Scene](https://www.youtube.com/watch?v=sRwM0vIYwZc) · [Avengers: Endgame - Tony Stark's Funeral Scene](https://www.youtube.com/watch?v=oFzXBg6jkAY) |

Critères de choix d'un fichier :

- **1080p minimum** : le recadrage vertical agrandit l'image à 178 % ou plus.
- **Éviter les versions « 60 FPS »** : ce sont des images interpolées, elles se montent mal en 23,976 i/s.
- **Éviter les versions HDR** si une version SDR existe : moins de conversion de couleur.
- **Écarter les versions doublées** (une version hindi apparaît dans les résultats) : il faut la piste anglaise.
- Vérifier chaque fichier avec `tools/probe_sources.sh`.

Ces liens servent au repérage. Les conditions de YouTube n'autorisent pas le téléchargement hors de sa propre fonction, et les images appartiennent à Marvel/Disney : les fichiers à monter doivent venir d'une source que tu as le droit d'utiliser (tes propres copies des films, par exemple).

## 4. Musique et bruitages

| Source | Coût relevé | Remarque |
|---|---|---|
| **Adobe Stock Audio** (dans Premiere : panneau Essential Sound → Parcourir) | Écoute gratuite ; la licence demande des crédits ou un abonnement Stock, **non inclus** dans Creative Cloud | Plus de 30 000 morceaux, recherche par ambiance, genre, tempo, durée |
| **Pixabay** | Gratuit, sans crédit obligatoire | Musique et bruitages |
| **Mixkit** | Gratuit, sans inscription | Conditions à relire sur le site |
| **Bibliothèque audio YouTube** | Gratuit | Dans YouTube Studio |
| **Freesound** | Gratuit avec inscription | Licence différente pour chaque son |
| **Uppbeat** | Gratuit (3 téléchargements/mois) ; ≈ 5,59 à 13,99 $/mois | Le moins cher des payants |
| **Epidemic Sound** | ≈ 9,99 $/mois (annuel) | Catalogue le plus utilisé par les créateurs |
| **Artlist** | ≈ 9,99 $/mois (annuel) | Musique et bruitages |

À chercher :

- **Musique héroïque** : *cinematic rock*, *hybrid trailer*, *electronic drums*, 120-140 BPM, 7 s utiles.
- **Musique triste** : *emotional piano*, *minimal strings*, 60-75 BPM, 15 s utiles avec une fin naturelle.
- **Bruitages** : *tape rewind*, *whoosh*, *impact / hit*, *sub drop*, *finger snap*, *riser*.

## 5. Petits outils gratuits

| Outil | Usage |
|---|---|
| MediaInfo | Lire cadence, définition, HDR et langue d'un fichier |
| HandBrake ou Shutter Encoder | Convertir une source en MP4 H.264 à cadence constante avant import |
| VLC | Vérifier la piste audio et relever des timecodes |
| Google Fonts (Montserrat, Inter) | Police des sous-titres |
| ffmpeg | Requis par `tools/probe_sources.sh` |

## 6. Publication

- Format commun à TikTok, Reels et Shorts : 9:16, 1080 × 1920, MP4 H.264.
- Durées maximales relevées : Shorts 3 min, Reels 90 s à 3 min selon les sources, TikTok 10 min. L'édit de 35 s passe partout.
- Zones sûres : aucune plateforme ne publie de valeurs officielles. Garder textes et visages dans le centre, loin des ≈ 350 px du bas et de la colonne de droite.
- **Droits** : un édit de film sans autorisation reste une contrefaçon, même si les studios le tolèrent souvent. Sur YouTube, une revendication Content ID peut bloquer ou monétiser la vidéo sans sanctionner la chaîne ; un retrait pour atteinte aux droits, lui, compte comme avertissement. Sur TikTok, le son peut être coupé ou la vidéo retirée.

## 7. À faire avant de lancer le montage

1. Choisir le chemin A, B ou C.
2. Installer les logiciels et vérifier les versions (Premiere et After Effects identiques).
3. Déposer les six clips dans `media/` avec les noms de `sources.csv`.
4. Choisir deux musiques et les bruitages, les déposer dans `media/music` et `media/sfx`.
5. Installer la police des sous-titres.
6. Lancer `tools/probe_sources.sh` et corriger les alertes.

## Sources

Logiciels et prix : [exigences techniques Premiere (Adobe)](https://helpx.adobe.com/lv/premiere/desktop/get-started/technical-requirements/adobe-premiere-pro-technical-requirements.html) · [prix Adobe France 2026](https://francefg.fr/photoshop/adobe-creative-cloud-prix-2026-comparatif/) · [quel abonnement Adobe choisir](https://apprendrelavideo.fr/quel-abonnement-adobe-choisir/) · [tarif étudiant](https://www.conseils-photos.com/articles/adobe-creative-cloud-pro-etudiant-enseignant-licence-education-2026-prix-conditions) · [Dynamic Link (Adobe)](https://helpx.adobe.com/cn/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/share-assets-between-after-effects-and-premiere-using-dynamic-link.html) · [Dynamic Link en v26 (forum Adobe)](https://community.adobe.com/questions-729/dynamic-link-with-after-effects-breaks-after-upgrade-to-v26-1621961) · [prix CapCut](https://www.eesel.ai/blog/capcut-pricing) · [CapCut gratuit ou Pro](https://vidpros.com/capcut-pro-vs-free/) · [CapCut sur PC](https://capcut.com/resource/capcut-for-windows) · [fonctions CapCut](https://unifab.ai/resource/how-to-use-capcut) · [prix DaVinci Resolve](https://www.activepieces.com/blog/davinci-resolve-pricing-free-vs-studio-cost-2026) · [Resolve gratuit](https://costbench.com/software/video-editing/davinci-resolve/free-plan)

Audio : [Adobe Stock dans Premiere](https://helpx.adobe.com/stock/help/streamline-workflows-premiere-pro.html) · [licence Adobe Stock Audio](https://helpx.adobe.com/stock/how-to/find-stock-audio-clips.html) · [sites de bruitages gratuits](https://wyzowl.com/free-sound-effects-sites/) · [musique libre de droits](https://toolradar.com/guides/best-free-music-and-sound-effects-for-commercial-use) · [prix Uppbeat](https://checkthat.ai/brands/uppbeat/pricing) · [Epidemic Sound et Artlist](https://shortstack.tools/compare/artlist-vs-epidemic-sound/)

Publication et droits : [formats verticaux](https://blckalpaca.at/en/knowledge-base/social-media/social-media-content-creation-formats/instagram-reels-format-shorts-tiktok-specs) · [spécifications vidéo 2026](https://quso.ai/blog/social-media-video-specs) · [revendication ou avertissement YouTube](https://www.trademarkengine.com/blog/youtube-copyright-claims-vs-copyright-strikes-creators-need-to-know/) · [extraits de films sur TikTok](https://www.jeffbullas.com/thread/is-it-legal-to-post-movie-clips-on-tiktok/) · [droits d'auteur TikTok](https://www.soundstripe.com/blogs/tiktok-copyright) · [les studios et les fan edits](https://keyt.com/news/money-and-business/cnn-business-consumer/2026/03/15/gen-zs-fan-edits-are-a-staple-of-internet-culture-movie-studios-are-finally-buying-in/)
