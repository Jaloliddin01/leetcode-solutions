class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f"attacks with power of {self.power}")
    
class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    
    def attack(self):
        print(f"number of arrows left - {self.arrows}")

    def run(self):
        print('runs really fast')

class HybridHero(Wizard, Archer):
    pass

hyb = HybridHero()
hyb.run()
