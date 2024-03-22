# Les conditions sont des outils permettant d'effectuer des instructions
# selon la condition établie auparavant
# C'est comme les intersections sur une route avec un panneau "cedez le passage"
# Si pas de voiture alors --> avance 
# SiNON                   --> attend
# Le panneau est la condition (Si pas de voiture) et les instructions sont avance/attend

def main():
    # enregistrer le prix d'un ordinateur dans une variable
    computer_price = 1000
    # enregistrer le prix du compte bancaire
    wallet = int(input("Entrez le solde votre compte "))
    # afficher si l'achat de l'ordinateur est possible ou non et le solde restant.
    if computer_price <= wallet:
           print("L'achat est possible, il vous restera "+str(wallet-computer_price)+" euros")
    else:
           print("L'achat est impossible, il vous manque "+str(computer_price-wallet)+" euros")
    # afficher la nouvelle valeur du compte si l'achat est possible avec 
    # une condition ternaire
    text = ("Transaction éffectué, votre nouveau solde est de "+str(wallet-computer_price)+" euros" 
            , "Transaction impossible, votre solde est de "+str(wallet)+" euros") [wallet < computer_price]
    print(text)


def Création_compte():
    #enregistrer identifiant et mot de passe ni trop long ni trop court, afficher un bienvenue avec format
    username = input("Entrez votre nom d'utilisateur ")
    password = input("Entrez un mot passe ")
    if len(password) < 9:
        print("Mot de passe trop court ")
    elif len(password) > 16:
        print("Mot de passe trop long")
    else:
        print("Mot de passe enregistré") 
        print("Bienvenue {} inscritption réussie, bienvenue au cinéma GregFilm" .format(username))
   
def Prix_place_GregFilm():
     # Programme qui donne le prix d'une place au cinéma selon l'âge et les supplément
     age = int(input("Quel est votre age ? "))
     prix = ("20" , "10") [age < 18]
     popcorn = input("Voulez vous des popcorn ? ")
     prix = (int(prix)+5 , prix) [popcorn != "oui" ]
     print("Le prix de la place est de {} vous payez par carte ? ".format(prix))


if __name__ == '__main__':
    main()
    Création_compte()
    Prix_place_GregFilm()