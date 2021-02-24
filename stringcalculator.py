

def Add(a):
    # Add implementation
    if a:

        numArray = a.split(",")
        result = 0
        for num in numArray:
            result += int(num)
        print(result)
        return result
    else:
        return 0
