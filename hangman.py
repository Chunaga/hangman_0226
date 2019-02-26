import random
answerlist = ["hello", "world", "greet"]
random.shuffle(answerlist)
answer = list(answerlist[0])

display = []
used = []

display.extend(answer)
used.extend(display)

for i in range (len(display)):
    display[i] = "_"

print(" ".join(display))
print()

count = 0
incorrect = 5

while count < len(answer) and incorrect > 0:
    guess = input("please guess  word: ")
    guess = guess.lower()
    print(count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count = count + 1
            used.remove(guess)

    if guess not in display:
        incorrect = incorrect -1
        print("BOOO")


    print("you have guessed: " ,count, "correct letters.")
    print("you have", incorrect, "chances left")
    
    print(" ".join(display))
    print()

if count == len(answer):
    print("well done")

else:
    print("zannenn")
