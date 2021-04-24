import keyboard
import time

"""
Ez meg csak egy teszt, hogy mukodik e. Es ugytunik, hogy mukodik.
"""
def main():
    while True:
        keyboard.send("2")
        time.sleep(1)
        keyboard.send("3")      
        time.sleep(1)
        keyboard.send("4")
        time.sleep(1)
        if keyboard.is_pressed("esc"):
            break

if __name__ == "__main__":
    main()