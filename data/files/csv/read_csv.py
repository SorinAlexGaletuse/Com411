import csv

def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        for remaing_line in csv_reader:
            print(remaing_line)

def run():
    read("bot.csv")

if __name__ == "__main__":
    run()



