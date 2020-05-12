from random import randrange

guessNumber = randrange(20)
inputNumber = -1

while guessNumber != inputNumber:
    inputNumber = int(input("Ihre Zahl eingeben:"))
    if inputNumber == guessNumber:
        print("Du hast die Zahl richtig erraten!")
    elif inputNumber > guessNumber:
        print("Die zu erratene Zahl is kleiner!")
    elif inputNumber < guessNumber:
        print("Die zu erratene Zahl ist größer")

