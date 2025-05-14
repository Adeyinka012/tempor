import random
options = ['z','x','o']
while True:
    user_choice=input("Enter z, x or o(or enter quit to stop)").lower()
    if user_choice =='quit':
        print("Thank you for playing")
        break
    if user_choice not in options:
        print("Invalid choice. Try again")
        continue
    computer_choice= random.choice(options)
    print(f"computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie: ")
    elif(
        (user_choice =='z' and computer_choice=='x') or
        (user_choice=='x' and computer_choice=='o') or
        (user_choice =='o' and computer_choice=='z') 
    ):
        print("you win")
    else:
        print("you lose")