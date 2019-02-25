from random import choice
from progress.bar import ShadyBar as Bar
from prettytable import PrettyTable
from collections import defaultdict


class Plugin:
    def main(self):
        cards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace", "Joker"]
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        while True:
            # Catch exception if user enters letters or nothing
            try:
                times = input("How many cards do you want to pull?: ")
                # Check if user entered `exit` or `quit` before converting to int
                # (So exception wouldn't trigger)
                if times == "exit" or times == "quit":
                    print("Exiting...")
                    # Exit the loop which quits the program
                    break
                else:
                    times = int(times)
                if times <= 0:
                    raise ZeroDivisionError
                # Initialize the progress bar
                bar = Bar('Choosing {} card(s)...'.format(times), max=times,
                          suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')
                # Create a dict that is incrementable
                chosen_card_dict = defaultdict(int)
                for x in range(times):
                    # choose a random card
                    card_choice = choice(cards)
                    # Check if the card is a joker (this is because the joker doesn't have a suit, so one doesn't
                    # need to be chosen for it
                    if card_choice == "Joker":
                        # Just add the `Joker` to the list of chosen cards
                        chosen_card_dict[card_choice] += 1
                    # If it's not a joker
                    else:
                        # Choose a suit
                        suit_choice = choice(suits)
                        with open("cards.txt", "a+") as f:
                            f.write(card_choice + " of " + suit_choice + "\n")
                        # Add the card + suit to the list of chosen cards
                        # Example: Ace of Spades
                        chosen_card_dict[card_choice + " of " + suit_choice] += 1
                    # Continue with the progress bar
                    bar.next()
                # Complete the bar
                bar.finish()
                # Loop over all the chosen cards
                table = PrettyTable(["Card", "Amount", "Percentage"])
                for card in chosen_card_dict:
                    # Loop over the rows instead of calling `add_row()` multiple times
                    # Allows for easy expandability
                    table.add_row([card, chosen_card_dict[card], f"%{round((chosen_card_dict[card] / times * 100), 4)}"])

                # Output the table
                print(table)

            except ValueError:
                print("Please only enter numbers")
            except ZeroDivisionError:
                print("You must pull at least 1 card")
