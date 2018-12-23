# -*-coding:utf-8 -*

message = "Lèche mes grosses couilles"
with open("fichier_exo_chiffrement.txt", "w", encoding="utf-8") as f:
    for caratere in message:
        code_caractere = ord(caratere)
        code_caractere += 1
        caratere_chiffre = chr(code_caractere)
        f.write(caratere_chiffre)

g = open("fichier_exo_chiffrement.txt", "r", encoding="utf-8")
decode = g.read()
for carac in decode:
    decode = ord(carac)
    decode -= 1
    carac_decode = chr(decode)
    print(carac_decode, end="")

