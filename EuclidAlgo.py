# Find the greatest commaon denominator (GCD) of 2 integer numbers


def gcd(a, b):
    # a>b condition to meet
    while(b != 0):
        t = a
        a = b
        b = t % a

    return a


def main():
    print(gcd(20,8))


if __name__ == "__main__":
    main()

