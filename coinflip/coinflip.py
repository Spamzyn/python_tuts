import random
import os


def toss_coin():
    return random.choice(["heads", "tails"])


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # Clears screen based on OS

        answer = input("Pick a side for the coin toss (heads/tails): ").lower()

        if answer not in ["heads", "tails"]:
            continue  # Ensures valid input

        result = toss_coin()
        print(f"You got... {result}")

        if answer == result:
            print("Nice, you won the coin toss!!")
        else:
            print("OOF. Better luck next time.")

        # Ask if user wants to play again
        while True:
            play_again = input("Wanna play again? (yes/no): ").lower()
            if play_again in ["no", "n"]:
                return  # Ends the game
            elif play_again in ["yes", "y"]:
                break  # Restarts the game
            else:
                print("Invalid input, please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()

