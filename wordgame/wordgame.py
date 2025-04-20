import random 

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word=random.choice(words)

guesses=[]
turns=12

while turns > 0:
    for char in word:
        failed=0
        if char in guesses:
            print(char, end=" ")
        else:
            print("_",end=" ")
            failed=failed+1
        
        if failed==0:
            print(" You have won the game : )")
            break
    guess=input ("Guess a character: ")
    guesses=guess
    
    if guess not in word:
        turns=turns-1
        print("wrong character entered")
        print (" You have ",turns, "more guesses...")
        
        if turns == 0:
            print("You Lose. The word was:", word)
            