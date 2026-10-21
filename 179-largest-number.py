class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        num_str = [str(num) for num in nums]

        """
            apporach 1: compare each element against the conscuitvie element and calculate wheither it will placed after or before in the sorted list
        """

        n = len(num_str)

        for i in range(n):
            for j in range(0, n-i-1):
                A = num_str[j]
                B = num_str[j+1]
                if B+A > A+B:
                    num_str[j], num_str[j+1] = num_str[j+1], num_str[j]
        result = "".join(num_str)

        return "0" if result[0] == "0" else result
                    