# Ce qui peut aider Claude à travailler dans Adobe

Recherche du 11 novembre 2026. Rien de ce qui suit n'a été installé ni testé : les descriptions viennent des pages des projets, d'annuaires et d'articles. Les nombres d'outils annoncés sont ceux des auteurs.

## 1. Officiel : le plugin Adobe (« Adobe for creativity »)

Publié par Adobe, présent dans l'annuaire de ton compte Claude, non activé pour l'instant.

- **Ce qu'il fait** : plus de 50 outils Adobe exécutés dans le cloud sur des fichiers envoyés à Claude (Photoshop, Premiere, Lightroom, Express, Firefly, Stock…).
- **Utile pour l'édit** : recherche et licence de musiques Adobe Stock, nettoyage audio, polices Adobe Fonts, redimensionnement de vidéos, montage rapide (« quick cut »).
- **Limite** : d'après un test tiers, il ne pilote pas la timeline du Premiere installé sur le PC. Il ne produit donc pas le projet `.prproj` modifiable demandé par le brief. Adobe précise que le connecteur ne reprend pas toutes les fonctions des applications.
- **Accès** : une partie des outils marche sans compte ; le reste demande un compte Adobe, et certains un abonnement payant.

## 2. Non officiel : serveurs MCP qui pilotent Premiere sur le PC

Ce sont des projets communautaires. Ils installent un panneau dans Premiere et un petit serveur local ; Claude envoie alors des commandes à la timeline. **Ils ne fonctionnent qu'avec un Claude lancé sur le PC** (Claude Desktop ou Claude Code), pas depuis une session cloud comme celle-ci.

| Projet | Annoncé par l'auteur | Points d'attention |
|---|---|---|
| [hetpatel-11/Adobe_Premiere_Pro_MCP](https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP) | 283 outils : import, séquences, timeline, effets ; fourni avec un skill | Le plus documenté. Installation Windows par `npm run setup:win`, mais seule l'installation est testée sous Windows, pas le lien avec Premiere. Compatibilité Premiere 26 non confirmée |
| [antipaster/Adobe-Premiere-Pro-MCP](https://github.com/antipaster/adobe-premiere-pro-mcp) | 170+ outils : montage, effets, sous-titres, export | Non vérifié |
| [leancoderkavy/premiere-pro-mcp](https://github.com/leancoderkavy/premiere-pro-mcp) | Serveur local avec panneau CEP | Non vérifié |
| [zahediamrei/prmcp](https://github.com/zahediamrei/prmcp) | Serveur, panneau Premiere et skill | Non vérifié |
| [mikechambers/adb-mcp](https://docsearch.algolia.com/mcp/docs/repo/mikechambers/adb-mcp) | Passerelle vers des plugins UXP pour plusieurs applications Adobe | Demande l'outil développeur UXP d'Adobe |

## 3. Non officiel : serveurs MCP pour After Effects

| Projet | Annoncé par l'auteur |
|---|---|
| [a-y-ibrahim/after-effects-mcp](https://github.com/a-y-ibrahim/after-effects-mcp) | 47 outils : compositions, calques, animation, effets, rendu, exécution de scripts |
| [dha-aa/ae-motion](https://mcpservers.org/servers/dha-aa/ae-motion) | 77 outils : images clés, expressions, masques, rendu ; Windows et macOS |

## 4. Skills (modes d'emploi pour Claude)

| Skill | Contenu | Remarque |
|---|---|---|
| Skill fourni avec le serveur hetpatel-11 | Installer, vérifier et utiliser le serveur Premiere | Va avec le serveur du §2 |
| [sfkislev/flue « Premiere »](https://www.skills.sh/sfkislev/flue/premiere) | Pilotage de Premiere par une passerelle locale (Flue) | Flue s'installe à part |
| [aedev-tools/adobe-agent-skills](https://skills.sh/aedev-tools/aedev-skills/after-effects-assistant) | Génère et lance des scripts After Effects | Lance les scripts par `osascript`, une commande macOS : a priori inutilisable sur Windows |
| major-ai-skills « adobe-premiere-pro » | Exemples de scripts, échange EDL/XML, rendu par lots | Aide-mémoire, ne pilote rien |

## 5. Sans rien installer

- **Premiere** : import de la séquence XML générée par `tools/build_premiere_xml.py` (déjà prêt).
- **After Effects** : exécution d'un script `.jsx` par Fichier → Scripts → Exécuter le fichier de script. Je peux écrire ce script pour le rembobinage et le raccord.

## 6. Recommandation

1. **Activer le plugin Adobe officiel** : sans risque, utile pour la musique Stock et le nettoyage audio.
2. **Pour un vrai pilotage de Premiere** : essayer le serveur hetpatel-11 avec Claude Desktop sur le PC. C'est du code tiers qui prend la main sur Premiere : lire le dépôt avant d'installer et tester sur un projet vide.
3. **Si le serveur ne marche pas avec Premiere 26** : repli sur le XML et les scripts du §5, qui ne dépendent de personne.

## Sources

[Annonce Adobe du connecteur](https://blog.adobe.com/en/publish/2026/04/28/adobe-for-creativity-connector) · [page Adobe for Claude](https://www.adobe.com/adobe-connectors/adobe-for-claude.html) · [fonctionnement du connecteur](https://weandthecolor.com/how-does-the-adobe-for-creativity-connector-work-in-claude/210357) · [test tiers : Claude dans Premiere](https://www.premierecopilot.com/en/blog/how-to-use-claude-ai-in-premiere-pro) · [Claude dans Resolve et Premiere](https://blackhateditors.com/blog/en/claude-davinci-resolve-premiere-pro/) · [README hetpatel-11](https://cdn.jsdelivr.net/gh/hetpatel-11/adobe_premiere_pro_mcp@main/README.md) · [skill du serveur hetpatel-11](https://skillselion.com/skills/hetpatel-11/adobe_premiere_pro_mcp/premiere-pro-mcp) · [serveurs After Effects](https://glama.ai/mcp/servers/a-y-ibrahim/after-effects-mcp) · [skills Adobe communautaires](https://cdn.jsdelivr.net/gh/aedev-tools/adobe-agent-skills@main/README.md)
