# Merge sort implementation

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # recursively breakdown the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # performing merging of sorted arrays broken before
        i=0
        j=0
        k=0

        # while both arrays have elements
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        # if the right array still has values add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1


def main():
    print(items)
    mergesort(items)
    print(items)


if __name__ == "__main__":
    main()