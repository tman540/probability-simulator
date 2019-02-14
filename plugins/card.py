from random import choice
from progress.bar import ShadyBar as Bar


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
                # Initialize the list of chosen cards
                chosen_card = []
                for x in range(times):
                    # choose a random card
                    card_choice = choice(cards)
                    # Check if the card is a joker (this is because the joker doesn't have a suit, so one doesn't
                    # need to be chosen for it
                    if card_choice == "Joker":
                        # Just add the `Joker` to the list of chosen cards
                        chosen_card.append(card_choice)
                    # If it's not a joker
                    else:
                        # Choose a suit
                        suit_choice = choice(suits)
                        # Add the card + suit to the list of chosen cards
                        # Example: Ace of Spades
                        chosen_card.append(card_choice + " of " + suit_choice)
                    # Continue with the progress bar
                    bar.next()
                # Complete the bar
                bar.finish()
                # Loop over all the chosen cards
                for card in chosen_card:
                    # Print that card
                    print(card)

            except ValueError:

                print("Please only enter number")
            except ZeroDivisionError:
                print("You must flip at least 1 coin")
