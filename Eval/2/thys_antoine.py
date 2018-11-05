# Vous pouvez utiliser print pour vous aider à débugger,
# car sys.stdout est ignoré par les tests.

# Ignorez ces deux lignes, elles servent pour la fin
# du programme.
import hashlib
import unittest

# Afficher les nombres de 1 à 100 en suivant l'algorithme suivant :
#
# Pour chaque nombre de 1 à 100 inclus:
#  - si le nombre est multiple de 3, afficher Toto à la place
#  - si le nombre est multiple de 5, afficher Tata à la place
#  - si le nombre contient un 3 (comme le nombre 23), afficher
#    Titi à la place
#  - si le nombre contient un 5 (comme le nombre 45), afficher
#    Tutu à la place
#  - si le nombre contient plusieurs 3 ou plusieurs 5, faire
#    comme s'il n'y avait qu'un seul 3 ou 5
#  - si le nombre respecte plusieurs règles, il faut appliquer
#    les règles dans l'ordre de l'énoncé
#  - si le nombre ne correspond à aucune règle, afficher le
#    nombre tel quel
#
# Exemples de conversions :
#  - 6 devient Toto
#  - 10 devient Tata
#  - 13 devient Titi
#  - 52 devient Tutu
#  - 33 devient TotoTiti
#  - 15 devient TotoTataTutu
#  - 2 devient 2
#
# Pour répondre à cet exercice, commencer par faire une fonction
# appelée convert_number qui prend comme paramètre un nombre
# entier et qui renvoie le texte correspondant à ce nombre


def convert_number(nombre_entier):
    nombre_entier_chaine = str(nombre_entier)
    resultat = ""
    if nombre_entier % 3 == 0:
        resultat += "Toto"
    if nombre_entier % 5 == 0:
        resultat += "Tata"
    if "3" in nombre_entier_chaine:
        resultat += "Titi"
    if "5" in nombre_entier_chaine:
        resultat += "Tutu"
    if resultat:
        return resultat
    else:
        return nombre_entier_chaine


# Faire ensuite une fonction appelée conversion_results qui ne prend
# pas de paramètre, et qui renvoie le texte correspondant
# à la conversion des nombres de 1 à 100 inclus, chaque
# nombre converti étant séparé par un espace avec le nombre
# suivant dans la liste.


def conversion_results():
    i = 1
    resultat = ""
    while i < 100:
        resultat += convert_number(i)
        resultat += " "
        i += 1
    resultat += convert_number(100)
    return resultat


class TestConvertNumber(unittest.TestCase):
    def test_6(self):
        self.assertEqual(convert_number(6), "Toto")

    def test_10(self):
        self.assertEqual(convert_number(10), "Tata")

    def test_13(self):
        self.assertEqual(convert_number(13), "Titi")

    def test_52(self):
        self.assertEqual(convert_number(52), "Tutu")

    def test_33(self):
        self.assertEqual(convert_number(33), "TotoTiti")

    def test_15(self):
        self.assertEqual(convert_number(15), "TotoTataTutu")

    def test_1(self):
        self.assertEqual(convert_number(1), "1")

    def test_35(self):
        self.assertEqual(convert_number(35), "TataTitiTutu")


class TestConversionResults(unittest.TestCase):
    def test_conversion_results_length(self):
        answer = conversion_results()
        self.assertEqual(len(answer), 534, "la réponse attendue fait 534 caractères")

    def test_conversion_results_value(self):
        answer = conversion_results()
        answer = answer.strip().lower()
        hash = hashlib.sha256(answer.encode("utf-8")).hexdigest()
        self.assertEqual(
            hash, "70859649c5ddf3183e519a6617e898a9452cc06726dc89edb6140f9f9e95aad4"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
