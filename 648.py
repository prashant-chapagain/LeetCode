class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        for key in dictionary:
            length = len(key)
            for i in range (len(words)):
                if words[i][:length] == key:
                    words[i] =key
        sentence = ' '.join(words)

        return sentence
    
