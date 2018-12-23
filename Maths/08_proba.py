from random import randrange


def un_tirage():
    urne = ["B"] * 3 + ["R"] * 4
    t1=urne.pop(randrange(len(urne)))
    t2=urne.pop(randrange(len(urne)))
    dico[t1+t2]+=1

def n_tirage(n):
    for i in range(n):
        un_tirage()
    for k,v in dico.items():
        dico[k]/=n

dico={'BB':0,'BR':0,'RB':0,'RR':0}
n_tirage(1000000)
print(dico,sum(dico.values()))