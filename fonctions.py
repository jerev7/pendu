"""Ce fichier définit des fonctions utiles pr le programme pendu.
On utilise les données du programme contenues dans donnee.py"""

import os
import pickle
from random import choice

from donnee import *

#Gestion des scores

def recup_scores():
	"""Cette fonction récupère les scores enregistrés si le fichier existe.
	Dans tous les cas, on renvoie un dictionnaire,
	soit l'objet dépicklé, soit un dictionnaire vide.

	On s'appuie sur nom_fichier_scores défini dans donnee.py"""

	if os.path.exists(nom_fichier_scores): # Le fichier existe
		#On le récupère
		fichier_scores = open(nom_fichier_scores, "rb")
		mon_depickler = pickle.Unpickler(fichier_scores)
		scores = mon_depickler.load()
		fichier_scores.close()
	else: #le fichier n'existe pas
		scores = {}
	return scores

def enregistrer_scores(scores):
	"""Cette fonction se charge d'enregistrer les scores dans le fichier nom_fichier_scores. Elle reçoit en paramètre le dictionnaire des scores à enregistrer."""

	fichier_scores = open(nom_fichier_scores, "wb") #On écrase le anciens scores à enregistrer"""
	mon_pickler = pickle.Pickler(fichier_scores)
	mon_pickler.dump(scores)
	fichier_scores.close()

#Fonctions gérant les éléments saisi par l'utilisateur

def recup_nom_utilisateur():
	"""Fonction chargée de récupérer le nom de l'utilisateur.
	Le nom de l'utilisateur doit être composé de 4 caractères minimum, chiffres et lettres exclusivement.
	Si ce nom n'est pas valide, on appelle récursivement la fonction pour en obtenir un nouveau"""

	nom_utilisateur = input("Tapez votre nom (4 caractères minimum): ")
	nom_utilisateur = nom_utilisateur.capitalize()
	if not nom_utilisateur.isalnum() or len(nom_utilisateur)<4:
		print("Ce nom est invalide.")
		return recup_nom_utilisateur()
	else:
		return nom_utilisateur

def recup_lettre():
	"""Cette fonction récupère une lettre saisie par l'utilisateur. Si la chaîne récupérée n'est pas une lettre, on appelle récursivement la fonction jusqu'à obtenir une lettre"""

	lettre = input("Tapez une lettre: ")
	lettre = lettre.lower()
	if len(lettre)>1 or not lettre.isalpha():
		print("Vous n'avez pas saisi une lettre valide.")
		return recup_lettre()
	else:
		return lettre

# Fonctions du jeu de pendu

def choisir_mot():
	"""Cette fonction renvoie le mot choisi dans la liste des mots liste_mots.
	On utilise la fonction choice du module random."""

	return choice(liste_mots)

def recup_mot_masque(mot_complet, lettres_trouvees):
	"""Cette fonction renvoie un mot masqué tout ou en partie, en fonction :
	- du mot d'origine (type str)
	- des lettres déjà trouvées (type list)
	On renvoie le mot d'origine avec des * remplaçant les lettres que l'on a déjà trouvées."""

	mot_masque = ""
	for lettre in mot_complet:
		if lettre in lettres_trouvees:
			mot_masque += lettre
		else:
			mot_masque += "*"
	return mot_masque