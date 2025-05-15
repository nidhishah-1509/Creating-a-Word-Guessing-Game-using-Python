import random

with open('List of Words.txt', 'r') as file:
    word_bank = [line.strip() for line in file if line.strip()]

word = random.choice(word_bank)
guessedword = ['_'] * len(word)
attempts = 10
guessed_letters = []

while attempts > 0:
    print('\nCurrent Word: ' + ' '.join(guessedword))
    print('Attempts left:', attempts)
    print('Guessed letters:', ', '.join(guessed_letters))
    
    guess = input('Guess a letter: ').lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedword[i] = guess
        print('Great Guess!')
    else:
        attempts -= 1
        print('Wrong Attempt')

    if '_' not in guessedword:
        print('\nCongratulations! You have guessed the word.')
        print('The word was:', word)
        break
else:
    print('\nYou have run out of attempts! The word is:', word)
