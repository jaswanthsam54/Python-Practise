a = int(input("Enter the first term of the GP: "))
n = int(input("Enter the number of terms in the GP: "))
r = 2
ans = a * (r ** (n-1))
print(ans)
