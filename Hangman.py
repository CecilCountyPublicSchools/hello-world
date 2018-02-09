import random
def fail(fails):
    if fails == 0:
        print("          .______", "          |", "          |", "          |", "          |", "         /|\\", "\n", sep='\n')
    elif fails == 1:
        print("          .______", "          |     O", "          |", "          |", "          |", "         /|\\", "\n", sep='\n')
    elif fails == 2:
        print("          .______", "          |     O", "          |     |", "          |     |", "          |", "         /|\\", "\n", sep='\n')
    elif fails == 3:
        print("          .______", "          |     O", "          |    /|", "          |     |", "          |", "         /|\\", "\n", sep='\n')
    elif fails == 4:
        print("          .______", "          |     O", "          |    /|\\", "          |     |", "          |", "         /|\\", "\n", sep='\n')
    elif fails == 5:
        print("          .______", "          |     O", "          |    /|\\", "          |     |", "          |    /", "         /|\\", "\n", sep='\n')
    elif fails == 6:
        print("          .______", "          |     O", "          |    /|\\", "          |     |", "          |    / \\", "         /|\\", "\n", sep='\n')
def hangman_display(guessed, secret):
    result = ""
    for letter in secret:
        if letter in "1234567890 !@#$%^&*()-_=+[{]}\\|\"';:/?.>,<`~":
            result += letter
        elif letter.lower() in guessed.lower():
            result += letter
        else:
            result += '-'
    return result
word = random.choice(['Hippopotomonstrosesquippedaliophobia', 'Different', 'Hawaii', 'Tuberculosis'])
guessed = ''
fails = 0
now = hangman_display(guessed, word)
print(now)
while True:
    guess = str(input("Guess a letter: "))
    if guess not in word:
        if guess in guessed:
            print("Already guessed that, try again!")
        else:
            fails += 1
            fail(fails)
            if fails > 6:
                print("You lose!")
                break
    guessed += guess
    now = hangman_display(guessed, word)
    if now == word:
        print("You win!")
        break
    print(now)