def observed():
    observations = []

    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations

def remove_observations(list_of_obs):
    rmv = True

    while(rmv):
        print("Do you wish to remove and observation?")
        user_input = input()

        if(user_input == "yes"):
            print("Please enter the observation you want to remove")
            observ = input()
            list_of_obs.remove(observ)
        else:
            rmv = False

def run():
    a = observed()
    remove_observations(a)

    observ_set = set()
    for observ in a:
        res = (observ, a.count(observ))
        observ_set.add(res)

    for res in sorted(observ_set):
        print(f"{res[0]} observed {res[1]} times")

run()

