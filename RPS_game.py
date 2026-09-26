r = "rock"
p = "paper"
s = "scissors"

def game():
    print("welcome to the game")
    print("choose your wepon rock, paper, or scissors")
    print("rock = r ")
    print("paper = p")
    print("scissors = s")

def get_user_choice():
    user_input = input("enter your choice : ")
    return user_input

def get_computer_choice():
    import random
    computer_input = random.choice([r, p, s])
    return computer_input

def winner(user_input, computer_input): 
    if user_input == computer_input:
        return "tie"
    elif (user_input == r and computer_input == s) or (user_input == p and computer_input == r) or (user_input == s and computer_input == p):
        return "user_wins"
    else:
        return "computer wins"

game()
user_choice = get_user_choice()
computer_choice = get_computer_choice()
result = winner(user_choice, computer_choice)
print("user_choice: ", user_choice)
print("computer_choice: ", computer_choice)
print(result)