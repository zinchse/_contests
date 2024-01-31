class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        even_n, odd_n = (n + 1) // 2, n // 2
        even_m, odd_m = (m + 1) // 2, m // 2
        return even_n * odd_m + odd_n * even_m
        