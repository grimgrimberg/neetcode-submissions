class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1),len(s2)
        if n1>n2:
            return False
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:n1]) #window in the size of n1 in s2

        if s1_counts == window_counts:
            return True
        #else, slide from left to right
        for i in range (n1,n2):
            #add char to the right
            window_counts[s2[i]] +=1
            #remove left char
            left_char = s2[i-n1]
            window_counts[left_char] -=1
            if window_counts[left_char] ==0:
                del window_counts[left_char]
            if s1_counts == window_counts:
                return True
        return False
        # set_s1 = set(s1)
        # set_s2 = set(s2)
        # return set_s1 in set_s2
        