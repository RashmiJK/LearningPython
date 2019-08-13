# Bubble Sort Algorithm


def bubblesort(dataset):
    # start with the array length and decrement each time
    for i in range(len(dataset)-1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
            print("(%d,%d) Current state:" % (i, j), dataset)


def main():
    list1 = [6, 20, 8, 19, 56]
    bubblesort(list1)
    print("Result:", list1)

if __name__ == "__main__":
    main()