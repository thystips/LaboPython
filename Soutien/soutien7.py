i = 0
while True :
    hey = input("Comment vas-tu ?\n")

    if i>1:
        print("Comme tu n'es pas foutu de répondre je vais m'occuper personnellement de ton cas dans d'atroces souffrances :)\n")
        break
    elif hey != "bien":
        i += 1
    else:
        print("Ceci est extrêmement dommage !\n")
        break
