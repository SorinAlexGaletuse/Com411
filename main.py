import basic.output.simple_message as simple_message
import basic.output.multiline_message as multiline_message
import basic.output.escape_characters as escape_characters
import basic.output.ascii_art as ascii_art
import basic.input.ascii_robot as ascii_robot
import basic.input.data_types as data_types
import basic.input.string_operator as string_operator
import basic.input.user_input as user_input

def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if response == "simple_message":
        simple_message.run()
    elif response == "multiline_message":
        multiline_message.run()
    elif response == "escape_characters":
        escape_characters.run()
    elif response == "ascii_art":
        ascii_art.run()
    elif response == "ascii_robot":
        ascii_robot.run()
    elif response == "data_types":
        data_types.run()
    elif response == "string_operator":
        string_operator.run()
    elif response == "user_input":
        user_input.run()

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