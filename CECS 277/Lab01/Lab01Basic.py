# Name: Thaw Han, Achal Mohandas
# Date: 01/28/2025
# Description: Creating a basic Three Card Monte game
import random
import check_input

def main():
    # Display the game instructions
    total = 100
    while True:
        print("-Three Card Monte-")
        print("Find the queen to double your bet!")
        print("")

        # Get the user's bet
        print(f"Your total is: ${total}")
        bet = check_input.get_int_range("How much do you want to bet? ", 1, total)

        #Create and shuffle thte cards 
        cards = ["K", "Q", "K"]
        random.shuffle(cards)

        # Display the game board
        print("+ - - - - - +  + - - - - - +  + - - - - - +")
        print("")
        print("|           |  |           |  |           |")
        print("")
        print("|     1     |  |     2     |  |     3     |")
        print("")
        print("|           |  |           |  |           |")
        print("")
        print("+ - - - - - +  + - - - - - +  + - - - - - +")
        print("")

        # Get the user's guess
        user_input = check_input.get_int_range("Find the queen: ", 1, 3)

        # Reveal the cards
        print("+ - - - - - +  + - - - - - +  + - - - - - +")
        print("")
        print("|           |  |           |  |           |")
        print("")
        print(f"|     {cards[0]}     |  |     {cards[1]}     |  |     {cards[2]}     |")
        print("")
        print("|           |  |           |  |           |")
        print("")
        print("+ - - - - - +  + - - - - - +  + - - - - - +")
        print("")

        # Check if the user's guess is correct
        if cards[user_input-1] == "Q":
            print("You got lucky this time...")
            total += bet
        else:
            print("Sorry... you lose.")
            total -= bet
            if total == 0:
                print("You're out of money. Beat it loser!")
                break
        
        # Ask if the user wants to play again
        repeat = check_input.get_yes_no("Play again (Y/N): ")

        if total == 0:
            print("You're out of money. Beat it loser!")
            break
        elif repeat == False:
            break
    
main()