# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word  # Single word passed at initialization

    def match(self, word_list):
        '''Returns a list of words that are anagrams of the initialized word.'''
        anagrams = []
        for word in word_list:
            if sorted(self.word) == sorted(word):  # Compare sorted letters
                anagrams.append(word)
        return anagrams
