import unittest


# Exercice 1
#    Créer une fonction appelée deux_des qui prend un entier en paramètre
#    (entre 2 et 12). La fonction donne le nombre de façons de faire cet
#    entier en lançant deux dés.

def deux_des(nombre):
    if nombre < 8:
        return nombre - 1
    else:
        return 13 - nombre

# Exercice 2
#    Créer une fonction appelée trois_des qui prend un entier en paramètre
#    (entre 3 et 18). La fonction donne le nombre de façons de faire cet
#    entier en lançant trois dés.

def trois_des(nombre):
    nb_possibilites = 0
    for valeur_de_1 in range(1, 7):
        for valeur_de_2 in range(1, 7):
            for valeur_de_3 in range(1, 7):
                if valeur_de_1 + valeur_de_2 + valeur_de_3 == nombre:
                    nb_possibilites +=1
    return nb_possibilites


# Exercice 3
#    Créer une fonction appelée filtre qui prend une liste de nombres
#    en paramètre. La fonction renvoie la liste telle que les nombres
#    non multiples de trois ont été supprimés.



class Test2Des(unittest.TestCase):
    def test_12(self):
        self.assertEqual(deux_des(12), 1)

    def test_11(self):
        self.assertEqual(deux_des(11), 2)

    def test_8(self):
        self.assertEqual(deux_des(8), 5)


class Test3Des(unittest.TestCase):
    def test_12(self):
        self.assertEqual(trois_des(12), 25)

    def test_3(self):
        self.assertEqual(trois_des(3), 1)

    def test_4(self):
        self.assertEqual(trois_des(4), 3)

    def test_18(self):
        self.assertEqual(trois_des(18), 1)


class TestFiltre(unittest.TestCase):
    def test_1245(self):
        self.assertEqual(filtre([1, 2, 4, 5]), [])

    def test_123456(self):
        self.assertEqual(filtre([1, 2, 3, 4, 5, 6]), [3, 6])

    def test_vide(self):
        self.assertEqual(filtre([]), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
