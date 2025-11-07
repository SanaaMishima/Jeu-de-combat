#!/usr/bin/env python
from random import randint

class Perso:
    
    def __init__(self, nom, niveau):
        self.nom=nom
        self.niveau=niveau
        self.etat="bien"
        self.vie=None
        self.attaque=None
        self.defense=None
        self.spe=None

    def personnages(dico_perso_vie):
        return list(dico_perso_vie.keys())
    
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
    


class MarioPasPeur(Perso): #Personnage principal équilibré

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.vie=niveau*10
        self.attaque=niveau*3
        self.defense=niveau*2
        self.spe=0


class Pitch(Perso): #Personnage de défense ayant peu de vie mais plutôt équilibré

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.vie=niveau*5
        self.attaque=niveau*2
        self.defense=niveau*3
        self.spe=randint(1,4) #Une chance sur quatre d'utiliser la capacité spéciale du personnage


class Bouser(Perso): #Personnage d'attaque qui a beaucoup de vie, fait beaucoup de dégâts, peut brûler, mais peu de défense

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.vie=niveau*15
        self.attaque=niveau*4
        self.defense=niveau
        self.spe=randint(1,4) #Une chance sur quatre d'utiliser la capacité spéciale du personnage


class Hoshi(Perso): #Personnage troll qui a une chance sur deux d'éviter tous les dégâts

    def __init__(self, nom, niveau):
        super().__init__(nom, niveau)
        self.vie=niveau
        self.attaque=niveau/2
        self.defense=0
        self.spe=randint(1,2) #Une chance sur deux d'utiliser la capacité spéciale du personnage
