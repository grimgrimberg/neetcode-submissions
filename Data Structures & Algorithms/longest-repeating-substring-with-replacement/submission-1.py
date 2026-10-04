class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        counts = Counter()
        max_freq =0 

        for right,char in enumerate(s):
            #add freq map
            counts[char] +=1
            #update max_freq

            max_freq = max(max_freq, counts[char])
            #calculate window length
            window_len = right - left +1
            #if letter need replace more than k, shrink left
            if window_len - max_freq >k:
                counts[s[left]] -=1
                left +=1
            #update max len
            max_length = max(max_length,right-left +1)
        return max_length
