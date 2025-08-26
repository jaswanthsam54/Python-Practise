# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Main function
def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(num, "is a Prime number")
    else:
        print(num, "is NOT a Prime number")

# Call main
main()
