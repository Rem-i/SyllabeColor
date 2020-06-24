#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# SyllabeColor.py
#  
# Auteur: Rémi Louche
# Date: Juin 2020
# Version : Python 3

# Règle pour séparer les syllabes :
# On sépare les syllabes entre deux consonnes sauf à la fin d’un mot.
# On sépare les syllabes entre une voyelle et une consonne.
# Lorsque trois consonnes se suivent et sont différentes, on sépare après la deuxième consonne.

# PARAMETRES
TitrePageHTML = "Texte traité par syllabes"     # Titre de la page HTML
séparateur = "%"                                # Séparateur utilisé
Couleur1 = "red"                                # Première couleur. La couleur doit être marqué en anglais parmis les noms de couleurs HTML
Couleur2 = "blue"                               # Deuxième couleur
Couleur3 = "black"                              # Couleur pour les mots que on as définit a ne pas traiter
NbrMinMotATraiter = 4                           # Nombre de caratère minimal des mots que on doit traiter. Si on met 4, "des" ne sera pas analysé

# Liste des voyelles
with open("data/Voyelles.txt", "r") as fichier:
    Voyelles = fichier.read()
    Voyelles = Voyelles.splitlines()

# Liste des caractères signifiant la fin d'un mot
with open("data/FinMot.txt", "r") as fichier:
    FinMot = fichier.read()
    FinMot = FinMot.splitlines()

# Liste des groupes de deux lettres qui forment un seul son
with open("data/GroupeSon.txt", "r") as fichier:
    GroupeSon = fichier.read()
    GroupeSon = GroupeSon.splitlines()

# Liste des exceptions
with open("data/Excepti0n.txt", "r") as fichier:
    Excepti0n = fichier.read()
    Excepti0n = Excepti0n.splitlines()

# Liste des exceptions
with open("Texte_De_Base.txt", "r") as fichier:
    Texte_De_Base = fichier.read()
    Texte_De_Base = Texte_De_Base.splitlines()



# Fonction pour trouver la place des syllabes dans un mots
def PlaceSyllabe(Mot):
    LongueurMot = len(Mot)
    PlaceSéparation = []

    for n in range(LongueurMot-1):

        DeuxLettres = Mot[n] + Mot[n+1]
        if DeuxLettres not in GroupeSon :

            if Mot[n] not in Voyelles and Mot[n+1] not in Voyelles and Mot[n+1] != len(Mot) :
                PlaceSéparation.append(n)

            if Mot[n] in Voyelles and Mot[n+1] not in Voyelles :
                PlaceSéparation.append(n)

            if n < LongueurMot-2 :
                if Mot[n] not in Voyelles and Mot[n+1] not in Voyelles and Mot[n+2] not in Voyelles:
                    PlaceSéparation.append(n+1)

    return(PlaceSéparation)



# Fonction pour sépare les syllabes dans un mots par le caractère séparateur
def SépareSyllabe(Mot,PlaceSyllabe,séparateur):

    MotSéparé = Mot
    for n in range(len(MotSéparé))[::-1]:
        if n-1 in PlaceSyllabe:
            MotSéparé = MotSéparé[:n] + séparateur + MotSéparé[n:]

    return(MotSéparé)



# Fonction pour découper le texte en mots et placer les séparateurs
def TexteEnMotsSyllabé(Texte,NbrMinMotATraiter,séparateur):
    temps = ""

    TexteAvecSéparateur = ""
    for n in range(len(Texte)):

        temps = temps + Texte[n]

        if Texte[n] in FinMot:

            if len(temps) <= NbrMinMotATraiter+1:
                TexteAvecSéparateur = TexteAvecSéparateur  + temps
                temps = ""

            else:
                # On isole le caractère qui a joué le rôle de séparateur
                SéparateurActuel = temps[len(temps)-1:len(temps)]

                # temps devient le mot donc on cherche a isoler les syllabes
                temps = temps[:len(temps)-1]

                # On vérifie si l'exeption se trouve dans la liste des exceptions
                if temps in Excepti0n :
                    PlaceListe = Excepti0n.index(temps)

                    # L'exception se trouve 1 plus loin dans la liste, après le mot trouvé
                    Excepti0nActuel = Excepti0n[PlaceListe+1]
                    Excepti0nActuel = Excepti0nActuel.replace("-",séparateur)

                    # On concate
                    TexteAvecSéparateur = TexteAvecSéparateur + Excepti0nActuel

                    temps = ""

                else :
                    # On concate tout dans le bonne ordre 
                    TexteAvecSéparateur = TexteAvecSéparateur + SépareSyllabe(temps,PlaceSyllabe(temps),séparateur)
                    temps = ""

                # On place le caractère qui a joué le rôle de séparateur à la fin
                TexteAvecSéparateur = TexteAvecSéparateur + SéparateurActuel

    return(TexteAvecSéparateur)



# Début de la page HTML
PageHTML = open("TexteTraité.html", "w")
PageHTML.write("<!DOCTYPE html><html><head><title>" + TitrePageHTML + "</title></head><body>")


for m in range(len(Texte_De_Base)):

    TexteAvecSéparateur = TexteEnMotsSyllabé(Texte_De_Base[m],NbrMinMotATraiter,séparateur)

    PageHTML.write("<p>")

    # On commence distribuer les couleurs aux différents syllabes
    CompteurCouleur = 1
    temps = ""
    for n in range(len(TexteAvecSéparateur)):

        temps = temps + TexteAvecSéparateur[n:n+1]
        if TexteAvecSéparateur[n] in FinMot or TexteAvecSéparateur[n] == séparateur:

            temps = temps.replace(séparateur,"")
            if len(temps)-1 <= NbrMinMotATraiter and TexteAvecSéparateur[n] != séparateur and TexteAvecSéparateur[n-len(temps)] != séparateur:
                PageHTML.write('<FONT color="' + Couleur3 + '">' + temps + "</FONT>")

            else:
                # temps = temps.replace(séparateur,"")

                if CompteurCouleur == 1 :
                    PageHTML.write('<FONT color="' + Couleur1 + '">' + temps + "</FONT>")
                    CompteurCouleur = 2
                else:
                    PageHTML.write('<FONT color="' + Couleur2 + '">' + temps + "</FONT>")
                    CompteurCouleur = 1
            temps = ""

    PageHTML.write("</p>")


# Fin de la page HTML
PageHTML.write("<body>  <html>")
PageHTML.close()

# print(PlaceSyllabe("manège"))

# print(TexteEnMotsSyllabé("manège",3,séparateur))

