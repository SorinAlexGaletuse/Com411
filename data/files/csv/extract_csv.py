import csv

def extract(file_path):
    print("Extrating...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        names =""
        print("Done!\nThe extracted names are as follows:")
        for value in csv_reader:
            print(f"{value[1]}")

def run():
    extract("bot.csv")

if __name__ == "__main__":
    run()