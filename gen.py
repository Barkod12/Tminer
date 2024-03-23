import time
import random
import re

def is_valid_iban(iban):
    iban_pattern = re.compile(r'^[A-Z]{2}\d{2}[A-Z\d]{4}\d{7}([A-Z\d]?){0,16}$')
    return iban_pattern.match(iban) is not None

def tl_mining():
    total_tl = 0
    print("Type 'start' to begin mining or 'exit' to close the program.")
    while True:
        user_input = input(">")
        if user_input.lower() == 'exit':
            print("Exiting the program...")
            break
        elif user_input.lower() == 'start':
            iban = input("Please enter your IBAN: ")
            if not is_valid_iban(iban):
                print("Invalid IBAN format. Please enter a valid IBAN.")
                continue
            print("Loading...")
            time.sleep(3.4)  # Simulate loading time
            print("Mining started...")
            while True:
                mining_time = random.uniform(1.5, 3.5)  # Vary mining time between 1.5 to 3.5 seconds
                time.sleep(mining_time)
                mined_tl = random.randint(6, 15)
                total_tl += mined_tl
                print(f"Mined {mined_tl} TL. Total TL mined: {total_tl}")
        else:
            print("Invalid command. Type 'start' to begin mining or 'exit' to close the program.")

tl_mining()
