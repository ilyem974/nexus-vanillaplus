# Musique de l'édit (publication TikTok)

Recherche du 12 novembre 2026. Je n'ai écouté aucun morceau : les tempos viennent de bases de données et les repères dans les morceaux sont à caler à l'écoute, sur les fichiers réels.

## Choix retenu : deux morceaux

| Partie | Morceau | Pourquoi |
|---|---|---|
| Héroïque (3 → 9 s) | **AC/DC — « Back in Black »** (album *Back in Black*, 1980) | C'est le morceau d'Iron Man (2008), et l'édit s'ouvre sur ce film. Le riff d'intro se reconnaît en deux secondes. C'est aussi un son très utilisé sur TikTok (≈ 3,9 millions de vidéos d'après un site de suivi) |
| Triste (19 → 38,5 s) | **Alan Silvestri — « The Real Hero »** (bande originale d'*Avengers: Endgame*) | C'est la musique du film sur la mort et les funérailles de Tony |

Variante pour la partie héroïque : **« Shoot to Thrill »** (Iron Man 2), plus rapide et plus nerveuse. Je garde « Back in Black » par défaut ; le changement ne touche que la piste musique et la grille de coupes.

### Tempos et grille de coupes

| Morceau | Tempo relevé | Durée d'un temps | En images (23,976 i/s) |
|---|---|---|---|
| Back in Black (studio) | 93,6 BPM | 0,64 s | ≈ 15,4 |
| Shoot to Thrill (studio) | ≈ 143 BPM | 0,42 s | ≈ 10 |
| Highway to Hell (studio) | ≈ 116 BPM | 0,52 s | ≈ 12,4 |

Avec « Back in Black », les coupes héroïques tombent sur les temps (0,64 s) et les demi-temps (0,32 s). Le découpage actuel (plans de 0,5 à 0,8 s) sera recalé sur cette grille une fois le tempo mesuré sur le fichier ; chaque coupe bougera de moins de 0,3 s. Le gel doit tomber sur un premier temps de mesure.

Entrée de la musique : le premier accord du riff sur la coupe à 3,0 s, juste après « I am Iron Man ». Si l'intro du morceau contient bien un décompte de guitare étouffée (souvenir à vérifier à l'écoute), ses deux derniers coups passent sous la fin de la réplique.

### Point technique sur la partie triste

Les extraits de la mort et des funérailles contiennent déjà la musique du film, mélangée aux voix. Poser une deuxième musique par-dessus créerait un doublon désynchronisé. Méthode prévue :

1. **Répliques de Peter et de Pepper** : isoler la voix avec l'outil « Remove Music » d'Adobe Podcast (Premiere n'a pas de séparation voix/musique intégrée). Résultat imparfait possible : garder l'original très bas en dessous si la voix sonne artificielle.
2. **Plans sans dialogue** (chute, réacteur, funérailles, lac) : son de l'extrait coupé.
3. **« The Real Hero » en continu** dessous, depuis un fichier propre, de 19 s à la fin.

Même traitement si la réplique d'Endgame (« And I… am… Iron Man ») a de la musique dessous.

### Où prendre les fichiers

Acheter les deux titres en téléchargement (boutique de musique en ligne) pour avoir un son propre. À déposer dans `media/music/` sous les noms `M1_hero.wav` et `M2_sad.wav`.

## Ce qu'il faut savoir pour TikTok

- **Une seule musique de la bibliothèque TikTok par vidéo, et pas de calage précis.** Un édit avec deux morceaux et des dialogues de film se publie donc avec le son déjà monté dans la vidéo (« son original »).
- **C'est le chemin risqué.** La détection automatique de TikTok reconnaît les morceaux commerciaux intégrés au fichier ; la vidéo peut être coupée du son, parfois seulement dans certains pays. Accélérer ou déformer le morceau n'est pas une parade fiable. Beaucoup d'édits de films passent, d'autres non : je ne peux pas le garantir.
- **Avant de publier** : activer la vérification des droits d'auteur dans les réglages de publication. TikTok signale alors un problème de musique avant la mise en ligne.
- **Si la vidéo est coupée du son** : « Modifier la vidéo → Changer le son » permet de remplacer la piste sans supprimer la publication, mais on perd alors le calage des coupes.
- **Compte professionnel** : la bibliothèque générale lui est interdite ; seule la bibliothèque commerciale est utilisable. Un compte personnel est plus adapté à cet édit.

Ces règles viennent de guides tiers, pas de l'aide officielle de TikTok.

## Plan B : musique créée, sans risque de droits

Je ne peux pas produire moi-même une musique de qualité depuis cette session. L'outil adapté est dans ton abonnement : **Adobe Firefly, générateur de musique** (« Generate Soundtrack »).

- Instrumental uniquement, libre de droits, utilisable commercialement d'après Adobe.
- On lui donne la vidéo ou une description ; il propose quatre variantes, jusqu'à cinq minutes, export en WAV.
- Il ne reproduit pas un artiste : le résultat sera « du hard rock », pas AC/DC.

Descriptions à lui donner (en anglais, c'est sa langue de travail) :

| Partie | Description | Réglages |
|---|---|---|
| Héroïque | `Driving classic hard rock instrumental, crunchy overdriven electric guitar riff, punchy live drums and bass, mid-tempo swagger, confident and energetic, no vocals` | 94 BPM, 15 s |
| Triste | `Slow emotional cinematic instrumental, solo piano with soft warm strings, sparse and intimate, gradually swelling, bittersweet farewell, no vocals` | 65 BPM, 30 s |

Le tempo de 94 BPM est volontaire : c'est celui de « Back in Black », donc les coupes restent calées si on échange les musiques.

## Livraison prévue

Deux exports du même montage, seules les pistes musique changent :

1. `iron_man_edit_v1_film.mp4` : AC/DC et Silvestri.
2. `iron_man_edit_v1_safe.mp4` : musiques Firefly, à publier si la première version est coupée du son.

## Sources

[AC/DC dans Iron Man 2 (Wikipédia)](https://www.wikipedia.org/wiki/AC/DC:_Iron_Man_2) · [Shoot to Thrill (Wikipédia)](https://en.wikipedia.org/wiki/Shoot_to_Thrill) · [tempo de Back in Black](https://cs.uwaterloo.ca/~dtompkin/music/track/ACDC_____LV1/ACDC_____LV1-03.html) · [tempo de Shoot to Thrill](https://acousticbrainz.org/3931e32f-debc-423a-8e1e-91d058f7dd1f) · [tempo de Highway to Hell](https://www.hooktheory.com/theorytab/view/ac-dc/highway-to-hell) · [Back in Black sur TikTok (tokchart)](https://tokchart.com/sounds/acdc-back-in-black_6715195986316101634) · [« The Real Hero » dans le film (TV Tropes)](https://tvtropes.org/pmwiki/pmwiki.php/AwesomeMusic/AvengersEndgame) · [morceaux clés d'Endgame](https://www.moviemarker.co.uk/avengers-endgame-6-key-tracks-from-the-films-staggering-soundtrack/) · [instrumentation de la bande originale](https://soundtrackworld.com/2019/05/avengers-endgame-alan-silvestri/) · [musique protégée sur TikTok](https://www.soundstripe.com/blogs/how-to-use-copyrighted-music-on-tiktok) · [éviter la coupure du son sur TikTok](https://mubert.com/blog/how-to-add-music-to-tiktok-videos-without-getting-muted-2026-guide) · [règles TikTok 2026](https://www.soundstripe.com/blogs/tiktok-copyright) · [comptes professionnels et bibliothèque commerciale](https://www.foximusic.com/blog/commercial-music-licensing-tiktok-guide/) · [générateur de musique Firefly (Adobe)](https://www.adobe.com/products/firefly/features/ai-music-generator.html) · [lancement des outils audio Firefly](https://routenote.com/radar/adobe-firefly-launches-ai-music-voiceover-and-sound-effects-generators/) · [séparer voix et musique (forum Adobe)](https://community.adobe.com/questions-729/the-spoken-dialogue-in-my-video-needs-to-be-better-distinguished-from-background-noise-and-music-on-the-same-track-1557813) · [limites d'Adobe Podcast](https://gauravtiwari.org/adobe-podcast-review/)
