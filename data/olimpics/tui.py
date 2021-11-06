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
          {"[ctally]":<10} Tally up medals for each team
          {"[exit]":<10} Exit the program
    """)
    print("Your selection:\n")
    menu_selection = input()

def display_medal_tally(tally):
    tally = {"Gold":10,"Silver":5,"Bronze":2}
    print(f"""
            | {'Gold':<10}|{tally['Gold']:<10}|
            | {'Silver':<10}|{tally['Silver']:<10}|
            | {'Bronze':<10}|{tally['Bronze']:<10}|
    """)

def run():
    started()
    completed()
    error("error")
    menu()
    display_medal_tally("Sweeden")

if __name__ == "__main__":
    run()