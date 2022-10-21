from newspaper import Article  # Pour l'extraction d'article
import random
import nltk  # pour le traitement des textes
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np  # pour les calculs nueriques
import warnings

warnings.filterwarnings('ignore')
"""Nous allons telecharger le packkage punktse trouvant  qui permettra de diviser 
un texte en phrases"""
nltk.download('punkt', quiet=True)
"""Relions maintenant le lien de notre article à notre programme on le telecharge et on 
l'envoie sous format texte"""
article = Article("https://fr.wikipedia.org/wiki/Maladie_%C3%A0_coronavirus_2019")
article.download()
article.parse()  # pour analyser notre article
article.nlp()
collection = article.text
texte = collection
liste_texte = nltk.sent_tokenize(texte)  # pour decomposer notre artccle en une liste de phrases suivant sa structure


# Nous allons definir une fonction qui retourne une salutation
def salutations(texte):
    texte = texte.lower()
    robots = ['salam', 'salut', 'bonjour', 'comment allez-vous?','Que puis je faire pour vous ?']
    utilisateur = ['salam', 'salut', 'bonjour', 'yo']
    etat_de_sante= ['Je vais bien et vous ? ','Hamdulilah']
    question = ['cava','comment vas-tu','bien']

    for i in texte.split():  # split pour diviser notre texte en liste de chaque mot
        if i in utilisateur:
            return random.choice(robots)  # Pour générer une réponse aléatoire du robot choisit dans la liste Robot
        if i in question :
            return random.choice(etat_de_sante)


# La reponse du robot
def tri_index(list_var):
    taille = len(list_var)
    index_liste = list(range(0, taille))
    x = list_var
    for i in range(taille):
        for j in range(taille):
            if x[index_liste[i]] > x[index_liste[j]]:
                change = index_liste[i]
                index_liste[i] = index_liste[j]
                index_liste[j] = change
    return index_liste


def reponses_du_robot(user_input):
    user_input = user_input.lower()
    liste_texte.append(user_input)
    reponses_du_robot = ''
    cmp = CountVectorizer().fit_transform(liste_texte)
    simularite = cosine_similarity(cmp[-1], cmp)  # Comparer la dernière phrase saisie pour la comparer à la matrice
    similarite_liste = simularite.flatten()
    index = tri_index(similarite_liste)
    index = index[1:]
    reponse_comptage = 0
    j = 0
    for i in range(len(index)):
        if similarite_liste[index[i]] > 0.0:
            reponses_du_robot = reponses_du_robot + ' ' + liste_texte[index[i]]
            reponse_comptage += 1
            j = j + 1
        if j > 6:
            break
    if reponse_comptage == 0:
        reponses_du_robot = reponses_du_robot + ' ' + "Je suis vraiment désolé pour vous !"
    liste_texte.remove(user_input)
    return reponses_du_robot


print('Robot : Je suis là pour vous servir ')
quitter=['bye','au revoir', 'merci','A la prochaine','chukrane']

while(True):
    user_input = input("Moi :")
    if user_input.lower() in quitter :
        print('Robot : A la prochaine')
        break
    else:
        if salutations(user_input) !=None :
            print('Robot : '+ salutations(user_input))
        else:
            print('Robot : '+ reponses_du_robot(user_input))
