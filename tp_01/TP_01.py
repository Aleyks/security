alphabet = [chr(i) for i in range(65, 91)]  # alphabet en majuscules
alphabet.append(' ')
alphabet.append('\'')
alphabet.append('.')


# print(alphabet)


D = {}

# Construire le dictionnaire pour inclure tous les caractères de l'alphabet
for c in range(len(alphabet)):
    D[alphabet[c]] = c

def encode(texte):
    code = []
    for i in texte:
        code.append(alphabet.index(i))
    return code

def encode_dic(texte):
    code = []
    for i in texte:
        code.append(D[i])
    return code


def decode(code):
    texte = []
    for n in code:
        texte.append(alphabet[n])
    return ''.join(texte)

print(D)


def chiffre_cesar(texte, cle):
    return decode([(n + cle) % 29 for n in encode(texte)])

def dechiffre_cesar(texte, cle):
    return chiffre_cesar(texte, (29 - cle) % 29)



texte = "HELLO WORLD."



code = encode(texte)
print("Encodage avec la fonction encode:", code)


code_dic = encode_dic(texte)
print("Encodage avec la fonction encode_dic:", code_dic)


clef_test = 20
texte_chiffre = chiffre_cesar(texte, clef_test)
print("Texte chiffré avec la clé {}: {}".format(clef_test, texte_chiffre))

#
texte_dechiffre = dechiffre_cesar(texte_chiffre, clef_test)
print("Texte déchiffré avec la clé {}: {}".format(clef_test, texte_dechiffre))







### on peut essayer toutes les clefs jusqu'à tomber sur celle qui affiche un texte lisible 
def trouver_cle(texte_chiffre):
    for clef in range(29):
        texte_dechiffre = dechiffre_cesar(texte_chiffre, clef)
        print(f"Clé {clef}: {texte_dechiffre}")
        
        
# trouver_cle(texte_chiffre)

        
        
# d'après le résultat sur le terminal ( voir resultat_terminal.png ), 3 est la clef
clef_trouve = 3


with open('enc_cesar.txt', 'r') as file:
    texte_chiffre = file.read().strip()
    
def lettre_la_plus_frequente(texte):
    
    frequences = {}
    
    
    for c in texte:
        if c in frequences:
            frequences[c] += 1
        else:
            frequences[c] = 1
    
    
    lettre_max = max(frequences, key=frequences.get)
    
    return lettre_max    
    
lettre_frequente = lettre_la_plus_frequente(texte_chiffre)
print("La lettre la plus fréquente est:", lettre_frequente)
## La lettre la plus frequente est A, qui correspond à la 3eme lettre dans le classement des lettres les plus féquentes de notre alphabet personnalité, on peut donc essayer la clef 3 pour déchiffrer le texte
    

texte_dechiffre = dechiffre_cesar(texte_chiffre, clef_trouve)
print("Texte déchiffré avec la clé {}: {}".format(clef_trouve, texte_dechiffre))


    

#
def chiffre_affine(texte, a, b):
    m = len(alphabet)  
    code = encode(texte)
    texte_chiffre = [(a * n + b) % m for n in code]
    return decode(texte_chiffre)


def dechiffre_affine(texte, a, b):
    m = len(alphabet)  
    inverse_mod = pow(a, -1, m)  
    code = encode(texte)
    texte_dechiffre = [(inverse_mod * (n - b)) % m for n in code]
    return decode(texte_dechiffre)

# 6:  → Vérifier que le chiffré de INFORMATIQUE par la clé (𝑎 = 13, 𝑏 = 12) est AHTUBXM'ARLG, puis que le déchiffrement se déroule correctement.


texte = "INFORMATIQUE."
a = 13  
b = 12  

texte_chiffre = chiffre_affine(texte, a, b)
print(f"Texte chiffré: {texte_chiffre}")

texte_dechiffre = dechiffre_affine(texte_chiffre, a, b)
print(f"Texte déchiffré: {texte_dechiffre}")

### resultat terminal
#### Texte chiffré: AHTUBXM"ARLG.
#####Texte déchiffré: INFORMATIQUE.




with open('enc_affine.txt', 'r') as file:
    texte_chiffre_affine = file.read().strip()
    
    
    
    

    
    
from collections import Counter

