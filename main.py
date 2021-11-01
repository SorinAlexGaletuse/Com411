import basic.output.simple_message as simple_message
import basic.output.multiline_message as multiline_message
import basic.output.escape_characters as escape_characters
import basic.output.ascii_art as ascii_art

def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "ecape_characters":
        escape_characters.run()
    elif response == "ascii_art":
        ascii_art.run()


def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    run()