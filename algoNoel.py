import random

random_list = ["Sudries Philippe", 
                 "Sudries Laura", 
                 "Sudries JC", 
                 "Augeron Louise", 
                 "Augeron Bernard",
                 "Augeron Grégoire",
                 "Isabelle Tanché",
                 "Boumard Marty",
                 "Coindreau Marc-Antoine",
                 "Coindreau François-Xavier",
                 "Coindreau Philippe",
                 "Coindreau Véronique"]

Coindreau = ["Coindreau Marc-Antoine",
             "Coindreau François-Xavier",
             "Coindreau Philippe",
             "Coindreau Véronique"]

Augeron = ["Augeron Louise",
           "Augeron Bernard",
           "Augeron Grégoire",
           "Isabelle Tanché",
           "Boumard Marty"]

Sudries = ["Sudries Philippe", 
           "Sudries Laura", 
           "Sudries JC"]

#Fonction permettant de creer aléatoirement une liste en faisant en sorte
#que le premier nom et le dernier soit compatibles pour s'offrir des cadeaux
def creationRandom_list(random_list):
    random.shuffle(random_list) 
    while (random_list[0] in Augeron and random_list[-1] in Sudries) or (random_list[0] in Sudries and random_list[-1] in Augeron) :
        random.shuffle(random_list)
    return random_list

#Fonction permettant de valider si la liste est conforme
#cad si aucun Sudrie ne doit offrir un cadeau à un Augeron ou l'inverse
def validation_liste(random_list):
    for index, elt in enumerate(random_list) :
        if (elt in Sudries and random_list[index + 1] in Augeron) or (elt in Augeron and random_list[index+1] in Sudries):
            liste_valide = False
            break        
        if index == 10 :
            liste_valide = True
            break
    return liste_valide
 
#Brute force, on essais plusieurs liste jusqu'à tomber sur une valide
i = 0
while i<1000:
    creationRandom_list(random_list)
    liste_valide = validation_liste(random_list)
    if liste_valide == True:
        break

#On crée les fichiers avec en haut le nom de la personne à qui est destinée le cadeau
#En bas le nom de la personne qui doit offrir le cadeau avec la mention "A mettre dans l'enveloppe destinée à"
for index, nom in enumerate(random_list):
    destination = "\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"A mettre dans l'enveloppe destinée à " + random_list[index-1]   
    nom_fichier = random_list[index-1]+".txt"   
    
    with open(nom_fichier, "w") as fichier:
        fichier.write(nom)
        fichier.write(destination)
