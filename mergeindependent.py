worda = input("enter word1: ")
wordb = input("enter word2: ")
def mergeAlternately(self, word1, word2):
    self = ""
    if len(word1) >= len(word2):
        for i in range(len(word2)):
            self = self + word1[i] + word2[i]
        for i in range(len(word2), len(word1)):
            self = self + word1[i]
    else:
        for i in range(len(word1)):
            self = self + word1[i] + word2[i]
        for i in range(len(word1), len(word2)):
            self = self + word2[i]
    return(self)
print(mergeAlternately("" , worda, wordb))