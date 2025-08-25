arr = [10, 20, 4, 45, 99]
arr = list(set(arr))  # remove duplicates
arr.sort()
print("Second largest:", arr[-2])
