a = int(input("Enter Number: "))
if a % 3 == 0 and a % 5 != 0:
    print("Divisible by 3")
elif a % 5 == 0 and a % 3 != 0:
    print("divisible by 5")
elif a % 5 == 0 and a % 5 == 0:
    print("Divisible by both 3 , 5")
else :
    print("Not divisible by both of them ")