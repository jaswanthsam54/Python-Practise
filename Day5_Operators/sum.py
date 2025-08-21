class Solution:
    def sumoffirstn(self, n: int) -> int:
        return n * (n+1) // 2
if __name__ == "__main__":
    sol = Solution()
    n = int(input("Enter a number: "))
    print(sol.sumoffirstn(n))