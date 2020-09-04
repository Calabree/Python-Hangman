def newWord(word, wordToGuess, blankWordToGuess):
    wordToGuess=list(word)
    for x in wordToGuess:
        blankWordToGuess.append('_')

def wordChecker(userGuess, wordToGuess, blankToGuess):
    x=0
    for i in word:
        if i == userGuess:
            print('found')
            blankToGuess[x] = userGuess
        else:
            print(f'{userGuess} is not in this word!')
        x+=1



word = input ("Provide a word: ")
wordToGuess= []
blankToGuess=[]
newWord(word, wordToGuess, blankToGuess)

userGuess = input('Guess a letter: ')
wordChecker(userGuess, wordToGuess, blankToGuess)
print(*blankToGuess)
