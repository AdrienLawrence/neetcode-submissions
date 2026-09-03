class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        left = 0
        right = 0
        max_sub = 1
        chars = set(s[0])

        while right < len(s) - 1:

            while s[right + 1] in chars:
                chars.remove(s[left])
                left += 1
            right += 1
            chars.add(s[right])

            cur_sub = right - left + 1

            if cur_sub > max_sub:
                max_sub = cur_sub
        return max_sub
