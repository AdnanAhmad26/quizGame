print("Welcome to the Quiz!")

playing = input("Ready to begin?  ")

if playing.lower() != "yes":
    quit()

print("Let's play!")
score = 0


answer = input("What are Animals that eat both plants and meat called? ")

if answer.lower() == "omnivores":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is the capital of Florida? ")

if answer.lower() == "tallahassee":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("When is Pi Day celebrated? ")

if answer.lower() == "march 14":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who's the youngest member of the band, The Beatles? ")

if answer.lower() == "george":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the main ingredient in falafel? ")

if answer.lower() == "chickpeas":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is considered the pioneer of abstract art? ")

if answer.lower() == "wassily kadinsky":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which country is brie cheese originally from? ")

if answer.lower() == "france":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("In what franchise would you find the character Katniss Everdeen? ")

if answer.lower() == "the hunger games":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which planet is closest to the sun? ")

if answer.lower() == "mercury":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What nut is in the middle of a Ferrero Rocher? ")

if answer.lower() == "hazelnut":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You scored " + str((score / 10) * 100) + " %.")




    


