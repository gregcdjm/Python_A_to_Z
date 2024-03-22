import json

eleves = {
    'Paul': {
        'note' : 12,
        'appreciation' : 'bon trimestre'
    },
    'gregoire': {
        'note' : 16,
        'appreciation': "tres bien"
    },
    'léo': {
        'note': 18,
        'appreciation' : 'exellent'
    }
}

#print(eleves['paul'])
#
# print(eleves.get("Léa", 'Prenom inconnue'))

#for eleve in  eleves.values():
#    print(eleve)

#print(round(sum(eleves.values())/ len(eleves)))

# ajouter un eleve
#eleves['léa'] = {
#    'note': 10,
#    'appreciation': 'moyen'
#}
# modification note de léo
#eleves['léo']['note'] = 20

# supprimer un eleve
#del eleves['gregoire']

# verifier un eleve existe dans la classe
#if 'léo' in eleves.keys():
#    print("léo est bien dans la classe")

#for eleve, moyenne in  eleves.items():
#    print(f"La moyene de {eleve} est de {moyenne} /20")

#for eleve in eleves:
#    print(eleve, eleves[eleve]['note'], eleves[eleve]['appreciation'])

# sauvegarder notre classe dans un fichier
with open('dictionnaire./dico.json', 'w+') as file:
    json.dump(eleves, file)

