# Tuples are immutable python objects
# Tuples are sequences like lists, but cannot be changed like lists
# Tuples have parenthesis, whereas lists use square brackets
# + - concatenation, * - repetition works for tuples

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

# empty tuple
tup3 = ()

print("tup1[0] : ", tup1[0])
print("tup2[1:5] : ", tup2[1:5])

tup3 = tup1 + tup2
print(tup3)

for x in tup2:
    print(x)

for x in tup2:
    print(x, end="")
