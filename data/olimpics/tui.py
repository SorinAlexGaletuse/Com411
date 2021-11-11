def started(msg=""):
    print("-"*85)
    msg = "Reading data from athlete_events.csv"
    print(f"Operation started: {msg}...")

def completed():
    print("\nOperation completed.")
    print("-"*85)

def error(msg):
    msg = "Invalid Selection!"
    print(f"Error! {msg}\n")

def menu():
    print(f"""Please select one of the following options:
          {"[years]":<10} List unique years
          {"[tally]":<10} Tally up medals
          {"[team]":<10} Tally up medals for each team
          {"[exit]":<10} Exit the program
    """)
    print("Your selection:\n")
    menu_selection = input()
    return menu_selection

def display_medal_tally(tally):
    #tally = {"Gold":10,"Silver":5,"Bronze":2}
    print(f"""
            | {'Gold':<10}|{tally['Gold']:<10}|
            | {'Silver':<10}|{tally['Silver']:<10}|
            | {'Bronze':<10}|{tally['Bronze']:<10}|
    """)

def display_team_medal_tally(team_tally):
    #team_tally = {"United Kingdom": {"Gold":10,"Silver":5,"Bronze":2}}
    for team, tally in team_tally.items():
        print(team)
        print(f"\nGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")

def display_years(years):
    #years = {"2008","2010","2012","2014","2016","2018","2020"}
    reverse_years = sorted(years, reverse=True)
    for years in reverse_years:
        print(years)


#def run():
    #started()
    #completed()
    #error("error")
    #menu()
    #display_medal_tally("medal")
    #display_team_medal_tally("team_medal")
    #display_years("years")

#if __name__ == "__main__":
    #run()