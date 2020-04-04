# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import random


print('Jeu des suites numériques')

class Jeu_des_Suites :
    def __init__(self, n0):
        self.suite = list()
        self.n0 = int(n0)
        self.answer = int()
        self.methodes = [self.suite1, self.suite2, self.suite3]
        
    
    def suite1(self, n):
        n_suivant = (n + 1)*2
        return n_suivant
    
    def suite2(self, n):
        n_suivant = 4*n -1
        return n_suivant
    
    def suite3(self, n):
        n_suivant = n*2 + 3
        return n_suivant
        
    
    def creerSuite(self):
        choix_calcul = random.randint(0, len(self.methodes) - 1)
        
        n = self.methodes[choix_calcul](self.n0)
        self.suite.append(n)
        
        
        
        for _ in range(5):
            n = self.methodes[choix_calcul](n)
            self.suite.append(n)
            
        self.answer = self.methodes[choix_calcul](n)
        
        
        return self.suite
    
    def jouer(self):
        suite = self.creerSuite()
        for index, nombre in enumerate(suite) :
            print('Terme {} = {}'.format(index, nombre))
        
        answer_player = input('Quel est le terme suivant ? ')
        
        print(answer_player)
        
        if int(answer_player) == self.answer:
            print('Victoire !')
        else:
            print('Perdu !')


game = Jeu_des_Suites(1)

game.jouer()
