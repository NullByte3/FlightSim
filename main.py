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
    budget = 12_500
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
    while len(visited_continents) < 7:
        print(Fore.BLUE + "\nCurrent Budget: ${}".format(budget))
        print(Fore.CYAN + f"Continents Visited: {', '.join([continent_names[c] for c in visited_continents])}")

        print(Fore.GREEN + "Where would you like to travel next?")
        for i, continent in enumerate(continents):
            if continent not in visited_continents:
                print(Fore.YELLOW + f"{i + 1}. {continent_names[continent]}")
        break
        pass

play_game()