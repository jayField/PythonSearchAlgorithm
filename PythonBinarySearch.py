# binary_search Algorithm
def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if x == a[mid]:
            return mid

        # number you input > mid index value
        elif x > a[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return -1


a = [1, 4, 9, 16, 20, 24, 30, 49, 84]
inputNum = int(input("input number you wanna find: "))

c = binary_search(a, inputNum)
print("It is index of number you wanna find: ", c)
