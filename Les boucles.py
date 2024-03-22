# Les boucles (While, for) sont des outils permettant de répéter des instructions en boucle jusqu'à/tant que
# la condition(While) ou l'initialisation(For) soit remplie.
# C'est comme un rond point qui fait tourner les voitures en boucle jusqu'à ce qu'elles trouvent leur chemin.
# Attention à ne pas définir une variable dans une boucle (à part si vous voulez qu'elle soit rénitialisée)
# pour chaque boucle.

def main():

    # Enregistrez la liste des utilisateurs du cinéma avec while comprenant une blacklist

    again = 1
    list_user = []
    black_list = []
    while(again == 1):
        new_or_no = input("Voulez vous rajouter un client ? ")      
        if new_or_no == "oui":
            list_user.append(input("Entre le nom du nouveau client : "))
            black_list_yes_or_no = input("Voulez vous qu'il soit dans la blackList ? ")
        else:
            again = 2
        if  new_or_no == "oui" and black_list_yes_or_no == "oui":
            black_list.append(list_user[len(list_user )- 1])       
        print(list_user)
        print(black_list)

    # Envoyez un email aux clients de la liste avec for (prendre en compte la BL)

    for email in list_user:
        if email in black_list:
            print("Email impossible à envoyer "+email+" est dans la blaclist ! ")
            continue 

        # "Continue" permet de passer à la prochaine boucle sans effectuer les instructions
        # suivantes (comme ci-dessous)

        print("Email envoyé à : ", email)

# Les fonctions récursives (qui s'appellent elles-mêmes dans leurs définitions) peuvent servir
# aussi à faire des boucles donnant le résultat à l'envers ! On parle de pile (stack) rangé dans l'ordre puis
# sortie dans l'ordre inverse, il y a une phase de remplissage (de First-in à Last-in) de la pile
# puis le sommet de la pile (last-in/First-out) puis la phase de vidage (de First-out à last-out).
# faire attention de ne pas définir une variable à l'intérieur de la fonction (elle sera rénitialisée à chaque fois)
# Faire un fonction récursive qui calcule la recette de la journée

def win_of_the_day(n):

    # Voici la phase 'First-in'jusqu'à 'Last-in', les éléments ici rentrent dans l'ordre dans la pile

    n += int(input("Entrez la recette du client(s) : "))
    stop = input("Suivant ? ")

    # On observe avec ce print que chaque élément rentre chacun leur tour

    print("Phase de remplissage (First-in à Last-in) "+str(n))

    # Voici la condition de sortie délimitant les phases de 'First-in à Last-in' et 'first-out à Last-out'

    if stop == "oui":
        win_of_the_day(n)
    else:

        # Voici La toute dérnière instruction de la phase de remplissage, c'est le 'Last-in'
        # utile pour renvoyer le résultat d'un calcul précédent (return n)
        # On le retrouve dans le 'else' de la condition de sortie

        print("Le sommet de la pile le Last-in First-out ")

    # Voici la phase 'Last

    print("Phase de vidage (First-out Last-out) (win_of_the_day) "+str(n))
    return n
    
    
if __name__ == '__main__':
    main()
    a = win_of_the_day(0)
    print("Voilà la dernière valeur de n "+str(a))