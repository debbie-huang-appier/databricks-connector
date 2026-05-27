a = input("Enter a list of numbers, separated by commas: ")
a = [int(x) for x in a.split(",")]
a.sort()
print(a)