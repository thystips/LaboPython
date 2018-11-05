# Dans cet exercice, vous allez coder des fonctions.
# Des tests sont fournis, vous disant si votre code
# fonctionne correctement.
#
# Il y a 20 tests, chacun étant sur 1 point.
# Il y a une question bonus, avec un 21ème test.
#
# Vous pouvez utiliser print pour vous aider à débugger,
# car sys.stdout est ignoré par les tests.

# Ignorez ces deux lignes, elles servent pour la fin
# du programme.
import hashlib
import unittest


# Définir une fonction nommée count_ones.
# Elle prend un paramètre :
#  * un nombre binaire sous forme de chaine
#    de caractères composée uniquement de
#    1 et de 0
#
# Cette fonction doit renvoyer le nombre de
# 1 présents dans le nombre binaire passé en
# paramètre.

# def count_ones(binaire):

def count_ones(binaire):
    return binaire.count('1')   

# Définir une fonction nommée invert_bit.
# Elle prend un paramètre :
#  * un nombre binaire sous forme de chaine
#    de caractère composée uniquement de
#    1 et de 0. Cette chaine représente
#    un bit, et est donc de longeur 1.
#
# Cette fonction doit inverser le bit :
#  * Si la chaine vaut '0', il faut retourner '1'.
#  * Si la chaine vaut '1', il faut retourner '0'

def invert_bit(binaire):
    if binaire == '1':
        return '0'
    else :
        return '1'


# Définir une fonction nommée index_of_last_one.
# Elle prend un paramètre :
#  * un nombre binaire sous forme de chaine
#    de caractères composée uniquement de
#    1 et de 0
#
# Cette fonction doit renvoyer l'index du dernier bit à 1,
# c'est à dire la position du bit à 1 le plus à
# droite. Il est évident que les index commencent
# à 0.

def index_of_last_one(binaire):
    index = 0
    index_of_last_one = -1
    for index,bit in enumerate(binaire):
        if bit == '1':
            index_of_last_one = index
    return index_of_last_one


# Définir une fonction nommée invert_bit_n.
# Elle prend deux paramètres :
#  * un nombre binaire sous forme de chaine
#    de caractères composée uniquement de
#    1 et de 0
#  * un entier l'index du bit à inverser
#
# Cette fonction doit renvoyer le nombre
# fourni, mais dans lequel le bit à l'index
# fourni a été inversé.

def invert_bit_n(binaire,index):
    return binaire[:index] + invert_bit(binaire[index]) + binaire[index+1:]

# Définir une fonction nommée result.
# Elle prend deux paramètres :
#  * un nombre binaire sous forme de chaine
#    de caractères composée uniquement de
#    1 et de 0
#  * un entier représentant le nombre d'étapes
#
# Cette fonction renvoie une liste, contenant
# n éléments, n étant le nombre d'étapes.
#
# Le premier élément de la liste est le nombre
# binaire passé en paramètre de la fonction.
#
# Chaque élément suivant dans la liste est
# ensuite calculé à partir du précédent.
#
# Lorsqu'il y a un nombre pair de 1 dans le nombre
# précédent, on inverse le dernier bit (celui de
# droite).
#
# Lorsqu'il y a un nombre impair de 1 dans le
# nombre précédent, on inverse le bit directement à
# gauche du 1 le plus à droite.
#
# Ce nouveau nombre est ajouté dans la liste
# des résultats.

#def result(binaire, etapes):

# Définir une fonction nommée bonus.
# Cette fonction renvoie une chaine de caractères.
# Cette chaine de caractères doit contenir le
# nom du codage que nous venons de réaliser.
# Ce codage a été breveté il y a longtemps et
# il a un énorme avantage que je vous expliquerai
# plus tard.

def bonus():
    return 'gray'

################################################################
################################################################
# La suite du programme est là pour tester ce que vous faites. #
# Vous n'avez pas à y toucher, et vous n'êtes pas obligés de   #
# la lire.                                                     #
################################################################
################################################################


class TestCountOnes(unittest.TestCase):
    def test_zero_bit_set_to_one(self):
        self.assertEqual(
            count_ones('0000'),
            0)

    def test_one_bit_set_to_one(self):
        self.assertEqual(
            count_ones('001000'),
            1)

    def test_two_bits_set_to_one(self):
        self.assertEqual(
            count_ones('0010001000'),
            2)

    def test_three_bits_set_to_one(self):
        self.assertEqual(
            count_ones('00100010001'),
            3)

    def test_four_bits_set_to_one(self):
        self.assertEqual(
            count_ones('100100010001'),
            4)


class TestInvertBit(unittest.TestCase):
    def test_invert_zero(self):
        self.assertEqual(
            invert_bit('0'),
            '1')

    def test_invert_one(self):
        self.assertEqual(
            invert_bit('1'),
            '0')


class TestIndexOfLastOne(unittest.TestCase):
    def test_first_bit(self):
        self.assertEqual(
            index_of_last_one('1000000'),
            0)

    def test_last_bit(self):
        self.assertEqual(
            index_of_last_one('00001'),
            4)

    def test_middle_bit(self):
        self.assertEqual(
            index_of_last_one('0000100'),
            4)

    def test_two_bits(self):
        self.assertEqual(
            index_of_last_one('0000100100'),
            7)


class TestInvertBitN(unittest.TestCase):
    def test_invert_zero(self):
        self.assertEqual(
            invert_bit_n('0', 0),
            '1')

    def test_invert_one(self):
        self.assertEqual(
            invert_bit_n('1', 0),
            '0')

    def test_invert_first(self):
        self.assertEqual(
            invert_bit_n('01', 0),
            '11')

    def test_invert_last(self):
        self.assertEqual(
            invert_bit_n('01', 1),
            '00')

    def test_invert_middle(self):
        self.assertEqual(
            invert_bit_n('010', 1),
            '000')

    def test_invert_middle_2(self):
        self.assertEqual(
            invert_bit_n('00010', 1),
            '01010')


class TestResult(unittest.TestCase):
    @staticmethod
    def secret(a, b=0):
        a += b
        a ^= a >> 1
        return bin(a)[2:]

    def test_nb_steps(self):
        for nb_steps in range(3, 10):
            res = result('000' * (nb_steps // 2), nb_steps)
            self.assertEqual(len(res), nb_steps)

    def test_0000_16(self):
        res = result('0000', 16)
        for index in range(16):
            self.assertEqual(self.secret(index).zfill(4), res[index])

    def test_0000101_20(self):
        res = result('0000101', 20)
        for index in range(20):
            self.assertEqual(self.secret(index, 6).zfill(7), res[index])


class TestBonus(unittest.TestCase):
    def test_bonus(self):
        answer = bonus()
        answer = answer.strip().lower()
        self.assertEqual(
            len(answer),
            4,
            'la réponse attendue fait 4 caractères')
        hash = hashlib.sha256(answer.encode('utf-8')).hexdigest()
        self.assertEqual(
            hash,
            '0e92d69f9b951b18299f34b2e53dbba7e9ad0b070883c040c0fcc1f74e1985ef')


if __name__ == '__main__':
    unittest.main(verbosity=2)
