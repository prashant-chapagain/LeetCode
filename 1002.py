class Solution(object):
    def commonChars(self, words):
        frequency  = Counter(words[0])
        for word in words:
            frequency = frequency & Counter(word)
        
        arr =  list(frequency.elements())
        return arr