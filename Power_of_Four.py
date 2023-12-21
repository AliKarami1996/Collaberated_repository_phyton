def power_of_four(n):

    power_four = 4 * n
    power_two = 1

    while power_two < power_four:
        power_two *= 2

    if power_four > 0 and power_four >= power_two:
        return True
    else:
        return False


def main():
    x = int(input("Enter an Integer: "))
    result = power_of_four(x)
    print(result)


main()
