class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)

        if num1 == "0" or num2 == "0":
            return "0"
        
        pos = [0] * (n+m)

        for i in range(n-1,-1, -1):
            for j in range(m-1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) *( ord(num2[j]) - ord("0"))
                p1, p2= i+j, i+j+1

                total = mul + pos[p2]
                pos[p2] = total % 10
                pos[p1] += total // 10


        res = []
        print(pos)
        for digit in pos:
            if not (len(res)== 0  and digit == 0):
                res.append(str(digit))

        return "".join(res)