#The birthday problem - high probability that 2 people will have the same birthday even in a small group of people

import datetime, random
import re

def getBirthdays(numberofBirthdays):
    """Returns a list of number random date objects for birthdays"""
    birthdays = []

    for i in range(numberofBirthdays):
        #Only interested in month and date as year is irrelevant
        startOfYear = datetime.date(2001, 1, 1)

        #Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    
    return birthdays

def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once in the list"""
    if len(birthdays) == len(set(birthdays)):
        return None #All birthdays are unique, hence no match
    
    #Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA == birthdayB:
                return birthdayA #Returning the matching birthday


#Set the tuple of months in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

while True:
    print("How many birthdays shall I generate? (Max 100)")
    response = input('> ')
    if response.isdecimal() and (0<int(response)<=100):
        numBDays = int(response)
        break #Break the infinite loop as user has entered correct data
print()

#Generate and Display birthdays
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i !=0:
        #Display a comma for each birthday after the first birthday
        print(', ', end ='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

#Determine if there are birthday matches
match = getMatch(birthdays)

#Display the results
if (match != None):
    monthName=MONTHS[match.month -1]
    dateText = "{} {}".format(monthName, match.day)
    print('multiple people have birthdays on', dateText)
else:
    print('there are no matching birthdays')
print()

#Run 100,000 simulations
print("Generating", numBDays, "random birthdays 100,000 times")
input("Press Enter to Begin...")

print("Executing")
simMatch = 0 #Number of simulations which had matching birthdays
for i in range(100_000):
    if i%10_000 == 0:
        print(i, "simulation runs...")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('completed all simulations')

#Display simulation results
probability = round(simMatch/100_000 * 100, 2)
print("Out of 100,000 simulations of", numBDays, "people")
print("Matches present = ", simMatch, "times")
print("Probability of Matching in a group = ",probability, "%")
