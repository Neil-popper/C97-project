import random
difficulty=input("What diffiulty do you want? (type easy or hard no uppercase) ")
if difficulty=="easy":
    print("You get 5 lives")
    lives=5
    number=random.randint(1,9)
    guess=int(input("Guess a number between 1 and 9"))
    if guess == number:
        print("YOU WIN!")
    elif guess>number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too high: Guess a number lower then",guess)
        guess=int(input(" "))
    elif guess<number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too low: Guess a number higher then",guess)
        guess=int(input(" "))
    if guess == number:
        print("YOU WIN!")
    elif guess>number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too high: Guess a number lower then",guess)
        guess=int(input(" "))
    elif guess<number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too low: Guess a number higher then",guess)
        guess=int(input(" "))
    if guess == number:
        print("YOU WIN!")
    elif guess>number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too high: Guess a number lower then",guess)
        guess=int(input(" "))
    elif guess<number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too low: Guess a number higher then",guess)
        guess=int(input(" "))
    if guess == number:
        print("YOU WIN!")
    elif guess>number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too high: Guess a number lower then",guess)
        guess=int(input(" "))
    elif guess<number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too low: Guess a number higher then",guess)
        guess=int(input(" "))
    if guess == number:
            print("YOU WIN!")
    elif guess>number:
        lives=lives-1
        print("GAME OVER :(")
    elif guess<number:
        lives=lives-1
        print("GAME OVER :(")
    
    



elif difficulty=="hard":
    print("You get 3 lives")
    lives=3
    number=random.randint(1,9)
    guess=int(input("Guess a number between 1 and 9"))
    if guess == number:
        print("YOU WIN!")
    elif guess>number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too high: Guess a number lower then",guess)
        guess=int(input(" "))
    elif guess<number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too low: Guess a number higher then",guess)
        guess=int(input(" "))
    if guess == number:
            print("YOU WIN!")
    elif guess>number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too high: Guess a number lower then",guess)
        guess=int(input(" "))
    elif guess<number:
        lives=lives-1
        print("You have",lives,"lives left")
        print("Your guess was too low: Guess a number higher then",guess)
        guess=int(input(" "))
    if guess == number:
            print("YOU WIN!")
    elif guess>number:
        lives=lives-1
        print("GAME OVER :(")
    elif guess<number:
        lives=lives-1
        print("GAME OVER :(")



else:
    print("Sorry that is not a valid difficulty. Please try again and make sure you spelled it correctly and you didn't capitalize anything")
