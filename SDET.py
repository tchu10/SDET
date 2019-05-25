import unittest
class sentence_parse():
    def parse(self,s):
        #The purpose of this method is to parse a sentence and return both the longest word and the length of the word in characters
        #The function return a tuple including the length of the word and the word itself (length,word)
        #Assumptions:
        #  input will only be a string.  non-string input will return a length of -1 and a string 'Must be a string'
        #  punctuation will not be counted.1
        import string
        if type(s)!=str:
            return(-1,'Must be a string')
        length=-1
        word=''
        s=s.translate(str.maketrans('','',string.punctuation)) #remove punctuation
        word_list=s.split(' ')
        word_list.sort(key=len,reverse=True)
        word=word_list[0]
        length=len(word)
        return (length,word)
class test_sentence_parse(unittest.TestCase):
    aut_class=sentence_parse()
    def test_parse(self):
        self.assertEqual(self.aut_class.parse('The cow jumped over the moon'),(6,'jumped'))
        self.assertEqual(self.aut_class.parse(''),(0,''))
        self.assertEqual(self.aut_class.parse(1),(-1,'Must be a string'))
        self.assertEqual(self.aut_class.parse(';'),(0,''))
        self.assertEqual(self.aut_class.parse('jumped.'),(6,'jumped'))
        self.assertEqual(self.aut_class.parse(True),(-1,'Must be a string'))
def main():
    s=sentence_parse()
    print(s.parse('The cow jumped. over the moon'))
    t=test_sentence_parse()
    t.test_parse()
main()
