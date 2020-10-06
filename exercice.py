
# TODO: Importez vos modules ici

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import pi

# importer un fichier que moé j'ai faitte!
import sys
sys.path.insert(1, r"D:\Universite\INF1007\Exercices")
from chapitre6.exercice import frequence

import turtle


# TODO: Définissez vos fonction ici

# Commentaire intelligent
def calculer_vm_ellipsoide(a=1, b=1, c=1, ro=1) ->tuple() :
    """
    Calcule le volume et la masse d'un ellipsoïde. C'est quoi un ellipsoide?
    :param a: demi-axe 1
    :param b: demi-axe 2
    :param c: demi-axe 3 (3 demies, comme j'aime mes pintes de bière)
    :param ro: La masse volumique, j'ai pas le clavier grec
    :return: Un tuple qui contient (volume, masse)
    """

    volume = 4 / 3 * pi * a * b * c

    masse = ro * volume

    masseEtVolume = (volume, masse)

    return masseEtVolume

def dessiner_arbre() :
    # Faut utiliser la librairie Turtle

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(calculer_vm_ellipsoide(1, 2, 3, 4))

    # phrase = "banane"
    print((lambda phrase: sorted(frequence(phrase), key=frequence(phrase).get)[-1])("banane banane"))
    print(frequence("BANANE"))

    pass
