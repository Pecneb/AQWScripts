import keyboard
import time
import subprocess
import sys
import getopt

class Klassz(object):
    nev = ""
    kepessegek = []
    skillrotation = []

    def __init__(self, nev):
        self.nev = nev

    def skill_rotation(self, rotation, intervallumok):
        for i in range(rotation):
            self.skillrotation.append(rotation[i])
            self.skillrotation.append(intervallumok[i])


def interface(klasszok):
    print("Classok:")
    for i in range(klasszok):
        print(f"{i+1}. {klasszok[i]}")
    chosen = input("Klassz szama: ")
    return klasszok[chosen]

def main(argv):
    if len(argv) != 1:
        print("Csak az eleresi utat ird be!")
        sys.exit(1)
    pathname = argv[0]
    klasszok =[]

if __name__ == "__main__":
    main(sys.argv[1:])