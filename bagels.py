#Bagels Program - 10 tries to guess secret 3-digit number based on clues.
#"Pico" when guess has correct digit in wrong place
#"Fermi" when guess has correct digit in the correct place
#"Bagels" when guess has no correct digits

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print("Bagels Game")
