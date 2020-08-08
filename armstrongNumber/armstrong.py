
def is_armstrong(number):
    """
    Method to determine if the input is an armstrong number
    e.g : 153
    1**3 + 5**3 + 3**3 = 153
    since number = addition of each digit raised to power of (number of digits)
    It's an armstrong number
    :param number:
    :return:
    """
    number_array = [int(x) for x in str(number)]
    power = len(number_array)
    output = sum(i**power for i in number_array)
    print("input {}".format(number))
    print("ouput {}".format(output))
    if number == output:
        print("Is armstrong number")
    else:
        print("Not an armstrong number")

is_armstrong(1634)
