from random import randrange


def un_tirage(B, R):
    urne = ["B"] * 3 + ["R"] * 4
    t1=urne.pop(randrange(len(urne)))
    t2=urne.pop(randrange(len(urne)))
    dico[t1+t2]+=1


dico={'BB':0,'BR':0,'RB':0,'RR':0}