from Les_objets_sur_python.playermodel import SuperPlayer

# Voici ici un exemple d'un héritage. Un héritage est la copie d'une classe (parent) à une autre 
# classe (son fils) 
class Gladiator (SuperPlayer):
        def __init__(self, pseudo , health, attack):
            super().__init__(pseudo, health, attack)
            self.armor = 3                    
        def damage(self, damage):   
            if self.armor > 0:
                self.armor -= 1
                damage = 0
            super().damage(damage)
        def re_armor(self):
            self.armor = 3
        def get_armor(self):
            return self.armor

centurion = Gladiator("gregGuerre", 30, 2)
centurion.damage(15)
print("vie : ", centurion.get_health(), "armure de : ", centurion.get_armor())

if issubclass(Gladiator, SuperPlayer):
     print("yes")