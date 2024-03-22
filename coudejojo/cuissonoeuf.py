import time

print("Cuisson des oeufs\n----------------\na) Oeufs à la coque (3 min)\nb) Oeufs mollets (6 min)\nc) Oeufs dur (9 min)")
timeleft = 0
while(timeleft == 0):
    choose = input("Votre choix : ")
    if choose == "a":
      timeleft = 180
    elif choose == "b":
       timeleft = 360
    elif choose == "c":
       timeleft = 540
    else:
        print("Entrer a,b ou c")
print("Cuisson en cours", end="", flush=True)
while(timeleft > 0):
    for i in range(10):
      time.sleep(1)
      print(".", end="", flush=True)
    timeleft -=10
    min = timeleft//60
    sec = timeleft-min*60
    print(f"\nDurée restante : {min:02d}:{sec:02d}", end="")
print("\nCuisson terminée !")


