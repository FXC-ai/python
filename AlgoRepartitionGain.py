from tkinter import *

print('algo repartition de gain')

nbr_individus = int(input('Nbr d\'individu ?'))


def algoRepartGain (nbr_individus):
	i = 0
	limite = 0
	list_repartition = []
	while limite < nbr_individus :
		i+=1
		limite += i
		list_repartition.append(i)

	reste_a_distribuer = sum(list_repartition) - nbr_individus
	
	c = 0
	while reste_a_distribuer > 0:
		list_repartition[c] -= 1
		reste_a_distribuer -= 1
		c += 1	

	return list_repartition


list_repartition = algoRepartGain(nbr_individus)

print(list_repartition)
list_resultats = list()


count = 1
while count <= nbr_individus :
	result = algoRepartGain(count)
	list_resultats.append(result)
	count+=1

	
print(list_resultats)


fenetre = Tk()

col = 0
lig = 0
for elt in list_resultats :
    Tk.Label(fenetre, text = sum(elt) , bg = 'blue').grid(row = lig, column = col)
    for nbr in reversed(elt) :
        lig+=1
        Tk.Label(fenetre, text = nbr , bg = 'green').grid(row = lig, column = col)
		
    col+=1
    lig = 0

fenetre.mainloop()

	
