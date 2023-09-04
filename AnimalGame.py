Spellings = [
    "e", "l", "e", "p", "h", "a", "n", "t"
]
print("Spell the animal: It begins with the letter "+ Spellings[0] + " and ends with the letter " + Spellings[7])
print("It has " + str(len(Spellings)) + " letters")
userGuess = input("what do you think the animal is? ").lower()

if userGuess == "elephant":
    print("Well Done!!")
else:
    print("Sorry that's wrong try again later")