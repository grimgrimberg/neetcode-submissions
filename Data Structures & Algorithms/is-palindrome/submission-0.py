class Solution:
    def isPalindrome(self, s: str) -> bool:
        # n = len(s)
        reversed_text = s[::-1]
        reversed_text.replace(" ", "")
        s.replace(" ", "")
        #cleaned = re.sub(r'[^a-zA-Z0-9]', '', text)
        cleaned_input = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_rev = re.sub(r'[^a-zA-Z0-9]', '', reversed_text)



        return cleaned_input.lower() == cleaned_rev.lower()
        