# simple recursion for countdown, power and factorial function


# power function : 2 ^ 4 = 2*2*2*2
def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)

# factorial function : 5! = 5 * 4 * 3 * 2 * 1, 0! = 1
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

# countdown function
def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x,"...")
        countdown(x-1)


def main():
    countdown(5)
    print("power = ", power(2,4))
    print("Factorial = ", factorial(0))


if __name__ == "__main__":
    main()