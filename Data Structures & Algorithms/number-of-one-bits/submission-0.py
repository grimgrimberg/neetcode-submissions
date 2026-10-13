class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_clean = format(n, 'b')
        # print(binary_clean)
        # print(type(binary_clean))
        # print(binary_clean.astype)
        res = 0
        for i in range(len(binary_clean)):
            if binary_clean[i] == "1":
                res +=1
        return res