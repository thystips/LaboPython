import unittest
from pathlib import Path

# Définir une fonction chiffre_caractere qui prend 2 paramètres :
#  - un caractère à chiffrer
#  - un caractère de la clé
#
# Elle doit renvoyer le caractère dont le code unicode (donné
# par la fonction ord) est la somme des codes unicode des deux
# caractères fournis à la fonction chiffre_caractere.

def chiffre_caractere(a, b):
    x = ord(a)
    y = ord(b)
    c = x + y
    return chr(c)

# Définir une fonction chiffre_chaine qui prend 2 paramètres :
#  - une chaine de caractères à chiffrer
#  - une chaine de caractères, la clé de chiffrement
#
# Elle doit renvoyer la chaine de caractères résultant du
# chiffrement de la chaine de caractères à chiffrer en utilisant
# la clé de chiffrement.
#
# Pour chaque caractère de la chaine à chiffrer, ce caractère
# est chiffré avec la fonction chiffre_caractere.
# Pour le premier caractère à chiffrer, le premier caractère
# de la clé est utilisé.
# Pour le deuxième caractère à chiffrer, le deuxième caractère
# de la clé est utilisé.
# Ainsi de suite.
# Si tous les caractères de la clé ont été utilisé, il faut
# repartir du début de la clé.

def chiffre_chaine(texte, cle):
    resultat = ""
    longueur_cle = len(cle)
    for index, caractere in enumerate(texte):
        resultat += chiffre_caractere(caractere, cle[index % longueur_cle])
    return resultat



# Définir une fonction chiffre_dans_fichier qui prend 3 paramètres :
#  - un chemin de fichier dans lequel sera écrit le résultat
#  - une chaine de caractères à chiffrer
#  - une chaine de caractères, la clé de chiffrement
#
# La fonction doit écrire en UTF-8 dans le fichier dont le chemin
# a été fourni. Le contenu du fichier doit être le résultat de
# l'appel à chiffre_chaine avec la chaine à chiffrer et la clé
# fournies à la fonction chiffre_dans_fichier.

def chiffre_dans_fichier(a, b, c):
    message = list(b)
    cle = list(c)
    resultat = chiffre_chaine(message, cle)
    with open(a, "w", encoding='utf-8') as f:
        f.write(resultat)


# Définir une fonction dechiffre_chaine qui prend 2 paramètres :
#  - une chaine de caractères à déchiffrer
#  - une chaine de caractères, la clé de déchiffrement
#
# Cette fonction doit renvoyer la chaine de caractères contenant
# le texte déchiffré, sachant que la chaine de caractères chiffrée
# a été chiffrée avec chiffre_chaine.
#
# Le code est donc très similaire à chiffre_chaine.

def dechiffre_chaine(a,b):
    return()


class TestChiffreCaractere(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(chiffre_caractere("a", "\x00"), "a")

    def test_A(self):
        self.assertEqual(chiffre_caractere("b", "A"), "£")


class TestChiffreChaine(unittest.TestCase):
    def test_cle_zero(self):
        self.assertEqual(chiffre_chaine("Vincent", "\x00"), "Vincent")

    def test_cle_un(self):
        self.assertEqual(chiffre_chaine("Vincent", "\x01"), "Wjodfou")

    def test_cle_zero_zero_zero_un(self):
        self.assertEqual(
            chiffre_chaine("Vincent", "\x00\x00\x00\x01"), "Vindent"
        )

    def test_cle_motdepasse(self):
        self.assertEqual(chiffre_chaine("Vincent", "Motdepasse"), "£ØâÇÊÞÕ")


class TestChiffreDansFichier(unittest.TestCase):
    def test_creation_fichier(self):
        path = Path("deleteme.txt")
        if path.exists():
            path.unlink()
        chiffre_dans_fichier(path, "Vincent", "Motdepasse")
        self.assertTrue(
            path.exists(), msg=f"Le fichier {path} n'a pas été créé"
        )
        if path.exists():
            path.unlink()

    def test_fichier_non_vide(self):
        path = Path("deleteme2.txt")
        if path.exists():
            path.unlink()
        chiffre_dans_fichier(path, "Vincent", "Motdepasse")
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                break
            self.assertTrue(line)
        if path.exists():
            path.unlink()

    def test_chiffrement_fichier(self):
        from itertools import cycle

        path = Path("deleteme3.txt")
        if path.exists():
            path.unlink()
        chiffre_dans_fichier(path, "Vincent", "Motdepasse")
        with open(path, "r", encoding="utf-8") as f:
            for l in f:
                break
        i = zip(l, cycle("Motdepasse"))
        self.assertEqual("Vincent", "".join(chr(ord(a) - ord(b)) for a, b in i))
        if path.exists():
            path.unlink()


class TestDechiffreChaine(unittest.TestCase):
    def test_dechiffre_1(self):
        chaine = "Ceci est un super message"
        cle = "Mouais"
        chaine_chiffree = chiffre_chaine(chaine, cle)
        chaine_dechiffre = dechiffre_chaine(chaine_chiffree, cle)
        self.assertEqual(chaine, chaine_dechiffre)


if __name__ == "__main__":
    unittest.main(verbosity=2)
