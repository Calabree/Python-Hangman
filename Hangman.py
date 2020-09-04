def newWord(word, wordToGuess, blankWordToGuess):
    wordToGuess=list(word)
    for x in wordToGuess:
        blankWordToGuess.append('_')

def wordChecker(userGuess, wordToGuess, blankToGuess):
    x=0
    global guessesLeft
    letterGuessedCorrectly=False
    for i in word:
        if i == userGuess:
            print('found')
            blankToGuess[x] = userGuess
            letterGuessedCorrectly=True
        x+=1
    if letterGuessedCorrectly == False:
        print(f'Looks like your guess {userGuess} was wrong')
        guessesLeft = guessesLeft-1
        print(f'You have {guessesLeft} guesses left! Choose carefully!')
gameOn = True
guessesLeft=5
word = input ("Provide a word: ")
wordToGuess= []
blankToGuess=[]
newWord(word, wordToGuess, blankToGuess)

while (gameOn ==  True):

    userGuess = input('Guess a letter: ')
    wordChecker(userGuess, wordToGuess, blankToGuess)
    print(*blankToGuess)

    if guessesLeft == 0:
        print ("Game Over!")
        gameOn = False