import re


# Valid a number input against a min and max numbers of digits
def input_number(input_text, numbers_of_digits_min, numbers_of_digits_max):
    input_in_progress = True
    pattern = "(^[0-9]{" + str(numbers_of_digits_min) + "," + str(numbers_of_digits_max) + "}$)"
    while True:
        user_input = input(input_text)
        try:
            user_input = str(user_input)
            # test
            test_regex = re.match(pattern, user_input)
            #
            if test_regex == None:
                # Test is unsuccessful
                print("This input is not valid")
            else:
                # Test is successful, loop can be exited
                return user_input
        except:
            print("This input is not valid")

def input_string(input_text, numbers_of_digits_min, numbers_of_digits_max):
    input_in_progress = True
    pattern = "(^[A-Z]{" + str(numbers_of_digits_min) + "," + str(numbers_of_digits_max) + "}$)"
    while True:
        user_input = input(input_text)
        try:
            user_input = str(user_input)
            # test
            test_regex = re.match(pattern, user_input)
            #
            if test_regex == None:
                # Test is unsuccessful
                print("This input is not valid")
            else:
                # Test is successful, loop can be exited
                return user_input
        except:
            print("This input is not valid")