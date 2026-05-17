secret = 87
guess = 0
while guess != secret:
    guess = int(input("enter your guess:-  "))
    if guess == secret:
        print("excelent! Correct answer ")
    elif guess < secret:
        print("try greater number!")
    else:
        print("try smaller number!!")        