# https://tedboy.github.io/python_stdlib/generated/generated/collections.Counter.most_common.html

def deux_plus_frequents(texte):
    # Compter la fréquence des caractères
    frequences = Counter(texte)
    # Trouver les deux caractères les plus fréquents
    deux_plus_frequents = frequences.most_common(2)
    return [c for c, count in deux_plus_frequents]






print("Les deux caractères les plus fréquents sont:", deux_plus_frequents(texte_chiffre_affine))





def retrouver_cle_affine(car_frequente_1, car_frequente_2, car_frequence_alphabet_1, car_frequence_alphabet_2):
    m = len(alphabet)  
    
    # calcule équations à deux inconnues d'après le pdf
    y1, y2 = D[car_frequente_1], D[car_frequente_2]
    x1, x2 = D[car_frequence_alphabet_1], D[car_frequence_alphabet_2]
    
    a = ((y1 - y2) * pow((x1 - x2), -1, m)) % m
    
    
    b = (y1 - a * x1) % m
    
    return a, b

 
 
# Les deux caractères les plus fréquents dans le texte chiffré
car_frequente_1, car_frequente_2 = "\'", 'T'

# les 2 caractères les plus fréquents dans l'alphabet d'après le classement du pdf
car_frequence_alphabet_1, car_frequence_alphabet_2 = ' ', 'E'

a, b = retrouver_cle_affine(car_frequente_1, car_frequente_2, car_frequence_alphabet_1, car_frequence_alphabet_2)




# Déchiffrer le texte avec les clés retrouvées
texte_chiffre_affine = dechiffre_affine(texte_chiffre_affine, a, b)
print(f"Texte déchiffré: {texte_chiffre_affine}") 


""" Texte déchiffré: UN LOGICIEL LIBRE EST UN LOGICIEL DONT L'UTILISATION L'ETUDE LA MODIFICATION ET LA DUPLICATION PAR AUTRUI EN VUE DE SA DIFFUSION SONT PERMISES TECHNIQUEMENT ET JURIDIQUEMENT CECI AFIN DE GARANTIR CERTAINES LIBERTES INDUITES DONT LE CONTROLE DU PROGRAMME PAR L'UTILISATEUR ET LA POSSIBILITE DE PARTAGE ENTRE INDIVIDUS.CES DROITS PEUVENT ETRE SIMPLEMENT DISPONIBLES  CAS DU DOMAINE PUBLIC  OU BIEN ETABLIS PAR UNE LICENCE DITE  LIBRE  BASEE SUR LE DROIT D'AUTEUR. LES  LICENCES COPYLEFT  GARANTISSENT LE MAINTIEN DE CES DROITS AUX UTILISATEURS MEME POUR LES TRAVAUX DERIVES.LES LOGICIELS LIBRES CONSTITUENT UNE ALTERNATIVE A CEUX QUI NE LE SONT PAS QUALIFIES DE  PROPRIETAIRES  OU DE  PRIVATEURS . CES DERNIERS SONT ALORS CONSIDERES PAR UNE PARTIE DE LA COMMUNAUTE DU LOGICIEL LIBRE COMME ETANT L'INSTRUMENT D'UN POUVOIR INJUSTE EN PERMETTANT AU DEVELOPPEUR DE CONTROLER L'UTILISATEUR.  """


####################################### EXERCICE 2 ##########################################


# Alphabet in uppercase for Vigenère cipher
alphabet_vig = [chr(i) for i in range(65, 91)]  

# print(alphabet_vig)


def IC(texte, longueur):
    
    somme = lambda nb : nb * (nb - 1)
    IC = []
    for i in range (longueur):
        nb_lettre = [0] * 26
        for compteur, lettre in enumerate(texte [i::longueur]):
            nb_lettre [ord(lettre)- 65] += 1
        IC.append(sum(map(somme, nb_lettre)) / float(compteur * (compteur + 1)))
    return sum(IC) / float(len(IC))


def calcule_longeur_cle(texte):
    """ l'indice de coincidence d'un texte en français est de 0.078, donc en testant plusieurs tailles de texte de longeur N clef on peut trouver la longeur de la clef probable si elle depasse 0.06 """
 
 
 
    for i in range(1, 20):
        IC_vig = IC(texte, i)
        if IC_vig > 0.06:
            return i
        




