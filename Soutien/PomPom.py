#message = ['C','O', 'u', 'C', 'O', 'U']
#for cursor in message:
#    print('Donne moi un', cursor)

def pompom(message):
    for cursor in message:
        print('Donne moi un', cursor)

result = input("Comment tu t'appelles ? \n")
pompom(result)
fin = result+" !!!"
print(fin)