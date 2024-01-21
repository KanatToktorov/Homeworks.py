import random
from decouple import config

MY_MONEY = int(config('MY_MONEY', default=1000))
SLOTS = list(range(1, 11))

def play_casino():
    global MY_MONEY
    while True:
        print(f"Your current money: ${MY_MONEY}")
        bet = int(input("Place your bet: $"))
        selected_slot = int(input("Choose a slot (1-10): "))
        winning_slot = random.choice(SLOTS)
        print(f"Winning slot is: {winning_slot}")

        if selected_slot == winning_slot:
            winnings = 2 * bet
            MY_MONEY += winnings
            print(f"Congratulations! You won ${winnings}")
        else:
            MY_MONEY -= bet
            print(f"Sorry! You lost ${bet}")

        if MY_MONEY <= 0:
            print("You're out of money! Game over.")
            break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'no':
            break
    print(f"Your final money: ${MY_MONEY}")


