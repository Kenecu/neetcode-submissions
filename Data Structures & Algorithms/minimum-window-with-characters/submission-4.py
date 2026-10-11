class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for ch in t:
            t_count[ch] += 1
       
        need = len(t_count)
        have = 0
        window = defaultdict(int)
        best = (float("inf"), 0, 0)   # (length, left, right)
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1
            if c in t_count and window[c] == t_count[c]: 
                have += 1

            while have == need:
               # record window if it's the smallest so far
                if right - left < best[0]:
                    best = (right - left, left, right)
                # remove s[left] from the window
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:      
                    have -= 1
                left += 1
        if best[0] == float("inf"):
            return ""
        else:
            return s[best[1]:best[2]+1]
            
            