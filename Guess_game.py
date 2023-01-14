#guessing game that gives the user 3 tries to guess a number between 1 and 10
secret_number=8
guess = 0
tries = 0
while tries < 3 and guess != secret_number:
     guess = int(input("Guess a number between 1 and 10:"))
     tries = tries + 1
if guess == secret_number:
    print("Your won and the secret number is" +" "+str(secret_number))
else:
    print("Your tries are over and the secret number is "+" "+str(secret_number))