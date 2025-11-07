#!/usr/bin/env python
from random import randint

class Ennemi:
    def __init__(self,nom,niveau):
        self.nom=nom
        self.niveau=niveau
        self.etat="bien"
    
    def vie(self,niveau):
        pass
    
    def capacites(self,niveau):
        pass

    def nom(self):
        print(self.nom)

    def setEtat(self,new_etat):
        self.etat=new_etat
        return self.etat

class Gooma (Ennemi):

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
    
    def vie(self):
        return self.niveau*5
    
    def capacites(self):
        return self.niveau*2,0,0
    
    def pieces_gagnees(self):
        if self.niveau<5:
            return 5
        if self.niveau>=5:
            return 10
        if self.niveau==99:
            return 100
    
class Koupape (Ennemi):

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
    
    def vie(self):
        return self.niveau*5
    
    def capacites(self):
        return self.niveau*2,self.niveau,randint(1,4)
    
    def pieces_gagnees(self):
        if self.niveau<5:
            return 10
        if self.niveau>=5:
            return 20
        if self.niveau==99:
            return 200

class Masscasse (Ennemi):

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
    
    def vie(self):
        return self.niveau*7
    
    def capacites(self):
        return self.niveau*3,1,randint(1,3)
    
    def pieces_gagnees(self):
        if self.niveau<5:
            return 50
        if self.niveau>=5:
            return 100
        
class BossBresom (Ennemi):

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
    
    def vie(self):
        return self.niveau*20
    
    def capacites(self):
        return self.niveau*5,self.niveau*2,randint(1,4)
    
    def pieces_gagnees(self):
        if self.niveau<5:
            return 100
        if self.niveau>=5:
            return 200
        if self.niveau==10:
            return 500