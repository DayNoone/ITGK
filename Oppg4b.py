def separate(numbers,threshold):
    mindre = numbers[0:threshold]
    storre = numbers[threshold:]
    return mindre, storre

x = [1,2,3,4,5]
print(separate(x,3))
