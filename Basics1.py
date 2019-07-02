#
# Some special features of Python
# 1. global and del keyword
# 2. Default argument value in function
# 3. Calling function with named parameters.
#    Can swap the positions of parameters in such cases.
# 4. Variable number of arguments
# 5. if, elif, else
# 6. conditional statement all in one line
# 7. break and continue in loops
# 8. enumerate to extract the index of list


f=123


def main():
    global f
    print("hello world ", f)
    # del f
    print(f)


# example for global and del (deletes the previous declaration) keyword
def someFunction():
    global f
    f = "def"


# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments
# we can combine the normal arguments with variable arguments
# , but variable argument always have to be the last argument
#  defined in the function
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# conditional statement all in one line
def OneLineConditional():
    x, y = 1000, 100
    st = "x is less than y" if (x < y) else "x is greater than or the same as y"
    print(st)


# enumerate use
def ExtractIndex():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
        print("[", i, "]", ":", d)

if __name__ == "__main__":
    main()
    print(power(3,4))
    # Python allows you to call functions with named
    # parameters and its allowed values, like below
    print(power(x=3, num=2))
    # calling variable number of argument function
    print("Multi add result : ", multi_add(4, 5, 10, 4, 10))
    OneLineConditional()
    ExtractIndex()