def calcul_frequence_lettres(texte):
    frequence = [0] * 26
    total_lettres = 0
    
    for lettre in texte:
        if lettre.isalpha():  
            index = ord(lettre.upper()) - ord('A')
            frequence[index] += 1
            total_lettres += 1

    
    return lettre



def calcule_decalage_vigenere(texte_chiffre, taille_clef):
    """
    Calcule les décalages probables pour chaque sous-texte en fonction de la taille de la clé.
    """
    # Créer les sous-textes en fonction de la taille de la clé
    sous_textes = ['' for _ in range(taille_clef)]
    for i in range(len(texte_chiffre)):
        sous_textes[i % taille_clef] += texte_chiffre[i]
    
    #
    decalages = []
    
    
    for i in range(taille_clef):
        decalage = calcule_decalage(sous_textes[i])  
        decalages.append(decalage)
    
    return decalages


def calcule_decalage(sous_texte):
    """
    Calcule le décalage probable d'un sous-texte en utilisant les fréquences des lettres.
    """
    
    frequence_lettre = Counter(sous_texte)
    lettre_plus_frequente = frequence_lettre.most_common(1)[0][0]
    
    # vu que c'est un texte français on va decaler la lettre la plus frequente
    decalage = (ord(lettre_plus_frequente) - ord('E')) % 26
    return decalage




def attaque_vigenere(message, decalages):
    """
    Déchiffre un message chiffré avec Vigenère en utilisant les décalages trouvés.
    """
    taille_clef = len(decalages)  # Longueur de la clé
    texte_dechiffre = []
    
    for i, lettre in enumerate(message):
        # Trouver le décalage correspondant à la position actuelle
        decalage = decalages[i % taille_clef]
        
        # Appliquer le décalage inverse pour déchiffrer la lettre
        lettre_dechiffree = chr((ord(lettre) - ord('A') - decalage) % 26 + ord('A'))
        
        # Ajouter la lettre déchiffrée au texte
        texte_dechiffre.append(lettre_dechiffree)
    
    return ''.join(texte_dechiffre)




##### Déchiffrer les textes chiffrés avec Vigenère ########




with open('file2_enc.txt', 'r') as file:
    file2_chiffre_vigenere = file.read().strip()
    
with open('file3_enc.txt', 'r') as file:
    file3_chiffre_vigenere = file.read().strip()

with open('file4_enc.txt', 'r') as file:
    file4_chiffre_vigenere = file.read().strip()


texte_chiffre_1 = file2_chiffre_vigenere
texte_chiffre_2 = file3_chiffre_vigenere
texte_chiffre_3 = file4_chiffre_vigenere


print(f"la longeur de la clef pour le texte 1 est surement ", calcule_longeur_cle(texte_chiffre_1))
print(f"la longeur de la clef pour le texte 2 est surement ", calcule_longeur_cle(texte_chiffre_2))
print(f"la longeur de la clef pour le texte 3 est surement ", calcule_longeur_cle(texte_chiffre_3))



taille_clef_1 = calcule_longeur_cle(texte_chiffre_1)
taille_clef_2 = calcule_longeur_cle(texte_chiffre_2)
taille_clef_3 = calcule_longeur_cle(texte_chiffre_3)


decalages_1 = calcule_decalage_vigenere(texte_chiffre_1, taille_clef_1)
decalages_2 = calcule_decalage_vigenere(texte_chiffre_2, taille_clef_2)
decalages_3 = calcule_decalage_vigenere(texte_chiffre_3, taille_clef_3)

print("Décalages pour le texte 1:", decalages_1)
print("Décalages pour le texte 2:", decalages_2)
print("Décalages pour le texte 3:", decalages_3)


texte_dechiffre_1 = attaque_vigenere(texte_chiffre_1, decalages_1)
texte_dechiffre_2 = attaque_vigenere(texte_chiffre_2, decalages_2)
texte_dechiffre_3 = attaque_vigenere(texte_chiffre_3, decalages_3)

print("Texte déchiffré 1:", texte_dechiffre_1)
print("Texte déchiffré 2:", texte_dechiffre_2)
print("Texte déchiffré 3:", texte_dechiffre_3)  
# affiche le dernier rend les résultats des tests précédents illisibles mais ça fonctionne








