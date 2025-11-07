#!/usr/bin/env python
from random import randint
class Choix:

    def __init__(self):
        self.choix=[1,2,3,4,5,6]

    def getChoix(self):
        return self.choix

    def choix():
        print("1: Attaquer")
        print("2: Défendre")
        print("3: Objets [4: Voir la liste des objets]")
        print("5: Changer de personnage")
        print("6: Fuir")
        choix=int(input())
        return choix

    def attaque(ptattaque):
        decision=int(input("Miser ? 1:Oui 2:Non "))
        if decision==1:
            mise=int(input("Miser sur quel chiffre ? (entre 1 et 6) "))
            while mise>6 or mise<1:
                mise=int(input("Miser sur un seul chiffre entre 1 et 6"))
            tirage=randint(1,6)
            if mise==tirage:
                print("Jackpot ! Votre puissance d'attaque est doublée")
                ptattaque*=2
            elif mise+4<=tirage:
                print("Perdu ! Votre puissance d'attaque est divisée par deux")
                ptattaque/=2
                ptattaque=int(ptattaque)
            else:
                print("Vous n'avez ni gagné, ni perdu... Votre puissance d'attaque ne change pas")
        if ptattaque<1:
            ptattaque=0
        return ptattaque

    def defense(ptdefense):
        decision=int(input("Miser ? 1:Oui 2:Non "))
        if decision==1:
            mise=int(input("Miser sur quel chiffre ? (entre 1 et 6) "))
            while mise>6 or mise<1:
                mise=int(input("Miser sur un seul chiffre entre 1 et 6"))
            tirage=randint(1,6)
            if mise==tirage:
                print("Jackpot ! Votre défense est doublée")
                ptdefense*=2
            elif mise+4<=tirage:
                print("Perdu ! Votre défense est divisée par deux")
                ptdefense/=2
            else:
                print("Vous n'avez ni gagné, ni perdu... Votre défense ne change pas")
        if ptdefense<1:
            ptdefense=0
        return ptdefense

    def objets(objet):
        print("Quel objet voulez-vous utiliser ?")
        d=[]
        for i in range (1,len(objet)+1):
            print(i,":",objet[i-1])
            d.append(i)
        ch=int(input())
        while ch not in d:
            print("Vous n'avez choisi aucun des objets proposés... Rechoisissez")
            for i in range (1,len(objet)+1):
                print(i,":",objet[i-1])
            ch=int(input())
        obj=objet[int(ch)-1]
        objet.remove(obj)
        return obj

    def chgtperso(dicopersoniv,dicopersovie,perso,vieperso):
        print("Quel personnage choisissez-vous ?")
        dico={}
        a=1
        dicopersovie[perso]=vieperso
        for i in dicopersoniv.keys():
            print(a,":",i,",",dicopersovie[i],"pv")
            dico[a]=i
            a+=1
        choix=int(input())
        p=dico[choix]
        while dicopersovie[p]==0:
            print("Le personnage que vous avez choisi n'a plus de vie... Choisissez un autre personnage")
            a=1
            for i in dicopersoniv.keys():
                print(a,":",i,",",dicopersovie[i],"pv")
                a+=1
            choix=int(input())
            p=dico[choix]
        return p,dicopersoniv[p],dicopersovie[p]

    def fuir(nivperso,nivennemi,ennemi):
        print("Vous tentez de fuir")
        tirage=randint(1,6)
        input("...")
        if ennemi=="Boss bresom":
            print("Vous ne pouvez pas fuir !")
            return 0
        if tirage>=5:
            print("Vous réussissez à fuir !")
            return 1
        if tirage>=3 and nivperso>nivennemi+5:
            print("Vous réussissez à fuir !")
            return 1
        if tirage<3:
            print("Vous n'arrivez pas à fuir...")
            return 0






