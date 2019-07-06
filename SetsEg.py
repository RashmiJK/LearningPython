# A set is an unordered collection with no duplicate elements.
# Being an unordered collection, sets do not record element position
# or order of insertion.

# Basic uses include membership testing and eliminating duplicate entries.
# To create an empty set one has to use set(), not {}

# union, intersection, difference, and symmetric difference


def main():
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)

    if 'orange' in basket:
        print('orange is in basket')

    if 'crabgrass' in basket:
        print('crabgrass is in basket')

    a = set('abracadabra')
    b = set('alacazam')

    print(a)
    print(b)

    # letters in a but not in b
    print(a-b)

    # letters in a or b or both
    print(a|b)

    # letters in both a and b
    print(a&b)

    # letters in a or b but not both
    print(a^b)


if __name__ == "__main__":
    main()