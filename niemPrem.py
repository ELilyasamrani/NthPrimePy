"""

<---------------------------------------------------------- Description -------------------------------------------------------->
|																																|
|																																|
| + Ce fichier résoud le problème du nième nombre premier, contient les fonctions suivantes : 									|
|	- siPremier : vérifier si un nombre fourni en argument (x) est premier.														|
|	- siPremierOpt : fait le même travaille mais d'une manière plus optimisé : test seulement si divisible par 					|
|					 les nombre premier inférieurs à la partie entière de sa racine (cas de test sur les grand chiffres)		|
|	- niemPremier : Retourne le nième nombre premier (n) en utilisant une boucle while de complexité d'ordre 2 : 				|
|			i : l'indice du dernier nombre premier trouvé lors de la boucle while.												|
|			j : Le nombre à tester. 																							|
|			on soustrail 1 de j vers la fin puisque on l'ajout après l'incrémentation de i.										|
|	- niemPremOpt : Retourn le nième nombre premier (n) en utilisant la méthode de mémorisation (facilite largement le calcul)	|
|	- MSMs : convertiseur du temps de Secondes vers Minutes,Secondes,Millisecondes.												|
|																																|
|	Le 10001eme nombre premier est 104743 : Durée de calcule : près 1min 44s 44ms sur un i5 520m								|
|																																|
|-------------------------- :::::::::: Programme réalisé par Ilyas El Amrani le 2/07/2022 :::::::::: ---------------------------|
<------------------------------------------------------------------------------------------------------------------------------->

"""
import sys #Pour résoudre le problème de récursion
import time #Pour avoir le temp 
import math #Pour calculer la racine carrée 

def siPremier(x):
	if(x>1):
		for i in range(2,int(math.sqrt(x))):
			if(x%i==0):
				return False
		return True
	else:
		return False 

def siPremierOpt(x):
	if(x>1): #Si le nombre
		for i in range(1,x):
			if(niemPremOpt(i)>int(math.sqrt(x))):
				return True
			if(x%niemPremOpt(i) == 0):
				return False
		return True
	else : return False 


def niemPremier(n):
	i=0;j=0

	if(n<100):
		while(i<n):
			if(siPremier(j)):
				i+=1
			j+=1
	else :
		while(i<n):
			if(siPremierOpt(j)):
				i+=1
			j+=1
	j-=1
	return j



#fonction de mémorisation :

memoire = {}

def niemPremOpt(n):
	if (n<=8000):
		memoire[n]=niemPremier(n)
	else :
		i=n-1;j=niemPremOpt(n-1)+1
		while(i<n):
			if(siPremier(j)):
				i+=1
			j +=1
		j-=1
		memoire[n]=j
	return memoire[n]

#convertiseur du temps
def MSMs(s):
	m =  s//60 if(s>=60) else 0
	s = s-m*60
	ms = int((s-int(s))*100)
	s = int(s)
	return m,s,ms

if(__name__ == "__main__"):
	
	#C : choix de l'utilisateur de continuer à executer le programme : O : OUI / N:NON
	c='O'

	#Pour éviter le probleme de dépassement des limites de récursion 
	sys.setrecursionlimit(10**6)
	
	#Programme :
	while(c=='O'):
		n=0
		#Entré de l'indice du nombre premier à calculer
		while(n<1):
			n = int(input("Veuillez saisir l'indice du chiffre du nombre premier que vous voulez calculer : \n >> "))

		#calcule de ce nombre avec le temps écoulé durant ce calcule (t1 et t2)
		t1=time.time()
		print("\n...\nLe {0}ième nombre premier est : {1} \n".format(n,niemPremOpt(n)))
		t2=time.time()

		#Calcule de temps fait pour le calcule :
		s=t2-t1 
		m,s,ms = MSMs(s)

		#Affichage de ce temps 
		print("<-------- Calculé en {0}m{1}s{2}ms -------->\n".format(m,s,ms))
		c='X'

		#Vérification du choix de l'utilisateur
		while(c!='O' and c!='N'):
			c = input('Tu veux continuer ? O/N : \n >> ')
	

"""<------------------ FIN ------------------>"""