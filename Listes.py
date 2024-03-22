import statistics
import random

# Les listes sont un peu comme des variables capable d'enregistrer plusieur valeurs (dit "éléments")
# rangé par un index commençant par 0, il est ansi possible de rajouter/extraire/trier
# les éléments qu'on shouaite et aussi d'éffectuer des opérations entre plusieurs liste.
# C'est comme un peu un dossier qui contient les immatriculations des voitures.


def main():
    # Création d'une liste contenant les noms des clients du cinéma GregFilm indexés sur leur numéro de place.
    user_name_GregFilm = ["Obiwan Kenobi", "Anakin Skywalker", "Palpatine"]
    print("Les clients du cinéma sont {}, voulez-vous en rajouter un ?".format(user_name_GregFilm))
    # Afficher le 1er élément et le dernier élément de la liste de façon générique
    print("Le premier inscrit est {} le dernier inscrit est {} "
          .format(user_name_GregFilm[0] , user_name_GregFilm[len(user_name_GregFilm) - 1]))
    # Ajouter un client à l'index donné
    new_comer = input("Voulez-vous échanger un client avec un nouveau client ? ")
    if new_comer == "oui":
        new_comer = input("Entrez son nom : ")
        index_client = int(input("Entrez sa place : "))
        user_name_GregFilm[index_client] = new_comer
        print("La nouvelle liste est "+str(user_name_GregFilm))
    # Mélanger la liste de façon aléatoire puis l'afficher de nouveau
    random.shuffle(user_name_GregFilm)
    print(user_name_GregFilm)
    # Ajouter plusieurs clients qui se suivent
    # tout ça pour dire qu'il faut utiliser name_list.append("new_client") 
    # ou name_list.extend(["new_client_1" , "new_client_2"])

    delete = input("Voulez-vous effacer la liste des clients ?")
    if "oui" == delete:
        user_name_GregFilm.clear() # del list_name[:] marche aussi

# faite la moyenne et afficher les prix des places d'une liste avec le module statistic.

def mean_price_sit():
    list_of_price = [15 , 16 , 20 ,
                     25 , 15 , 10 , 10 
                     , 10 , 25 , 25]
    print("La moyenne des prix des places est de "+str(statistics.mean(list_of_price))+" euros")


if __name__ == '__main__':
    main()
    mean_price_sit()