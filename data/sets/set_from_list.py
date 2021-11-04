def observed():
    observations = []

    for count in range(7):
        print("Please enter a record:")
        observations.append(input())
    return observations

def run():
    print("Counting observations...")
    record = observed()

    record_set = set()

    for observation in record:
        data = (observation, record.count(observation))
        record_set.add(data)

    for data in record_set:
        print(f"{data[0]} observed {data[1]} times")

if __name__ == "__main__":
    run()