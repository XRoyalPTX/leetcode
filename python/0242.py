class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            let_cnt = {}
            for i in s:
                let_cnt[i] = let_cnt.get(i, 0) + 1
            for j in t:
                if j in let_cnt:
                    let_cnt[j] -= 1
                else:
                    return False
            for x in let_cnt:
                if let_cnt[x] != 0:
                    return False
            return True
        else:
            return False
