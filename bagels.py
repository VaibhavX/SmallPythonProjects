#Bagels Program - 10 tries to guess secret 3-digit number based on clues.
#"Pico" when guess has correct digit in wrong place
#"Fermi" when guess has correct digit in the correct place
#"Bagels" when guess has no correct digits

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def getSecretNum():
    numbers = list('0123456789') #Create a list of digits 0 to 9
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Correct Guess - Number Found'

    clues =[]

    for i in range(len(guess)):
        if (guess[i]==secretNum[i]):
            #Correct Digit in correct place
            clues.append('Fermi')
        elif (guess[i] in secretNum):
            #Correct Digit in wrong place
            clues.append('Pico')
    if(len(clues)==0):
        return 'Bagels' #No correct digit present
    else:
        #Sort clues so order does not give away any information
        clues.sort()
        #Return as a single string
        return ' '.join(clues)


def main():
    print("Bagels Game")

    while(True):
        secretNum = getSecretNum() #Obtain a random 3 digit number as a string
        print("Guess Available = {}".format(MAX_GUESSES))

        guessctr = 1
        while (guessctr <= MAX_GUESSES):
            guess=''
            while(len(guess)!= NUM_DIGITS or not guess.isdecimal()):
                print("Guess #{}".format(guessctr))
                guess = input('> ') #Keep receiving input till user inputs in the correct format

            clues = getClues(guess, secretNum)
            print(clues)

            guessctr += 1

            if guess == secretNum:
                break
            if (guessctr>MAX_GUESSES):
                print("No more guesses")
                print("Correct Answer was {}".format(secretNum))

        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Game Ended!")


if(__name__ =='__main__'):
    main()
