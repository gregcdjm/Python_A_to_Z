import random
import os
import time

number_to_memo = str(random.randint(1000, 9999))
score = 0
while 1:
    print("Retenez la séquence : "+number_to_memo)
    time.sleep(3)
    os.system('cls')
    answer = str(input("Votre réponse : "))
    os.system('cls')
    if answer != number_to_memo:
        break
    score += 1
    print("Bonne réponse !\nVotre score est de "+str(score))
    number_to_memo += str(random.randint(0, 9))
print("Vous avez perdu !\nVotre score final est de "+str(score))