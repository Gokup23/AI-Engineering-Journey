import random
import time

characters = ["0", "1", " ", " ", " ", "2", "3", "4", "5", "8", "9"]

width = 60

print("--- INITIALIZING MATRIX UPLINK ---")
time.sleep(1)

try:
    while True:
        line = ""

        for i in range(width):
            line += random.choice(characters) + " "
        
        print(f"\033[92m{line}")
        time.sleep(0.05)

except KeyboardInterrupt:
    print("\n\033[0m--- DISCONNECTED ---")
