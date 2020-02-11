from tkinter import *

def suiteConway (nbr):
	list_nbr = []
	
	for chiffre in str(nbr) :
		list_nbr.append(chiffre)

	i = 0
	c = 1
	list_iteration = []
	while i < len(list_nbr) :
		try :
			while list_nbr[i] == list_nbr[i+1]:
				c+=1
				i+=1
		except IndexError:
			pass

		list_iteration.append(c)
		list_iteration.append(list_nbr[i])
		i+=1
		c = 1

	nv_nbr = str()
	for chiffre in list_iteration :
		nv_nbr += str(chiffre)
	return int(nv_nbr)
		

def repeat(nbr_rep, nbr):
	i = 0
	list_Conway = [nbr]
	while i < nbr_rep :
		nbr = suiteConway(nbr)
		i+=1
		list_Conway.append(nbr)

	return list_Conway


list_Conway = repeat(17, 2)


root = Tk()

dict_couleur = {'0' : 'red', '1' : 'green', '2' : 'blue', '3' : 'black', '4' : 'black', '5' : 'orange', '6':'purple'}

r = 0
for nbr in list_Conway:
	c = 0
	for chiffre in str(nbr) :
		if c%2 == 0 :
			Label(root, text = ' ', bg = dict_couleur[chiffre]).grid(row = r, column = c)
		else :
			Label(root, text = ' ', bg = 'white').grid(row = r, column = c)	
		c+=1
	
	r+=1

root.mainloop()

