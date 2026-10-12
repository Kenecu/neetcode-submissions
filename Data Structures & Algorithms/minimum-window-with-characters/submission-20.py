class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for x in t:
            t_count[x] += 1
        
        need = len(t_count)
        have = 0
        window = defaultdict(int)
        left = 0
        right = 0
        best = (float("inf"),left,right)
    
        while right < len(s):
            window[s[right]] += 1
            if s[right] in t_count and window[s[right]] == t_count[s[right]]:
                have += 1
            
            while have == need:
                if right - left < best[0]:
                    best = (right-left,left, right)
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -=1
                left += 1
            right += 1

        if best[0] == float("inf"):
            return ""
        else:
            return s[best[1]:best[2] + 1]
        




