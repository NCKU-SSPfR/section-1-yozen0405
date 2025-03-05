import webbrowser
import random
import sys

RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
MAX_ATTEMPTS = 3


def open_video():
    """Opens the Rickroll video."""
    webbrowser.open(RICKROLL_URL)
    print("Rickroll incoming...")


def get_user_input():
    """Prompt user for the correct answer."""
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        try:
            user_input = input("1 times 1 = ? ")

            if user_input.strip() == "1":
                open_video()
                return

            elif user_input.lower() == "exit":
                sys.exit()

            else:
                print("Wrong! Try again.")
                attempts += 1

        except ValueError:
            print("Invalid input, please enter a number.")

    print("Too many failed attempts. Exiting...")


if __name__ == "__main__":
    get_user_input()