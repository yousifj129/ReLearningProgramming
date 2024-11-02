class Character:
    def __init__(self, name:str, context: list[str], dialogue: list[str]):
        self.name = name
        self.context = context
        self.dialogue = dialogue
    
    def levenstheinDistance(self, str1, str2):
        d = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
        # iterate over d rows and columns
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                if i == 0:
                    d[i][j] = j
                elif j == 0:
                    d[i][j] = i
                elif str1[i-1] == str2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1])

        return d[len(str1)][len(str2)]
    def levenstheinSimilarity(self, str1, str2):
        d = self.levenstheinDistance(str1, str2)
        return 1 - d / max(len(str1), len(str2))
    
    def Chat(self, text):
        # check for the most similar dialogue string in the text
        sim = 0
        best = ""
        for i in range(len(self.dialogue)):
            simi = self.levenstheinSimilarity(text, self.dialogue[i])
            if simi > sim:
                sim = simi
                best = self.dialogue[i]
        return best
    

