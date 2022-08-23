print("Welcome to my random trivia game!")
playing = input("Would you like to play? ")

if playing.lower() != "yes":
    print("Ok, see ya!"),
    quit()
else: 
    print("Awesome! Let's get started.")

#loop in case players want to try multiple times
while True:
    score = 0

    #Q1
    answer = input("What does BBC stand for? ")
    if answer.lower() == "british broadcasting corporation":
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    #Q2
    answer = input("What element does 'O' represent on the periodic table? ")
    if answer.lower() == "oxygen":
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    #Q3
    senses = ['sight', 'touch', 'hearing', 'taste', 'smell']
    answer = input("For one point, what are the five senses humans have? ")

    #Split the answer to create a list to run through 'check' func
    answerList = answer.split(", ")

    # Check makes sure users type in all 5 senses 
    check = all(item in answerList for item in senses) 
    if check == True:
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    #Q4
    answer = input("Where would you find the Golden Gate Bridge? ")
    if answer.lower() == "san francisco":
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    #Q5
    answer = input("Who is Ashton Kutcher married to? ")
    if answer.lower() == "mila kunis":
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    print("Halfway there!")
    #Q6
    colors = ['blue', 'yellow', 'black', 'green', 'red']
    answer = input("What five colors are the Olympic rings? ")

    #Split the answer to create a list to run through 'check' func
    answerList = answer.split(", ")

    # Check makes sure users type in all 5 colors 
    check = all(item in answerList for item in colors) 
    if check == True:
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    #Q7
    answer = input("What river runs through Egypt? (two words) ")
    if answer.lower() == "the nile":
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    #Q8
    answer = input("What is the only english word that truely has no rhyme? ")
    if answer.lower() == "orange":
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    #Q9
    answer = input("Who wrote the horror novel 'It?'? ")
    if answer.lower() == "stephen king":
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    #Q10
    answer = input("How many days are in a leap year? ")
    if answer.lower() == "366":
        print("Correct!")
        score += 1
    else:
        print("Incorrect...")

    print("Congrats, you finished the quiz!")
    print("You answered correctly " + str(score)+ " times!")
    print("This is a score of " + str((score/10)*100) + "%.")
    print()
    check = input("Do you want to try again? Enter 'Y' to start over, or another key to end: ")
    if check.upper() == "Y":
        continue
    print("Bye...")
    break