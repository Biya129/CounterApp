import argparse
import time
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
    parser = argparse.ArgumentParser(description="Run a counter up to a target number.")
    parser.add_argument('--target', type=int, help="The target number to count up to")
    args = parser.parse_args()
    
    counter_app(args.target)
 
