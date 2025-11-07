#!/usr/bin/env python
from random import randint

class Ennemi:
    def __init__(self,nom,niveau):
        self.nom=nom
        self.niveau=niveau
        self.etat="bien"
        self.vie=None
        self.attaque=None
        self.defense=None
        self.spe=None
    
    def getNom(self):
        return self.nom
    
    def getVie(self):
        return self.vie

    def getAttaque(self):
        return self.attaque

    def getDefense(self):
        return self.defense

    def getSpe(self):
        return self.spe
    
    def getEtat(self):
        return self.etat
    
    def setEtat(self,new_etat):
        self.etat=new_etat
        return self.etat
    
    
class Gooma (Ennemi): #Ennemi de base, faible vie, attaque et défense, pas de capacité spéciale

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.vie=niveau*5
        self.attaque=niveau*2
        self.defense=0
        self.spe=0
    
    def pieces_gagnees(self): #Pièces que l'on gagne à la fin du combat
        if self.niveau<5:
            return 5
        if self.niveau>=5:
            return 10
        if self.niveau==99:
            return 100
    
class Koupape (Ennemi): #Ennemi ayant une légère défense 

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.vie=niveau*5
        self.attaque=niveau*2
        self.defense=niveau
        self.spe=randint(1,4) #Une chance sur quatre d'utiliser la capacité spéciale

    def setSpe(self):
        self.spe=randint(1,4)
        return self.spe
    
    def pieces_gagnees(self):
        if self.niveau<5:
            return 10
        if self.niveau>=5:
            return 20
        if self.niveau==99:
            return 200

class Masscasse (Ennemi): #Ennemi assez fort, avec beaucoup de vie et a une chance sur trois de s'enfuir

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.vie=niveau*7
        self.attaque=niveau*3
        self.defense=1
        self.spe=randint(1,3)

    def setSpe(self):
        self.spe=randint(1,3)
        return self.spe
    
    def pieces_gagnees(self):
        if self.niveau<5:
            return 50
        if self.niveau>=5:
            return 100
        
class BossBresom (Ennemi): #Boss du jeu, possède des stats élevés

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.vie=niveau*20
        self.attaque=niveau*5
        self.defense=niveau*2
        self.spe=randint(1,4) #Une chance sur quatre d'utiliser la capacité spéciale

    def setSpe(self):
        self.spe=randint(1,4)
        return self.spe
    
    def pieces_gagnees(self):
        if self.niveau<5:
            return 100
        if self.niveau>=5:
            return 200
        if self.niveau==10:
            return 500