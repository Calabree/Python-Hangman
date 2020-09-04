def newWord(word, wordToGuess, blankWordToGuess):
    wordToGuess=list(word)
    for x in wordToGuess:
        blankWordToGuess.append('_')

def wordChecker(userGuess, wordToGuess, blankToGuess):
    x=0
    letterGuessedCorrectly=False
    for i in word:
        if i == userGuess:
            print('found')
            blankToGuess[x] = userGuess
            letterGuessedCorrectly=True
        x+=1
    if letterGuessedCorrectly == False:
        print(f'Looks like your guess {userGuess} was wrong')



word = input ("Provide a word: ")
wordToGuess= []
blankToGuess=[]
newWord(word, wordToGuess, blankToGuess)

userGuess = input('Guess a letter: ')
wordChecker(userGuess, wordToGuess, blankToGuess)
print(*blankToGuess)
