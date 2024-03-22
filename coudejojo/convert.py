def convert_to_pouce():
    while(1):
        cm = input("Entrez votre valeur à convertir en pouce : ")
        try: 
            cm = float(cm)
        except:
            print("Error: entrer un nombre seulement")
            continue
        else:
            if cm < 0:
                print("Error: une distance ne peut être inférieur à 0")
                continue
            pouce = cm*2.54
            print(f"{pouce} pouce")
            break


def convert_to_cm():
    while(1):
        pouce = input("Entrez votre valeur à convertir en pouce : ")
        try:
            pouce = float(pouce)
        except:
            print("Error: entrer un nombre seulement")
            continue
        else:
            if pouce < 0:
                print("Error: une distance ne peut être inférieur à 0")
                continue
            cm = pouce/2.54
            print(f"{cm} cm")
            break
            

while(1):
    quoi = input("Taper l'unité de la valeur à convertir cm ou pouce ")
    if quoi == "cm":
       convert_to_pouce()
       break
    elif quoi == "pouce":
       convert_to_cm()
       break
    print("Veuillez taper : cm ou pouce")

