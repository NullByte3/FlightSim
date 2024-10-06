import time
from dotenv import load_dotenv
load_dotenv()
import database
from colorama import init, Fore, Back, Style
init(autoreset=True)

def play_game():
    continents = ['AF', 'AN', 'AS', 'EU', 'NA', 'OC', 'SA']
    continent_names = {
        'AF': 'Africa', 'AN': 'Antarctica', 'AS': 'Asia',
        'EU': 'Europe', 'NA': 'North America', 'OC': 'Oceania',
        'SA': 'South America'
    }
    visited_continents = set()
    budget = 18_500
    spawn_airport = database.get_random_airport()
    visited_continents.add(spawn_airport[1])
    print(Fore.CYAN + "Welcome to the 7 Continents Adventure!")
    print(Fore.RED + "You've spawned in...")
    # Python sucks, time package sleeps and not threading? Idfk what syntax is that. - NullByte3
    # Also, why in the hell the time is in seconds, not milliseconds :skull:
    time.sleep(0.5)
    print(Fore.GREEN + f"{continent_names[spawn_airport[1]]}, on the airport {spawn_airport[0]} ")
    time.sleep(1.0)
    print(Fore.YELLOW + f"Visit all 7 continents with a budget of ${budget}.")
    time.sleep(0.5)
    print(Fore.YELLOW + "The game has begun!")
    time.sleep(1.0)
    print(Fore.YELLOW + "Good luck with your adventure and " + Fore.GREEN + "have fun!")
    # Example usage of harversine formula - NullByte3
    print(database.haversine(spawn_airport[3], spawn_airport[2], 0, 0))
    # The game loop - NullByte3
    # This will run as long as the player has not visited all continents.
    while len(visited_continents) < 7:
        print(Fore.BLUE + "\nCurrent Budget: ${}".format(budget))
        print(Fore.CYAN + f"Continents Visited: {', '.join([continent_names[c] for c in visited_continents])}")

        print(Fore.GREEN + "Where would you like to travel next?")
        for i, continent in enumerate(continents):
            if continent not in visited_continents:
                print(Fore.YELLOW + f"{i + 1}. {continent_names[continent]}")
        break
        pass
    print()
    print(Fore.CYAN + "Congratulations! You've visited all 7 continents!")
    print(Fore.CYAN + "You've completed the 7 Continents Adventure!")
    play_again = input(Fore.GREEN + "Would you like to play again? (y/n) [Yes]: ")
    if play_again.lower() in ['y', 'yes', '']:
        for _ in range(5):
            print()
        play_game()
    else:
        print(Fore.YELLOW + "Thank you for playing! Goodbye!")
        exit()

play_game()