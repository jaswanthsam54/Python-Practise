arr = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
print("Frequency:", freq)
