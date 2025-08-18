n = int(input("Enter A Number: "))
count = 0;
while n > 0:
    n = n // 10
    count = count + 1 
print(count)