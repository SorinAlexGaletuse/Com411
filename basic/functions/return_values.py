def sum_weights(bop_weight , beep_weight):
    total_weight = bop_weight + beep_weight
    return total_weight

def calc_avg_weight(bop_weight , beep_weight):
    avg_weight = (bop_weight+beep_weight) / 2
    return avg_weight

def run():
    print("What is the weight of Beep?")
    beep_weight = float(input())
    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("What would you like to calculate(sum or average):")
    calculate = input()

    if calculate == 'sum':
            result = sum_weights(bop_weight, beep_weight)
            print(f"The sum of Beep and Bop's weight is: {result:.2f} ")

    elif calculate == 'average':
            result = calc_avg_weight(bop_weight, beep_weight)
            print(f"The average weight of Beep and Bop is:{result:.2f}")
    else:
            print("Please enter the words sum or average.")

run()

