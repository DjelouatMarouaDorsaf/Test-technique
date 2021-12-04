from random import *

LONGUEUR=10
MIN=1
MAX=47

tab =[randint(MIN,MAX) for i in range (LONGUEUR)]
tab.sort()

X=randint(MIN,MAX)

def DPMR(tab, i, j, X):
	if(i==j):
		return i
	else :
		K=(i+j)//2
		if (X<=tab[K]):
			return DPMR(tab,i,K,X)
		else:
			return DPMR(tab,K+1,j,X)


print('Nombre à insérer : ' + str(X))
print("______________")
print('tabelau trié avant insertion : '+ str(tab))
print("______________")
result=DPMR(tab,0,len(tab)-1,X)
tab.insert(result, X)
print('tabelau trié après insertion : '+ str(tab))
