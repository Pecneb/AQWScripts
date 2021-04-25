import keyboard
import time
import subprocess
import sys
import getopt

class Klassz(object):
    nev = ""
    kepessegek = []
    skillrotation = []
    heal = []
    healtime = 0

    def __init__(self, nev):
        self.nev = nev

    # Sets the class skill rotation
    def skill_rotation(self, rotation):
        for i in range(rotation):
            self.skillrotation.append(rotation[i])

    # Adds heal if the class has one
    def add_heal(self, heals, healtime):
        for i in range(heals):
            self.heal.append(heals[i])
        self.healtime = healtime
    
    # Heals with all the skills that given
    def press_heal(self):
        for i in range(self.heal):
            keyboard.send(str(self.heal[i]))

    # Starts the rotation
    def start_rotation(self):
        healtimer = 0
        while True:
            if(healtimer == self.healtime):
                self.press_heal()
            for i in range(self.skillrotation):
                keyboard.send(str(i))
                sleep(1.5)
            healtimer += 1

# Gives a little shell interface,
# that lists all the classes the user can chose from.
def interface(klasszok):
    print("Classok:")
    for i in range(klasszok):
        print(f"{i+1}. {klasszok[i]}")
    chosen = input("Klassz szama: ")
    return klasszok[chosen]


# Opens the Game if needed (further implepentation is coming!)
def open_aqw(PATH):
    subprocess.Popen(PATH)


def main():
    Klasszok = []
    Klasszok.append(Klassz("Infinite Legion Dark Caster"))
    Klasszok[0].skill_rotation([4, 5, 3, 2], [1, 1, 1, 1])
    Klasszok.append(Klassz("Blaze Binder"))
    Klasszok[1].skill_rotation([2, 3, 5, 4], [1, 1, 1, 1])

if __name__ == "__main__":
    main()