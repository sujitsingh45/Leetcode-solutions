class Solution:
    def countGoodNumbers(self, n: int) -> int:

        # Modulo value to keep the answer within limits
        MOD = 10**9 + 7

        # Function to calculate (base^exp) % MOD using Binary Exponentiation
        def power(base, exp):

            # Initialize answer as 1
            result = 1

            # Continue until exponent becomes 0
            while exp > 0:

                # If exponent is odd, multiply current base with result
                if exp % 2 == 1:
                    result = (result * base) % MOD

                # Square the base for the next bit
                base = (base * base) % MOD

                # Divide exponent by 2 (move to the next bit)
                exp //= 2

            # Return the computed power
            return result

        # Count of even indices (0,2,4,...)
        even = (n + 1) // 2

        # Count of odd indices (1,3,5,...)
        odd = n // 2

        # Calculate 5^(even positions)
        evenWays = power(5, even)

        # Calculate 4^(odd positions)
        oddWays = power(4, odd)

        # Multiply both results and take modulo
        return (evenWays * oddWays) % MOD