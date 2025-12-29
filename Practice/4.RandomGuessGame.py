
import random 
rand = random.randint(1,10)
attemps = 3
print(rand)

for i in range(1,4):
    guess = int(input('Enter your guess: '))
    if guess == rand:
        print('You are correct')
        break
    elif guess < rand:
        print('To low')
    else:
        print('To high')
else:
    print('correct guess is: ',rand)