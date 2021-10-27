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

def run():
    load_data("titanic.csv")
    print(f"Succesfully loaded {len(records)} records.")

if __name__ == "__main__":
    run()
