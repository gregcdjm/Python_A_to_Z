# Les variables servent d'outil pour enregistrer des informations
# de plusieurs types différents int, char, string etc..
# C'est comme une voiture capable de contenir des humains, des objets etc..

def main():
    # création variable 'username' ayant pour valeur grégoire
    username = "grégoire"
    # création variable 'age' ayant pour valeur 23
    age = 23
    # affiche l'username et l'age
    print(username, age)
    # change la valeur de age par 24
    age += 1 # age = age + 1
    # change la valeur de 'username' par 'coudrin'
    username = "coudrin"
    # affiche la nouvelle valeur de username et de age
    print(username, age)
    # affiche "Bonjour Mr coudrin, vous avez 24 ans le 21 juin 2024"
    # en utilisant la concaténation
    print("Bonjour Mr "+username+", vous avez "+str(age)+ "ans le 21 juin 2024")
    # caster age (int) en char avec str.

def moyenne():
        # moyenne de 3 notes
        # utilisation de input pour enregister dans les variables un chaîne de char depuis la console
        # et afficher un texte sur la console
        note1 = input("Entrez la premierre note ") 
        note2 = input("Entrez la deuxième note ")
        note3 = input("Entrez la troisième note ")
        # calcul de la moyenne
        # conversion des chaînes de char en int pour les additionner
        # int(input("Entr....note")) donne le même résultat à result seul
        # le type des variables 'noteX' est différent
        result = (int(note1)+int(note2)+int(note3))/3
        # affichage de la moyenne
        print("La moyenne est de "+ str(result))

def achat_télévision_500euros():
     # enregistrement de la valeur du compte bancaire en int dans wallet
     wallet = int(input("Entrez votre solde "))
     # calcul du nouveau solde après l'achat de la télévision
     wallet -= 500
     # affichage du nouveau solde
     print("Votre nouveau solde est de "+str(wallet))


if __name__ == '__main__':
    print()
    main()
    moyenne()
    achat_télévision_500euros()
