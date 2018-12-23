# input() représente ton entrée, là où ton code récupèrera tes valeurs. Le int force juste Python à mettre les valeures en entier naturel.
n = int(input())
# "pis" représente la puissance de ton cheval i tu peux l'écrire "les p[i]s" aussi.
# "sorted" indique que tu tris par ordre croissant les valeurs qui sont envoyées par ton jeu, les (int(input()) for _ in range(n)).
pis = sorted(int(input()) for _ in range(n))
# "delta" représente la plus petite différence de puissance entre chaque cheval grâce au "min".
# Les "pis" sont dans une liste donc tu prends pour la première fois la deuxième plus petite valeur de puissance et tu lui enlève la plus petite et tu regardes si c'est la plus petite différence.
# Tu prends ensuite la toisième et la deuxième et ainsi de suite jusqu'à la plus grande valeur et la deuxième plus grande.
delta = min(pis[i + 1] - pis[i] for i in range(n - 1))
print(delta)
# Et tu finis par afficher delta