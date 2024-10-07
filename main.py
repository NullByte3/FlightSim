import time
from dotenv import load_dotenv
load_dotenv()
import database
from colorama import init, Fore, Back, Style
init(autoreset=True)

username = input(Fore.GREEN + "Enter your username: ")
if database.has_played_before(username):
    print(Fore.YELLOW + "Welcome back!")
else:
    print(Fore.CYAN + "Welcome to the 7 Continents Adventure!")
    print(Fore.CYAN + "You will travel to all 7 continents on a budget of $8,500.")
    print(Fore.CYAN + "You will start at a random airport and choose where to go next.")
    print(Fore.CYAN + "The game ends when you have visited all 7 continents.")
    print(Fore.CYAN + "Good luck and have fun!")
    time.sleep(5)
    for _ in range(5):
        print()
def play_game():
    continents = ['AF', 'AN', 'AS', 'EU', 'NA', 'OC', 'SA']
    continent_names = {
        'AF': 'Africa', 'AN': 'Antarctica', 'AS': 'Asia',
        'EU': 'Europe', 'NA': 'North America', 'OC': 'Oceania',
        'SA': 'South America'
    }
    visited_continents = set()
    budget = 8_500
    spawn_airport = database.get_random_airport()
    current_airport = spawn_airport
    visited_continents.add(spawn_airport[1])
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
                print(Fore.YELLOW + f"{i + 1}. {continent_names[continent]} [{continent}]")
        where_to = ask_for_input(Fore.GREEN + "Enter the number of the continent you'd like to travel to: ", [str(i + 1) for i in range(7)])
        continent = continents[int(where_to) - 1]

        airports = database.get_airports_by_continent(continent)
        print(Fore.GREEN + "Choose an airport to travel to:")
        possible_airports = []
        for i, airport in enumerate(airports):
            print(Fore.YELLOW + f"{i + 1}. {airport[0]} ${database.get_cost(current_airport, airport)}")
            if database.get_cost(current_airport, airport) <= budget:
                possible_airports.append(airport)
        if len(possible_airports) == 0:
            print(Fore.RED + "You don't have enough money to travel to any of these airports.")
            print(Fore.RED + "Game Over! You've run out of money.")
            break
        where_to = ask_for_input(Fore.GREEN + "Enter the number of the airport you'd like to travel to: ", [str(i + 1) for i in range(len(possible_airports))])
        budget -= database.get_cost(current_airport, possible_airports[int(where_to) - 1])
        airport = airports[int(where_to) - 1]
        print(Fore.CYAN + f"Travelling to {airport[0]}...")
        current_airport = airport
        visited_continents.add(continent)

        continue

    print()
    print(Fore.CYAN + "Congratulations! You've visited all 7 continents!")
    print(Fore.CYAN + "You've completed the 7 Continents Adventure!")
    print(Fore.CYAN + "You have ${} left in your budget.".format(budget))
    database.add_score(username, 1)
    print(Fore.CYAN + "Your score has been saved: Your score is now: {}".format(database.get_score(username)))
    play_again = input(Fore.GREEN + "Would you like to play again? (y/n) [Yes]: ")
    if play_again.lower() in ['y', 'yes', '']:
        for _ in range(5):
            print()
        play_game()
    else:
        print(Fore.YELLOW + "Thank you for playing! Goodbye!")
        exit()

def ask_for_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        print(Fore.MAGENTA + "Invalid input please try again!")

play_game()