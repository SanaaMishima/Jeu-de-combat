#!/usr/bin/env python
import os

def init_sauvegarde():
    print("Avant de commencer, entrez votre nom d'utilisateur")
    nom=input('Nom : ')
    path=nom+'.txt'
    if os.path.exists(path):
        print("Une sauvegarde portant le nom '"+path+"' existe déjà")
        choix=input("Est-ce le votre ? Taper oui ou non ")
        choix=choix.lower()
        if choix=='non':
            while os.path.exists(path):
                print("Entrez un autre nom d'utilisateur")
                nom=input("Nom : ")
                path=nom+'.txt'
    else :
        f=open(path,'x')
        f.close()
    return path

def sauvegarde():
    print("Entrez votre nom d'utilisateur pour accéder à votre sauvegarde")
    nom=input("Nom : ")
    path=nom+'.txt'
    if not os.path.exists(path):
        print("Il n'existe aucune sauvegarde portant le nom '"+path+"'")
        choix=input("Avez-vous commencé une partie ? Taper oui ou non ")
        choix=choix.lower()
        if choix=='oui':
            while not os.path.exists(path) and choix!='non':
                print("Voici toutes les sauvegardes de ce jeu :")
                for i in os.listdir('./'):
                    if i.endswith('.txt'):
                        print(os.path.join('./', i))
                print("Quelle est votre sauvegarde ?")
                print("Si votre sauvegarde n'apparait pas, taper non")
                nom=input("Nom : ")
                path=nom+'.txt'
                choix=nom.lower()
        if choix=='non':
            print("Ceci n'est pas le début de ce jeu, commencer une partie avec le 'premier_chapitre'")
            return()
    return path
