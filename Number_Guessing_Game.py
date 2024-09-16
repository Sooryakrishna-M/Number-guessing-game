import random

top_of_range=input("Type a number :")
guesses=0
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Please enter a number greater than 0 next time")
        quit()
else:
    print("Please enter a number next time")
    quit()


random_number=random.randint(0,top_of_range)
print(random_number)

while True:
    guesses+=1
    user_input=input("Make a guess")
    if user_input.isdigit():
        user_input=int(user_input)
    else:
        print("Please type a number next time")
        continue
    if user_input == random_number:
        print("You got it correct!")
        break
    elif user_input>random_number:
        print("You were above the number")
    else:
        print("You were below the number")
print("You got it in",guesses,"guesses")