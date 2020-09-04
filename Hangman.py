def split(s):
    return [char for char in s]
    
def newWord(word):
    wordToGuess=split(word)
    wordToGuess2=[]
    for x in range(len(wordToGuess)):
        wordToGuess2.append('_')
    print(*wordToGuess2)


word = input ("Provide a word: ")
newWord(word)