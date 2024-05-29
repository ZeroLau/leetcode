def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = frozenset("aeiou")
        cnt = ans = sum(s[i] in vowels for i in range(k))
        print(cnt, ans, k)
        if ans != k:
            for i in range(k, len(s)):
                cnt += (s[i] in vowels) - (s[i - k] in vowels)
                print(cnt)
                if (ans := max(cnt, ans)) == k:
                    break
        return ans

print(maxVowels("", "hmzrixgfjwjgbrgdiryezvzyfjfmseujpegjhwnhsegtehsoanrryxngsocwnopblztcixtwdhbiidufbennibeqortatxaavbbljfnzofldoocflnqcqemmffntdvbnuyhnmniwrnxcrrumfeafmuungpylomljzpikiptakrtdqzchfrsoen", 90))