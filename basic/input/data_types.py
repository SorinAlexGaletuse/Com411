def run():
    print("What is your name?")
    name = input()
    print("How old are you(in years)?")
    years = input()
    print("How tall are you(in meters)?")
    tall = float(input())
    print("How much do you weigh(in kilograms)?")
    weigh = float(input())
    bmi = (weigh/(tall*2))

    print(f"{name} you are {years} years old and your bmi is {bmi:.2f}")