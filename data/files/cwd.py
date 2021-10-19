import os

def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    for file in os.listdir(path):
        print(f"The directory contains the following {file}")

def run():
    print("Processing...")
    cwd()

run()