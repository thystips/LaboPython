import matplotlib.pyplot as plt
from math import sqrt


nb=[2,1,1,3,2,2,7,4,1,2,3,1,2,4,3,1,1,1,2,2,1,6,2,2,3,1,1,2,1,3,2,1,3]

dico={}

def probas():
    for n in nb:
        if n in dico.keys():
            dico[n]+=1
        else:
            dico[n]=1

    for i in dico.keys():
        dico[i]/=len(nb)

def esperance():
    res=0
    for k, v in dico.items():
        res+=k*v
    return res
    
def variance(esp):
    res = 0
    for k, v in dico.items():
        res+=v*((k-esp)**2)
    return res



nb.sort()
probas()
print(dico)
print(sum(dico.values()))
esp=esperance()
var=variance(esp)
ecart_type=sqrt(var)
print('Esperance : {}; Variance : {}; Ecart_type : {}'.format(esp,var,ecart_type))

fig,ax = plt.subplots()
ax.plot(list(dico.keys()), list(dico.values()))
ax.set(xlabel='nbre enfants',ylabel='probabilité')
ax.axvline(esp,ls='--',color='r')
ax.grid()
plt.show()