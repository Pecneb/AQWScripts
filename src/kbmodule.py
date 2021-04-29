import keyboard
import time
import subprocess
# TODO: Maybe can implement pyautogui elements to the app aswell!
#import pyautogui

class Klassz(object):
    nev = ""
    kepessegek = []
    skillrotation = []
    heal = 0
    healtime = 0

    def __init__(self, nev, skillrotation, heal, healtime):
        self.nev = nev
        self.skillrotation = skillrotation
        self.heal = heal
        self.healtime = healtime

    # Heals with all the skills that given (not working gotta fix)
    def press_heal(self):
        for heal in self.heal:
            keyboard.send(str(heal))

    # Starts the rotation (not working gotta fix)
    def start_rotation(self):
        time.sleep(5)
        healtimer = 0
        while True:
            if(healtimer == self.healtime):
                self.press_heal()
                healtimer = 0
            for number in self.skillrotation:
                keyboard.send(str(number))
                time.sleep(1)     
            healtimer += 1

# Gives a little shell interface,
# that lists all the classes the user can chose from.
def interface(klasszok):
    print("Classok:")
    for i in range(len(klasszok)):
        print(f"{i+1}. {klasszok[i].nev}")
    chosen = int(input("Klassz szama: ")) - 1
    print(f"Starting...")
    return klasszok[chosen]


# Opens the Game if needed (further implepentation is coming!)
def open_aqw(PATH):
    subprocess.Popen(PATH)


# Do rotation while the other on in the Class is not fixed
def do_rotation(Klassz):
    time.sleep(5)
    healtimer = 0
    while True:
        if(healtimer == Klassz.healtime):
            keyboard.send(str(Klassz.heal))
            healtimer = 0
            time.sleep(1)
        for number in Klassz.skillrotation:
            keyboard.send(str(number))
            time.sleep(1)     
        healtimer += 1


def main():
    print("Press Ctrl-C to EXIT.")
    try:
        Klasszok = []
        Klasszok.append(Klassz("Infinite Legion Dark Caster", [4, 5, 3], 2, 3))
        Klasszok.append(Klassz("Blaze Binder", [2, 3, 5], 4, 2))
        do_rotation(interface(Klasszok))
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()