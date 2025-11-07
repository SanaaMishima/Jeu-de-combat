#!/usr/bin/env python
from module_choix import *
from module_ennemi import *
from module_perso import *

class Tour :

    def __init__(self,perso,dicopersoniv,dicopersovie,objets,ennemi):
        self.perso=perso

class TourEnnemi(Tour):
    
    def __init__(self, perso, dicopersoniv, dicopersovie, objets, ennemi):
        super().__init__(perso, dicopersoniv, dicopersovie, objets, ennemi)

class TourPerso(Tour):

    def __init__(self, perso, dicopersoniv, dicopersovie, objets, ennemi):
        super().__init__(perso, dicopersoniv, dicopersovie, objets, ennemi)
