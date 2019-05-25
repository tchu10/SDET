SDET unit test instructions:
1.  import the 'test_sentence_parse' class from SDET.py file
2.  instantiate an instance of the 'test_sentence_parse' class
3.  invoke the 'test_parse' method

Sample:

from SDET import test_sentence_parse

tc=test_sentence_parse()
tc.test_parse()

Normally I would create a separate .py file for the test class, but for brevity I built both the parse() method and the test into the same file (SDET.py)
