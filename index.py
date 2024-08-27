import argparse
import time
import sys
import keyboard

def counter_app(target):
    count = 0

    while count <= target:
        if keyboard.is_pressed('space'):
            print("\nCounter interrupted!")
            break
        print(f"\rCounter: {count}", end="")
        time.sleep(1)
        count += 1
    else:
        print(f"\nCounter reached target: {target}")

if __name__ == "__main__":
    target = int(input("Enter the target number: "))
    counter_app(target)
