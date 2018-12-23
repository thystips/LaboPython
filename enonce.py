# En démarrant de la fin :
#  - un chiffre sur deux est laissé tel quel (en particulier le dernier)
#  - un chiffre sur deux est multiplié par deux, et si le résultat est
#    strictement supérieur à 9 alors on lui soustrait 9
#
# La somme de ces chiffres doit faire un nombre divisible par 10, sinon
# le numéro de carte bleue est invalide.
#
# Cet algorithme est appelé clé de Luhn, vous pouvez l'essayer avec
# votre carte bleue.

def supprime_espace(chaine):
    resultat = ""
    for caractere in chaine:
        if caractere != " ":
            resultat += caractere
    return resultat

#def verif_carte_bleue(numero_carte_bleue):
#    numero_carte_bleue = numero_carte_bleue.replace(" ","")
#    numero = list(numero_carte_bleue)
#    for index in range(0, 16, 2):
#        numero[index] = numero[index] * 2
#        if numero[index] > 9:
#            numero[index] -= 9
#        numero[index] = str(numero[index])
#
#    resultat = 0
#    for chiffre in numero:
#        resultat += int(chiffre)
#
#    if resultat % 10:
#        print("invalide")
#    else:
#        print("valide")

def verif_carte_bleue(numero_carte_bleue):
    numero_carte_bleue = numero_carte_bleue.replace(" ","")
    numero_list = [int(chiffre) for chiffre in numero_carte_bleue]
    for index in range(0, 16, 2):
        numero_list[index] *= 2
        numero_list[index] %= 9
    if sum(numero_list) % 10:
        print("invalide")
    else:
        print("valide")


verif_carte_bleue("4975 8971 6458 4022")
verif_carte_bleue("4975 8971 6458 4023")
