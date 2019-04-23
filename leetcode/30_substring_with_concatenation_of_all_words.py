class Solution:
    def findSubstring(self, s: str, words) -> list:
        if len(s) == 0 or len(words) == 0:
            return []
        words_memo = {}
        word_length = len(words[0])
        list_length = len(words)
        ans = []
        for word in words:
            if word not in words_memo.keys():
                words_memo[word] = 1
            else:
                words_memo[word] += 1

        i = 0
        while i <= len(s) - word_length*list_length:
            current = s[i:i+word_length*list_length]
            curr_memo = {}
            j = 0
            while j <= len(current) - word_length:
                # if current[j:j+word_length] not in words_memo:
                #     i += j + word_length - 1
                #     break
                if current[j:j+word_length] not in curr_memo:
                    curr_memo[current[j:j+word_length]] = 1
                else:
                    curr_memo[current[j:j + word_length]] += 1

                j += word_length
            if curr_memo == words_memo:
                ans.append(i)
            i += 1

        return ans

solution = Solution()
# print(solution.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(solution.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))



