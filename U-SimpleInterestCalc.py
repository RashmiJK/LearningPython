

def main():
    p = input("Enter value for Principle : ")
    n = input("Enter value for Number of Years : ")
    r = input("Enter value for Rate of Interest : ")

    p = int(p)
    n = int(n)
    r = int(r)

    si = (p * n * r) / 100
    print("Simple Interest = %d" % si)


if __name__ == "__main__":
    main()