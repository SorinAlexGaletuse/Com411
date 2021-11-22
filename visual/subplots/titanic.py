import matplotlib.pyplot as plt
import csv

def read_data():
    titanic = {"survived":[], "sex":[], "age":[], "fare":[]}

    with open("C:/Users/user/PycharmProjects/Com411/visual/subplots/titanic.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            survived = line[1].strip()
            sex = line[14].strip()
            age = line[4].strip()
            fare = line[8].strip()
            if(survived!="" and sex!="" and age!="" and fare!=""):
                titanic["survived"].append(bool(int(survived)))
                if (int(sex)==0):
                    titanic["sex"].append("male")
                else:
                    titanic["sex"].append("female")

                titanic["age"].append(float(age))
                titanic["fare"].append(round(float(fare),2))
    return titanic

def run():
    data = read_data()
    fig, axs = plt.subplots(2,2)
    axs[0,0].pie(data["survived"],data["age"])
    axs[0,1].pie(data["survived"],data["fare"])
    axs[1,0].scatter(data["age"],data["fare"])
    axs[1,1].plot(data["sex"],data["survived"])
    plt.show()

run()
