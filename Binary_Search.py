def binarySearch(numbers, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if (numbers[mid] == x):
            #if mid is equal to x
            return mid
        elif (numbers[mid] > x):
            #if mid is greater than the element X
            return binarySearch(numbers, low, mid-1, x)
        else:
            return binarySearch(numbers, mid+1, high, x)
    else:
        return -1
numbers = [ 1,4,6,7,12,17,25, 30 ]  
x = 7
result = binarySearch(numbers, 0, len(numbers)-1, x)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")