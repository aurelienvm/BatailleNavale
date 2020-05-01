import numpy as np
import random
from tkinter import *

fregate=1
croiseur=2
sous=3
cuirasse=4
porte=5



def creation(tableau):
    tableau=np.full((10,10),0)
    return(tableau)
    

# Placement aléatoires des 5 bateaux
def placement_aleaEtudiant(damier):
    # Taille des différents bateaux
    Taille_Bateaux=[2,3,3,4,5]
    Nb_Bateaux=len(Taille_Bateaux)

    for Bateau in range(Nb_Bateaux):
        Taille=Taille_Bateaux[Bateau];

        OK=1

        while OK:
            # Choix de coordonnées de départ sur le damier
            L=random.randint(0,9)
            C=random.randint(0,9)

            # Case libre ?
            if damier[L,C]==0:
                # Horizontale = 1 / Verticale = 0
                Orientation=random.randint(0,1)

                # Placement Horizontal
                if Orientation==1:
                    if C+Taille-1<10:
                        if sum(damier[L,C:C+Taille])==0:
                            for n in range(Taille):
                                damier[L,C+n]=Bateau+1 #Numéro du bateau sur le damier
                                OK=0
     
                # Placement Vertical
                else:
                    if L+Taille-1<10:
                        if sum(damier[L:L+Taille,C])==0:
                            for n in range(Taille):
                                damier[L+n,C]=Bateau+1 #Numéro du bateau sur le damier
                                OK=0
    return(damier)
    
# Placement manuel des 5 bateaux
def placement_manuel(damier):
    # Taille des différents bateaux
    Taille_Bateaux=[2,3,3,4,5]
    Nb_Bateaux=len(Taille_Bateaux)

    for Bateau in range(Nb_Bateaux):
        Taille=Taille_Bateaux[Bateau];

        OK=1

        while OK:
            print("On place le bateau",Bateau+1,"d'une longueur de",Taille,"cases")
            # Choix de coordonnées de départ sur le damier
            L=int(input("Entrez une valeur de ligne entre 0 et 9 :"))
            C=int(input("Entrez une valeur de colonne entre 0 et 9 :"))

            # Case libre ?
            if damier[L,C]==0:
                # Horizontale = 1 / Verticale = 0
                Orientation=int(input("Entrez une orientation 1 pour Horizontal et 0 pour vertical :"))

                # Placement Horizontal
                if Orientation==1:
                    if C+Taille-1<10:
                        if sum(damier[L,C:C+Taille])==0:
                            for n in range(Taille):
                                damier[L,C+n]=Bateau+1 #Numéro du bateau sur le damier
                                OK=0
                        else:
                            print("Case(s) occupée(s)")
                # Placement Vertical
                else:
                    if L+Taille-1<10:
                        if sum(damier[L:L+Taille,C])==0:
                            for n in range(Taille):
                                damier[L+n,C]=Bateau+1 #Numéro du bateau sur le damier
                                OK=0
                        else:
                            print("Case(s) occupée(s)")
            else:
                print("Case occupée")
    return(damier)

#Tour du joueur 
def bombe_joueur(Tableau_Ordi,Tableau_touche_Joueur, bateau_pc):
    nbtir=0
    fin=False
    while nbtir !=3:
        colonne_tir=int(input("Sur quelle colonne voulez-vous tirer ? :"))
        ligne_tir=int(input("Sur quelle ligne voulez-vous tirer ? :"))
        nbtir=nbtir+1
        if Tableau_Ordi[colonne_tir, ligne_tir] !=0:
            print("Touché !")
            Tableau_touche_Joueur[colonne_tir, ligne_tir]=9
            bateau_pc=bateau_pc-1
            if(bateau_pc==0):
                fin=True
        else:
            print("A l'eau !")
            Tableau_touche_Joueur[colonne_tir, ligne_tir]=8
    
    return fin
    
#Tour de l'ordinateur
def bombe_bot(Tableau_Joueur,Tableau_touche_Ordi, bateau_joueur):
    nbtir=0
    fin=False
    while nbtir !=3:
        colonne_tir=random.randint(0,9)
        ligne_tir=random.randint(0,9)
        nbtir=nbtir+1
        if Tableau_Joueur[colonne_tir, ligne_tir] !=0:
            print("touché")
            Tableau_touche_Ordi[colonne_tir, ligne_tir]=9
            bateau_joueur=bateau_joueur-1
            if (bateau_joueur==0):
                fin=True
        else:
            print("à l'eau")
            Tableau_touche_Ordi[colonne_tir, ligne_tir]=8
    
    return fin
    



#Programme principal

bateau_pc=17
bateau_joueur=17

Tableau_Joueur=[]
Tableau_Joueur = creation(Tableau_Joueur)

Tableau_Ordi=[]
Tableau_Ordi = creation(Tableau_Ordi)

Tableau_touche_Ordi=[]
Tableau_touche_Ordi = creation(Tableau_touche_Ordi)

Tableau_touche_Joueur=[]
Tableau_touche_Joueur = creation(Tableau_touche_Joueur)

#Question à l'utilisateur (mode jeu)
bool = False
while bool == False:
    choix=int(input("Entrez choix entre 1 (Aléatoire) et 2 (Manuel) :"))
    if choix == 1 or choix == 2:
        bool = True 

if choix==1:
    Tableau_Joueur=placement_aleaEtudiant(Tableau_Joueur)
elif choix==2:
    Tableau_Joueur=placement_manuel(Tableau_Joueur)

Tableau_Ordi=placement_aleaEtudiant(Tableau_Ordi)

print(Tableau_Joueur)

#Permet de jouer tant que tous les bateaux ne sont pas coulés.
fin=False
while (fin==False):
    print(Tableau_touche_Ordi)
    print(Tableau_touche_Joueur)
    fin=bombe_joueur(Tableau_Ordi,Tableau_touche_Joueur, bateau_pc)
    print(Tableau_touche_Joueur)
    fin=bombe_bot(Tableau_Joueur,Tableau_touche_Ordi, bateau_joueur)







# 
# print(Tableau_touche_Ordi)
# print(Tableau_touche_Joueur)
# fin=bombe_joueur(Tableau_Ordi,Tableau_touche_Joueur, bateau_pc)
# print(Tableau_touche_Joueur)
# fin=bombe_bot(Tableau_Joueur,Tableau_touche_Ordi, bateau_joueur)
# print(Tableau_touche_Ordi)
# print(Tableau_Joueur)
