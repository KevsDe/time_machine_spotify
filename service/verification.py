from datetime import datetime


def in_range_verification(user_input):
    """Verifies that the input is in the available range of dates,
    the accepted input is a date with the format YY-MM-DD"""
    today = datetime.now().strftime("%Y-%m-%d")
    past = "1958-08-02"
    in_range = True
    while in_range:
        if today >= user_input >= past:
            in_range = False
            return True
        else:
            print(f"The date is out of the acceptable range, please choose a day between {past} and {today}")
            user_input = input("Select the day with the following format 'YY'-'MM'-'DD': ")


def format_verification(user_input):
    """Verifies that the input's format is correct, the accepted input is a date with the format YY-MM-DD"""
    is_format = True
    while is_format:
        if "-" not in user_input:
            print("The format is not correct, please use the following one 'YY'-'MM'-'DD'")
            user_input = input("Select the day with the following format 'YY'-'MM'-'DD': ")
        elif "-" in user_input:
            divided_user_input = user_input.split("-")
            if len(divided_user_input[0]) == 4 and len(divided_user_input[1]) == 2 and len(divided_user_input[2]) == 2:
                digit = user_input.replace("-", "")
                correct_len = 8
                input_len = 0
                for x in digit:
                    if x.isdigit():
                        input_len += 1
                if correct_len == input_len:
                    is_format = False
                    return True
                else:
                    print("The format is not correct, please use the following one 'YY'-'MM'-'DD'")
                    user_input = input("Select the day with the following format 'YY'-'MM'-'DD': ")
            else:
                print("The format is not correct, please use the following one 'YY'-'MM'-'DD'")
                user_input = input("Select the day with the following format 'YY'-'MM'-'DD': ")