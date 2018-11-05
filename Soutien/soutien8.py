def ex1():
    def pompom(message):
        for cursor in message:
            print('Donne moi un', cursor)

    result = input("Comment tu t'appelles ? \n")
    pompom(result)
    fin = result+" !!!"
    print(fin)
    return

def ex2():
    i=0
    while i<2:
        print("Haec igitur Epicuri non probo, inquam. De cetero vellem equidem aut ipse doctrinis fuisset instructior est enim, quod tibi ita videri necesse est, non satis politus iis artibus, quas qui tenent, eruditi appellantur aut ne deterruisset alios a studiis. quamquam te quidem video minime esse deterritum.\n")
        i+=1
    return

def ex3():
    Hey = input('Comment ça va ? \n')

    if Hey == 'bien' :
        print("Je m'en bas les couilles" )

    elif Hey =='mal' :    
        print("Du coup tu veux bien me sucer ?")
    else:
        print("J'ai pas compris du con apprends à parler :)")
    return

def ex4():
    Hey=""
    while Hey != "bien":
        Hey = input("Comment vas-tu bâtard ?\n")
    return

def ex5():
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
    return


Choix = input("Choisi ton exercice du con\n")


if Choix == "1":
    ex1()
elif Choix == "2":
    ex2()
elif Choix == "3":
    ex3()
elif Choix == "4":
    ex4()
elif Choix == "5":
    ex5()
else:
    print("T'es vraiment une merde.")