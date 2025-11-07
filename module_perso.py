#!/usr/bin/env python
from random import randint

class Perso:
    
    def __init__(self, nom, niveau):
        self.nom=nom
        self.niveau=niveau
        self.etat="bien"

    def personnages(dico_perso_vie):
        return list(dico_perso_vie.keys())
    
    def nom(self):
        print(self.nom)

    def setEtat(self,new_etat):
        self.etat=new_etat
        return self.etat
    
    def vie(self):
        pass

    def capacites(self):
        pass

class MarioPasPeur(Perso):

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)

    def vie(self):
        return self.niveau*10
    
    def capacites(self):
        return self.niveau*3,self.niveau*2,0

class Pitch(Perso):

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)

    def vie(self):
        return self.niveau*5
    
    def capacites(self):
        return self.niveau*2,self.niveau*3,randint(1,4)

class Bouser(Perso):

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)

    def vie(self):
        return self.niveau*15
    
    def capacites(self):
        return self.niveau*4,self.niveau,randint(1,4)
    
class Hoshi(Perso):

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)

    def vie(self):
        return self.niveau
    
    def capacites(self):
        return self.niveau/2,0,randint(1,2)