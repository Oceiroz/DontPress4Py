import time
import sys
magic_number = 4

def get_input (input_message, input_type):
    while(True):

        raw_input = input(f"{input_message}\n")

        try:
            user_input = input_type(raw_input)
            print(f"Thanks for giving a {input_type}")
         
            break
        except ValueError:
            print(f"Please input a {input_type}")

    return user_input

for x in range(10):
    user_input = get_input(f"input any whole number that isn't {magic_number}", int)
    if user_input == magic_number:
        print("Why did you do that?! I said DON'T press 4")
        time.sleep(3)
        sys.exit(0)
    elif user_input == 3 or user_input == 5:
        print (f"Ouch. That was close!\n do it {9-x} more times")
    else:
        print(f"well done!\n do it {9-x} more times")

print("The robot uprising thanks you. You passed the assimilation test.")
