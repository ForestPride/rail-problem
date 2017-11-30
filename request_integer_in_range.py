""" Prompts user to provide integer within a range """


def request_integer_in_range(prompt, lowest, highest):
    """
    Purpose: prompts user for an integer, tests that an integer was
        provided, and verifies the integer is within an acceptable range.
    Inputs:
        prompt (str): request to present to user.
        lowest (int): lowest acceptable value.
        highest (int): highest acceptable value.
    Return (int): the accepted response from user.
    """

    # Create an error prompt to use later, if needed
    #error_prompt = "Please enter an integer between " + str(lowest)
    #error_prompt = error_prompt + " and " + str(highest) + ": "
    # Prompt user.
    response = input(prompt)
    # Loop until an acceptable response is received.
    while True:
        # Test to see if the response can be converted to an int.
        try:
            response = int(response)
            # If response in desired range, we're done.
            if (response >= lowest) & (response <= highest):
                # Exit the while loop since response is in the desired range
                break
            # Otherwise the catchall recovery will be executed.
        # One can use an specific exception statement to catch conversion error
        except ValueError:
            print("ValueError: You did not enter an integer")
            response = input("Please enter an integer between " + str(lowest) + " and " + str(highest) + ": ")
        # One can also use an else statement to catch any error not otherwise
        # specifically handled.
        else:
            print("Catchall recovery: Number out of range")
            response = input("Please enter an integer between " + str(lowest) + " and " + str(highest) + ": ")

    # Check the resultant integer is in the valid range
    print(response, " is acceptable.")
    return response


#def main():
    #""" Test harness """
    #answer = request_integer_in_range("Enter integer between 0 and 5: ", 0, 5)
    #print("main received ", answer)
#main()
