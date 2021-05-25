import random
import art
import words

word = random.choice(words.word_list)
display = []
for char in range(0,len(word)):
    display.append("_")

def update_display(count, value):
    display[count]=value
    
def print_display():
    print(" ".join(display))

print(f"{art.logo}\nWelcome to the game\n")

turns = 6

while True:
    
    print_display()
    print(f"\n{art.stages[turns]}")
    
    if turns == 0:
        print(f"You Lost\nThe word was {word}")
        break
    if "_" not in display:
        print("You Won!")
        break
    
    guess = input("choose a letter\n")
    if guess in word:
        count = 0
        while count < len(word):
            if word[count] == guess:
                print(word)
                update_display(count, guess)
            count += 1
        print(f"There is the letter {guess}\n")
    else:
        turns -= 1
        print(f"There is no letter {guess}\n")