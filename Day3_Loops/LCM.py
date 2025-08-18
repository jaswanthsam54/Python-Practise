a = int(input("Enter A: "))
b = int(input("Enter B: "))
result = max(a, b)
while True:
    if result % a == 0 and result % b == 0:
        break
    result += max(a, b)
print(result)