# SyllabeColor
Programme en Python 3 permettant de découper un texte en syllabe puis de les colorer. Un fichier HTML est généré pour permettre l'impression. Cet outil peut être utilisé pour facilité la lecture aux personnes dyslexiques.

Certains paramètres peut être modifiés au début du code :
- Le titre de la page HTML généré
- Le séparateur utilisé (pas d'utilité particulière a le modifier sauf cas spécifique)
- Les 3 couleurs utilisée : deux pour différencier les syllabes et une autres pour les mots non pris en compte
- Le nombre de caractères minimal des mots a traité (si on choisit 4, "Rémi" ne sera pas analysé mais "école" si).


On peut retrouver dans le dossier "data" 4 fichiers textes :
- Excepti0n.txt : liste des exceptions française. Je vous invite à la compléter et a la partager.
- FinMot.txt : ce sont les caractères qui définissent la fin d'un mot / transition entre deux mots.
- GroupeSon.txt : liste des groupes de son qui ne doivent pas être séparé dans les mots (digramme, trigramme, ...).
- Voyelles.txt : liste des voyelles, sous toutes leurs formes
