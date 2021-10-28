import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)
    print("Done!")

def display_menu():
    print("""
    Please select one of the following options:
    [1] Display the names of all passengers
    [2] Display the number of passengers that survived
    [3] Display the number of passengers per gender
    [4] Display the number of passengers per age group
    [5] Display the number of survivors per age group
    """)
    user_choice = int(input())
    return user_choice

def display_passenger_names():
    print("The names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)

def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1

    print(f"{num_survived} passengers survided")

def display_passengers_per_gender():
    females = 0
    male = 0

    for record in records:
        gender = record[4]

        if gender == "male":
            male += 1
        else:
            females += 1
    print(f"females: {females}\nmales: {male}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in records:
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1

    print(f"children: {children}\nadults: {adults}\nelderly: {elderly}")

def display_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    childssurvived = 0
    adultssurvived = 0
    elderlysurvived =0

    for record in records:
        survived = int(record[1])
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
                if survived == 1:
                    childssurvived += 1
            elif age < 65:
                adults += 1
                if survived == 1:
                    adultssurvived += 1
            else:
                elderly += 1
                if survived == 1:
                    elderlysurvived += 1

    print(f"children: {childssurvived}/{children}\nadults: {adultssurvived}/{adults}\nelderly: {elderlysurvived}/{elderly}")




def run():
    load_data("titanic.csv")
    print(f"Succesfully loaded {len(records)} records.")

    selected_option = display_menu()
    print(f"You have selection option: {selected_option}")

    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option ==3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")

if __name__ == "__main__":
    run()
